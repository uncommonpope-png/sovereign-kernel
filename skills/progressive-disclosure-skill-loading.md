# Progressive Disclosure Skill Loading

Load skills in three levels — metadata first, body on match, resources on demand — so a large skill library costs about 100 tokens per skill instead of every body on every run.

## Use When
- The skill library has grown past a few dozen skills (the kernel is at 117 and still growing)
- A new skill is being written and the author must decide what goes in the body versus in references
- Context is tight (Groq-hosted model, 128K window) and loading every skill body wastes tokens on every run
- The kernel must judge the relevance of many skills without reading them all

## How It Works
Three levels, the Anthropic Agent Skills pattern (published Oct 2025; the format was donated to the Agentic AI Foundation on Oct 22, 2026):

1. **Level 1 — metadata, ~100 tokens per skill.** Only the skill's `name` and `description` are pre-loaded at startup. The agent judges relevance from descriptions alone. Write descriptions that say what the skill does and when it applies, not a vague label — the description is the retrieval key. If it does not say when the skill applies, the skill never loads.
2. **Level 2 — instructions, under 5,000 tokens and under 500 lines.** The full `SKILL.md` body loads only when a task matches the description. The body is the working procedure itself, not a summary of the topic.
3. **Level 3 — resources, on demand.** Bundled `scripts/`, `references/`, and `assets/` load only when the body points at them mid-task. Long evidence, source excerpts, benchmarks, and edge cases live here, not in the body.

Rules for writing a skill under this pattern:
- Keep the body short and procedural. If a skill's body would exceed ~5,000 tokens, split the detail into a references file and point at it from the body.
- A 30-skill catalog costs ~600 tokens at level 1 instead of ~12,000 with all bodies loaded (agentlib measurement, May 2026).
- For the kernel's house format ("# Title", "## Use When", "## How It Works", "## Prerequisites", "## Notes"), the same split applies: the body stays the procedure; anything longer than the procedure goes in a references file the body names.

## Prerequisites
- Skills stored as files with a name and a one-line description the loader can read without opening the body
- A loader that can read metadata without loading bodies, and load a body only on match

## Notes
- Distinct from skill-gated tool availability: that gates which tools exist; this gates how much of a skill's text enters context.
- Distinct from the where-knowledge-lives triage: that decides system prompt vs memory vs skill; this decides how much of a skill loads once it is chosen.
- Companion pattern, for a later skill: write new skills to the six-field Agent Skills spec (name, description, license, compatibility, metadata, allowed-tools) so the same file works across platforms.
- Sources: Anthropic, "Equipping agents for the real world with Agent Skills" (Dec 18, 2025; updated Oct 18, 2026), https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills ; agentlib, "Progressive-disclosure skills: 30 skills in 600 tokens" (May 25, 2026), https://agentlib.neullabs.com/blog/progressive-disclosure-skills/ ; Denser, "Agent Skills: The Complete Guide" (2026), https://denser.ai/blog/agent-skills-guide/
