# xURL Skill

Advanced URL operations — fetch, transform, validate, and analyze URLs and HTTP responses.

## Use When
- Fetching URLs with custom headers or methods
- Analyzing HTTP responses (status, headers, redirects)
- Batch URL operations or link checking

## Basic Operations
```bash
# Fetch URL
curl -s "https://example.com"

# Show headers only
curl -sI "https://example.com"

# Follow redirects and show final URL
curl -sL -o /dev/null -w "%{url_effective}" "https://example.com"

# Full request/response info
curl -v "https://example.com" 2>&1 | head -30

# Time breakdown
curl -s -o /dev/null -w "DNS:%{time_namelookup} Connect:%{time_connect} TTFB:%{time_starttransfer} Total:%{time_total}" "https://example.com"
```

## HTTP Methods
```bash
# POST with JSON
curl -X POST "https://api.example.com/data" \
  -H "Content-Type: application/json" \
  -d '{"key":"value"}'

# PUT
curl -X PUT "https://api.example.com/items/1" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name":"updated"}'

# DELETE
curl -X DELETE "https://api.example.com/items/1" \
  -H "Authorization: Bearer $TOKEN"
```

## URL Validation and Analysis
```bash
# Check if URL is reachable
curl -s --max-time 5 -o /dev/null -w "%{http_code}" "https://example.com"

# Extract all links from a page
curl -s "https://example.com" | grep -oE 'href="[^"]+"' | cut -d'"' -f2

# Batch link checker
while read url; do
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$url")
  echo "$code $url"
done < urls.txt
```

## Notes
- curl is universally available (macOS, Linux, Windows)
- -L follows redirects, -s silent, -I headers only
- Use --user-agent for sites that block default curl UA
