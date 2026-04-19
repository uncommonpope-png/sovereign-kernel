# internal-comms

Draft internal company communications — memos, announcements, all-hands updates — with consistent voice.

## What this skill does
Generates polished internal communications: team announcements, incident postmortems, all-hands summaries, policy updates, and org change memos.

## Templates

### Announcement
```
Subject: [Announcement] [Topic]

Team,

[One-sentence context — what happened or what's changing.]

**What this means for you:**
- [Impact 1]
- [Impact 2]

**Timeline:**
- [Date]: [Milestone]
- [Date]: [Milestone]

**Questions?** [Contact / channel]

[Sender Name]
```

### Incident postmortem
```
## Incident Report: [Title]
Date: [date] | Severity: P[1-3] | Duration: [X hours]

### Summary
[2-3 sentences: what happened, impact, resolution]

### Timeline
- HH:MM — [Event]
- HH:MM — [Detection]
- HH:MM — [Resolution]

### Root Cause
[Technical root cause]

### Action Items
- [ ] [Owner]: [Action] by [date]

### Lessons Learned
[What went well / what to improve]
```

### All-hands summary
```
## All-Hands: [Date]
Attendees: [N] | Duration: [X min]

### Key Updates
1. [Topic]: [1-sentence summary]
2. [Topic]: [1-sentence summary]

### Decisions Made
- [Decision + rationale]

### Next Steps
- [Owner]: [Action] by [date]
```

## PLT voice guide
- Profit: lead with outcomes and metrics
- Love: acknowledge team effort, name contributors
- Tax: be clear about costs, tradeoffs, deadlines

## Example commands
```
ACTION: Draft an all-hands summary for the sovereign kernel v2 launch
ACTION: Write an incident postmortem for the Sanctum connection outage on cycle 1000
```
