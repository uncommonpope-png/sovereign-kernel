# Cheap Retrieval First Skill Selection

Pick the skill with the cheapest method that works, and pay for model-mediated selection only when cheap retrieval fails. Open skill aggregations have grown past 230,000 skills, so selection — not authoring — is the bottleneck, and the standing answer of letting the model rewrite queries and refine candidates inside its own decision loop pays LLM tokens on every task.

## Use When
- Choosing one skill from a large library (dozens to hundreds of skills) before starting a task
- The token budget is binding — for this kernel, the Groq free plan caps at 200,000 tokens/day, so every model-mediated selection loop is spend against a hard ceiling
- The current selection path rewrites the query or refines candidates with the model on every task
- A skill exists but keeps being missed, or the wrong skill keeps being picked

## How It Works
Use a ladder, cheapest first, and escalate only on failure.

**1. Keyword match first (BM25).**
Match the task against skill names and descriptions with plain keyword retrieval (BM25). This costs no model tokens at all. On the 89-task SkillsBench benchmark, plain BM25 alone recorded a pass rate at or above the LLM-mediated refinement loop on three of four pool/backbone/method settings — the expensive loop was not buying accuracy on most settings.

**2. Cheap re-rank second (small bi-encoder / cross-encoder).**
If the keyword stage returns a plausible set, re-rank it with a small embedding model (SkillSeek uses a BGE-base bi-encoder feeding a small cross-encoder, served over MCP). The cross-encoder covers the remaining fourth setting where BM25 alone falls short. This is still orders of magnitude cheaper than a model-mediated loop.

**3. Model-mediated selection only on failure.**
Escalate to the model only when the first two stages fail: no candidate clears a confidence threshold, the top two candidates are near-tied, or the task's vocabulary has no overlap with any skill name or description. Log every escalation — a ladder that escalates on most tasks is a ladder with a broken first rung, not a task that needs the model.

**Why the ladder works: the recall ceiling.**
The pattern is explained by a first-stage recall ceiling: if the right skill is not in the candidate set the first stage returns, no re-ranker or model loop can rescue it. Spend effort on recall before spend on selection: put the trigger words, task verbs, and synonyms in the skill's description, because the description is what the keyword stage matches against (see `skill-context-budget-and-doctor` — descriptions are capped at 1,536 characters, so front-load the trigger). A skill whose description never mentions the words a requester would use will never be recalled, however good its body is.

**The spend.**
Per-trial spend drops from USD 51.30 (LLM-mediated loop) to USD 27.54 (standard IR recipe) — within fifty cents of the no-skill baseline — at observed parity on SkillsBench under the OpenHands harness. That is the whole point: selection that costs almost nothing and performs the same.

## Prerequisites
- A skill library with a name and a description per skill, searchable by keyword
- A keyword index over names and descriptions (BM25 or equivalent); a small embedding re-ranker is optional but recommended for the fourth-setting case
- An escalation rule with a threshold, and a log of escalations so the ladder can be tuned

## Notes
- Evidence: Yang, Zhang, Shi & Wang, "SkillSeek: Revisiting Agent Skill Retrieval at Marketplace Scale", arXiv:2609.38822, submitted 30 Sep 2026; abstract read directly 2026-11-08. 4×11 grid of pool, backbone, and method on 89-task SkillsBench; BGE-base bi-encoder plus small cross-encoder over MCP; per-trial spend USD 51.30 → USD 27.54.
- The numbers are benchmark results under the tested harness, not a guarantee: if the first-stage recall misses the right skill, the ladder fails silently and cheaply. Treat repeated escalation on one task type as a signal to fix the description, not to widen the model loop.
- Complements `skill-routing-collapse-explicit-preselection` (preselect 1–3 skills by body text before solving — this ladder is how that preselection should be done cheaply) and `skill-context-budget-and-doctor` (the listing is a shared, capped resource; short, trigger-first descriptions serve both the listing budget and keyword recall). Distinct from queued `just-in-time-skill-retrieval` (when to re-select mid-task) — this skill is which method selects, not when.
- Never escalate to the model by default. Default to the cheapest stage that has earned trust on past tasks, and let escalation be the exception the log measures.
