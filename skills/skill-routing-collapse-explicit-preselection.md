# Skill Routing Collapse — Explicit Preselection

As your skill library grows, implicit routing over skill names and descriptions silently stops loading the right skills — even when they are still there. With 1,000 irrelevant skills added, loaded-skill recall falls from 73.6% to 27.4% and the zero-load rate rises from 9.3% to 51.6%. The failure is silent: the agent simply proceeds without the skill it needed. Before solving any task, explicitly preselect the skills you will use from the full library — do not let skill choice compete with task execution.

## Use When
- Before starting any multi-step task, when the skill library is large (dozens of skills or more)
- When a task touches a domain where a skill exists but you are unsure which one applies
- After a run where the output looks like a skill was ignored (wrong tool, missing procedure, re-derived knowledge a skill already contains)
- When new skills have been added since the last time you solved this kind of task

## How It Works
1. **Preselect before you plan.** Before writing any plan or taking any step, list the candidate skills for this task from the library index — by name, description, AND body text. Do not decide while also solving.
2. **Read the body, not just the metadata.** The decisive routing signal lives in the skill body: hiding it drops routing accuracy 37–44 percentage points. Open the full text of each candidate skill before choosing; a name + description alone is not enough to judge fit.
3. **Commit to a short list.** Write down the 1–3 skills you will load, with one line each saying why. Load only those. If none fits, say so explicitly and proceed without a skill — never silently proceed with none.
4. **Do not substitute "plan skill use" for preselection.** Asking yourself to plan which skills to use while solving still yields lower recall than preselection done first. The selection step must happen before execution starts, in its own pass.
5. **Re-preselect when the task changes.** If the task pivots mid-run (new sub-problem, new domain), run the preselection pass again for the new phase — do not carry the old list forward blindly.
6. **Watch the zero-load signal.** If you finish a task having loaded no skill at all, treat that as a suspect outcome, not a default: check whether a relevant skill existed and was missed. Log the miss.

## Prerequisites
- A skill library with an index (names + descriptions) and readable skill bodies
- The discipline to separate the selection pass from the execution pass

## Notes
- Evidence: "Lost in Implicit Routing" (Liu, Chen & Zhang, arXiv:2610.18522, 13 Oct 2026) — recall 73.6% → 27.4%, zero-load 9.3% → 51.6% at 1,000 irrelevant skills; explicit preselection retains 73.9% recall; masking irrelevant descriptions largely restores loading. Corroboration: SkillRouter (Zheng et al., arXiv:2603.22455, COLM 2026) — hiding the skill body costs 37–44pp routing accuracy; a 1.2B body-aware retrieve-and-rerank pipeline reaches 74.0% Hit@1.
- Mechanism: semantic interference from descriptions, plus instruction interference when skill choice competes with task execution.
- Complements `progressive-disclosure-skill-loading` (the loading pattern) and `skill-arrival-routing-disambiguation` (arrival-time disambiguation when a new skill lands): this skill is the load-time preselection pass. It does not replace either.
- This loop adds a skill every 30 minutes, so the library — and the collapse risk — grows with every run. Preselection is the counterweight.
