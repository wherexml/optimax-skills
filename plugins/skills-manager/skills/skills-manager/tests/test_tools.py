from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURE = ROOT / "tests" / "fixtures" / "valid-skill"


class PublicToolsTest(unittest.TestCase):
    def run_command(self, *command: str, expected: int = 0):
        result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def test_skill_is_structurally_valid(self):
        result = self.run_command(sys.executable, str(SCRIPTS / "quick_validate.py"), str(ROOT))
        self.assertIn("Skill is valid", result.stdout)

    def test_inventory_requires_an_explicit_root(self):
        result = self.run_command("node", str(SCRIPTS / "inventory_skills.mjs"), expected=1)
        self.assertIn("at least one --root is required", result.stderr)

    def test_inventory_finds_fixture(self):
        result = self.run_command(
            "node", str(SCRIPTS / "inventory_skills.mjs"),
            "--root", str(FIXTURE.parent), "--json",
        )
        report = json.loads(result.stdout)
        self.assertTrue(report["readOnly"])
        self.assertEqual(report["summary"]["skillEntries"], 1)
        self.assertEqual(report["skills"][0]["frontmatterName"], "sample-skill")

    def test_publication_audit_passes_repository(self):
        result = self.run_command(
            sys.executable, str(SCRIPTS / "audit_publication.py"), str(ROOT), "--json",
        )
        report = json.loads(result.stdout)
        self.assertTrue(report["publishable"])
        self.assertEqual(report["summary"]["errors"], 0)

    def test_publication_audit_catches_local_and_agent_specific_content(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ("README.md", "LICENSE", "NOTICE"):
                (root / name).write_text("fixture\n")
            local_path = "/" + "home" + "/" + "alice/private"
            client_path = "." + "claude" + "/" + "commands/test.md"
            (root / "SKILL.md").write_text(
                "---\nname: unsafe-skill\ndescription: Unsafe fixture.\n---\n"
                f"Read {local_path} and create {client_path}.\n"
            )
            result = self.run_command(
                sys.executable, str(SCRIPTS / "audit_publication.py"), str(root), "--json",
                expected=1,
            )
            report = json.loads(result.stdout)
            rules = {finding["rule"] for finding in report["findings"]}
            self.assertIn("absolute-user-path", rules)
            self.assertIn("client-command-injection", rules)

    def test_package_contains_runtime_files_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            result = self.run_command(
                sys.executable, str(SCRIPTS / "package_skill.py"), str(ROOT), str(output),
            )
            archive_path = Path(result.stdout.strip())
            self.assertTrue(archive_path.is_file())
            with zipfile.ZipFile(archive_path) as archive:
                names = set(archive.namelist())
            self.assertIn("skills-manager/SKILL.md", names)
            self.assertIn("skills-manager/LICENSE", names)
            self.assertFalse(any("tests/" in name for name in names))
            self.assertFalse(any(".github/" in name for name in names))


if __name__ == "__main__":
    unittest.main()
