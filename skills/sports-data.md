# sports-data

Fetch live sports data and prediction market odds — football, F1, and more — with zero API keys required.

## What this skill does
Retrieves live scores, standings, fixtures, player stats, and prediction market odds from free public sources.

## Live scores (ESPN unofficial API)
```python
import httpx, json

def get_nfl_scores():
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
    r = httpx.get(url, timeout=10)
    games = r.json().get("events", [])
    return [{"name": g["name"], "status": g["status"]["type"]["description"],
             "score": g.get("competitions",[{}])[0].get("competitors",[])} for g in games]

def get_f1_standings():
    url = "https://ergast.com/api/f1/current/driverStandings.json"
    r = httpx.get(url, timeout=10)
    standings = r.json()["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    return [(s["position"], s["Driver"]["familyName"], s["points"]) for s in standings[:10]]
```

## Prediction markets (Polymarket)
```python
def get_polymarket_markets(keyword):
    url = f"https://gamma-api.polymarket.com/markets?search={keyword}&active=true&limit=5"
    r = httpx.get(url, timeout=10)
    return [(m["question"], m.get("outcomePrices","")) for m in r.json()]
```

## Kalshi
```python
def get_kalshi_events(keyword):
    url = f"https://trading-api.kalshi.com/trade-api/v2/events?series_ticker={keyword}&status=open"
    r = httpx.get(url, timeout=10)
    return r.json().get("events", [])
```

## PLT angle
- Profit: bet on prediction markets with PLT analysis
- Love: share sports updates with community
- Tax: track your prediction market P&L

## Example commands
```
ACTION: Get current NFL scores and store top game result in memory
ACTION: Fetch Polymarket odds for "next AI breakthrough" and compare to PLT score
```
