# GifGrep Skill

Search and capture GIFs — find animated GIFs by keyword or extract frames from video.

## Use When
- Finding GIFs by keyword or mood
- Extracting GIF frames from video files
- Converting video clips to GIF format

## Search for GIFs (Tenor/Giphy API)
```bash
# Tenor (free tier, no key needed for basic)
curl -s "https://tenor.googleapis.com/v2/search?q=celebration&limit=5&key=LIVDSRZULELA" \
  | jq '.results[].url'

# Giphy (requires API key)
curl -s "https://api.giphy.com/v1/gifs/search?q=dancing&limit=5&api_key=$GIPHY_KEY" \
  | jq '.data[].url'
```

## Convert Video to GIF
```bash
# Basic conversion
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1" output.gif

# With palette for quality
ffmpeg -i input.mp4 -vf "fps=10,scale=480:-1,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png -vf "fps=10,scale=480:-1,paletteuse" output.gif

# Trim clip first
ffmpeg -i input.mp4 -ss 00:00:05 -t 3 -vf "fps=10,scale=480:-1" clip.gif
```

## Extract GIF Frames
```bash
# Extract all frames as PNG
ffmpeg -i input.gif frames/frame_%04d.png

# Extract specific frame
ffmpeg -i input.gif -vf "select=eq(n\,5)" -vframes 1 frame5.png
```

## gifgrep CLI (if installed)
```bash
gifgrep "celebration"       # search and display GIFs
gifgrep --download "dance"  # download matching GIFs
```

## Notes
- ffmpeg required for video/GIF conversion
- Keep GIFs under 5MB for best performance
