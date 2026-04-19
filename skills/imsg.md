# iMsg Skill

Send and read iMessages via macOS AppleScript or imsg CLI.

## Use When
- Sending iMessages programmatically on macOS
- Reading recent iMessage conversations

## Send iMessage (AppleScript)
```bash
osascript -e 'tell application "Messages"
  set targetBuddy to "+1234567890"
  set targetService to 1st service whose service type = iMessage
  set textBuddy to buddy targetBuddy of targetService
  send "Hello from terminal!" to textBuddy
end tell'
```

## imsg CLI (if installed)
```bash
imsg send "+1234567890" "Hello!"
imsg list                          # list recent conversations
imsg read "+1234567890"            # read messages from contact
```

## Read Messages (AppleScript)
```applescript
tell application "Messages"
  set theChats to chats
  set output to {}
  repeat with c in theChats
    set end of output to name of c
  end repeat
  return output
end tell
```

## Notes
- macOS only
- Requires Messages app running and iMessage account signed in
- Phone numbers must include country code: +1XXXXXXXXXX
- osascript may prompt for Automation permission on first use
- Messages.app must have permission in Privacy & Security > Automation
