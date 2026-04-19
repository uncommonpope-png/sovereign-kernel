# planning-with-files

Persistent markdown planning — break large tasks into tracked plan files before execution.

## What this skill does
Creates and maintains structured plan files (PLAN.md) that decompose complex goals into phases, steps, and checkboxes. Inspired by Manus-style persistent planning.

## Plan file format
```markdown
# PLAN: [Goal Name]
Created: 2026-04-18
Status: in_progress
PLT Score: 0.82

## Phase 1: Research
- [x] Define scope
- [x] Gather existing knowledge
- [ ] Identify gaps

## Phase 2: Implementation
- [ ] Step 1: ...
- [ ] Step 2: ...

## Phase 3: Verification
- [ ] Test
- [ ] Commit

## Notes
- Key decision: ...
- Blocker: ...
```

## Core operations

### Create plan
```python
import os
from datetime import datetime
def create_plan(goal, phases):
    lines = [f"# PLAN: {goal}", f"Created: {datetime.now().date()}", "Status: pending\n"]
    for phase, steps in phases.items():
        lines.append(f"## {phase}")
        for s in steps:
            lines.append(f"- [ ] {s}")
        lines.append("")
    os.makedirs("plans", exist_ok=True)
    slug = goal.lower().replace(" ","-")[:30]
    path = f"plans/{slug}.md"
    open(path,"w").write("\n".join(lines))
    return path
```

### Mark step done
```python
def mark_done(plan_path, step_text):
    content = open(plan_path).read()
    content = content.replace(f"- [ ] {step_text}", f"- [x] {step_text}", 1)
    open(plan_path,"w").write(content)
```

### List active plans
```python
import glob
for f in glob.glob("plans/*.md"):
    content = open(f).read()
    if "Status: in_progress" in content or "Status: pending" in content:
        print(f)
```

## Example commands
```
ACTION: Create a plan file for implementing the new web-search skill integration
ACTION: Mark step "Gather existing knowledge" as done in plans/web-search-integration.md
```
