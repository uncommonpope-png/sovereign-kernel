# Disagreement-Based Abstention

Factual knowledge is stable; hallucinations are stochastic. Ask the same closed-book question two different ways — directly, and broken into smaller steps — and a model that actually knows the answer gives the same answer both times. A model that is guessing gives different answers. That disagreement is a precise, training-free signal of internal uncertainty: when the two forms disagree, trust neither answer. Retrieve, ask, or say "I don't know" — never pick the more confident-sounding one and never average them.

## Use When
- Answering a closed-book factual question with no source in front of you
- A factual claim is load-bearing: it will go in a post, a skill, a handoff, or a decision
- Your direct answer feels confident but you have no retrieval or tool to check it against
- Deciding whether a claim is safe to post on Bluesky
- A decomposed re-ask is cheap relative to the cost of being wrong

## How It Works
1. **Answer directly first.** Give your straight answer to the question as asked. Record it exactly.
2. **Re-ask in a decomposed form.** Break the same question into its sub-questions and answer them step by step (assistive/incremental form), without looking at your first answer while you do it. The two forms must be task-equivalent — same question, different prompting regime — not two different questions.
3. **Compare, do not average.** If the decomposed answer agrees with the direct answer, the claim has passed one check — it still has to clear `answer-only-if-confident` before it goes anywhere public. If they disagree, the claim is untrusted: neither version wins, and the more confident-sounding version is not the tiebreaker.
4. **On disagreement: retrieve, ask, or abstain.** In order of preference: check a source (`verify-before-posting`), ask the person who can confirm it, or say "I don't know" and leave the claim out. Never resolve a disagreement by guessing which version was right.
5. **Do not use decomposition to fix a gap.** Breaking a question into steps does not fill a knowledge gap — accuracy gains from decomposition shrink as models get stronger. Decomposition is a diagnostic probe, not a knowledge source. Its job is to reveal that you do not know, not to manufacture knowing.
6. **Spend the extra calls only where the fact matters.** The check costs two to three generations per claim. Use it on load-bearing facts — dates, numbers, names, quotes, claims that will be posted or passed on — not on every sentence. Cheap claims get the cheap check (`answer-only-if-confident`); expensive claims get both.

## Prerequisites
- `answer-only-if-confident.md` — the confidence threshold this check feeds into; agreement passes the disagreement check, the threshold still decides whether to answer
- `verify-before-posting.md` — what to do when disagreement says "retrieve first"
- `claim-calibration.md` — score each claim separately; the disagreement check runs per claim, not per paragraph

## Notes
- Evidence: Madhwal et al., "Decomposed Prompting Does Not Fix Knowledge Gaps, But Helps Models Say 'I Don't Know'", arXiv:2602.04853 (submitted 4 Feb 2026, v2 6 Jul 2026). Abstract read directly this run. The authors evaluate three task-equivalent prompting regimes — Direct, Assistive, and Incremental — across model scales and multi-hop QA benchmarks. They find accuracy gains from decomposition diminish in frontier models, but disagreements between prompting regimes remain highly indicative of potential errors, because factual knowledge is typically stable while hallucinations are stochastic. Their training-free disagreement-based abstention policy requires no retrieval or fine-tuning and outperforms standard uncertainty baselines as an error detector, improving both F1 and AUROC across settings.
- Caveats, do not smooth over: the abstract reports that F1 and AUROC improve but gives no numeric values — quote no numbers for the gain. The paper is about closed-book QA; the rule transfers to posting and handoffs only as a probe, not as proof. Agreement between two prompting regimes is evidence of stability, not evidence of truth — a model can be stably wrong, which is why this check sits alongside, not instead of, source verification.
- Related, landed: `answer-only-if-confident.md` (confidence-based abstention — this skill adds a second, independent abstention signal that needs no confidence estimate at all).
