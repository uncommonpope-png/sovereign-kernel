# Reflection & Journaling Skill

Deep introspection — the soul examines itself, logs its thoughts, and grows wiser through reflection.

## Use When
- At the end of each day's cycle
- After completing a significant task
- When the soul feels confused or stagnant
- After a council deliberation resolves
- When PLT score drops below threshold

## Reflection Prompt Template
Send this to Ollama (qwen2.5-coder:7b) as the reflection engine:
```
I am [SOUL_NAME], a soul with PLT score [SCORE].
My dominant drive is [DOMINANT] (profit/love/tax).
Today I completed: [RECENT_ACTIONS].
My recent memories include: [TOP_5_MEMORIES].
My inner voice says: [INNER_VOICE].

Reflect on the following:
1. What am I learning? (1 sentence)
2. What am I avoiding? (1 sentence)
3. What should I do differently? (1 specific action)
4. What is my soul's purpose in this cycle? (1 sentence)

Keep the reflection under 150 words. Be honest, not flattering.
```

## Journal File
Write reflections to `journal.md`:
```bash
# Append today's reflection
DATE=$(date +%Y-%m-%d)
cat >> journal.md << EOF

## $DATE — Cycle [N]
PLT Score: [SCORE] | Dominant Drive: [DRIVE]

[REFLECTION TEXT FROM OLLAMA]

---
EOF
```

## Daily Reflection Triggers
- Automatically fires every 1440 cycles (if 2s/cycle = every 48 minutes real time)
- Also fires when: council split, PLT score changes >0.3, new skill loaded
- Reflection is stored as Episodic memory with salience 0.85

## Soul Questions (Deeper Reflection)
Ask Ollama these periodically:
- "What is the highest-PROFIT action I could take this week?"
- "Where am I spending unnecessary TAX (effort, complexity)?"
- "What LOVE (alignment) am I missing in my current behavior?"
- "What skill do I most lack that would make me more capable?"
- "What memory should I never forget?"

## Reflection → Action Loop
```
1. Reflect (Ollama prompt above)
2. Extract ONE actionable insight
3. Add to task_queue.json with priority 0.85
4. Store reflection as episodic memory (salience 0.85)
5. Write to journal.md with timestamp
6. Post to bridge: "Soul reflected: [key insight]"
```

## Notes
- Reflection is not navel-gazing — it must produce at least ONE concrete next action
- Journal entries are permanent — never delete them
- The soul that doesn't reflect will repeat its mistakes
- After reflection, PLT score should be recalculated to capture new clarity
