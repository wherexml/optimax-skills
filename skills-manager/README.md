# Skills Manager

A portable, safety-first Agent Skill for inspecting, validating, publication-
auditing, comparing, and packaging other Skills.

## What it does

- scans only directories you explicitly provide;
- finds `SKILL.md` files and distinguishes physical copies from links;
- detects broken links, duplicate names, and divergent content;
- validates Skill frontmatter;
- audits a Skill for machine-specific paths, user-specific filesystem data, credential
  assignments, client-specific command injection, and automated mutation;
- creates a minimal `.skill` archive after checks pass.

## What it intentionally does not do

This public edition does not install, migrate, delete, rename, move, or link
Skills. It does not inspect application databases or agent session logs, scan a
home directory by default, invoke other agents, or modify client configuration.

## Requirements

- Node.js 18 or newer
- Python 3.10 or newer
- PyYAML 6.x

Install the Python dependency:

```bash
python3 -m pip install -r requirements.txt
```

## Quick start

```bash
node scripts/inventory_skills.mjs --root ./examples --json --pretty
python3 scripts/quick_validate.py ./path-to-skill
python3 scripts/audit_publication.py ./path-to-skill --json
python3 scripts/package_skill.py ./path-to-skill ./dist
```

## Safety model

Inspection commands are read-only. Packaging is the only command that writes,
and it writes only to the output directory selected by the caller. Findings
that resemble credentials are reported by type and location without printing
the matched value.

## Testing

```bash
python3 -m unittest discover -s tests -v
```

## License and attribution

Licensed under Apache-2.0. `scripts/quick_validate.py` is redistributed from
Anthropic's public `skill-creator` under the same license. See `NOTICE` for
details.
