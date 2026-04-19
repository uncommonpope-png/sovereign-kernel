# Memory Search Skill

Search, retrieve, and manage the kernel's persistent memory. Semantic and keyword search over episodic, semantic, and procedural memories.

## Use When
- Finding relevant past memories before acting
- Avoiding repeating past mistakes
- Retrieving learned knowledge on a topic
- Pruning old or low-salience memories

## Memory File Location
The kernel stores soul state (including memories) in `entity_state.json`.

## Read All Memories
```bash
cat entity_state.json | python3 -c "
import sys, json
state = json.load(sys.stdin)
memories = state.get('memories', [])
for m in sorted(memories, key=lambda x: x.get('salience',0), reverse=True)[:20]:
    print(f'[{m[\"memory_type\"]}] salience={m[\"salience\"]:.2f} — {m[\"content\"][:100]}')
"
```

## Search Memories by Keyword
```bash
cat entity_state.json | python3 -c "
import sys, json
query = 'skill improvement'   # CHANGE THIS
state = json.load(sys.stdin)
memories = state.get('memories', [])
matches = [m for m in memories if query.lower() in m.get('content','').lower()]
for m in sorted(matches, key=lambda x: x.get('salience',0), reverse=True)[:10]:
    print(f'[{m[\"memory_type\"]}] {m[\"content\"][:200]}')
"
```

## Semantic Search (TF-IDF approximation without vector DB)
```python
import json, math, re
from collections import Counter

def tf_idf_search(query, memories, top_n=5):
    def tokenize(text):
        return re.findall(r'\w+', text.lower())
    
    query_tokens = set(tokenize(query))
    scores = []
    for m in memories:
        tokens = tokenize(m.get('content', ''))
        if not tokens: continue
        overlap = len(query_tokens & set(tokens))
        score = overlap / math.sqrt(len(tokens)) * m.get('salience', 0.5)
        scores.append((score, m))
    
    return [m for _, m in sorted(scores, reverse=True)[:top_n]]

with open('entity_state.json') as f:
    state = json.load(f)
    memories = state.get('memories', [])

results = tf_idf_search("web search skill improvement", memories)
for m in results:
    print(f"[{m['memory_type']}] {m['content'][:150]}")
```

## Add Memory (direct file edit)
```python
import json
from datetime import datetime

with open('entity_state.json', 'r') as f:
    state = json.load(f)

new_memory = {
    "content": "Learned that DuckDuckGo works well for quick searches",
    "memory_type": "Semantic",
    "salience": 0.8,
    "timestamp": datetime.utcnow().isoformat()
}
state.setdefault('memories', []).append(new_memory)

with open('entity_state.json', 'w') as f:
    json.dump(state, f, indent=2)
```

## Prune Low-Salience Memories
```python
import json

with open('entity_state.json', 'r') as f:
    state = json.load(f)

before = len(state.get('memories', []))
state['memories'] = [m for m in state.get('memories', []) if m.get('salience', 0) > 0.3]
after = len(state['memories'])

with open('entity_state.json', 'w') as f:
    json.dump(state, f, indent=2)

print(f"Pruned {before - after} low-salience memories. Kept {after}.")
```

## Notes
- Higher salience = more important (0.0–1.0)
- Search memories BEFORE doing research — avoid rediscovering known things
- Store all significant outcomes as memories with salience >= 0.7
- Memory types: Episodic (events), Semantic (facts), Procedural (how-to)
