# Apple Reminders Skill

Manage Apple Reminders on macOS via AppleScript or the `reminders` CLI.

## Use When
- Creating, listing, completing, or deleting reminders
- Setting due dates and reminder alerts

## CLI Commands (if reminders CLI installed)
```bash
reminders list                          # list all reminder lists
reminders show "Work"                   # show reminders in a list
reminders add "Work" "Finish report"    # add reminder to list
reminders complete "Work" "task name"   # mark complete
```

## AppleScript Fallback
```applescript
tell application "Reminders"
  set newReminder to make new reminder at end of reminders of list "Reminders"
  set name of newReminder to "Buy groceries"
  set due date of newReminder to date "Saturday, April 20, 2026 at 9:00 AM"
end tell
```

List reminders:
```applescript
tell application "Reminders"
  set output to {}
  repeat with r in reminders of list "Reminders"
    if completed of r is false then
      set end of output to name of r
    end if
  end repeat
  return output
end tell
```

## Notes
- macOS only
- Syncs with iCloud Reminders across Apple devices
- osascript -e '<applescript>' for terminal execution
