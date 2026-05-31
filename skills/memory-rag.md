# Memory RAG (Keyword Search)

Search across all memories using keyword matching to find relevant context.

## Use When
- Aria needs to recall past events, conversations, decisions
- Finding relevant context before responding
- Connecting current experiences with past patterns

## How It Works
The `search_memories_by_keyword()` function searches all stored memory entries for keyword matches, scoring each by match count × importance. Results are sorted by relevance.

## Usage
The Tool Engine can query: `[[TOOL:search_memory:what did Craig say about deployment?]]`

## Notes
- Searches all memories (episodic + semantic) up to 500 entries
- Keywords are extracted from the query (words > 2 chars)
- Results weighted by memory importance (0.0–1.0)
- No external API or embedding model needed
- Deployed: fully local, zero cost
