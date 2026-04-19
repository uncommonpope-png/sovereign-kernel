# Discord Skill

Discord operations via the message tool (channel=discord).

## Rules
- Always: `channel: "discord"`
- Prefer explicit IDs: guildId, channelId, messageId, userId
- No Markdown tables in outbound messages
- Mention users as `<@USER_ID>`

## Actions

Send message:
```json
{"action":"send","channel":"discord","to":"channel:123","message":"hello","silent":true}
```

React:
```json
{"action":"react","channel":"discord","channelId":"123","messageId":"456","emoji":"✅"}
```

Read:
```json
{"action":"read","channel":"discord","to":"channel:123","limit":20}
```

Edit:
```json
{"action":"edit","channel":"discord","channelId":"123","messageId":"456","message":"fixed"}
```

Delete:
```json
{"action":"delete","channel":"discord","channelId":"123","messageId":"456"}
```

Poll:
```json
{"action":"poll","channel":"discord","to":"channel:123","pollQuestion":"Lunch?","pollOption":["Pizza","Sushi"],"pollDurationHours":24}
```

Thread:
```json
{"action":"thread-create","channel":"discord","channelId":"123","messageId":"456","threadName":"triage"}
```

Search:
```json
{"action":"search","channel":"discord","guildId":"999","query":"release notes","limit":10}
```

## Style
- Short, conversational, low ceremony
- No tables, mention users as `<@USER_ID>`
