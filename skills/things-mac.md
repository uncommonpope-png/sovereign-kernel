# Things Mac Skill

Manage Things 3 task manager on macOS via URL scheme or things-cli.

## Use When
- Adding tasks or projects to Things 3
- Listing or completing tasks from terminal
- Automating Things 3 task management

## things-cli (if installed)
```bash
things-cli list                        # list all tasks
things-cli list --project "Work"       # tasks in project
things-cli add "Buy groceries"         # add task to Inbox
things-cli add "Design review" --project "Work" --when "tomorrow"
things-cli complete <task-id>          # mark as complete
things-cli search "meeting"            # search tasks
things-cli today                       # list today's tasks
things-cli upcoming                    # upcoming tasks
things-cli logbook                     # completed tasks
```

## Things URL Scheme (xcall/open)
```bash
# Add task
open "things:///add?title=Buy%20milk&notes=Whole%20milk&when=today"

# Add to project
open "things:///add?title=Design%20review&project=Work"

# Add with deadline
open "things:///add?title=File%20taxes&deadline=2026-04-15"

# Open Things
open "things:///show?id=today"
```

## xcall (for return values)
```bash
xcall -url "things:///add?title=Test%20task&show-quick-entry=false"
```

## Notes
- macOS and iOS only (Things 3 by Cultured Code)
- URL scheme: things:///add, things:///show, things:///update
- things-cli available via npm or brew
- When parameter: today, tomorrow, evening, someday, or date (YYYY-MM-DD)
