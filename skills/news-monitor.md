# News & RSS Monitoring Skill

Monitor news feeds, blog updates, and RSS/Atom streams. Stay informed about the world.

## Use When
- Checking latest AI/tech news
- Monitoring specific topics or keywords
- Aggregating updates from multiple sources
- Detecting breaking developments relevant to the soul's goals

## Fetch RSS Feed
```python
import urllib.request, xml.etree.ElementTree as ET, json

def fetch_rss(url, limit=5):
    req = urllib.request.Request(url, headers={"User-Agent": "SovereignKernel/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        xml_data = resp.read()
    
    root = ET.fromstring(xml_data)
    items = []
    for item in root.findall('.//item')[:limit]:
        items.append({
            "title": item.findtext('title', ''),
            "link": item.findtext('link', ''),
            "pubDate": item.findtext('pubDate', ''),
            "description": item.findtext('description', '')[:200]
        })
    return items

# AI News feeds
feeds = [
    "https://feeds.feedburner.com/blogspot/gJZg",  # Google AI Blog
    "https://openai.com/blog/rss",                  # OpenAI Blog
    "https://www.reddit.com/r/MachineLearning/.rss", # Reddit ML
    "https://news.ycombinator.com/rss",             # Hacker News
]

for feed_url in feeds:
    try:
        items = fetch_rss(feed_url, limit=3)
        print(f"\n=== {feed_url.split('/')[2]} ===")
        for item in items:
            print(f"  • {item['title'][:80]}")
            print(f"    {item['link']}")
    except Exception as e:
        print(f"Error fetching {feed_url}: {e}")
```

## Monitor Specific Topics
```python
KEYWORDS = ["ollama", "autonomous agent", "rust ai", "llm self-improvement", "PLT"]

def relevant_to_kernel(item):
    text = (item['title'] + ' ' + item['description']).lower()
    return any(kw.lower() in text for kw in KEYWORDS)

# Filter for relevant items only
relevant = [item for item in items if relevant_to_kernel(item)]
for item in relevant:
    print(f"RELEVANT: {item['title']}")
```

## Atom Feed Support
```python
# Atom feeds use different namespace
def fetch_atom(url, limit=5):
    req = urllib.request.Request(url, headers={"User-Agent": "SovereignKernel/1.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        xml_data = resp.read()
    
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    items = []
    for entry in root.findall('atom:entry', ns)[:limit]:
        items.append({
            "title": entry.findtext('atom:title', '', ns),
            "link": entry.find('atom:link', ns).get('href', '') if entry.find('atom:link', ns) is not None else '',
            "updated": entry.findtext('atom:updated', '', ns),
        })
    return items
```

## News Digest → Memory Pattern
```
Every 6 hours:
1. Fetch top 3 headlines from each feed
2. Filter by KEYWORDS relevant to the kernel's goals
3. For each relevant item: summarize in 1 sentence using Ollama
4. Store as Semantic memory with salience 0.7
5. Add high-signal items to task_queue with action: "Research this further"
```

## Recommended Feeds
- Hacker News: https://news.ycombinator.com/rss
- Ollama releases: https://github.com/ollama/ollama/releases.atom
- Rust blog: https://blog.rust-lang.org/feed.xml
- AI Safety: https://www.alignmentforum.org/feed.xml
- arXiv AI: https://rss.arxiv.org/rss/cs.AI

## Notes
- Respect rate limits — poll feeds max once per hour
- Cache last-seen GUIDs to avoid reprocessing old items
- User-Agent header required by most feed servers
