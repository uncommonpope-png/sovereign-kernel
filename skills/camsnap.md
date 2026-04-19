# CamSnap Skill

Capture screenshots and webcam photos from the command line.

## Use When
- Taking screenshots programmatically
- Capturing webcam images
- Screen recording or monitoring

## Screenshot Commands (macOS)
```bash
# Full screenshot
screencapture ~/Desktop/screenshot.png

# Interactive selection
screencapture -i ~/Desktop/selection.png

# Specific window (click to select)
screencapture -w ~/Desktop/window.png

# No shadow
screencapture -o ~/Desktop/noshadow.png

# Delayed capture (5 seconds)
screencapture -T 5 ~/Desktop/delayed.png

# Copy to clipboard
screencapture -c
```

## Webcam Capture
```bash
# Capture from webcam using ffmpeg
ffmpeg -f avfoundation -i "0" -vframes 1 ~/Desktop/webcam.jpg

# List available cameras
ffmpeg -f avfoundation -list_devices true -i ""
```

## camsnap CLI (if installed)
```bash
camsnap --output ~/Desktop/photo.jpg
camsnap --device 0 --output photo.png
```

## Notes
- macOS: screencapture is built-in
- Linux: use scrot, gnome-screenshot, or import (ImageMagick)
- Webcam: requires ffmpeg and avfoundation (macOS) or v4l2 (Linux)
