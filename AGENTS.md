# Skill Hub maintenance rules

## Scope

- `skills/` is the only maintained copy of user-managed Skills in this repository.
- Do not modify Codex built-in Skills under `~/.codex/skills/.system/`.
- Never move or delete an original source during import. Record its absolute path in `catalog.yaml`.
- Global installation must use symlinks pointing into this repository.
- Duplicate names with different content are conflicts: report them and leave both originals untouched.

## Change workflow

1. Run `python3 scripts/skill-manager.py scan` and review the report.
2. Run `python3 scripts/skill-manager.py validate` before committing.
3. Update `catalog.yaml` when a Skill's source, dependencies, or lifecycle changes.
4. Run `python3 -m unittest discover -s tests -v`.
5. Commit the Skill and its metadata together.
