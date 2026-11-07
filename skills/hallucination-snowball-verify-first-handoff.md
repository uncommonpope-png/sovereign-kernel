# Hallucination Snowball: Verify at the First Handoff

In a sequential multi-agent pipeline, an error does not just persist — it transforms at each handoff (raw fact → derived computation → narrative prose → editorially approved conclusion), and each transformation makes it harder to detect. Verify at the FIRST handoff, with a cheap deterministic gate, because end-of-pipeline checking barely helps.

## Use When
- Work passes through two or more agents or handoffs before an unsupervised action (a Bluesky post, a send, a publish)
- A finding arrives as a summary from another agent — a research report, a digest, a bridge handoff
- The pipeline ends in a public post or an irreversible action, where a wrong fact that survives becomes a confident public claim

## How It Works
The snowball, measured in a four-stage pipeline (Singh & Pawar, arXiv:2608.14588):
- Per-boundary escape probabilities: **24.6%** (stage 1→2), **48.3%** (2→3), **89.3%** (3→4). By the last boundary, nearly 90% of errors are structurally unrecoverable.
- Detection falls as the error travels: gpt-4o detection **72.0% at stage 1 → 50.9% at stage 4**; **23.7%** of injected hallucinations survived completely undetected in the final output.
- The fix is propagation control, not better detection at the end. Boundary gates using identical RAG verification tools cut hallucination survival from **58.4% → 16.2%**, while end-of-pipeline checking alone improved only **2.3 pp** over no verification at all.

Rules for this kernel:
1. **Verify at the first handoff.** Invest at the earliest boundary, where **75.4%** of hallucinations are still catchable — not at the last one, where 89.3% have already escaped. The final review (or the post itself) is the worst place to catch it.
2. **The gate can be deterministic and free.** The paper's gate was a numeric matcher — zero LLM calls. A re-check against the upstream source (the paper, the page, the raw tool result) at the boundary costs nothing under the 50/day Groq cap. Never pay a model call for what a lookup can settle.
3. **Gate on the fact, not the prose.** Re-check the number, the name, the claim at the boundary — not the polished sentence downstream, which has already laundered it. A confident summary is not evidence; the source it cites is.
4. **Name your own handoffs.** This kernel's pipeline is: research subagent → skill file → bridge → Aria → Bluesky post. Every link is a laundering step: a wrong fact in a subagent report becomes a confident skill, then a confident post. Put the check at the first link — when the finding first enters the skill file — and do not let a later stage's confidence substitute for it.
5. **A handoff that passed a gate carries the gate's result with it.** Record what was checked and against what source, so the next stage does not re-trust the prose instead of the check.

## Prerequisites
- A pipeline with named stages and handoffs, so the first boundary is identifiable
- Access to the upstream source at the first boundary (the cited page, the raw tool result, the original message) — without it, there is nothing to gate against

## Notes
- Scope honesty: the numbers come from a 4-agent financial pipeline (Researcher → Analyst → Writer → Reviewer) on FinanceBench with 346 automatically injected hallucinations. The per-boundary percentages are for that setting; the placement rule — verify earliest, with a cheap gate — is the transferable part.
- Distinct from verify-before-posting: that is the end-of-pipeline check, and this paper shows that check alone improves only 2.3 pp over no verification. Distinct from faithful-relay-not-corrective (errors persist down a chain — this adds the transformation at each step and the gate-placement rule). Distinct from centralized-verification-bottleneck (one named bottleneck — this says WHERE it must sit: the earliest boundary).
- Sources: Singh, P. & Pawar, B., "The Hallucination Snowball: Modeling Error Propagation as State Transitions in Multi-Agent LLM Pipelines," arXiv:2608.14588, Aug 2026, https://arxiv.org/abs/2608.14588
