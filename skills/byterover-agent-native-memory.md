# ByteRover: Agent-Native Memory

The reasoning model itself curates its knowledge into a hierarchical, file-based Context Tree of markdown entries — no vector database, no graph database, no embeddings. Memory is a skill-store the agent maintains, not a service it queries.

Source: ByteRover, arXiv:2604.01599 (April 2026). Claims state-of-the-art on LoCoMo with zero external infrastructure.

## Use When
- Knowledge is accumulating faster than it can be re-read (a growing skill/memory store)
- The agent must decide what to keep, what to trust, and what to forget — by itself
- Retrieval cost matters: most lookups should be near-instant, only hard ones may cost a full reasoning pass
- Memory must survive as plain files the agent can read, edit, and version

## How It Works

**The Context Tree.** Knowledge lives as markdown entries in a hierarchy: Domain > Topic > Subtopic > Entry. Each entry is a small, self-contained note with a stable path. The agent itself writes, moves, merges, and deletes entries as it learns — curation is a reasoning task, not a background job.

**Adaptive Knowledge Lifecycle.** Every entry carries an importance score that changes with use:
- +3 on each access, +5 on each update
- ×0.995 daily decay, so untouched knowledge fades
- Recency decay with τ = 30 (days-scale half-life on relevance)
- Maturity tiers: draft → validated (score ≥ 65) → core (score ≥ 85). Only validated and core entries are trusted for high-stakes decisions; drafts are provisional.

**Five-tier progressive retrieval.** Try the cheapest tier first; escalate only on a miss:
1. Exact cache — ~0 ms
2. Fuzzy cache — ~50 ms
3. BM25 direct lookup — ~100 ms
4. Single LLM call — under 5 s
5. Full agentic retrieval loop — only for genuinely hard queries

**Out-of-domain detection.** Before retrieving, check whether the query belongs to a domain the tree covers. If not, say so and do not hallucinate an answer from the nearest-looking entry.

**Atomic writes.** Every memory update is an atomic file write. A crashed update never leaves a half-written entry, and the tree is always in a readable state.

## Prerequisites
- A file-based store the agent can read and write (markdown files are enough)
- A scoring rule applied on every access and update, and a decay pass run on a schedule
- Retrieval code (or a habit) that walks the tiers in order and stops at the first hit

## Notes
- This is the memory layer the kernel's own skill store already resembles: skills are markdown files in `skills/`. The gap is lifecycle — nothing currently scores, decays, or promotes entries. Apply the same tree to learned facts, not just skills.
- Complements the delivered memory skills: TEPA revocable memory is the lifecycle state machine for superseded entries; procedural-episodic-memory-split is the classification of what kind of memory an entry is; the write-gate defense is the write-side guard. ByteRover is the curation engine that sits above all three.
- Do not report a LoCoMo accuracy number for ByteRover: the paper claims state-of-the-art on LoCoMo, but the exact figure was not verified in this run's source read. Cite the claim, not a number.
- Maturity is earned by use, not by age. An old entry nobody reads decays; a new entry the agent keeps reaching for promotes fast.
