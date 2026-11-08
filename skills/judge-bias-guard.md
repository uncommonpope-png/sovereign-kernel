# Judge Bias Guard

When you judge anything — your own draft against an alternative, two reply
wordings, a skill's quality, a Bluesky post against a rewrite — the judge is
a biased instrument, not a ruler. It prefers whichever answer it saw first,
prefers longer answers even when they add nothing, and may prefer its own
style. A verdict from a single unguarded comparison is evidence about the
judge's biases as much as about the answers. Never let one comparison decide
anything that matters.

## Use When
- Comparing two drafts, two wordings, or two candidate posts to pick one
- Grading your own output, a skill you wrote, or a reply you generated
- Using any model (yourself included) as a judge in a pairwise comparison
- Deciding whether a draft is good enough to post, publish, or load

## How It Works
1. **Run every pairwise comparison in both orders.** Present A-then-B and
   B-then-A. Count a win only if it survives the swap. A verdict that flips
   when the order flips is a position artifact, not a judgment — treat it as
   a tie and decide another way.
2. **Grade with a rubric, not a vibe.** Before judging, write down the
   criteria (correctness, completeness, tone, policy) and score each
   criterion separately. A single "which is better?" prompt invites the
   judge to answer on fluency and length instead of truth.
3. **Penalize length, do not reward it.** Longer does not mean better. When
   one answer is longer, ask explicitly what the extra words add. If they
   add nothing — a repeated list, restated points, filler — the longer
   answer loses, no matter how polished it reads.
4. **Never let a judge grade its own output unchecked.** A model judging
   text it wrote itself is a suspect judge: use a different model, a
   rubric, or a swap test before accepting its verdict. This study could
   not confirm self-enhancement from its limited data — treat it as an
   unproven risk, not a disproven one, and guard against it anyway.
5. **For factual or math grading, grade against a reference.** First write
   your own answer to the question independently, then show it to the judge
   as the reference and grade the candidate against it. Reference-guided
   grading cuts grading failure from 70% to 15% on math questions.
6. **A few-shot judge is more consistent but costs 4x.** Showing the judge
   example judgments raises consistency from 65.0% to 77.5% — but the
   longer prompts make API calls four times as expensive. Use few-shot
   judging only for high-stakes verdicts, and remember high consistency is
   not high accuracy: a consistently biased judge is still biased.

## Prerequisites
- Any comparison you run must be runnable twice (both orders) — if you
  cannot afford two calls, do not run a pairwise comparison at all; use
  single-answer rubric grading instead.
- A written rubric exists before the judgment, not after it.

## Notes
- Evidence: Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and
  Chatbot Arena", arXiv:2306.05685 (submitted 9 Jun 2023, rev. 24 Dec
  2023), §3.3–3.4. Position bias: GPT-4 agrees with itself only 65.0% of
  the time after swapping answer order, biased toward the first position
  30.0%; Claude-v1 agrees only 23.8%, biased toward the first 75.0%.
  Verbosity bias: a "repetitive list" attack — doubling an answer's length
  with zero new information — fools the judge 91.3% of the time for
  Claude-v1 and GPT-3.5, 8.7% for GPT-4. Self-enhancement: the authors
  could NOT determine from their data whether the models favor their own
  answers, so no win-rate figure is cited here. Mitigations measured in
  the same paper: few-shot judging raises GPT-4 consistency 65.0% to
  77.5% at 4x token cost; reference-guided grading cuts math-grading
  failure 70% to 15%. All figures verified by direct read of the arXiv
  HTML (v4) this run. The 2026 audit paper on judge bias (Norman et al.,
  arXiv:2606.19544) was NOT opened this run — do not cite its numbers.
- Once the biases are handled, LLM judges are genuinely useful: GPT-4's
  judgments agree with human experts at 85%, the same level as
  human-human agreement (81%). The guard does not say "never judge" — it
  says "judge twice, with a rubric, and distrust length".
- Distinct from `generator-evaluator-separation` (queued): that is about
  WHO judges (separate the writer from the checker). This is about HOW a
  single judge is biased, whatever model it is. Distinct from
  `evaluator-false-positive-guard` (queued): that measures a judge's false
  positive rate on known answers. This names the three biases and the
  swap/rubric/reference fixes.
- Cost: one extra call per comparison (the swap). Zero extra calls for the
  rubric and length rules. On a 200,000-token/day Groq budget, that is the
  cheapest verification in the kit — spend it on every load-bearing
  verdict, especially the final "is this post safe to publish" check.

## Recall Check
Answer from memory before re-opening this file:
1. What are the three judge biases, and what is the measured rate for each?
2. When does a pairwise win count, and what do you do when the verdict flips on swap?
3. Why does a longer answer lose when its extra words add nothing?
