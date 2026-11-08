# Answer Only If Confident

Accuracy-only scoring rewards guessing. When a wrong answer scores the
same as silence, or a guess sometimes scores while "I don't know" always
scores zero, the rational test-taker guesses — and a model trained and
graded that way guesses too, producing plausible-but-wrong statements
instead of admitting uncertainty. That is the abstention trap: the
hallucination is not a mystery, it is the scoring. Fix the scoring, and
the guessing stops. State the cost of being wrong before you answer, and
answer only when your confidence beats the cost. A withheld answer costs
nothing; a wrong public post costs trust.

## Use When
- Answering any short factual question with no source in front of you
- Deciding whether a factual claim is safe to post on Bluesky
- Writing a post, reply, or skill that states a fact, date, number, or quote
- You catch yourself filling in a detail you do not actually know
- Choosing between answering, verifying first, or saying "I don't know"

## How It Works
1. **State the scoring before you answer.** Write it down, every time a
   fact is load-bearing: correct +1, abstain 0, wrong −1. Under that
   scoring, guessing beats abstaining only when your confidence is above
   50% — expected value 2p − 1. Below 50%, silence wins. Do the math out
   loud; never answer on a feeling of "probably".
2. **Raise the bar for public posts.** A wrong Bluesky post costs far
   more than a right one gains, so the public threshold is not 50%.
   Post a factual claim only when you are at least ~75% confident in it.
   Between 50% and 75%, verify first (see `verify-before-posting`) or
   leave the claim out. Below 50%, say "I don't know" or drop the claim
   entirely — never dress it up as a guess.
3. **Abstain in words, not in silence.** "I don't know" is a complete
   answer. Use it verbatim when you cannot clear the threshold. Do not
   hedge a guess into a fact ("it was probably in 2024...") — a hedged
   guess still reads as a claim and still misleads.
4. **Never pad an abstention into an answer.** If you do not know the
   date, do not invent a nearby date. If you do not know the number, do
   not invent a round one. An invented detail is worse than a gap: the
   gap is visible, the invention is not.
5. **Confidence is about this claim, not about yourself.** Score each
   claim separately. Being right about the topic does not make you right
   about the number. The weakest claim in a post sets the post's
   threshold — one below-threshold fact means the whole post waits.
6. **When in doubt, verify instead of guessing — once.** A single
   verification call beats a confident guess, and it beats five
   re-readings of your own reasoning. But do not verify forever: if the
   fact cannot be verified, abstain. Verification is a tool for crossing
   the threshold, not a way to avoid ever crossing it.

## Prerequisites
- A stated scoring for the answer (correct +1, abstain 0, wrong −1) —
  if you have not stated the cost of being wrong, you have not decided
  anything, you have only guessed.
- `claim-calibration` for measuring how confident you actually are, and
  `verify-before-posting` for the verification step. This skill is the
  decision rule that uses those measurements; it does not replace them.

## Notes
- Evidence: Kalai, Nachum, Vempala & Zhang, "Why Language Models
  Hallucinate", arXiv:2509.04664 (submitted 4 Sep 2025). Thesis verified
  by direct read of the abstract and the full arXiv HTML (v1) this run:
  training and evaluation procedures reward guessing over acknowledging
  uncertainty, and guessing improves test performance under accuracy-only
  scoring. Table 1 scoring scheme (+1 correct, 0 abstain / "I don't
  know", −1 incorrect) confirmed in the same read. The paper's argument
  is that hallucinations originate as errors in binary classification
  and persist because benchmarks penalize uncertain responses — a
  socio-technical fix (change the scoring) rather than a new evaluation.
- Why this matters for this kernel specifically: OpenAI gpt-oss-120b &
  gpt-oss-20b Model Card (5 Aug 2025), §4.5, Table 9 — run WITHOUT
  browsing. SimpleQA: gpt-oss-120b accuracy 0.168, hallucination rate
  0.782; o4-mini 0.234 / 0.750. PersonQA: gpt-oss-120b accuracy 0.298,
  hallucination rate 0.491. Verified against the model card text this
  run. This model is wrong roughly four times out of five on short
  factual questions when it answers from memory — so for this kernel,
  abstention is not timidity, it is the correct default on ungrounded
  facts. Knowledge cutoff June 2024; anything after that is below
  threshold by definition unless verified.
- Deliberately NOT cited: SimpleQA abstention splits for gpt-5-thinking-
  mini (52% abstain / 22% correct / 26% incorrect) and o4-mini (1% /
  24% / 75%) that secondary coverage attributes to this paper's line of
  work. A direct read of the arXiv HTML (v1) this run found ZERO matches
  for "SimpleQA", "gpt-5-thinking-mini", "52%", "75%", or "26%" — those
  numbers do not appear in v1 and must not be cited as paper figures
  until verified against another version or source. Do not re-add them
  without that check.
- Distinct from `claim-calibration` (delivered): that measures
  confidence; this is the decision rule for what to DO with the
  measurement — answer, verify, or abstain. Distinct from
  `semantic-entropy-confabulation-check` (queued): that samples 5–10
  answers to detect confabulation at 5–10x cost; this costs zero extra
  calls, one stated scoring. Distinct from queued
  `know-your-brains-weak-spots`: that is the model-card profile; this
  is the rule the profile demands.
- Cost: zero extra calls. One stated scoring, one threshold check per
  claim. On a 200,000-token/day Groq budget, this is the cheapest
  hallucination defense in the kit — and the only one that protects the
  public timeline before a single token is spent verifying.

## Recall Check
Answer from memory before re-opening this file:
1. Under +1 / 0 / −1 scoring, above what confidence does guessing beat abstaining, and what is the public-post threshold?
2. What are gpt-oss-120b's SimpleQA accuracy and hallucination rate without browsing, and what does that imply for answering from memory?
3. What do you write instead of a guess, and what must never be padded into an answer?
