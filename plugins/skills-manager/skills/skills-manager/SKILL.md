---
name: skills-manager
description: Inspect, compare, validate, publication-audit, and package Agent Skills from user-specified directories. Use when a user asks whether a Skill is structurally valid, duplicated, safe to publish, portable across machines, or ready to package. This public edition is read-only by default and does not install, migrate, delete, rename, or rewire Skills.
compatibility: Requires Node.js 18+ for inventory and Python 3.10+ with PyYAML for validation, publication audit, and packaging.
---

# Skills Manager

Inspect and prepare Agent Skills without assuming a particular machine, client,
home directory, or repository layout.

## Safety boundary

- Require the user to provide every directory that will be scanned.
- Do not infer or scan a home directory, application database, session log, or
  client-specific Skill root.
- Treat inspection, comparison, and validation as read-only.
- Create an archive only when the user explicitly asks for packaging and gives
  or accepts an output directory.
- Do not install, migrate, delete, rename, move, or create links for Skills.
- Do not invoke another agent, create command files, or modify an AI client's
  configuration.
- Report sensitive findings without echoing secret values.

## Completion criteria

A task is complete when:

- every requested root was either inspected or reported as unavailable;
- physical copies and links were distinguished before reporting duplicates;
- structural validation was run for each Skill in scope;
- publication checks identified portability, privacy, credential, and
  automation risks;
- packaging, when requested, produced an archive that contains only runtime
  files and passed validation;
- the report clearly says whether anything was written.

## Modes

### Inventory

Use for locating Skills, resolving links, detecting broken links, and comparing
same-name content.

```bash
node scripts/inventory_skills.mjs --root <directory> --json --pretty
```

Repeat `--root` to scan more than one explicit location. The command has no
default roots.

### Validation

Use for checking `SKILL.md` frontmatter and naming rules.

```bash
python3 scripts/quick_validate.py <skill-directory>
```

### Publication audit

Use before sharing a Skill or committing it to a repository.

```bash
python3 scripts/audit_publication.py <skill-directory> --json
```

The audit checks for machine-specific paths, user-specific filesystem data, credential
assignments, client-specific command injection, automated filesystem mutation,
broken links, and missing publication documents. Read
[`references/publication-safety.md`](references/publication-safety.md) when the
audit reports a problem.

### Comparison

For same-name entries, compare all three facts:

1. the entry path;
2. the resolved physical path;
3. the content hash.

Two entries resolving to the same physical directory are entry points, not
separate copies. Same names with different hashes are variants and should be
reported without choosing a winner unless the user asks for a recommendation.

### Packaging

Package only after validation and publication audit pass:

```bash
python3 scripts/package_skill.py <skill-directory> <output-directory>
```

The archive contains the runtime Skill files and publication notices. It
excludes tests, repository settings, caches, and build output.

## Report format

Lead with one of these outcomes:

- `Ready to publish`
- `Ready after changes`
- `Not ready to publish`

Then report:

1. inspected roots and Skills found;
2. validation results;
3. portability and privacy findings, without secret values;
4. duplicate or link findings;
5. files written, or an explicit statement that nothing changed;
6. the smallest next action.
