# 1Password Skill

Set up and use 1Password CLI (op). Read, inject, and run secrets via op.

## Requirements
- op CLI installed: `op --version`
- Desktop app integration enabled and app unlocked
- REQUIRED: run all op commands inside a tmux session (TTY requirement)

## Workflow
1. Verify CLI: `op --version`
2. Confirm desktop app integration is enabled
3. Create tmux session for op commands
4. Sign in inside tmux: `op signin`
5. Verify: `op whoami`
6. Multi-account: use `--account` or `OP_ACCOUNT`

## tmux Session Pattern
```bash
SOCKET="/tmp/openclaw-tmux-sockets/openclaw-op.sock"
SESSION="op-auth-$(date +%Y%m%d-%H%M%S)"
tmux -S "$SOCKET" new -d -s "$SESSION" -n shell
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op signin" Enter
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op whoami" Enter
tmux -S "$SOCKET" send-keys -t "$SESSION":0.0 -- "op vault list" Enter
tmux -S "$SOCKET" capture-pane -p -J -t "$SESSION":0.0 -S -200
tmux -S "$SOCKET" kill-session -t "$SESSION"
```

## Guardrails
- Never paste secrets into logs or code
- Prefer `op run` / `op inject` over writing secrets to disk
- Do not run op outside tmux
