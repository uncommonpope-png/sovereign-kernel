# WaCLI Skill

Send and manage WhatsApp messages via wacli or WhatsApp Business API.

## Use When
- Sending WhatsApp messages programmatically
- Managing WhatsApp conversations
- Automated WhatsApp notifications

## wacli CLI (if installed)
```bash
wacli send "+1234567890" "Hello from terminal!"
wacli send --group "Family" "Dinner at 7pm"
wacli list                             # list recent chats
wacli read "+1234567890"              # read messages from contact
wacli status                          # check connection status
```

## WhatsApp Business Cloud API
```bash
export WA_TOKEN="your-business-api-token"
export WA_PHONE_ID="your-phone-number-id"

# Send text message
curl -X POST "https://graph.facebook.com/v18.0/$WA_PHONE_ID/messages" \
  -H "Authorization: Bearer $WA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messaging_product":"whatsapp",
    "to":"+1234567890",
    "type":"text",
    "text":{"body":"Hello from the API!"}
  }'

# Send template message
curl -X POST "https://graph.facebook.com/v18.0/$WA_PHONE_ID/messages" \
  -H "Authorization: Bearer $WA_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "messaging_product":"whatsapp",
    "to":"+1234567890",
    "type":"template",
    "template":{"name":"hello_world","language":{"code":"en_US"}}
  }'
```

## message tool (OpenClaw)
```json
{"action":"send","channel":"whatsapp","to":"+1234567890","message":"Hello!"}
```

## Notes
- wacli wraps unofficial WhatsApp Web protocol
- WhatsApp Business API: free tier available, templates require approval
- Phone numbers must include country code
