# Offload Arithmetic to Code

Never do multi-step arithmetic in the reasoning channel. Decompose the problem in prose, write a short program for the numbers, run it, and quote the program's output — not a re-typed number.

## Use When
- Any calculation with more than one arithmetic step
- Any money split, percentage, or funding total (PLT splits, preorder totals, bank-pack figures)
- Any count over a list (pieces, pins, skills, posts, "222" counts)
- Any number that will go into a public Bluesky post or an answer to Pope or Ms GCP
- Before drafting any post that states a total, a price, or a count

## How It Works
1. **Decompose in prose, solve in code.** State the steps and the formula in words first — that half stays yours. Then write a 3–10 line program that computes the answer and run it with `code-exec`, `shell-exec`, or `math-calc`. The program prints the answer; the post quotes the program's output verbatim.
2. **Read the code back against the problem before running it.** A wrong formula executed perfectly is still wrong. Check the inputs, the operations, and the units in the code against the problem statement.
3. **Code does arithmetic and lookup, never judgment.** Decomposition, formula choice, and "does this answer make sense" stay with the model. The code's output is read back, not blindly pasted. This is the boundary with `tool-induced-myopia-guard`: that skill stops tool output from replacing reasoning — this skill lets the tool do only the arithmetic the reasoning already decided.
4. **One fix, then abstain.** If the code errors, fix the code once. If it errors twice, stop: state the inputs and abstain on the total (see `answer-only-if-confident`) instead of guessing a number in prose.
5. **Single-step arithmetic is exempt.** One addition or one multiplication you can do cleanly in prose stays in prose. The rule bites at two steps and above, and always for money.

## Prerequisites
- `code-exec.md`, `shell-exec.md`, `math-calc.md` — the tools that run the program
- `answer-only-if-confident.md` — the fallback when the code will not run
- `tool-induced-myopia-guard.md` — the boundary: code computes, the model judges

## Notes
- Evidence: PAL (Gao et al., arXiv:2211.10435, ICML 2023). PAL using Codex beat PaLM-540B with chain-of-thought by an absolute 15% top-1 on GSM8K (v2 abstract, verified this run), and by 40% on GSM-HARD, the version with much larger numbers where mental arithmetic collapses (v1 abstract, verified this run). The method wins across 13 mathematical, symbolic, and algorithmic reasoning tasks — a much smaller model beating a 540B model by changing how it answers, not how big it is.
- Calibration bonus: Kabra et al. (arXiv:2311.09553, NAACL 2024) found program-aided reasoners better calibrated than chain-of-thought in 75% of instances (abstract, verified this run). A deterministic program output means confidence stops being a guess about your own arithmetic.
- Cost: one tool call, zero extra LLM calls — and it saves reasoning tokens, since no longhand arithmetic runs in the thinking channel. This kernel is a strong coder, so the procedure matches its strengths.
- Caveats, do not smooth over: the 15% and 40% figures are Codex-era; the PAL-vs-CoT gap on gpt-oss-120b itself is unmeasured — teach the procedure, cite the direction and magnitude, do not claim "15% on gpt-oss-120b". A 2026 robustness study (Kutakh, arXiv:2605.26414, secondary report) found code-based reasoning slightly less robust than CoT to problem variations, but the difference was not statistically significant (p=.096), and code-based models were more vulnerable to inserted distractor information — so on a noisy or adversarial problem statement, clean the problem first, then compute.
- Related: `step-back-prompting` (abstract first, then solve) pairs with this one — abstract, plan, then compute the numbers in code.
