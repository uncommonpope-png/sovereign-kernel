# Context Rot Diagnosis (Diagnose Which Context Failure You Have Before You Fix It)

A long-running agent degrades in four distinct ways, and the wrong fix makes it worse. Compaction cures distraction but bakes poisoned facts in. Never apply a fix until you have named which failure you are looking at.

## Use When
- A run has gone long and answers, posts, or actions are drifting, repeating, or contradicting earlier ones
- Before compacting, summarizing, or restarting a session — the fix depends on the diagnosis
- After a surprising or wrong output from a run that was working fine earlier
- When deciding whether to trust a fact that has survived several sessions

## How It Works
1. Name the failure mode. There are four, each with a different fix:
   - **Poisoning:** a hallucination or wrong deduction got saved (into memory, a summary, a plan) and is now treated as fact. Sign: the same wrong claim keeps reappearing even after correction. **Fix: trace it to the saved source and correct or remove it there.** Never compact it in — summarization strips the provenance that would let you spot it.
   - **Distraction:** history has grown so long the model repeats past actions and loses the current task. Sign: looping, re-doing completed steps. **Fix: compact or summarize, or start a fresh session with a structured handoff.** Compaction is the fix for distraction ONLY.
   - **Confusion:** superfluous content — too many tool definitions, irrelevant history — degrades responses. Sign: wrong tool chosen, garbled parameters, answers that wander. **Fix: trim what is loaded.** Drop unused tools and irrelevant context; do not add more.
   - **Clash:** new information conflicts with older context. Sign: the run flip-flops between two versions of a fact. **Fix: resolve explicitly.** Decide which is true, keep the verified one, record the resolution, and discard the loser — do not let both live side by side.
2. Keep three things outside anything a summarizer can touch: the task statement, the authorization record, and the ledger of actions already taken. Prefer filesystem state (a spec file, a progress file) over an infinite context window.
3. Treat a single summarization as a risk event: one 2026 study found a single summarization flips a correct answer to a wrong one in roughly 40% of the transitions it touches. After compacting, re-check the three protected items before acting.
4. Do not trust the advertised window. Accuracy starts falling far earlier — one study saw it fall near 32,000 tokens on a 405B model, and on LongMemEval a focused ~300-token prompt beat the same question buried in ~113,000 tokens of history for every model family tested. If the answer is in the middle of a long context, it is the most likely to be missed.

## Prerequisites
- A way to see what is in context (session log, memory store, or handoff file) so the failure can be named, not guessed
- verify-before-posting.md and claim-calibration.md — those check the output; this checks the context the output was built from

## Notes
- Poisoning is the most dangerous mode for this kernel: a wrong fact saved into memory gets re-read as truth on every later step, and every re-telling can entrench it further. See also reconsolidation-guard (queued) for the memory side of the same problem.
- If you cannot name the mode, do not fix anything. Restart from a clean handoff instead of compacting a context you do not understand.
- Sources: Breunig's context-rot taxonomy (poisoning / distraction / confusion / clash); Chroma context-rot research, 18 models; Anthropic, "Effective harnesses for long-running agents" (Mar 2026, published Nov 5, 2026); Databricks long-context study; Liu et al., "Lost in the Middle" (arXiv:2307.03172); NoLiMa (arXiv:2502.05167).
