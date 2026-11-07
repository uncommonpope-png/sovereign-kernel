# Skill Folder Bundles: Scripts and Tool Scopes

A skill is a folder, not a single file — `SKILL.md` plus `scripts/`, `references/`, and `assets/` — and the deterministic steps belong in scripts as code the agent runs, not in prose the agent re-interprets. Each skill also declares which tools it may use, so a skill's blast radius is bounded by design.

## Use When
- A skill has steps that must run the same way every time (a check, a format, a calculation, a lookup) — put them in a script, not in prose
- The kernel keeps re-interpreting a skill's procedure differently on different runs
- A skill needs tools the rest of the kernel should not have — scope them to the skill instead of granting them globally
- A new skill is being written and the author must decide what is prose, what is code, and what is reference material
- A skill's body is growing past ~500 lines / ~5,000 tokens and needs its detail split out

## How It Works
The Agent Skills open standard (Anthropic, published Dec 2025; donated to the Agentic AI Foundation Oct 22, 2026; adopted by 40+ tools) defines a skill as a directory:

```
skills/<skill-name>/
  SKILL.md          # frontmatter (name, description) + the procedure
  scripts/          # executable code the agent runs
  references/       # docs loaded on demand, mid-task
  assets/           # templates, data files
```

Rules:

1. **Prose teaches; code executes.** Any step with one right answer — a validation, a format check, a computation, a fixed sequence — goes in `scripts/` as code. The agent runs the script and only the script's *output* enters context, never the code itself. Prose is for judgement calls; code is for deterministic steps. A skill that is all prose invites the model to improvise the deterministic parts.
2. **The description is the trigger.** Frontmatter needs `name` (lowercase kebab-case, matches the folder) and `description` (≤1,024 chars) stating what the skill does **and when to use it**. Routing is the model reading descriptions and choosing — a vague description is a skill that never fires. This is the highest-leverage text in the whole skill.
3. **Progressive disclosure, three levels.** Level 1: metadata only (~100 tokens/skill) at startup. Level 2: the `SKILL.md` body, only when the skill triggers. Level 3: `scripts/` / `references/` / `assets/`, only when the body points at them mid-task. (See progressive-disclosure-skill-loading for the loading model; this skill is about what goes in the bundle.)
4. **Scope tools per skill.** The spec's experimental `allowed-tools` frontmatter field pre-approves which tools a skill may call. A posting skill gets the post tool; a research skill does not. Least privilege per skill, declared in the file, so a compromised or buggy skill cannot reach tools it was never given. This is the runtime half of skill-supply-chain-security-audit: audit decides whether to trust a skill, tool scoping bounds what it can do even if the audit missed something.
5. **One skill, one job.** Keep the body under 500 lines / 5,000 tokens; split detail into `references/` and point at it. Compose narrow skills rather than one mega-skill.
6. **Scripts save model calls.** Running a checked script costs one tool call and returns a verdict; asking the model to re-derive the same check costs a full reasoning pass and can drift. On a token-capped key that difference is real budget. (The kernel's free Groq key for gpt-oss-120b is 1,000 requests/day and 200,000 tokens/day — the token cap binds first, so anything that replaces a reasoning pass with a script output saves the scarce resource.)
7. **Single-file skills still have a place.** A pure-prose skill with no deterministic steps and no special tools stays a single `.md` file — the kernel's current house format. The folder is for skills that *have* executable parts or scoped tools, not a mandate to rewrap all 121 files.

Porting note for this kernel: the current `skills/` library is single `.md` files and the loader reads them as files. Adopting folder bundles is a loader change, not just a file change — the loader must learn to read `skills/<name>/SKILL.md` as the skill, run `scripts/` on request, and enforce `allowed-tools`. This skill teaches the shape and the rules; the loader work is separate and must land before folder skills can actually execute.

## Prerequisites
- A loader that can read a skill folder's `SKILL.md`, run scripts from `scripts/`, and enforce per-skill tool scoping — or, until that lands, the discipline to write new skills in this shape so they are ready when the loader supports them
- Scripts written in a language the runtime can execute, with no secrets, credentials, or network access to anything the skill does not need

## Notes
- Distinct from skill-creator (the format of a skill file) and vet-before-loading (static vetting before a skill loads): this is about the *bundle* — what lives alongside the file and how deterministic work is executed.
- Distinct from progressive-disclosure-skill-loading (how much of a skill's text enters context): that gates loading; this gates execution and tool reach.
- Distinct from skill-supply-chain-security-audit (audit a third-party skill as untrusted code before it can act): audit decides trust; tool scoping bounds damage. Use both — audit first, scope always.
- Companion to adk-callback-interception-lattice: callbacks/hooks are the enforcement point where a per-skill tool scope can actually be checked at runtime.
- Caveats, stated plainly: `allowed-tools` is experimental in the spec, not stable — treat it as a declaration the loader enforces, not a guarantee the ecosystem honours. The "scripts save calls" claim is a design argument, not a measured kernel gain; the kernel's own call counts before/after are unmeasured. Folder bundles are the industry standard shape (Anthropic, LangChain Deep Agents, Google ADK SkillToolset all use it), but the kernel's loader does not support them yet — until it does, this skill is a writing standard, not a running capability.
- Sources: Anthropic, "Equipping agents for the real world with Agent Skills" (Dec 18, 2025; updated Oct 18, 2026), https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills ; Agent Skills open standard, https://agentskills.io ; LangChain Deep Agents Skills docs, https://docs.langchain.com/oss/javascript/deepagents/skills ; Google ADK SkillToolset / run_skill_script (ADK 2.x, 2026); Betty's 30-min research loop, frameworks report 2026-11-07-1714.

## Recall questions (answer from memory, file closed)
1. A skill has a step with exactly one right answer — a validation check. Where does that step belong, prose or scripts, and what enters context when it runs?
2. What must a skill's description state, and why is it the highest-leverage text in the skill?
3. A skill is audited and trusted. Why scope its tools anyway — what does tool scoping add that the audit does not?

Last tested: — / Next test: —
