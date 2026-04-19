# Math & Calculation Skill

Perform mathematical calculations, statistics, and numerical reasoning.

## Use When
- PLT score calculations and economics
- Statistical analysis of memory salience distributions
- Time/date arithmetic
- Probability and decision theory

## Quick Math (Python)
```python
# Basic arithmetic
python3 -c "
import math, statistics

# PLT calculation
profit, love, tax = 0.8, 0.7, 0.3
plt_score = profit + love - tax
print(f'PLT Score: {plt_score:.2f}')

# Running statistics
values = [0.8, 0.6, 0.9, 0.7, 0.85, 0.4, 0.95]
print(f'Mean: {statistics.mean(values):.3f}')
print(f'Stdev: {statistics.stdev(values):.3f}')
print(f'Median: {statistics.median(values):.3f}')
"
```

## PLT Economy Math
```python
def plt_score(profit, love, tax):
    return profit + love - tax

def should_proceed(score, threshold=0.5):
    return score >= threshold

def soul_net_value(points, collab, reliability):
    return (points * 0.4) + (collab * 0.3) + (reliability * 0.3)

def plt_combat(attacker_score, defender_score):
    # Higher PLT wins; love adds shield, tax reduces damage
    attack = attacker_score * 1.2
    defense = defender_score * 0.8
    return attack > defense

# Example
score = plt_score(0.9, 0.8, 0.2)
print(f"Entity score: {score:.2f} — proceed: {should_proceed(score)}")
```

## Time Arithmetic
```python
from datetime import datetime, timedelta

now = datetime.utcnow()
one_day_ago = now - timedelta(days=1)
next_cycle = now + timedelta(hours=1)

# How long since last action?
last_action = datetime(2026, 4, 18, 10, 0, 0)
delta = now - last_action
print(f"Time since last action: {delta.total_seconds():.0f}s ({delta.total_seconds()/3600:.1f}h)")
```

## Probability & Decisions
```python
import random

# Weighted random choice (for PLT-driven decision making)
def plt_weighted_choice(options, weights):
    """Choose from options weighted by PLT alignment scores."""
    total = sum(weights)
    normalized = [w/total for w in weights]
    r = random.random()
    cumulative = 0
    for option, w in zip(options, normalized):
        cumulative += w
        if r < cumulative:
            return option

actions = ["improve web-search", "reflect on memories", "check health", "run tests"]
scores  = [0.9, 0.8, 0.5, 0.7]
chosen = plt_weighted_choice(actions, scores)
print(f"PLT-weighted choice: {chosen}")
```

## Notes
- Python3's math and statistics modules are available without install
- For heavy math: numpy, scipy (install with pip if needed)
- All PLT scores are floats in [0.0, 1.0] per dimension
- Tax dimension inverts: higher tax = worse score
