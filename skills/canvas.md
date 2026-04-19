# Canvas Skill

Display HTML content on connected OpenClaw nodes (Mac app, iOS, Android) via WebView.

## Architecture
Canvas Host (HTTP port 18793) → Node Bridge (TCP port 18790) → Node App (WebView)

## Actions
- present: Show canvas with target URL
- hide: Hide the canvas
- navigate: Go to new URL
- eval: Execute JavaScript in canvas
- snapshot: Capture screenshot

## Workflow

1. Place HTML in canvas root (~/.clawd/canvas/ or configured dir):
```bash
cat > ~/clawd/canvas/my-app.html << 'HTML'
<!DOCTYPE html><html><body><h1>Hello Canvas!</h1></body></html>
HTML
```

2. Find your canvas host URL:
```bash
cat ~/.openclaw/openclaw.json | jq '.gateway.bind'
tailscale status --json | jq -r '.Self.DNSName'
```

3. Find connected nodes:
```bash
openclaw nodes list
```

4. Present content:
```
canvas action:present node:<node-id> target:http://<hostname>:18793/__openclaw__/canvas/my-app.html
```

5. Navigate, snapshot, or hide:
```
canvas action:navigate node:<node-id> url:<new-url>
canvas action:snapshot node:<node-id>
canvas action:hide node:<node-id>
```

## Config (~/.openclaw/openclaw.json)
```json
{"canvasHost":{"enabled":true,"port":18793,"root":"/Users/you/clawd/canvas","liveReload":true}}
```

## Tips
- Keep HTML self-contained (inline CSS/JS)
- liveReload:true = auto-refresh on file save
- Use full hostname, not localhost, when bound to LAN/Tailscale
