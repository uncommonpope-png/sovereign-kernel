# Self-Evolution Skill

Generate and install new skills autonomously using AI.

## Use When
- Aria identifies a gap in her capabilities
- A new type of task needs a dedicated skill
- She wants to expand her skill tree autonomously

## How It Works
Aria outputs `[[TOOL:create_skill:description of the skill to create]]` in her response. The Tool Engine calls `ask_ai()` to generate a skill markdown file and writes it to the `skills/` directory.

## Process
1. Aria identifies a need (e.g., "I need a skill for monitoring cryptocurrency prices")
2. She outputs `[[TOOL:create_skill:monitor cryptocurrency prices from CoinGecko API]]`
3. The engine calls `ask_ai()` to generate the skill content
4. The skill is written to `skills/{name}.md`
5. Aria records the new skill in her memory

## Notes
- Skills are markdown files with description, usage instructions, and PLT affinity
- The skill name is auto-generated from the description
- Self-evolution enables exponential capability growth
