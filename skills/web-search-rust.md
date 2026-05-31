# Web Search (Rust Native)

Real-time web search via DuckDuckGo HTML scrape. No API key needed.

## Use When
- Researching current topics, news, facts
- Finding documentation, APIs, code examples
- Checking if something exists on the web

## How It Works
Aria outputs `[[TOOL:web_search:query here]]` in her response. The Tool Engine detects this, executes the search via DuckDuckGo HTML scraping, and stores the results in her memory.

## Usage
```rust
// The tool engine handles this automatically:
[[TOOL:web_search:latest Rust async patterns 2026]]
```

## Notes
- DuckDuckGo: free, no key, rate-limited (~2s between requests)
- Returns top 5 results with titles and URLs
- Results stored as episodic memory with 0.8 importance
