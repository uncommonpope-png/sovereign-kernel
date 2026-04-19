# OpenHue Skill

Control Philips Hue smart lights via openhue CLI or Hue Bridge REST API.

## Use When
- Turning Hue lights on/off
- Changing light colors and brightness
- Setting light scenes and schedules

## openhue CLI (if installed)
```bash
openhue lights                         # list all lights
openhue light "Living Room" on         # turn on light
openhue light "Living Room" off        # turn off light
openhue light "Living Room" --brightness 80
openhue light "Living Room" --color red
openhue scenes                         # list scenes
openhue scene "Relax"                  # activate scene
```

## Hue Bridge REST API (direct)
```bash
BRIDGE_IP="192.168.1.100"
TOKEN="your-bridge-token"

# Get all lights
curl "http://$BRIDGE_IP/api/$TOKEN/lights" | jq 'keys'

# Turn light on/off
curl -X PUT "http://$BRIDGE_IP/api/$TOKEN/lights/1/state" \
  -d '{"on":true}'

# Set color (hue 0-65535, sat 0-254, bri 1-254)
curl -X PUT "http://$BRIDGE_IP/api/$TOKEN/lights/1/state" \
  -d '{"on":true,"hue":46920,"sat":254,"bri":200}'

# Activate scene
curl -X PUT "http://$BRIDGE_IP/api/$TOKEN/groups/0/action" \
  -d '{"scene":"<scene-id>"}'
```

## First-Time Auth
```bash
# Press bridge button, then:
curl -X POST "http://$BRIDGE_IP/api" -d '{"devicetype":"my_app#device"}'
# Returns token
```

## Notes
- Find bridge IP: openhue discover or check router DHCP
- Colors: hue (0=red,25500=green,46920=blue), sat, bri
