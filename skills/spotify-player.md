# Spotify Player Skill

Control Spotify playback and search directly from the terminal using either **spogo** (recommended) or **spotify_player**.

## Prerequisites
1. **Spotify Premium account** (required for playback control).
2. **spogo** (preferred) or **spotify_player** installed.

## Setup
Authenticate **spogo** using your Spotify account:
```bash
spogo auth import --browser chrome
```

## spogo Commands (Preferred Option)
### General Commands
- **Search for a track:**
  ```bash
  spogo search track "<query>"
  ```
- **Play or resume playback:**
  ```bash
  spogo play
  ```
- **Pause playback:**
  ```bash
  spogo pause
  ```
- **Skip to the next track:**
  ```bash
  spogo next
  ```
- **Return to the previous track:**
  ```bash
  spogo prev
  ```

### Device Management
- **List available devices:**
  ```bash
  spogo device list
  ```
- **Set active playback device:**
  ```bash
  spogo device set "<device-name>"
  ```

### Example Commands
1. Search for and play a song directly:
   ```bash
   spogo search track "Bohemian Rhapsody" && spogo play
   ```
2. Switch playback to a specific device:
   ```bash
   spogo device set "Living Room Speaker"
   ```

## Alternative: spotify_player
Commands for **spotify_player** are also supported, but **spogo** is recommended for a more seamless experience.

Enhance your command-line interface with smooth Spotify control!