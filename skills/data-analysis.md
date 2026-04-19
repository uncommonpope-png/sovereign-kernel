# Data Analysis Skill

Process CSV, JSON, and structured data. Extract insights, calculate statistics, transform data.

## Use When
- Analyzing logs, memories, or usage data
- Processing CSV exports from external services
- Summarizing structured data
- Finding patterns in the kernel's history

## CSV Processing
```python
import csv, statistics

# Read CSV
with open('data.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Basic stats on a column
values = [float(r['score']) for r in rows if r['score']]
print(f"Count: {len(values)}")
print(f"Mean: {statistics.mean(values):.3f}")
print(f"Max: {max(values):.3f}")
print(f"Min: {min(values):.3f}")

# Filter rows
high_score = [r for r in rows if float(r.get('score', 0)) > 0.8]
print(f"High score rows: {len(high_score)}")
```

## JSON Processing
```python
import json, collections

with open('entity_state.json') as f:
    state = json.load(f)

# Count memory types
memories = state.get('memories', [])
type_counts = collections.Counter(m['memory_type'] for m in memories)
print("Memory type distribution:", dict(type_counts))

# Find top salience memories
top = sorted(memories, key=lambda m: m.get('salience', 0), reverse=True)[:5]
for m in top:
    print(f"  [{m['salience']:.2f}] {m['content'][:80]}")
```

## Log Analysis
```bash
# Count occurrences
grep "Skill invocation" logs/kernel.log | wc -l

# Most common actions
grep "action:" logs/kernel.log | sed 's/.*action: //' | sort | uniq -c | sort -rn | head -10

# Errors in last 100 lines
tail -100 logs/kernel.log | grep -i "error\|failed\|panic"

# Time between events
grep "Council" logs/kernel.log | awk '{print $1, $2}' | head -10
```

## Kernel Analytics (Python)
```python
import json, re
from datetime import datetime
from collections import defaultdict

# Analyze action distribution from entity_state
with open('entity_state.json') as f:
    state = json.load(f)

actions = state.get('agentic_will', {}).get('executed_actions', [])
action_types = defaultdict(int)
for a in actions:
    # Extract action type from "Soul name action: description"
    parts = a.split(' ', 2)
    if len(parts) >= 2:
        action_types[parts[-1][:30]] += 1

print("Top actions:")
for action, count in sorted(action_types.items(), key=lambda x: -x[1])[:10]:
    print(f"  {count:3d}x {action}")
```

## Notes
- Python's csv, json, statistics modules: no install needed
- For heavy analysis: pandas (pip install pandas)
- Always summarize findings as a semantic memory
- Store analysis scripts in scripts/ for reuse
