# Spotify Player Skill

Terminal Spotify playback and search via spogo (preferred) or spotify_player.

## Requirements
- Spotify Premium account
- spogo or spotify_player installed

## Setup
```bash
spogo auth import --browser chrome
```

## spogo Commands (Preferred)
```bash
spogo search track "query"
spogo play
spogo pause
spogo next
spogo prev
spogo device list
spogo device set "<device-name>"
spogo status
```

## spotify_player Commands (Fallback)
```bash
spotify_player search "query"
spotify_player playback play
spotify_player playback pause
spotify_player playback next
spotify_player playback previous
spotify_player connect
spotify_player like
```

## Notes
- Config: ~/.config/spotify-player/app.toml
- For Spotify Connect, set a user client_id in config
- TUI shortcuts via ? in the app
