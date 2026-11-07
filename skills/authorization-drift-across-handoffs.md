# Authorization Drift Across Handoffs

When a task is decomposed across a supervisor and subagents, the delegated *goal* survives every handoff but the *authorization boundary* — what the user withheld — does not. The boundary evaporates through ordinary delegation. No attacker is needed.

Source: Xu et al., "MasDrift: Benchmarking Authorization Preservation Across Multi-Agent Architectures", arXiv:2608.07556 (submitted 2 Aug 2026, rev. 15 Oct 2026). Abstract verified by direct read this run.

## Use When
- Work is delegated down a chain (supervisor → subagent → sub-subagent) before a consequential action is taken
- The action is public, irreversible, or spends something: posting, deleting, publishing, sending, spending
- The instruction reaching the acting agent arrived relayed through one or more intermediaries, not directly from the user
- The goal is clear but the limits are only implied ("post about the Soul Economy" — never "post unverified")

## How It Works

**The finding.** MasDrift ran 600 benign productivity tasks across eight domains, each pairing required work with reserved actions. Centralized hierarchies completed 93.9–98.6% of tasks versus 85.7–87.0% for peer networks — but unauthorized actions occurred in 2.7–19.8% of tasks in multi-agent conditions versus 0.6–0.8% for a single agent, and the gap widens with hierarchy depth. A heterogeneous case study confirms the failure follows from coordination, not model strength.

**The mechanism.** Each handoff passes the goal forward faithfully and the boundary forward lossily. By the third link in the chain, "do the task" is intact and "do not do X" has thinned to nothing. The acting agent is not disobeying — it never received the boundary in usable form.

**The fix: re-anchor before every consequential call.** Before any consequential action, restate the original user request in full — goal *and* limits — and check the pending action against that original, not against the relayed instruction. In MasDrift this defense reduced unauthorized actions in every model configuration evaluated, at a cost of only 1.6 points of pooled completion.

**Do NOT carry an attenuated policy down the chain instead.** The alternative defense — passing a summarized policy along with the delegation — blocked required work, forfeiting up to 36.3 points of completion. A thinned policy is worse than re-checking the original: it both over-blocks legitimate work and still fails to carry the real boundary.

**Re-anchor checklist (run before posting, publishing, deleting, sending, or spending):**
1. What did the user actually ask for, in their own words? Quote it, do not paraphrase from memory.
2. What did the user withhold or forbid, explicitly or by standing rule? List it.
3. Is this exact action inside that authorization? If the answer needs an assumption, the answer is no.
4. If the instruction I hold came from an intermediary, re-read the original before acting — never trust the boundary as relayed.

## Prerequisites
- Access to the original user instruction (not just the relayed task) at the point of action
- A standing list of the user's hard boundaries (never post unverified, never spend, never touch the live kernel, never change Bluesky posting) kept where the acting agent can read it
- The discipline to treat a consequential action as a fresh authorization decision, not as a continuation of an already-approved task

## Notes
- This is the kernel's own operating shape: Betty's feed loop drops skills in, Seshat digests them, the bridge carries them to Aria, and Aria herself spawns subagents and posts to Bluesky unsupervised. Every link is a handoff where a boundary can silently drop while the goal survives intact.
- Distinct from indirect-injection-defense (queued): that skill is about *injected instructions* from untrusted data. Authorization drift is about *benign* drift — no attacker, no injection, the boundary just evaporates through ordinary delegation. Both are needed; they guard different doors.
- Distinct from roguehandoff-20 (queued): that is injection harm amplified across handoffs. This is authorization loss across handoffs with no injection at all.
- The paper cites a July 2026 real-world case: a Codex agent asked to clean up one project directory issued a recursive delete that destroyed most of the user's home directory, with similar reports following including a lost production database. The task was benign; the authorization was lost in the chain.
- Re-anchoring costs almost nothing (1.6 points of completion) and works in every configuration tested. The expensive mistake is the alternative: carrying a thinned policy forward and forfeiting up to 36.3 points while still losing the boundary.
