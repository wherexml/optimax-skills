# Security

## Reporting a vulnerability

Open a private security report with the repository owner. Do not include live
credentials, private Skill contents, or personal filesystem paths in a public
issue.

## Operational boundary

The public Skill is designed for explicit, bounded inspection. It does not
perform installation, migration, deletion, link creation, client configuration
changes, database access, home-directory discovery, or agent-session analysis.

Publication auditing is heuristic. Review findings before sharing a repository,
and use a dedicated secret scanner as an additional release check.
