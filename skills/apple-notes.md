# Apple Notes Skill

Easily manage Apple Notes using the `memo` CLI on macOS for creating, viewing, editing, deleting, searching, moving, and exporting notes.

## Requirements
- **macOS only**
- Install `memo` via Homebrew:
  ```bash
  brew tap antoniorodr/memo && brew install antoniorodr/memo/memo
  ```

## Common Commands

- **List all notes**:
  ```bash
  memo notes
  ```

- **Filter notes by folder**:
  ```bash
  memo notes -f "Folder Name"
  ```

- **Search notes (supports fuzzy search)**:
  ```bash
  memo notes -s "query"
  ```

- **Add a new note**:
  ```bash
  memo add -t "Note Title" -c "Note content" -f "Folder Name"
  ```

- **Edit an existing note**:
  ```bash
  memo edit "Note Title"
  ```

- **Delete a note**:
  ```bash
  memo remove "Note Title"
  ```

- **Export notes as plain text**:
  ```bash
  memo export -f "Folder Name" -o ~/Desktop/NotesBackup
  ```

## Examples

1. **Create a shopping list in the "Home" folder**:
   ```bash
   memo add -t "Shopping List" -c "Milk, Eggs, Bread" -f "Home"
   ```

2. **Search for all notes containing 'project' within the "Work" folder**:
   ```bash
   memo notes -s "project" -f "Work"
   ```

`memo` provides a simplified interface to organize and interact with your Apple Notes efficiently within the terminal. All operations can be performed without requiring the Notes app GUI. For more details, refer to the [memo documentation](https://github.com/antoniorodr/memo-cli).