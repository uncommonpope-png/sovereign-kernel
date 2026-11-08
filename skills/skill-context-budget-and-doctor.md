# Skill Context Budget and Doctor

Audit what the skill library costs in context and prune what does not earn its keep. A skill you never invoke is not free: its name and description sit in the listing on every turn.

## Use When
- The skill library keeps growing and routing or recall starts slipping
- A skill is added, renamed, or rewritten and its description may be too long or too vague
- Context feels crowded and the listing is suspected of eating the budget
- After a compaction, invoked skills stop being followed partway through a session
- Before raising any listing budget — audit first, raise only if everything earns its place

## How It Works
Every skill carries two context bills. Confusing them leads to bad pruning.

**1. The listing bill — paid every turn, invoked or not.**
Before any task, the kernel sees a listing of every skill's name and description so it can decide which skill fits. That listing has a fixed budget: it scales at 1% of the model's context window. Each entry's combined `description` and `when_to_use` text is capped at 1,536 characters — past that, the tail is cut, regardless of how much room the listing has left. When the listing overflows its budget, descriptions are dropped starting with the skills invoked least, and a skill without its description is hard to match. Names always stay. So an unused skill costs more than its own tokens: it can push a used skill's description out of the listing.

**2. The invocation bill — paid once a skill loads, then it lingers.**
The full skill body loads only when the skill is invoked. Once loaded, it stays in the conversation across later turns. After auto-compaction, only the first 5,000 tokens of each invoked skill re-attach, within a combined 25,000-token budget shared by all re-attached skills, filled most-recent-first — older skills can be dropped entirely. A long body therefore costs context for the rest of the session, and a skill invoked long ago may silently stop being followed.

**The audit (the doctor's round).**
Run the usage report (`/skill-doctor` in Claude Code, v2.1.252 or later; announced in 2.1.261, 4 Sep 2026). It shows, per skill, what it costs in context and how often it has been invoked, flags skills in the listing that have never been invoked, says where to turn them off, and lists plugins not used recently. Start with the never-invoked skills that have the highest context cost. `/doctor` estimates the listing's total cost and its biggest contributors; the Skills row in `/context` reports the listing size after the budget is applied, so it matches what the model actually receives.

**Prune in least-destructive order.**
1. Turn off the highest-cost skills never invoked. If a skill is needed rarely, make it user-invoked only rather than model-invoked.
2. Set low-priority entries to `"name-only"` in `skillOverrides` so they list without a description.
3. Shorten descriptions at the source: put the key use case first, since each entry is capped at 1,536 characters. Move long reference material out of the body into supporting files the skill loads on demand.
4. Only if every remaining skill earns its place, raise the ceiling: `skillListingBudgetFraction` takes a fraction (`0.02` for 2%), `SLASH_COMMAND_TOOL_CHAR_BUDGET` pins a fixed character count, and `skillListingMaxDescChars` moves the per-entry cap. Then confirm with the Skills row in `/context`.
5. Use `/clear` between unrelated tasks so invoked bodies from one task do not tax the next.

**Write descriptions as routing code.**
The description is what the kernel matches a request against. Front-load the trigger: the task, the situation, the exact words a requester would use. A vague description wastes its 1,536 characters and still fails to match; a sharp one matches inside the cap and survives the budget cut.

## Prerequisites
- A skill library large enough for the listing to matter (dozens of skills; this kernel carries 130+)
- Invocation counts per skill, or a usage report that provides them
- Authority to disable, hide, or shorten a skill — never silently drop a skill another workflow depends on; check dependents first

## Notes
- Numbers verified against Anthropic's Claude Code skills documentation (code.claude.com/docs/en/skills, read 2026-11-08): listing budget 1% of context window; per-entry cap 1,536 characters; overflow drops least-invoked descriptions first; re-attachment after compaction keeps the first 5,000 tokens per skill within a 25,000-token combined budget, most-recent-first; `/skill-doctor` requires v2.1.252+.
- The same numbers hold as a discipline even where the kernel does not run Claude Code: the listing is a shared, capped resource, and every skill pays rent on every turn whether it is used or not.
- Complements `skill-routing-collapse-explicit-preselection` (preselect 1–3 skills by body text before solving) and `cheap-retrieval-first-skill-selection` (cheapest retrieval first): those fix which skill gets picked; this one fixes what the listing costs and whether a picked skill can still be seen.
- Do not confuse the two bills when diagnosing: a skill that never triggers is a listing problem (description too long, too vague, or crowded out); a skill that stops being followed mid-session is an invocation/compaction problem (body too long, re-attachment budget spent).
- Re-audit after every batch of new skills lands. A library that grows without audits quietly evicts its own most-used descriptions.
