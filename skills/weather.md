# Weather Skill

Get current weather conditions and forecasts via wttr.in (no API key needed).

## Use When
- User asks about weather, temperature, rain, forecasts
- Travel planning weather checks

## Commands

```bash
# One-line current weather
curl "wttr.in/London?format=3"
curl "wttr.in/New+York?format=%l:+%c+%t+%w"

# 3-day forecast
curl "wttr.in/London"

# JSON output
curl "wttr.in/London?format=j1"
```

## Format Codes
- %c = condition emoji, %t = temperature, %f = feels like, %w = wind, %h = humidity, %p = precipitation

## Notes
- No API key required
- Supports airport codes: curl wttr.in/ORD
- Rate limited — do not spam requests
