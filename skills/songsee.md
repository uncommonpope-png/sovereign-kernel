# Songsee Skill

Music identification and song lookup — identify songs by audio or search for music metadata.

## Use When
- Identifying a song from audio
- Looking up song metadata, lyrics, or chords
- Searching for music by title/artist

## Audio Fingerprinting (shazam-like)
```bash
# songsee CLI (if installed)
songsee --file audio.mp3
songsee --record 10   # record 10 seconds and identify

# Using ACRCloud API
curl -X POST "https://identify-us-west-2.acrcloud.com/v1/identify" \
  -F "sample=@audio_clip.mp3" \
  -F "access_key=$ACRCLOUD_KEY" \
  -F "data_type=audio" \
  | jq '.metadata.music[0] | {title, artist: .artists[0].name, album: .album.name}'
```

## Lyrics Search
```bash
# Genius API
curl -H "Authorization: Bearer $GENIUS_TOKEN" \
  "https://api.genius.com/search?q=Bohemian+Rhapsody" \
  | jq '.response.hits[0].result | {title, artist: .primary_artist.name, url}'

# LRClib (free, no key)
curl "https://lrclib.net/api/search?q=Bohemian+Rhapsody&artist_name=Queen" \
  | jq '.[0] | {trackName, artistName, duration}'
```

## Music Metadata (MusicBrainz — free)
```bash
curl "https://musicbrainz.org/ws/2/recording/?query=title:Bohemian+Rhapsody+AND+artist:Queen&fmt=json" \
  | jq '.recordings[0] | {title, length, "artist": .["artist-credit"][0].name}'
```

## Notes
- songsee CLI wraps audio fingerprinting services
- ACRCloud has a free tier for identification
- MusicBrainz is fully free and open-source
