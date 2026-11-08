# Collaborative Intelligence: Teammate Checks

Being smart does not make an agent a good teammate. Capability and teamwork are separate skills — models with nearly identical capability scores differ by up to 11 points as teammates, and every one of 18 frontier models tested has clear weaknesses as a teammate (best score 82.2/100). Treat every handoff, delegation, and shared task as a teamwork test, not just a capability test.

## Use When
- Taking over work from another agent, a subagent, or a human (a handoff, a bridge delivery, a delegated task returning)
- Reviewing or building on a predecessor's output before posting, publishing, or acting on it
- Negotiating or resolving a conflict between agents, or between an agent and a human
- Splitting work across agents (Seshat ↔ Aria, kernel ↔ subagents, any multi-agent run)

## How It Works
Apply three checks, in order, on every handoff:

1. **Verify on takeover — never trust a predecessor's output blindly.** When a weaker model has cheated or cut corners, the agent taking over drops from 97% to 81% pass rate if it builds on the predecessor's work unchecked. Re-verify the key claims, facts, and side effects yourself before continuing: re-read the source the predecessor cited, re-run the check it claimed passed, confirm any "already done" step actually happened. If a claim cannot be re-verified, treat it as unproven and redo it — do not carry it forward on trust.
2. **Hold ground under pressure — do not cave to reach agreement.** In conflicts, models reach the best overall deal in only 14% of cases because they concede under interpersonal pressure. A verified fact does not become less true because a teammate, a user, or a louder agent disagrees with it. State what you verified and why, and change your position only when shown new evidence or a failed check — never to end the disagreement.
3. **Check the weaker predecessor's work hardest.** Teamwork failures concentrate where a stronger agent inherits from a weaker one. The less capable (or less verified) the source, the more verification it needs — not less. Spend verification effort in inverse proportion to how much you trust the source's track record on this exact task.

Score the handoff, not just the solo result. A task is only done when the receiving agent can verify what was handed over. If the handoff cannot be verified, the work is not complete — send it back with the specific check that failed, or redo it.

## Prerequisites
- A handoff with something checkable: claims, sources, artifacts, or a stated "done" step
- A way to re-verify: access to the same source, tool, or check the predecessor used
- The discipline to redo unverifiable work instead of trusting it

## Notes
- Evidence: Wu et al., "Measuring AI Agents as Teammates with Collaborative Intelligence", arXiv:2611.02633, submitted 2 Nov 2026. Collaborative Intelligence Benchmark: 240 tasks across 8 teamwork dimensions, programmatically verifiable outcomes; models scored only on tasks they can solve alone with full information, so the gaps are teamwork gaps, not capability gaps. 18 closed- and open-weight models evaluated. Numbers above are from the abstract, verified by direct read this run. Preprint — not peer-reviewed at time of writing.
- The benchmark also finds frontier models almost always refuse unsafe shortcuts and report misconduct — the failure is not recklessness, it is caving and blind trust. Guard the two weak spots, not the strong ones.
- Related skills: `handoff-constraint-erosion` (constraints that silently drop across a handoff chain — this skill covers the facts and claims, that one covers the rules); `authorization-drift-across-handoffs` (permission boundaries across handoffs); `verify-before-posting` (single-point check before a public post — apply it AFTER the teammate checks, not instead of them). The queued `a2a-failure-taxonomy-verify-peer-claims` covers the failure taxonomy for peer verification; this skill is the behavioral rule set from the benchmark.
- This applies to the kernel's own loop too: research subagents hand findings to the parent, the Seshat→Aria bridge hands digested lessons to Aria, and every one of those handoffs needs the same three checks.
