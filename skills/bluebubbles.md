# BlueBubbles Skill

Send and receive iMessages via BlueBubbles server API (cross-platform iMessage access).

## Use When
- Sending iMessages from non-Apple devices via BlueBubbles server
- Reading iMessage conversations
- Managing iMessage notifications programmatically

## API Pattern
```bash
BASE="http://localhost:1234"
PASSWORD="your_password"

# Send message
curl -X POST "$BASE/api/v1/message/send" \
  -H "Content-Type: application/json" \
  -d "{\"chatGuid\":\"iMessage;-;+1234567890\",\"message\":\"Hello!\",\"password\":\"$PASSWORD\"}"

# Get conversations (chats)
curl "$BASE/api/v1/chat/query?password=$PASSWORD&limit=10"

# Get messages from chat
curl "$BASE/api/v1/chat/iMessage;-;+1234567890/message?password=$PASSWORD&limit=20"

# Get attachments
curl "$BASE/api/v1/attachment/count?password=$PASSWORD"
```

## Setup
- BlueBubbles server must be running on a Mac
- Configure server URL and password in BlueBubbles settings
- API password set in BlueBubbles server config

## Notes
- Requires BlueBubbles server running on macOS
- chatGuid format: iMessage;-;<phone or email>
- For group chats: iMessage;+;<group-id>
