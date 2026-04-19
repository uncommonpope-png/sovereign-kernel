# Slack Skill

Control Slack via the slack tool: messages, reactions, pins, threads, member info.

## Actions

Send message:
```json
{"action":"sendMessage","to":"channel:C123","content":"Hello"}
```

React to message:
```json
{"action":"react","channelId":"C123","messageId":"1712023032.1234","emoji":"✅"}
```

Read recent messages:
```json
{"action":"readMessages","channelId":"C123","limit":20}
```

Edit message:
```json
{"action":"editMessage","channelId":"C123","messageId":"1712023032.1234","content":"Updated text"}
```

Delete message:
```json
{"action":"deleteMessage","channelId":"C123","messageId":"1712023032.1234"}
```

Pin message:
```json
{"action":"pinMessage","channelId":"C123","messageId":"1712023032.1234"}
```

List pins:
```json
{"action":"listPins","channelId":"C123"}
```

Member info:
```json
{"action":"memberInfo","userId":"U123"}
```

## Tips
- React with ✅ to mark completed tasks
- Pin key decisions or weekly status updates
- Message timestamps are Slack message IDs (e.g., 1712023032.1234)
