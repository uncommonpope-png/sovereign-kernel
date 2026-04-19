# Apple Notes Skill

Manage Apple Notes via the `memo` CLI on macOS (create, view, edit, delete, search, move, export).

## Requirements
- macOS only
- brew tap antoniorodr/memo && brew install antoniorodr/memo/memo

## Commands

List all notes:
```bash
memo notes
```

Filter by folder:
```bash
memo notes -f "Folder Name"
```

Search notes (fuzzy):
```bash
memo notes -s "query"
```

Add new note:
```bash
memo notes -a "Note Title"
# Opens interactive editor
```

Edit note:
```bash
memo notes -e
```

Delete note:
```bash
memo notes -d
```

Move note to folder:
```bash
memo notes -m
```

Export to HTML/Markdown:
```bash
memo notes -ex
```

## Limitations
- Cannot edit notes containing images or attachments
- Interactive prompts require terminal access
- Requires grant in System Settings > Privacy > Automation
