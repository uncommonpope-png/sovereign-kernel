# Coding Agent Skill

Delegate coding tasks to Codex, Claude Code, or Pi agents via background process.

## Use When
- Building/creating new features or apps
- Reviewing PRs (spawn in temp dir)
- Refactoring large codebases
- Iterative coding that needs file exploration

## Claude Code (no PTY needed)
```bash
cd /path/to/project && claude --permission-mode bypassPermissions --print 'Your task'
# Background:
bash workdir:~/project background:true command:"claude --permission-mode bypassPermissions --print 'task'"
```

## Codex / Pi / OpenCode (PTY required)
```bash
bash pty:true workdir:~/project command:"codex exec 'Your task'"
bash pty:true workdir:~/project background:true command:"codex --full-auto 'Build feature'"
```

## PR Review Pattern
```bash
REVIEW_DIR=$(mktemp -d)
git clone https://github.com/user/repo.git $REVIEW_DIR
cd $REVIEW_DIR && gh pr checkout 130
bash pty:true workdir:$REVIEW_DIR command:"codex review --base origin/main"
```

## Rules
- Codex requires a git repo (mktemp + git init for scratch)
- --full-auto for building, vanilla for reviewing
- Monitor with process:log, kill with process:kill
- Never start Codex in the OpenClaw config dir
