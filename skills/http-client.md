# HTTP Client Skill

Make HTTP requests to any API or web service. The kernel's generic interface to the outside world.

## Use When
- Calling REST APIs
- Sending webhooks
- Checking web service health
- Posting data to external services

## GET Request
```bash
# Simple fetch
curl -s "https://api.example.com/endpoint"

# With auth
curl -s -H "Authorization: Bearer $TOKEN" "https://api.example.com/data"

# With headers
curl -s -H "Accept: application/json" -H "X-API-Key: $KEY" "https://api.example.com/v1/resource"

# Parse JSON response
curl -s "https://api.example.com/data" | python3 -m json.tool
curl -s "https://api.example.com/data" | jq '.results[:3]'
```

## POST Request
```bash
# JSON body
curl -s -X POST "https://api.example.com/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name":"test","value":42}'

# Form data
curl -s -X POST "https://api.example.com/upload" \
  -F "file=@/path/to/file.txt" \
  -F "description=My upload"
```

## PUT / PATCH / DELETE
```bash
curl -s -X PUT "https://api.example.com/items/1" \
  -H "Content-Type: application/json" \
  -d '{"status":"active"}'

curl -s -X PATCH "https://api.example.com/items/1" \
  -H "Content-Type: application/json" \
  -d '{"field":"updated_value"}'

curl -s -X DELETE "https://api.example.com/items/1" \
  -H "Authorization: Bearer $TOKEN"
```

## Python Requests (for complex flows)
```python
import urllib.request, json

# GET
req = urllib.request.Request("https://api.example.com/data",
    headers={"Authorization": f"Bearer {TOKEN}"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read())
    print(data)

# POST
payload = json.dumps({"key": "value"}).encode()
req = urllib.request.Request("https://api.example.com/create",
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST")
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
```

## Response Handling
```bash
# Status code only
curl -s -o /dev/null -w "%{http_code}" "https://example.com"

# Full timing
curl -s -o /dev/null -w "DNS:%{time_namelookup} Total:%{time_total} Code:%{http_code}" "https://example.com"

# Follow redirects
curl -sL "https://example.com"

# Save to file
curl -s "https://example.com/file.zip" -o /tmp/download.zip
```

## Notes
- Always set --max-time to avoid hanging: curl --max-time 15
- Check HTTP status code before trusting response body
- Use -sS (silent but show errors) not just -s
- Store successful API patterns as procedural memories
