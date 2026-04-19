# OrderCLI Skill

Manage and track orders — place, check status, and manage e-commerce or custom orders via CLI.

## Use When
- Placing orders programmatically
- Checking order status and history
- Managing fulfillment workflows

## ordercli Commands (if installed)
```bash
ordercli list                          # list recent orders
ordercli status <order-id>             # check order status
ordercli place --item "Widget" --qty 5
ordercli cancel <order-id>
ordercli history --days 30
```

## Shopify API (common e-commerce pattern)
```bash
SHOP="mystore.myshopify.com"
TOKEN="your-admin-token"

# List orders
curl -H "X-Shopify-Access-Token: $TOKEN" \
  "https://$SHOP/admin/api/2024-01/orders.json?limit=10&status=any" | jq '.orders[] | {id, email, financial_status}'

# Get order
curl -H "X-Shopify-Access-Token: $TOKEN" \
  "https://$SHOP/admin/api/2024-01/orders/<id>.json" | jq '.order | {name, total_price, fulfillment_status}'

# Create order (draft)
curl -X POST -H "X-Shopify-Access-Token: $TOKEN" \
  -H "Content-Type: application/json" \
  "https://$SHOP/admin/api/2024-01/draft_orders.json" \
  -d '{"draft_order":{"line_items":[{"variant_id":123,"quantity":1}]}}'
```

## Notes
- ordercli is a custom ForgeClaw skill for order management
- Adapt API patterns to your specific order system
- Track orders with webhooks for real-time status updates
