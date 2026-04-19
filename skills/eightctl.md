# eightctl Skill

Control the Eight Sleep smart mattress via eightctl CLI or API.

## Use When
- Adjusting Eight Sleep pod temperature
- Reading sleep data and scores
- Scheduling temperature changes for bedtime/wake

## eightctl Commands
```bash
# Check pod status
eightctl status

# Set bed temperature (-100 to 100 scale)
eightctl set-temp --level 20

# Set alarm / scheduled temperature change
eightctl alarm set --time "22:30" --level 30

# Get sleep data
eightctl sleep-data

# Turn heating on/off
eightctl power on
eightctl power off
```

## API (direct)
```bash
# Auth token obtained via eightctl login
TOKEN="your-token"

# Get device info
curl -H "Authorization: Bearer $TOKEN" \
  "https://client-api.8slp.net/v1/users/me/device"

# Set temperature
curl -X PUT -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  "https://client-api.8slp.net/v1/devices/<deviceId>/temperature" \
  -d '{"currentLevel":20}'
```

## Notes
- Requires Eight Sleep Pod
- Temperature scale: -100 (coldest) to 100 (hottest)
- Changes take ~20 min to reach target temperature
