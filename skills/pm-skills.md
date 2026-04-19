# pm-skills

Product management skills — discovery, strategy, execution, launch, and growth workflows.

## What this skill does
Provides 100+ product management frameworks: user research synthesis, PRD writing, OKR setting, roadmap prioritization, launch checklists, and growth analysis.

## PRD template
```markdown
# PRD: [Feature Name]
Owner: [Name] | Date: [date] | Status: Draft

## Problem
[User pain point, evidence, frequency]

## Goal
[Measurable outcome — OKR tie-in]

## User Stories
- As a [user], I want [action] so that [benefit]

## Requirements
### Must Have
- [ ] ...
### Should Have
- [ ] ...
### Won't Have (this cycle)
- [ ] ...

## Success Metrics
- Primary: [metric, target, timeline]
- Guardrail: [metric that must not regress]

## Open Questions
- [ ] ...
```

## Prioritization (RICE)
```python
def rice_score(reach, impact, confidence, effort):
    # reach: users/period, impact: 0.25/0.5/1/2/3, confidence: %, effort: person-months
    return (reach * impact * confidence) / effort
```

## OKR format
```
Objective: [Ambitious qualitative goal]
KR1: Increase [metric] from X to Y by [date]
KR2: Achieve [milestone] by [date]
KR3: Reduce [cost/churn] by Z%
```

## Launch checklist
- [ ] PRD approved
- [ ] Engineering sign-off
- [ ] QA complete
- [ ] Rollout plan (% of users)
- [ ] Rollback plan defined
- [ ] Metrics dashboard live
- [ ] Support team briefed

## Growth analysis
```python
# Week-over-week retention
wow_retention = (week2_users / week1_users) * 100
# DAU/MAU ratio (engagement)
engagement = (dau / mau) * 100
```

## Example commands
```
ACTION: Write a PRD for adding a REST API to the sovereign kernel
ACTION: Score these 3 features using RICE and recommend which to build first
```
