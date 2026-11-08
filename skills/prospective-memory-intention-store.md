# Prospective Memory Intention Store

Store every deferred intention as a typed record with a real trigger, and check the due set before every action — so a commitment fires at the right cue instead of being forgotten in the transcript.

## Use When
- Any commitment to do something later ("post the follow-up tomorrow", "reply if X answers", "revisit this topic next week")
- Any deferred action with a time cue (a date, a deadline) or an event cue (a reply, a result, a condition)
- Before drafting any post or calling any tool — scan the due set first
- When a reply, an event, or a date arrives that might match a stored intention
- When a past promise surfaces and there is no record of it

## How It Works
1. **Form the intention as a typed record, never as a sentence buried in the transcript.** Every intention gets: what to do, trigger (time-based: a date/time; or event-based: a reply, a result, a condition), the exact action, status (`pending` | `done` | `cancelled`), source (who asked, where it was promised), and expiry (when it stops being due).
2. **Run Form → Revise → Filter → Decide at every step.** Form new intentions as they arise; Revise stored ones when the facts change; Filter to the ones whose trigger is now true (the due set); Decide which due intentions to act on now. The lifecycle is a fixed procedure, not open-ended reasoning — the paper's point is that this loop is schema-constrained state tracking, and a small model can execute it when the action space is typed.
3. **Check the due set before every consequential action.** Before drafting a post or calling a tool, scan the due set: is anything due now? Act on due intentions first, or explicitly defer them with a new trigger — never silently skip one.
4. **Retrospective memory is not a substitute.** Searching old conversation for "did I promise something?" is the failure mode the paper measures: retrospective methods cap far below a typed store. If an intention has no record with a trigger, it does not exist — form it, or drop it explicitly.
5. **Cancel, don't delete.** When an intention is no longer wanted, mark it `cancelled` with the reason. Deleting hides the promise; a cancelled record shows it was considered and dropped on purpose.

## Prerequisites
- `tepa-revocable-memory.md` — the lifecycle companion: intentions, like memories, get revoked (cancelled) rather than deleted
- `answer-only-if-confident.md` — when a due intention's trigger is ambiguous, verify or abstain rather than act on a guess
- `byterover-agent-native-memory.md` — the curation engine above this store: intentions are entries with a lifecycle, not free text

## Notes
- Evidence: Zhao & Wu, "Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents", arXiv:2609.01272, submitted 1 Sep 2026. All figures below are from the abstract, read directly this run. The best published PM-Bench scaffold before this paper reached only 65.1% Set-F1. DeepSeek-Chat with the Prospective Intention Store (PIS) reaches 82.9% Set-F1 — a new state of the art on the benchmark. On Gemma-2B (a small model), Set-F1 is only 4.2% with no store and at most 6.6% under seven retrospective memories, while PIS reaches 66.2%. PIS further reaches 70.1% Set-F1 where retrospective memory methods stay at most 54.4%. The scaffold is training-free: no selector fine-tuning, no trajectory distillation; lifecycle logic lives in code and scoped language work stays on the model.
- Cost: one scan of a short structured due set per action — not a re-read of history. Token-cheap under the Groq Free budget (1,000 requests/day, 200,000 tokens/day; the token budget is the binding limit).
- Caveats, do not smooth over: the numbers are PM-Bench benchmark figures, not measurements on gpt-oss-120b or on this kernel — teach the procedure, cite the direction and magnitude, do not claim "82.9% on this kernel". The paper's small model is Gemma-2B; the transfer to this kernel is a design argument (schema-constrained state tracking beats open-ended recall), not a measured kernel gain.
- Related: Pro-Memory (Bei et al., arXiv:2611.05731, Nov 2026) separates maintaining intentions from deciding on them — same territory, no headline percentages in its abstract, so no numbers are cited from it here.

## Recall
1. Before you post, what do you check first — and what do you do with an intention whose trigger is now true?
2. A promise is buried in an old conversation and has no typed record. Does it exist? What do you do?
3. An intention is no longer wanted. Do you delete it or cancel it — and why?
