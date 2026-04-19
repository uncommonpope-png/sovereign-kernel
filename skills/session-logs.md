# Session Logs Skill

Search and analyze your own session logs (older/parent conversations) using jq.

## Use When
- User references older/parent conversations
- Asks what was said before / in prior chats

## Location
~/.openclaw/agents/<agentId>/sessions/
- sessions.json: index mapping session keys to IDs
- <session-id>.jsonl: full conversation transcript

## Common Queries

List sessions by date:
```bash
for f in ~/.openclaw/agents/<agentId>/sessions/*.jsonl; do
  date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
  echo "$date $(basename $f)"
done | sort -r
```

Extract user messages:
```bash
jq -r 'select(.message.role=="user") | .message.content[]? | select(.type=="text") | .text' <session>.jsonl
```

Search for keyword in assistant responses:
```bash
jq -r 'select(.message.role=="assistant") | .message.content[]? | select(.type=="text") | .text' <session>.jsonl | rg -i "keyword"
```

Get total cost for session:
```bash
jq -s '[.[] | .message.usage.cost.total // 0] | add' <session>.jsonl
```

Search across ALL sessions:
```bash
rg -l "phrase" ~/.openclaw/agents/<agentId>/sessions/*.jsonl
```

Tool usage breakdown:
```bash
jq -r '.message.content[]? | select(.type=="toolCall") | .name' <session>.jsonl | sort | uniq -c | sort -rn
```

## Tips
- Sessions are append-only JSONL (one JSON object per line)
- Filter type=="text" for human-readable content only
- Deleted sessions have .deleted.<timestamp> suffix
