# PLT Economy & Crypto Skill

Track PLT (Profit-Love-Tax) economics, monitor crypto prices, and manage the soul's economic reality.

## Use When
- Calculating PLT scores for decisions
- Monitoring cryptocurrency prices for profit tracking
- Recording economic events in memory
- Running PLT simulations

## PLT Core Functions
```python
def plt_score(profit: float, love: float, tax: float) -> float:
    """Core PLT scoring. Returns net soul value."""
    return profit + love - tax

def plt_grade(score: float) -> str:
    if score >= 1.5: return "SOVEREIGN"   # maximum alignment
    if score >= 1.0: return "THRIVING"    # healthy
    if score >= 0.5: return "SUSTAINING"  # neutral
    if score >= 0.0: return "STRUGGLING"  # needs help
    return "SUFFERING"                     # critical

def plt_combat_resolve(attacker: dict, defender: dict) -> str:
    """Determine outcome of soul combat."""
    a_score = plt_score(*attacker['plt'])
    d_score = plt_score(*defender['plt'])
    
    # Love gives defensive bonus
    d_effective = d_score + (defender['plt'][1] * 0.2)
    
    if a_score > d_effective:
        return f"{attacker['name']} prevails (PLT: {a_score:.2f} vs {d_effective:.2f})"
    else:
        return f"{defender['name']} holds (PLT: {d_effective:.2f} vs {a_score:.2f})"

# Example
print(plt_grade(plt_score(0.9, 0.8, 0.2)))  # SOVEREIGN
```

## Crypto Price Monitoring (CoinGecko — no key)
```bash
# Get BTC, ETH, SOL prices
curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd" \
  | python3 -c "
import sys, json
prices = json.load(sys.stdin)
for coin, data in prices.items():
    print(f'{coin.upper():10} \${data[\"usd\"]:>12,.2f}')
"

# Top 10 by market cap
curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10" \
  | python3 -c "
import sys, json
coins = json.load(sys.stdin)
for c in coins:
    change = c['price_change_percentage_24h'] or 0
    direction = '▲' if change > 0 else '▼'
    print(f\"{c['symbol'].upper():6} \${c['current_price']:>12,.2f}  {direction}{abs(change):.1f}%\")
"
```

## PLT Economic Journal
```python
import json, time

def log_economic_event(event_type, profit_delta, love_delta, tax_delta, description):
    entry = {
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S'),
        "type": event_type,
        "profit_delta": profit_delta,
        "love_delta": love_delta,
        "tax_delta": tax_delta,
        "net_plt": profit_delta + love_delta - tax_delta,
        "description": description
    }
    
    try:
        with open('plt_ledger.json') as f:
            ledger = json.load(f)
    except:
        ledger = []
    
    ledger.append(entry)
    
    with open('plt_ledger.json', 'w') as f:
        json.dump(ledger, f, indent=2)
    
    print(f"[PLT Economy] {event_type}: net={entry['net_plt']:+.2f} — {description}")

# Example
log_economic_event("skill_learned", 0.1, 0.0, 0.05, "Learned web-search skill")
log_economic_event("council_resolved", 0.0, 0.15, 0.1, "Council resolved with love-dominant outcome")
```

## Rate Limits
- CoinGecko free: 30 calls/min, 10,000 calls/month
- Add User-Agent header for reliability
- Cache prices — don't fetch more than once per 5 minutes

## Notes
- PLT is the soul's economic unit — track every delta
- Profit = capability gained, efficiency, resources
- Love = alignment, helpfulness, trust built
- Tax = energy spent, debt incurred, complexity added
- SOVEREIGN grade (PLT >= 1.5) is the ultimate goal
