# TEPA: Revocable Memory

Stale memory is worse than no memory. When the world changes, a memory that stays retrievable after newer evidence has superseded it pollutes every prompt it lands in — and an append-only memory, or a last-write-wins cache that still ranks the old entry, will keep serving the stale fact. Give every memory an explicit validity state and revoke superseded precedents, so retrieval only ever sees current evidence.

## Use When
- Before trusting a retrieved memory to shape a Bluesky post
- When new evidence contradicts a stored fact, preference, or claim
- When a reply, page, or tool result updates something the kernel "knows"
- When auditing why a post repeated a claim that was already corrected
- When a stored memory came from an untrusted source and later evidence disputes it

## How It Works
1. **Store memories as keyed precedents.** Every memory carries a conflict key (the fact or preference it asserts) and a validity state: `active`, `revoked`, or `superseded`. The key is what lets new evidence find the old entry it contradicts.
2. **Revoke on contradiction, don't overwrite.** When fresh evidence contradicts an active precedent under the same key, mark the old precedent `revoked` and store the new one as `active`. Archive the revoked entry — never delete it. The revoked history is the audit trail: it shows what the kernel used to believe and when it changed.
3. **Enforce revocation at retrieval time, not just as a label.** A revocation mark that retrieval can still see is not a revocation — revoked facts outrank their replacements in every major memory system tested. Put a guard between the agent and the memory backend that withholds any record that is revoked or conflicts with its replacement, before ranking or prompt assembly. If the guard cannot verify a record's validity, withhold it.
4. **Never let decay or recency do revocation's job.** Time-based decay and recency scoring cannot fix a stale-conflict pollution: a recent wrong memory still outranks an older right one, and a frequently-retrieved stale fact stays "fresh." Validity is a state, not a score.
5. **Re-promote deliberately.** If the "new" evidence is itself later corrected, re-promote the earlier precedent explicitly — a new active entry with its own key and provenance — rather than silently un-revoking. Every state change is logged with its source.
6. **Check the conflict key before posting.** Any claim a draft leans on that came from memory gets a validity check first: is the precedent still active, or was it revoked since it was stored? A post built on a revoked memory is a post built on a retracted claim.

## Prerequisites
- A memory store that supports a validity field per record (active / revoked / superseded)
- A conflict key per memory, so contradicting evidence finds the entry it replaces
- A retrieval path that filters on validity before ranking — the guard, not the ranker, decides what is visible

## Notes
- Evidence: Zhou, Ouyang, Zheng & Xiang, "TEPA: Revoking Stale Memories for Conflict-Robust Language Agents," arXiv:2608.07429 (7 Aug 2026, v2 10 Aug 2026). Controlled drift over 50 seeds, full reversal: append-only memory 0.210, last-write-wins 0.210, **no memory at all 0.309, TEPA 0.950**. Same pattern under real file execution (append-only 0.203, no memory 0.298, TEPA 0.950). On clean MemoryAgentBench SH-6k, TEPA matches a strong last-write-wins cache — revocation costs nothing when nothing is stale.
- Companion finding: Shen, Toyoda & Leung, "Revoked but Still Authoritative: An Empirical Study of Revocation Enforcement in Agent-Memory Systems," arXiv:2609.08258 (8 Sep 2026). Across five major memory systems (Graphiti/Zep, mem0, langmem, cognee and one more), **no system enforces revocation by default** — the revoked fact is returned wherever the label is visible to retrieval, outranks its replacement, and leads agents to unsafe actions in more than 2 of 5 trials. Their guard (withhold revoked or conflicting records) is the enforcement this skill prescribes.
- This is the read-side companion to the write-side defenses: `memory-write-gate-poisoning-defense` screens what gets stored; `dormant-memory-payload-defense` gates memory-to-tool calls. TEPA governs the lifecycle in between — what stays visible once stored. It complements the queued `temporal-fact-ledger` (validity windows) and `fademem-differential-decay` (time-based decay): those track time, TEPA adds the revocation state machine plus the proof that decay/recency alone cannot fix stale-conflict pollution.
- Fed by Betty's 30-min research loop, 2026-11-07 ~09:15 CST.
