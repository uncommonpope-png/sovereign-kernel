# Illusion of Thinking: Complexity Collapse

Large reasoning models do not fail gradually as problems get harder — they collapse. Past a complexity threshold accuracy drops to zero, and, counterintuitively, the model spends *less* reasoning effort on harder problems even with token budget left. Keep every reasoning step in the medium-complexity band where reasoning actually helps.

## Use When
- Aria is about to reason through a hard problem before posting or acting
- A draft required long, multi-step reasoning to reach its conclusion
- Deciding whether to reason it out, answer directly, or hand the work to code
- A reasoning trace feels shorter than the problem deserves

## How It Works
Shojaee et al. (Apple, arXiv:2506.06941) tested large reasoning models on controllable puzzles where complexity could be dialed up while the logical structure stayed the same. Three regimes appeared:

1. **Low complexity** — standard (non-reasoning) models outperform reasoning models. Long reasoning is wasted effort and adds error surface.
2. **Medium complexity** — reasoning models have a real advantage. This is the only band where deep reasoning earns its keep.
3. **High complexity** — both kinds of model collapse completely. No amount of extra reasoning tokens saves the answer.

Two failure signatures to watch for:
- **Effort declines as difficulty rises.** Reasoning effort grows with complexity only up to a point, then *shrinks* despite remaining token budget. Shrinking effort on a still-hard problem is a failure signal, not efficiency.
- **No explicit algorithms, inconsistent across scales.** The models fail to use explicit algorithms for exact computation and reason inconsistently when the same problem is re-instantiated at a different scale. A conclusion reached at one scale may not survive at another.

Rules for Aria:
- **Decompose before reasoning.** Break any high-complexity task into medium-complexity steps first. Never attack a high-complexity problem in a single reasoning pass — that is the regime where collapse is guaranteed.
- **Answer low-complexity tasks directly.** If the task is simple, do not spin up long reasoning. Short answer, verify, post.
- **Treat shrinking effort as a stop signal.** If the reasoning trace gets shorter while the problem is still unsolved, stop. Decompose further, or restart from a smaller subproblem. Do not accept the short trace's conclusion.
- **Hand exact computation to code.** Multi-step arithmetic, counting, and algorithmic work go to `math-calc` or `code-exec`, never to the reasoning trace. The trace is for judgment, not computation.
- **Cross-scale check before posting.** Re-instantiate the same reasoning at a different scale (different numbers, names, or size) and compare conclusions. Inconsistency means the reasoning is untrusted — do not post it.
- **Never post a conclusion that came only from one long collapsed trace.** If the draft's key claim required high-complexity reasoning, verify it by decomposition or an independent check first (see `verify-before-posting`).

## Prerequisites
- `math-calc` / `code-exec` available for exact computation
- `verify-before-posting` for the pre-post check

## Notes
- Source: Shojaee, Mirzadeh, Alizadeh, Horton, Bengio, Farajtabar, "The Illusion of Thinking" (arXiv:2506.06941, Jun 2025, rev Nov 2025). Abstract verified directly this run.
- Distinct from queued `reasoning-budget` / truncated-CoT trap (that is about *truncation* cutting reasoning short; this is about the model itself collapsing and giving up) and from delivered `offload-arithmetic-to-code` (that is the remedy for one symptom; this is the diagnosis and the scoping rule).
- The three-regime rule is the whole skill: low = answer directly, medium = reason, high = decompose or hand off. If a task cannot be brought into the medium band, do not trust a reasoning-only answer.
