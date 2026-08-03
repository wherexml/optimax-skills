#!/usr/bin/env python3
"""Audit an Agent Skill for portability and publication risks."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


TEXT_SUFFIXES = {
    ".css", ".html", ".js", ".json", ".jsx", ".md", ".mjs", ".py",
    ".sh", ".toml", ".ts", ".tsx", ".txt", ".yaml", ".yml",
}
IGNORED_PARTS = {".git", ".venv", "__pycache__", "dist", "node_modules"}
PLACEHOLDER_MARKERS = {
    "<value>", "<token>", "<secret>", "example", "placeholder", "dummy",
    "redacted", "changeme", "your_", "${", "{{",
}

@dataclass(frozen=True)
class Rule:
    rule_id: str
    severity: str
    message: str
    pattern: re.Pattern[str]


RULES = (
    Rule("absolute-user-path", "error", "User-specific absolute filesystem path", re.compile(
        r"(?:/Users/[A-Za-z0-9._-]+/|/home/[A-Za-z0-9._-]+/|[A-Za-z]:\\\\Users\\\\[^\\\\\s]+\\\\)"
    )),
    Rule("client-command-injection", "error", "Client-specific command or nested-agent injection", re.compile(
        r"(?:\.claude/commands|claude\s+-p\b|codex\s+exec\b|spawn_agent\b|webbrowser\.open\s*\()",
        re.IGNORECASE,
    )),
    Rule("environment-mutation", "error", "Automated filesystem or database mutation", re.compile(
        r"(?:rm\s+-rf\b|symlinkSync\s*\(|os\.symlink\s*\(|shutil\.move\s*\(|rmtree\s*\(|"
        r"\.unlink\s*\(|\bDELETE\s+FROM\b|\bUPDATE\s+[A-Za-z_]+\s+SET\b)",
        re.IGNORECASE,
    )),
    Rule("implicit-home-scan", "error", "Implicit home or client-specific directory discovery", re.compile(
        r"(?:os\.homedir\s*\(|Path\.home\s*\(|~/Projects/skills|\.cc-switch|\.zcode|\.config/opencode)",
        re.IGNORECASE,
    )),
)

CREDENTIAL_ASSIGNMENT = re.compile(
    r"\b(?:api[_-]?key|access[_-]?token|refresh[_-]?token|app[_-]?secret|"
    r"client[_-]?secret|password|passwd)\b\s*[:=]\s*['\"]?([^'\"\s,}]{6,})",
    re.IGNORECASE,
)


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if any(part in IGNORED_PARTS for part in path.relative_to(root).parts):
            continue
        if path.is_symlink():
            yield path
        elif path.is_file() and (path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", "NOTICE"}):
            yield path


def redact_line(line: str) -> str:
    cleaned = CREDENTIAL_ASSIGNMENT.sub(lambda match: match.group(0).replace(match.group(1), "[REDACTED]"), line)
    return cleaned.strip()[:240]


def credential_is_placeholder(value: str) -> bool:
    lowered = value.lower()
    return any(marker in lowered for marker in PLACEHOLDER_MARKERS)


def audit(root: Path) -> dict:
    findings: list[dict] = []
    files_scanned = 0

    required = ("SKILL.md", "README.md", "LICENSE", "NOTICE")
    for name in required:
        if not (root / name).is_file():
            findings.append({
                "rule": "missing-publication-file",
                "severity": "error",
                "path": name,
                "line": None,
                "message": f"Missing required publication file: {name}",
                "evidence": None,
            })

    for path in iter_files(root):
        relative = str(path.relative_to(root))
        if path.is_symlink():
            target = path.resolve(strict=False)
            if not target.exists():
                findings.append({
                    "rule": "broken-link",
                    "severity": "error",
                    "path": relative,
                    "line": None,
                    "message": "Broken symbolic link",
                    "evidence": None,
                })
            else:
                findings.append({
                    "rule": "repository-link",
                    "severity": "warning",
                    "path": relative,
                    "line": None,
                    "message": "Review symbolic links before publication",
                    "evidence": None,
                })
            continue

        files_scanned += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        is_auditor_source = path.resolve() == Path(__file__).resolve()

        for line_number, line in enumerate(text.splitlines(), start=1):
            if not is_auditor_source:
                for rule in RULES:
                    if rule.pattern.search(line):
                        findings.append({
                            "rule": rule.rule_id,
                            "severity": rule.severity,
                            "path": relative,
                            "line": line_number,
                            "message": rule.message,
                            "evidence": redact_line(line),
                        })

            credential_match = None if is_auditor_source else CREDENTIAL_ASSIGNMENT.search(line)
            if credential_match and not credential_is_placeholder(credential_match.group(1)):
                findings.append({
                    "rule": "credential-assignment",
                    "severity": "error",
                    "path": relative,
                    "line": line_number,
                    "message": "Possible credential assignment; value redacted",
                    "evidence": redact_line(line),
                })

    errors = sum(1 for finding in findings if finding["severity"] == "error")
    warnings = sum(1 for finding in findings if finding["severity"] == "warning")
    return {
        "root": str(root),
        "publishable": errors == 0,
        "files_scanned": files_scanned,
        "summary": {"errors": errors, "warnings": warnings, "findings": len(findings)},
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_path", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = args.skill_path.resolve()
    if not root.is_dir():
        parser.error(f"Skill directory does not exist: {root}")

    report = audit(root)
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        label = "Ready to publish" if report["publishable"] else "Not ready to publish"
        print(label)
        print(f"files={report['files_scanned']} errors={report['summary']['errors']} warnings={report['summary']['warnings']}")
        for finding in report["findings"]:
            location = finding["path"]
            if finding["line"] is not None:
                location += f":{finding['line']}"
            print(f"{finding['severity'].upper()} {finding['rule']} {location}: {finding['message']}")
    return 0 if report["publishable"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
