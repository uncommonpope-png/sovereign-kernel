# ClamHub Skill

Interface with ClawHub — the ForgeClaw skills repository and skill management system.

## Use When
- Installing or updating ForgeClaw skills
- Publishing skills to the ClawHub registry
- Browsing available skills

## Registry
```bash
# List available skills
curl -s https://raw.githubusercontent.com/uncommonpope-png/forgeclaw-skills/main/forgeclaw_skills/registry.json | jq '.[] | {name, description}'

# Get specific skill SKILL.md
curl -s "https://raw.githubusercontent.com/uncommonpope-png/forgeclaw-skills/main/forgeclaw_skills/skills/<name>/SKILL.md"
```

## clawhub CLI (if installed)
```bash
clawhub list                     # list available skills
clawhub install <skill-name>     # install a skill
clawhub update                   # update all skills
clawhub search "query"           # search skills by name/description
clawhub publish ./my-skill       # publish skill to registry
```

## Manual Install
```bash
# Clone skills repo
git clone https://github.com/uncommonpope-png/forgeclaw-skills
# Copy skill to local skills dir
cp -r forgeclaw-skills/forgeclaw_skills/skills/<name>/ ~/.openclaw/skills/
```

## Notes
- 52 skills in the registry as of 2026
- Skills are SKILL.md prompt files injected into AI context
- Each skill lives in forgeclaw_skills/skills/<name>/SKILL.md
