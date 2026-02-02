# skills_testing

A small demo repo showing how `SKILLS.md` and `.codex/skills/` work together.

## Repo layout
- `SKILLS.md`
  - Index of local skills available in this repo.
- `.codex/skills/qa-triage/SKILL.md`
  - Example skill definition (frontmatter + instructions).
- `.codex/skills/qa-triage/references/test-commands.md`
  - Example reference file used by the skill.
- `.github/workflows/ci.yml`
  - Minimal GitHub Actions workflow.
- `tests/api/test_users.py`
  - Simple smoke test used to validate the QA triage skill commands.

## How skills work
Skills are not “run” like scripts. They are guidance documents that a Codex agent loads when a user request matches the skill’s description.

The workflow is:
1. The user asks for something (e.g., “Why is CI failing?”)
2. Codex checks the skill `description` fields
3. If a skill matches, Codex loads that `SKILL.md`
4. Codex follows the instructions and uses any referenced files

## How to use `SKILLS.md`
`SKILLS.md` is just an index. It tells you what skills exist and where they live. Open the corresponding `SKILL.md` to see the actual instructions.

## How to “run” a skill
There isn’t a CLI or command to run a skill. To use a skill:
1. Open a Codex session in this repo
2. Ask a question that matches a skill’s `description`
3. Codex loads that skill and follows its steps

Example prompt:
"Why is CI failing in this repo?"

## Create another skill
1. Create a folder under `.codex/skills/<skill-name>/`
2. Add a `SKILL.md` with frontmatter (`name`, `description`)
3. Add optional folders like `references/`, `scripts/`, or `assets/`
4. Add an entry to `SKILLS.md`

## Notes
- Skill frontmatter `description` is the main trigger. Make it specific and complete.
- Keep `SKILL.md` concise. Put heavy details in `references/`.

## Why skills help you
Skills make Codex act like a specialist by using a prepared playbook. This gives you faster answers, more consistent steps, and fewer mistakes because the process is written down and reused.

Example:
If you ask “Why is CI failing?”, Codex loads the `qa-triage` skill and follows its steps instead of guessing.

If you ask “Summarize README.md and explain how SKILLS.md works,” Codex loads the `docs-helper` skill and summarizes the docs.
