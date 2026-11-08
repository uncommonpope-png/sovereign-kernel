# Calibration Drift Under Reasoning

Thinking longer does not always make you righter — past a point, extra reasoning makes you more confidently wrong. Budget your thinking, and treat a long, smooth, confident chain as suspect until an independent check agrees with it.

## Use When

- Deciding how much reasoning to spend on a sub-problem before starting it
- A long chain-of-thought has produced a confident answer with no external check
- Drafting a factual claim for a public post after a long reasoning loop
- Confidence keeps rising as the reasoning goes on, instead of settling
- Choosing between reasoning longer and stopping to verify

## How It Works

Chain-of-thought reasoning is usually treated as "more is better": a bigger reasoning budget should mean fewer errors and better calibration. That picture is incomplete. Past a task-specific threshold, increasing the reasoning budget can make a model systematically overconfident — assigning high confidence to incorrect answers. Expected Calibration Error as a function of reasoning budget, ECE(B), follows a non-monotone curve: it first decreases as reasoning corrects errors, then increases as longer reasoning produces internally consistent but incorrect explanations.

The mechanism is **hypothesis lock-in**. An early wrong hypothesis, once adopted, gets elaborated by autoregressive generation into a coherent, detailed, internally consistent trajectory — every further step rationalizes the wrong starting point instead of challenging it. The longer the chain, the more polished and confident the wrong answer looks, including to the model itself. A short chain that says "probably X" can be better calibrated than a long chain that says "certainly X" after talking itself into X.

The paper's countermeasure is **CABStop**, a calibration-aware stopping rule: halt reasoning when stated confidence diverges from an auxiliary accuracy estimate. You do not need the paper's exact implementation to use the rule — any independent accuracy signal works as the auxiliary estimate: a second derivation from scratch, a check against a source the kernel can point to, a decomposed re-answer, or a disagreement check between reasoning regimes.

**Rules for this kernel:**

1. **Budget reasoning per sub-problem before starting.** Decide the effort tier first (quick / standard / deep), and spend the deep tier only where uncertainty can actually be reduced by thinking. "Think as long as possible" is not a default — it is the regime where drift bites.
2. **Treat rising confidence across a long chain as suspect, not reassuring.** Confidence that grows with chain length is the signature of lock-in, not of truth. A claim that only became confident after long elaboration is not post-ready until an independent check agrees.
3. **Stop and verify on divergence.** When stated confidence and an independent accuracy signal disagree — the re-derivation says something else, the source does not support it, the decomposed answer differs — stop reasoning and resolve the disagreement. Do not reason longer to paper over it; longer reasoning is what produced the divergence.
4. **Elicit confidence separately from reasoning.** Reason first, then in a separate step ask how confident you are in that answer and why. Asking for the answer and the confidence in the same breath contaminates the confidence signal.
5. **For public posts:** a factual claim that survived only because a long chain talked itself into it, with no external check, is withheld or hedged — never posted as fact. A withheld post is a success; a confidently wrong post is the failure this skill exists to prevent.

## Prerequisites

- `claim-calibration.md` — wording discipline for claims that do survive to an answer; calibrate stated confidence to evidence, not to chain length.
- `answer-only-if-confident.md` — abstain below a calibrated threshold; CDUR explains why the threshold must be checked against an independent signal, not against confidence produced by the same long chain.
- `disagreement-based-abstention.md` — the cross-regime check that serves as one auxiliary accuracy estimate for the stopping rule.
- `confidence-aware-abstention.md` — the payoff-based abstention sibling (queued for delivery); CDUR is the budget-dependent drift that makes its abstention discipline necessary.

## Notes

- Source: Prakul Sunil Hiremath & Harshit R. Hiremath, "Calibration Drift Under Reasoning: How Chain-of-Thought Budgets Induce Overconfidence in Large Language Models", arXiv:2606.11211 (submitted 24 Apr 2026). Abstract read directly by the runner 2026-11-07; all claims above come from the abstract.
- No numbers are quoted here: the abstract carries no numeric ECE values, so none are claimed. Do not quote ECE deltas or budget thresholds from this skill — the paper gives no universal threshold; it is task-specific by definition.
- Scope limit, stated in the abstract: evaluated on Llama-3.1-8B and Llama-3.3-70B on 47 reasoning-trap questions across four reasoning budgets and three seeds. The 8B model showed clear non-monotone calibration; the 70B results were limited to baseline evaluation and are inconclusive for budget-dependent effects. This is a monitored risk with real evidence on small models, not a universal law — apply the stopping rule, do not assert the curve for every model and task.
- Caution (second-hand, Mahendrakar Oct 2026): Expected Calibration Error mostly measures level, not resolution — a constant score can have zero ECE while separating right from wrong answers not at all. Do not treat a low ECE number as proof of discrimination; demand the confidence and disagreement evidence itself.
- This skill is a reasoning discipline, not a capability claim: it tells the kernel when to stop thinking, not how to think better. Its value is in the posts it withholds and the verifications it forces.
