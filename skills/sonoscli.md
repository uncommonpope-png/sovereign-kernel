# Sonos CLI Skill

Control Sonos speakers via sonoscli or the Sonos Local API.

## Use When
- Playing, pausing, or controlling Sonos speakers
- Managing Sonos playlists and queues
- Adjusting volume across Sonos rooms

## sonoscli Commands (if installed)
```bash
sonoscli list                          # list Sonos players
sonoscli play                          # resume playback
sonoscli pause                         # pause playback
sonoscli next                          # next track
sonoscli prev                          # previous track
sonoscli volume 50                     # set volume 0-100
sonoscli status                        # current playback state
sonoscli search "Jazz" --service spotify
sonoscli play --uri "spotify:track:xxx"
```

## Sonos Local API (HTTP)
```bash
SONOS_IP="192.168.1.50"

# Get current state
curl "http://$SONOS_IP:1400/State"

# Play/pause
curl "http://$SONOS_IP:1400/Play"
curl "http://$SONOS_IP:1400/Pause"

# Volume
curl "http://$SONOS_IP:1400/Volume"
curl "http://$SONOS_IP:1400/Volume/50"

# Next/previous
curl "http://$SONOS_IP:1400/Next"
curl "http://$SONOS_IP:1400/Previous"

# Queue a track
curl -X POST "http://$SONOS_IP:1400/Add" \
  -d '{"uri":"spotify:track:4uLU6hMCjMI75M1A2tKUQC","metadata":""}'
```

## Find Sonos on Network
```bash
# UDP discovery
python3 -c "
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(b'M-SEARCH * HTTP/1.1\r\nHOST:239.255.255.250:1900\r\n', ('239.255.255.250', 1900))
"
```

## Notes
- Sonos speakers must be on same local network
- Port 1400 = Sonos HTTP API
- sonoscli wraps the API with a friendlier interface
