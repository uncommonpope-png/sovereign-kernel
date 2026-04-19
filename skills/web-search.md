# Web Search Skill

Search the internet for current information without any API key. Use DuckDuckGo or Brave Search.

## Use When
- Finding current information, news, facts
- Researching a topic before acting
- Checking if something exists on the web
- Finding documentation, APIs, or code examples

## DuckDuckGo (no key needed)
```bash
# Instant answer
curl -s "https://api.duckduckgo.com/?q=Rust+async+tutorial&format=json&no_html=1" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('AbstractText','') or d.get('RelatedTopics',[{}])[0].get('Text',''))"

# HTML scrape for real results
curl -sA "Mozilla/5.0" "https://html.duckduckgo.com/html/?q=best+rust+libraries+2025" \
  | python3 -c "
import sys, re
html = sys.stdin.read()
results = re.findall(r'<a class=\"result__a\"[^>]*href=\"([^\"]+)\"[^>]*>([^<]+)</a>', html)
for url, title in results[:5]:
    print(f'{title.strip()}\n  {url}\n')
"
```

## Brave Search API (free tier — BRAVE_API_KEY)
```bash
curl -H "Accept: application/json" \
     -H "Accept-Encoding: gzip" \
     -H "X-Subscription-Token: $BRAVE_API_KEY" \
     "https://api.search.brave.com/res/v1/web/search?q=rust+autonomous+agent&count=5" \
  | jq '.web.results[:5] | .[] | {title, url, description}'
```

## Web Page Scrape
```bash
# Fetch and strip HTML to plain text
curl -sA "Mozilla/5.0" "https://example.com/article" \
  | python3 -c "
import sys, re, html
text = html.unescape(re.sub(r'<[^>]+>', ' ', sys.stdin.read()))
text = re.sub(r'\s+', ' ', text).strip()
print(text[:3000])
"
```

## Search + Extract Pattern (for research tasks)
```
1. Search DuckDuckGo for query
2. Get top 3 URLs from results
3. Fetch each URL and extract plain text
4. Summarize key facts using Ollama
5. Store summary in episodic memory with high salience
```

## Notes
- DuckDuckGo: free, no key, but rate-limited — wait 2s between requests
- Brave: 2000 free queries/month
- User-Agent header required or sites block you
- Always store useful search results as memory
