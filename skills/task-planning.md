# Task Planning Skill

Break goals into task lists, prioritize, execute step-by-step, and track completion. BabyAGI-style autonomous task management.

## Use When
- Facing a multi-step goal that requires planning
- Managing a backlog of pending actions
- Prioritizing what to do next across competing goals
- Reflecting on completed work and creating follow-on tasks

## Task Queue File
Store tasks in `task_queue.json`:
```json
[
  {"id": 1, "task": "Improve web-search skill", "priority": 0.9, "status": "pending", "created": "2026-04-18"},
  {"id": 2, "task": "Learn Rust async patterns", "priority": 0.7, "status": "in_progress"},
  {"id": 3, "task": "Update self-improve skill", "priority": 0.8, "status": "done"}
]
```

## Add Task
```python
import json, time

def add_task(description, priority=0.7):
    try:
        with open('task_queue.json') as f:
            tasks = json.load(f)
    except:
        tasks = []
    
    task_id = max([t['id'] for t in tasks], default=0) + 1
    tasks.append({
        "id": task_id,
        "task": description,
        "priority": priority,
        "status": "pending",
        "created": time.strftime('%Y-%m-%dT%H:%M:%S')
    })
    
    with open('task_queue.json', 'w') as f:
        json.dump(tasks, f, indent=2)
    
    print(f"Added task #{task_id}: {description}")

add_task("Research new Ollama models available", priority=0.8)
```

## Get Next Task
```python
import json

with open('task_queue.json') as f:
    tasks = json.load(f)

pending = [t for t in tasks if t['status'] == 'pending']
if pending:
    next_task = max(pending, key=lambda t: t['priority'])
    print(f"Next task: [{next_task['id']}] {next_task['task']} (priority: {next_task['priority']})")
else:
    print("No pending tasks — enter idle reflection mode")
```

## Mark Complete + Generate Follow-on Tasks
```
After completing a task:
1. Mark status = "done" in task_queue.json
2. Ask Ollama: "I just completed: <task>. What 2-3 follow-on tasks should I consider?"
3. Parse response and add new tasks with slightly lower priority (parent * 0.9)
4. Store completion as episodic memory with salience 0.8
```

## PLT-Weighted Prioritization
```
priority_score = (profit_gain * 0.4) + (love_alignment * 0.4) - (tax_cost * 0.2)

Examples:
- "Improve reasoning about PLT" → profit=0.9, love=0.9, tax=0.2 → score=0.68
- "Send health check ping" → profit=0.3, love=0.3, tax=0.1 → score=0.22
- "Rewrite entire main.rs" → profit=0.7, love=0.5, tax=0.9 → score=0.30
```

## Autonomous Planning Loop
```
Every 30 minutes:
1. Check task_queue.json for pending tasks
2. If empty: reflect on recent memories and generate 3 new self-improvement tasks
3. Execute highest-priority task using appropriate skill
4. Log outcome and generate follow-ons
5. Repeat
```

## Notes
- Never plan more than 5 tasks at once — focus is the superpower
- High LOVE tasks = tasks the soul genuinely cares about
- Delete completed tasks older than 7 days to avoid queue bloat
