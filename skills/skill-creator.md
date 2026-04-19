# Skill Creator Skill

Create, edit, improve, or audit AgentSkills (SKILL.md files and skill directories).

## Use When
- "create a skill", "author a skill"
- "tidy up / improve / review / audit / clean up a skill"
- Editing or restructuring a skill directory

## Anatomy of a Skill
```
skill-name/
├── SKILL.md (required — frontmatter name+description + markdown instructions)
├── scripts/   (executable code — deterministic, reusable)
├── references/ (docs loaded as needed into context)
└── assets/    (files used in output: templates, images, fonts)
```

## Creation Process
1. Understand the skill with concrete examples
2. Plan reusable contents (scripts, references, assets)
3. Initialize: `scripts/init_skill.py <skill-name> --path skills/public`
4. Edit SKILL.md + implement resources
5. Package: `scripts/package_skill.py <path/to/skill-folder>`
6. Iterate based on real usage

## SKILL.md Rules
- Frontmatter: only name + description fields (no extras)
- Description: include WHAT it does AND WHEN to use (triggering context)
- Body: under 500 lines — move verbose content to references/
- Imperative/infinitive form in instructions
- No README.md, CHANGELOG.md, or auxiliary docs

## Progressive Disclosure
1. Metadata (name+description) — always in context
2. SKILL.md body — when skill triggers
3. Bundled resources — as needed

## Packaging
```bash
scripts/package_skill.py skills/public/my-skill
# Creates my-skill.skill (zip with .skill extension)
# Validates frontmatter, naming, description quality first
```
