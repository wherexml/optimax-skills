#!/usr/bin/env python3
"""Create a minimal distributable .skill archive."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

import yaml

from quick_validate import validate_skill


RUNTIME_FILES = {"SKILL.md", "LICENSE", "NOTICE"}
RUNTIME_DIRECTORIES = {"assets", "references", "scripts"}
EXCLUDED_PARTS = {".git", ".venv", "__pycache__", "dist", "node_modules", "tests"}
EXCLUDED_NAMES = {".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc"}


def include_path(relative: Path) -> bool:
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return False
    if relative.name in EXCLUDED_NAMES or relative.suffix in EXCLUDED_SUFFIXES:
        return False
    return relative.name in RUNTIME_FILES or (relative.parts and relative.parts[0] in RUNTIME_DIRECTORIES)


def package_skill(skill_path: Path, output_directory: Path) -> Path:
    skill_path = skill_path.resolve()
    output_directory = output_directory.resolve()
    valid, message = validate_skill(skill_path)
    if not valid:
        raise ValueError(message)

    frontmatter_text = (skill_path / "SKILL.md").read_text().split("---", 2)[1]
    skill_name = yaml.safe_load(frontmatter_text)["name"]

    output_directory.mkdir(parents=True, exist_ok=True)
    archive_path = output_directory / f"{skill_name}.skill"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for file_path in sorted(skill_path.rglob("*")):
            if not file_path.is_file():
                continue
            relative = file_path.relative_to(skill_path)
            if include_path(relative):
                archive.write(file_path, Path(skill_name) / relative)
    return archive_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_path", type=Path)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()

    if not args.skill_path.is_dir():
        parser.error(f"Skill directory does not exist: {args.skill_path}")
    archive = package_skill(args.skill_path, args.output_directory)
    print(archive)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
