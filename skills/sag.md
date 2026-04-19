# SAG Skill

Spawn and manage autonomous sub-agents — delegate tasks to parallel AI workers.

## Use When
- Breaking a large task into parallel sub-tasks
- Running multiple agents simultaneously
- Orchestrating multi-step workflows across agents

## sessions_spawn Pattern
```bash
# Spawn a sub-agent with a task
sessions_spawn --task "Analyze the sales data in /data/sales.csv and return a summary"

# Spawn with timeout
sessions_spawn --task "Your task here" --timeout 3600

# Spawn in specific directory
sessions_spawn --workdir /path/to/project --task "Fix the bug in auth.ts"
```

## Parallel Sub-agent Pattern
```bash
# Launch 3 agents simultaneously
ID1=$(sessions_spawn --task "Task A" --background)
ID2=$(sessions_spawn --task "Task B" --background)
ID3=$(sessions_spawn --task "Task C" --background)

# Monitor progress
process action:log sessionId:$ID1
process action:log sessionId:$ID2

# Wait for completion
process action:poll sessionId:$ID1
```

## Task Design Principles
- Give each agent ONE clear, bounded task
- Include all needed context in the task prompt
- Specify expected output format explicitly
- Set realistic timeouts (complex tasks: 3600s)
- Use workdir to scope the agent's context

## Orchestrator Rules
- Never take over if an agent fails silently — respawn or ask user
- Collect results from all agents before synthesizing
- Monitor with process:log, intervene with process:write
- Keep user informed of progress and completions

## Notes
- Max 8 concurrent agents (subagents.maxConcurrent: 8)
- Use cleanup:keep to preserve transcripts for review
- Fire-and-forget with --cron flag for scheduled runs
