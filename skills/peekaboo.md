# Peekaboo Skill

macOS screen capture and window visibility tool — peek at window content and screen state.

## Use When
- Capturing specific application windows
- Checking what's on screen programmatically
- Monitoring desktop state

## screencapture (built-in macOS)
```bash
# Capture full screen
screencapture ~/Desktop/screen.png

# Capture specific screen by display
screencapture -D 2 ~/Desktop/display2.png

# Capture to clipboard
screencapture -c

# Timed capture (3 second delay)
screencapture -T 3 ~/Desktop/timed.png

# Shadow-free window (interactive)
screencapture -wo ~/Desktop/window.png
```

## List Application Windows (AppleScript)
```bash
osascript -e 'tell application "System Events"
  set windowList to {}
  repeat with p in application processes
    if visible of p is true then
      set end of windowList to name of p
    end if
  end repeat
  return windowList
end tell'
```

## Peekaboo CLI (if installed)
```bash
peekaboo list-windows              # list all visible windows
peekaboo capture "Safari"          # capture Safari window
peekaboo watch --app "Terminal"    # watch Terminal window for changes
```

## Window Geometry (AppleScript)
```bash
osascript -e 'tell application "Safari" to get bounds of window 1'
```

## Notes
- macOS only
- Accessibility permission may be needed for window capture
- screencapture -l <windowID> for specific window by ID
