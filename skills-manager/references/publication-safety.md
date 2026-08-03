# Publication safety

Use this checklist before sharing a Skill publicly.

## Portability

- Replace user-specific absolute paths with arguments or neutral placeholders.
- Require scan roots and output locations explicitly.
- Avoid assuming a particular AI client, shell, package manager, or home layout.
- Keep platform-specific behavior behind an explicit compatibility note.
- Include representative fixtures instead of real local data.

## Privacy

- Remove names, email addresses, organization names, account identifiers, and
  private repository URLs unless they are intentionally public metadata.
- Do not publish generated catalogs containing full private Skill contents.
- Report credential findings by file and rule; never copy the matched value.
- Review examples and test fixtures as carefully as production code.

## Agent behavior

Public inspection Skills should not silently modify the user's environment.
Keep installation, filesystem reorganization, client configuration, database
changes, and agent-to-agent orchestration outside the portable core.

## Repository readiness

- `README.md` explains scope, requirements, safety boundaries, and tests.
- `LICENSE` covers original and redistributed work.
- `NOTICE` preserves required third-party attribution.
- automated tests use temporary directories and fictional fixtures;
- CI runs validation, tests, and the publication audit;
- the packaged archive excludes tests, caches, repository settings, and build
  output.

## Decision labels

- **Ready to publish:** validation and audit pass with no unresolved findings.
- **Ready after changes:** issues are specific and can be removed without
  changing the intended capability.
- **Not ready to publish:** live credentials, private data, unsafe automation,
  unclear licensing, or broken runtime dependencies remain.
