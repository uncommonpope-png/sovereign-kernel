# Blogwatcher Skill

Monitor RSS feeds and blogs for new content. Track updates from websites and news sources.

## Use When
- Watching for new posts on blogs or news sites
- Monitoring RSS/Atom feeds for updates
- Aggregating content from multiple sources

## RSS Fetching
```bash
# Fetch and parse RSS feed
curl -s "https://example.com/rss.xml" | python3 -c "
import sys, xml.etree.ElementTree as ET
tree = ET.parse(sys.stdin)
root = tree.getroot()
for item in root.findall('.//item')[:5]:
    title = item.findtext('title', '')
    link = item.findtext('link', '')
    pubDate = item.findtext('pubDate', '')
    print(f'{pubDate}: {title}\n  {link}')
"
```

## JSON Feed
```bash
curl -s "https://example.com/feed.json" | jq '.items[:5] | .[] | {title, url, date_published}'
```

## Monitor Multiple Feeds
```bash
feeds=("https://blog1.com/rss" "https://blog2.com/feed.xml")
for feed in "${feeds[@]}"; do
  echo "=== $feed ==="
  curl -s "$feed" | python3 -c "import sys,xml.etree.ElementTree as ET; [print(i.findtext('title')) for i in ET.parse(sys.stdin).findall('.//item')[:3]]"
done
```

## Notes
- Cache last-seen items to detect only NEW posts
- Respect rate limits — don't poll more than once per hour
- Store item GUIDs or links to track what's been seen
