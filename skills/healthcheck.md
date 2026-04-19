# Healthcheck Skill

Monitor service health, uptime, and system status. Check if services are running.

## Use When
- Checking if a web service or API is up
- Monitoring system resource usage
- Verifying service endpoints respond correctly

## HTTP Health Checks
```bash
# Simple up/down check
curl -s -o /dev/null -w "%{http_code}" https://example.com/health

# Check with timeout
curl -s --max-time 5 -o /dev/null -w "%{http_code} %{time_total}s" https://api.example.com

# Check JSON health endpoint
curl -s https://api.example.com/health | jq '.status'

# Multiple endpoints
for url in "https://api1.com/health" "https://api2.com/health" "https://api3.com/ping"; do
  status=$(curl -s -o /dev/null -w "%{http_code}" --max-time 3 "$url")
  echo "$url: $status"
done
```

## System Health
```bash
# CPU and memory
top -bn1 | head -5

# Disk usage
df -h

# Process check
pgrep -x "nginx" && echo "nginx running" || echo "nginx not running"

# Port check
nc -z localhost 8080 && echo "port 8080 open" || echo "port 8080 closed"
```

## Uptime Monitoring
```bash
# Check with retry and alert
for i in {1..3}; do
  if curl -sf https://example.com/health > /dev/null; then
    echo "UP"; break
  else
    echo "Attempt $i failed"
    sleep 5
  fi
done
```

## Notes
- 200 = healthy, 4xx/5xx or timeout = unhealthy
- Use --max-time to avoid hanging on slow services
