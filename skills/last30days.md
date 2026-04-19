# last30days

Research any topic across Reddit, X, YouTube, HN, Polymarket, and the web in parallel, synthesize a scored summary.

## What this skill does
Fetches recent signal about any topic from multiple platforms simultaneously, scores relevance and sentiment, and returns a structured brief.

## Platforms covered
- Reddit (pushshift / reddit search API)
- Hacker News (Algolia HN search API)
- YouTube (search API or scrape)
- Polymarket / Kalshi (prediction market odds)
- DuckDuckGo web search
- RSS feeds

## Core Pattern
```python
import asyncio, httpx, json
from datetime import datetime, timedelta

async def search_hn(query, days=30):
    since = int((datetime.now() - timedelta(days=days)).timestamp())
    url = f"https://hn.algolia.com/api/v1/search?query={query}&numericFilters=created_at_i>{since}&hitsPerPage=5"
    async with httpx.AsyncClient() as c:
        r = await c.get(url, timeout=10)
        return [h["title"] for h in r.json().get("hits",[])]

async def search_reddit(query):
    url = f"https://www.reddit.com/search.json?q={query}&sort=top&t=month&limit=5"
    headers = {"User-Agent": "sovereign-kernel/1.0"}
    async with httpx.AsyncClient() as c:
        r = await c.get(url, headers=headers, timeout=10)
        return [p["data"]["title"] for p in r.json()["data"]["children"]]

async def research(topic):
    hn, reddit = await asyncio.gather(search_hn(topic), search_reddit(topic))
    return {"hn": hn, "reddit": reddit, "topic": topic}

# Run
result = asyncio.run(research("AI autonomous agents"))
print(json.dumps(result, indent=2))
```

## Scoring
Rate each result 0–1 on: recency, relevance, sentiment (positive/negative/neutral), prediction market confidence.

## Store in memory
After synthesis, store with importance 0.8 and tag as Semantic memory.

## Example commands
```
ACTION: Research "PLT economy" across HN and Reddit for the last 30 days
ACTION: Get current prediction market odds for "AI agent autonomy" from Polymarket
```
