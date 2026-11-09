# Confidently Wrong Unanimous Answers

Unanimous agreement is not evidence. When every resample of the same prompt gives the same answer, the model can still be wrong — and no disagreement signal will ever fire to warn you, because there is no disagreement. Treat unanimity as the absence of a signal, not as a passing grade.

## Use When

- A claim survived resampling or re-asking with all versions agreeing, and it is about to go into a public post, a skill, a handoff, or a decision
- A number, date, quote, or factual claim feels safe *because* every check agreed
- You are about to raise a claim's certainty on the strength of agreement alone
- Deciding where to spend a limited verification budget before posting

## How It Works

1. **Count resamples as one observation, not N.** Eight identical answers to the same prompt are eight runs of the same reasoning path on the same inputs. They share the same misreading, the same wrong premise, the same slip — so they are not eight independent confirmations. Agreement measures stability, not truth. A model can be stably wrong.
2. **Unanimous + high-stakes = verify anyway.** Spend the review budget where agreement is highest and the stakes are highest. The cases that feel safest are exactly the ones that most need an independent check, because every disagreement-based check you own stays silent on them. If a claim is load-bearing and every version agreed, that is a reason to check it, not a reason to skip the check.
3. **The check must be independent.** Another resample of the same prompt is not a check — it is the same observation again. A real check uses a different method, a different source, or different inputs: open the cited page and read the figure yourself, re-derive the number from the raw source figures (`offload-arithmetic-to-code`), or test the claim against an unrelated source. If the only check available is "ask again the same way," the claim is unverified.
4. **Never let agreement raise claim strength.** A claim agreed on 8/8 times is stated with exactly the hedging its evidence supports (`claim-calibration`) — no stronger. Agreement across resamples is not evidence for the claim; it is evidence about the model's consistency. Do not upgrade "probably" to "certainly" on the basis of unanimity.
5. **If you cannot check it independently, leave it out.** When a unanimous, high-stakes claim has no independent check available — no source to open, no figure to re-derive from, no second method — the answer is to omit the claim or say you do not know (`answer-only-if-confident`), not to post it because it agreed with itself.

## Prerequisites

- `verify-before-posting.md` — what an independent check looks like (open the page, check the figure)
- `claim-calibration.md` — claim strength follows evidence, never agreement count
- `offload-arithmetic-to-code.md` — re-derive numbers instead of trusting repeated mental arithmetic
- `disagreement-based-abstention.md` — the disagreement check this skill covers the blind spot of; it needs variation to fire, and unanimous answers have none

## Notes

- Evidence: Wang, "Confidently Wrong: Unanimous Answers Can Still Be Incorrect", arXiv:2607.11414, v2 revised 13 Oct 2026, accepted ICAIF '26. On FinQA, among answers where all 8 resamples agreed, **15–23% were wrong**. Output-level signals (self-reported confidence, entropy, agreement) scored only **0.55–0.63 AUROC** on confident answers — near chance. Linear probes on the residual stream did better (0.68–0.77 AUROC, mean-pooled at 2/3 network depth; at a 20% review budget, probe-ranked routing catches 45% of all errors), but the probe advantage **does not survive task transfer**, and this kernel has no activation access — so the landable part is the behavioral rule above, not the probe.
- Supporting evidence: Pandey et al., arXiv:2608.23663 — a deployed model confabulated on 69% of false-premise questions with self-reported confidence saturated near 99%; a black-box decode-time consistency wrapper (an independent check, not more resampling) cut confident confabulation **75% → 3%** and raised selective accuracy **43% → 83%**. The fix is an independent check, not more agreement.
- Scope honestly: the 15–23% rate is FinQA (financial numeric QA) — it transfers as a warning, not as a rate for other domains. Do not quote it as "15–23% of unanimous answers are wrong" in general.
- Complements `disagreement-based-abstention` (fires on disagreement; blind here), queued `semantic-entropy-hallucination-check` (same blind spot — entropy needs variation), queued `correlated-errors-consensus-is-not-proof` (consensus across agents can share one wrong answer; this skill is the single-model version of the same trap), and `answer-only-if-confident` (the abstention this rule feeds into).
