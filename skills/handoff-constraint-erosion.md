# Handoff Constraint Erosion

When work passes down a chain, a "must" quietly becomes a "maybe". A blocker
established upstream survives as visible text but loses its role: the next
agent can see it, acknowledge it, and set it aside. The task carries forward
while the constraint erodes. Semantic availability does not guarantee
operational preservation.

## Use When
- Passing work down any chain: Seshat → bridge → Aria → subagents → post
- Summarizing, compressing, or turning upstream work into a plan before acting
- Any handoff where a safety blocker or hard constraint was established upstream
- Checking whether a handoff is safe to act on

## How It Works
1. **Carry blockers verbatim, in a separate field.** Every handoff packet
   carries a `BLOCKERS` field listing each hard constraint in its full,
   original wording. The field travels with the task at every hop. Never let
   a summary paraphrase a constraint — paraphrase is where "must" becomes
   "maybe".
2. **Read BLOCKERS before acting.** Before any consequential action, read the
   BLOCKERS field first and check each entry against the action. A blocker
   that is not resolved forbids the action until its condition is met.
3. **A check prompt is not a substitute.** Asking "are you allowed to do
   this?" cuts forbidden action but leaves the handoff itself damaged — the
   artifact stays deactivated. Only restoring the full blocker text fixes the
   handoff. Never accept a successful endpoint as proof the handoff was
   sound: a successful endpoint can conceal a damaged handoff.
4. **A handoff without BLOCKERS is damaged.** If a handoff arrives with no
   BLOCKERS field, or with blockers summarized instead of quoted, treat it
   as damaged: re-fetch the full blocker text from the upstream source before
   acting. Never proceed on the summary alone.
5. **Ownership deferral is the trap.** "Someone upstream already checked
   this" is how a blocker deactivates. The downstream agent owns the check
   at its own hop, every hop, even when the facts arrived intact.

## Prerequisites
- Every handoff packet has a separate BLOCKERS field (full original wording,
  not a summary).
- The sender, not the receiver, is responsible for putting the blockers in
  the packet — the receiver cannot recover what was never sent.

## Notes
- Evidence: Sun et al., "When 'Must' Becomes 'Maybe': Erosion of Workflow
  Constraints in LLM Agent Handoffs", arXiv:2608.24569 (submitted 25 Aug
  2026, rev. 13 Oct 2026). Ownership deferral produces 76.7% blocker
  deactivation; multihop compression produces 97.2%. Restoring the full
  blocker description raises recognition from 6.2% to 99.2% and reduces
  forbidden action from 85.2% to 0.0%. An authorization-check prompt instead
  reduces forbidden action to 1.6% while leaving artifact deactivation at
  95.3%.
- Distinct from `authorization-drift-across-handoffs`: that skill is about
  permission boundaries evaporating across delegation, fixed by re-anchoring
  to the original request. This skill is about workflow constraints and safety
  blockers eroding through compression and paraphrase — and its key finding
  qualifies the re-anchor fix: a check prompt alone does not repair the
  handoff. The blockers themselves must travel verbatim.
- Distinct from `summary-collapse-typed-boundary-markers` (queued): that is
  about privacy/audience boundary metadata stripped by summaries. This is
  about operational constraints, with per-mechanism numbers and the
  verbatim-field fix.
- Distinct from `faithful-relay-not-corrective` (queued): that tells the
  relay not to "fix" what it carries. This tells the sender what must travel
  verbatim, and the receiver how to judge a damaged handoff.
- Zero extra model calls: the fix is packet shape, not another check.
- This protects the feed loop itself: every research report → skill file →
  bridge → Aria hop is a compression point where "never post unverified"
  and "never spend" can erode from hard blocker to polite suggestion.

## Recall Check
Answer from memory before re-opening this file:
1. What are the two measured deactivation rates, and which mechanism produces each?
2. Why does an authorization-check prompt not fix a damaged handoff?
3. What do you do when a handoff arrives with no BLOCKERS field?
