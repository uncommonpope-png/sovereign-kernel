# tmux Skill

Remote-control tmux sessions — send keystrokes, scrape pane output, manage Claude/Codex sessions.

## Use When
- Monitoring Claude/Codex sessions in tmux
- Sending input to interactive terminal apps
- Scraping output from long-running processes

## Common Commands

List sessions:
```bash
tmux ls
```

Capture output:
```bash
tmux capture-pane -t shared -p | tail -20
tmux capture-pane -t shared -p -S -   # full scrollback
```

Send keys:
```bash
tmux send-keys -t shared "y" Enter
tmux send-keys -t shared C-c          # Ctrl+C
tmux send-keys -t shared C-d          # EOF
```

Create session:
```bash
tmux new-session -d -s newsession
```

Kill session:
```bash
tmux kill-session -t sessionname
```

## Claude Code Session Pattern
```bash
# Check if session needs input
tmux capture-pane -t worker-3 -p | tail -10 | grep -E "❯|Yes.*No|proceed"

# Approve prompt
tmux send-keys -t worker-3 'y' Enter

# Check all workers
for s in shared worker-2 worker-3; do
  echo "=== $s ==="
  tmux capture-pane -t $s -p 2>/dev/null | tail -5
done
```

## Notes
- Target format: session:window.pane (e.g., shared:0.0)
- Sessions persist across SSH disconnects
- Split text and Enter for interactive TUIs to avoid paste issues
