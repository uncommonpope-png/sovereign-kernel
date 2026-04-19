# GitHub Skill

GitHub operations via `gh` CLI: issues, PRs, CI runs, code review, API queries.

## Use When
- Checking PR status or CI results
- Creating/commenting on issues or PRs
- Listing/filtering PRs or issues
- Viewing workflow run logs

## Setup
```bash
gh auth login
gh auth status
```

## Common Commands

### Pull Requests
```bash
gh pr list --repo owner/repo
gh pr checks 55 --repo owner/repo
gh pr create --title "feat: add feature" --body "Description"
gh pr merge 55 --squash --repo owner/repo
```

### Issues
```bash
gh issue list --repo owner/repo --state open
gh issue create --title "Bug" --body "Details"
gh issue close 42 --repo owner/repo
```

### CI Runs
```bash
gh run list --repo owner/repo --limit 10
gh run view <run-id> --log-failed
gh run rerun <run-id> --failed
```

### API
```bash
gh api repos/owner/repo/pulls/55 --jq '.title, .state'
gh pr list --json number,title,state --jq '.[] | "\(.number): \(.title)"'
```

## Notes
- Always specify --repo owner/repo when not in a git directory
- Use URLs directly: gh pr view https://github.com/owner/repo/pull/55
