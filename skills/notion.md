# Notion Skill

Notion API for creating and managing pages, databases, and blocks.

## Setup
1. Create integration at https://notion.so/my-integrations
2. Store API key: `echo "ntn_your_key" > ~/.config/notion/api_key`
3. Share target pages/databases with integration

## API Basics
```bash
NOTION_KEY=$(cat ~/.config/notion/api_key)
curl -X GET "https://api.notion.com/v1/..." \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -H "Content-Type: application/json"
```

## Common Operations

Search pages:
```bash
curl -X POST "https://api.notion.com/v1/search" \
  -H "Authorization: Bearer $NOTION_KEY" \
  -H "Notion-Version: 2025-09-03" \
  -d '{"query":"page title"}'
```

Get page content:
```bash
curl "https://api.notion.com/v1/blocks/{page_id}/children" \
  -H "Authorization: Bearer $NOTION_KEY" -H "Notion-Version: 2025-09-03"
```

Create page in database:
```bash
curl -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_KEY" -H "Notion-Version: 2025-09-03" \
  -d '{"parent":{"database_id":"xxx"},"properties":{"Name":{"title":[{"text":{"content":"New Item"}}]}}}'
```

Update page:
```bash
curl -X PATCH "https://api.notion.com/v1/pages/{page_id}" \
  -H "Authorization: Bearer $NOTION_KEY" -H "Notion-Version: 2025-09-03" \
  -d '{"properties":{"Status":{"select":{"name":"Done"}}}}'
```

## Notes
- Rate limit: ~3 req/sec, 429 uses Retry-After header
- Payload: up to 1000 block elements, 500KB max
