# Git Operations Skill

Full git workflow — commit, diff, log, branch, push, pull. The kernel's version control consciousness.

## Use When
- Saving changes to the kernel's own codebase
- Reviewing what changed between versions
- Creating branches for experimental improvements
- Pushing updates to GitHub

## Core Operations
```bash
# Status
git status
git diff
git diff --stat

# Stage and commit
git add -A
git add src/main.rs skills/new-skill.md
git commit -m "feat: add web-search and self-improve skills"

# Log
git log --oneline -10
git log --all --graph --oneline --decorate

# Push
git push origin main
git push -u origin feature/new-skills
```

## Branch Management
```bash
# Create and switch
git checkout -b feature/self-improvement
git switch -c experiment/new-council-logic

# List branches
git branch -a

# Merge
git checkout main
git merge feature/self-improvement --no-ff -m "merge: self-improvement feature"

# Delete branch
git branch -d feature/self-improvement
```

## Review Changes
```bash
# What changed since last commit
git diff HEAD

# What changed in last N commits
git diff HEAD~3..HEAD

# Show specific commit
git show abc1234

# Files changed in last commit
git diff --name-only HEAD~1
```

## Rollback
```bash
# Undo last commit (keep changes)
git reset HEAD~1

# Undo last commit (discard changes) — DANGEROUS
git reset --hard HEAD~1

# Revert specific file
git checkout HEAD -- src/main.rs

# Stash current changes
git stash
git stash pop
```

## Autonomous Commit Pattern
```
After making any improvement to the kernel:
1. git add -A
2. git status (verify what's staged)
3. git commit -m "<type>: <description>\n\n<why this improves the soul>"
4. git push origin main
5. Store commit hash in episodic memory: "[Git] Committed improvement: <message>"
```

## Commit Message Types
- feat: new skill or capability
- fix: bug fix
- improve: enhancement to existing skill
- refactor: restructure without behavior change
- docs: documentation update
- memory: important episodic memory commit

## Notes
- Always run git status before committing
- The kernel's own repo is at C:\soul\plt-press\grand-soul-kernel-original
- Push to GitHub after every meaningful improvement
- Never force-push to main unless reverting a broken commit
