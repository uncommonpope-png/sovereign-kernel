# gh-issues Skill

Fetch GitHub issues, spawn sub-agents to implement fixes, open PRs, then monitor review comments.

## Use When
- Auto-fixing GitHub issues in a repo
- Running: /gh-issues [owner/repo] [--label bug] [--limit 5]

## Phases
1. Parse arguments (owner/repo, --label, --limit, --fork, --watch, --dry-run, --yes)
2. Fetch issues from GitHub REST API using GH_TOKEN
3. Present table and confirm which to process
4. Pre-flight checks (git status, verify remote access, check existing PRs)
5. Spawn parallel sub-agents to implement fixes and open PRs
6. Monitor PRs for review comments, spawn agents to address them

## Token Setup
```bash
export GH_TOKEN="your-token"
# or from config:
cat ~/.openclaw/openclaw.json | jq -r '.skills.entries["gh-issues"].apiKey'
```

## API Pattern (no gh CLI — use curl)
```bash
curl -s -H "Authorization: Bearer $GH_TOKEN" \
     -H "Accept: application/vnd.github+json" \
     "https://api.github.com/repos/{owner}/{repo}/issues?per_page=10&state=open"
```

## Flags
- --limit N: max issues to fetch
- --label bug: filter by label
- --fork user/repo: push to fork, PR to source
- --watch: poll for new issues every --interval minutes
- --dry-run: display only, no agents
- --yes: skip confirmation
- --cron: fire-and-forget one issue then exit
