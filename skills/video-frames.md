# Video Frames Skill

Extract frames from video files and process video content with ffmpeg.

## Use When
- Extracting specific frames or thumbnails from videos
- Converting video clips or formats
- Analyzing video content frame by frame

## Extract Frames
```bash
# Extract all frames
ffmpeg -i video.mp4 frames/frame_%04d.png

# Extract every 1 second (1 fps)
ffmpeg -i video.mp4 -vf fps=1 frames/frame_%04d.png

# Extract specific time range
ffmpeg -i video.mp4 -ss 00:00:10 -t 5 -vf fps=2 frames/frame_%04d.png

# Extract single frame at timestamp
ffmpeg -i video.mp4 -ss 00:00:30 -vframes 1 thumbnail.png

# Extract at specific scene changes
ffmpeg -i video.mp4 -vf "select=gt(scene\,0.4),scale=320:-1" -vsync vfr frames/scene_%04d.jpg
```

## Create Thumbnails
```bash
# Grid of thumbnails (contact sheet)
ffmpeg -i video.mp4 -vf "select=not(mod(n\,50)),scale=160:-1,tile=5x5" thumbnail_grid.png

# Single best thumbnail
ffmpeg -i video.mp4 -vf thumbnail,scale=640:-1 -frames:v 1 best_thumb.png
```

## Video Info
```bash
ffprobe -v quiet -print_format json -show_streams video.mp4 | jq '.streams[0] | {width, height, duration, r_frame_rate, codec_name}'
```

## Trim Video
```bash
ffmpeg -i input.mp4 -ss 00:00:10 -to 00:00:30 -c copy output.mp4
```

## Notes
- ffmpeg required (brew install ffmpeg)
- Frames directory must exist before extraction
- JPEG smaller than PNG, PNG lossless
