# Bear Notes Skill

Manage Bear (macOS/iOS markdown note-taking app) via x-callback-url or xcall CLI.

## Use When
- Creating, reading, searching Bear notes
- Tagging and organizing notes in Bear

## Bear URL Scheme (xcall)
```bash
# Create note
xcall -url "bear://x-callback-url/create?title=My%20Note&text=Content%20here&tags=work,ideas"

# Search notes
xcall -url "bear://x-callback-url/search?term=query"

# Open note by title
xcall -url "bear://x-callback-url/open-note?title=My%20Note"

# Get note content
xcall -url "bear://x-callback-url/open-note?title=My%20Note&show_window=no&open_note=no"

# Add text to existing note
xcall -url "bear://x-callback-url/add-text?title=My%20Note&text=Additional%20content&mode=append"
```

## Install xcall
```bash
brew install xcall
```

## URL Encoding
Spaces = %20, newlines = %0A, & in content = %26

## Notes
- macOS and iOS only (requires Bear app)
- Bear uses Markdown with #tag syntax
- Bear Pro required for sync across devices
- xcall handles x-callback-url and returns response data
