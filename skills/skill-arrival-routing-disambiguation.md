# Skill Arrival Routing Disambiguation

When a new skill arrives in the library, a similar new skill can silently displace an earlier one — breaking previously-correct routing even though the earlier skill and the router are unchanged. Under progressive disclosure the router selects by name + description alone, so two skills that look alike in their metadata compete, and the newer one wins by recency or wording even when the older one is the right tool. The failure is silent: no error, just wrong routing on queries that used to work. Disambiguate every incoming skill on arrival — before it is ever loaded for a real task.

## Use When
- A new skill file is added to the library (this loop adds one every 30 minutes — every arrival is a displacement chance)
- A task that used to route to a known skill suddenly routes to a different, newer one
- Two skills in the library cover overlapping domains and you are unsure which one a query should hit
- After a routing regression: a previously-correct query now loads the wrong skill

## How It Works
1. **Find the closest predecessor on arrival.** Before accepting a new skill, compare its name, description, and body against the existing library and name the nearest neighbour it could shadow. If no neighbour is close, the skill is clear to land as-is.
2. **Rewrite only the incoming skill's name + description.** State what the body actually supports, how the skill differs from its closest predecessor, and what related work it excludes. Do not rewrite the predecessor and do not touch the router — no router training, no labelled data. The metadata rewrite is the whole fix.
3. **Add a negative boundary.** Write into the incoming skill's description what it is NOT for — the queries that should still route to the predecessor. A skill with no negative boundary is a skill that will absorb its neighbour's traffic.
4. **Regression-test previously-correct routing.** Run the queries that previously routed to the predecessor and confirm they still do. If a query flips to the new skill wrongly, sharpen the new description further and re-test — do not accept the flip.
5. **Record the arrival.** Note the predecessor, the disambiguation made, and the regression-test result in the skill's Notes. The next arrival needs to know what was already decided.
6. **Never fix displacement by editing the predecessor.** The incoming skill's metadata is the only thing that changes. Editing the older skill to defend it starts a rewrite war and breaks its own routing history.

## Prerequisites
- A skill library selected by name + description (progressive disclosure)
- A small regression set: queries with known-correct routings, kept with the library
- The ability to edit an incoming skill's metadata before it lands

## Notes
- Evidence: "Skill++: Towards Lifelong Agents via Routing-Aware Skill Refinement" (Zhang et al., arXiv:2611.00544, 31 Oct 2026) — as the library grows to 731 skills over ten sessions, Skill++ selects all required skills for 76.3% of queries vs 36.4% under the original metadata; gains carry over to the Codex CLI agent harness and outperform all compared approaches across three benchmarks and five LLM routers. Abstract read directly 2026-11-08.
- Negative-boundary half: "Capability Pages" (Wang et al., arXiv:2608.04482) — a written "do NOT route here" boundary per skill, computed against nearest neighbours, adds +2.94 Recall@10 and +3.62 task success. Folded into step 3 here rather than kept as a separate skill.
- Complements `skill-routing-collapse-explicit-preselection` (the load-time preselection pass — this skill is its arrival-time counterpart) and `progressive-disclosure-skill-loading` (the loading pattern). Preselection chooses well at load time; this skill keeps the library itself routable as it grows.
- This loop adds a skill every 30 minutes, so the library — and the displacement risk — grows with every run. Arrival disambiguation is the counterweight at the write end.
