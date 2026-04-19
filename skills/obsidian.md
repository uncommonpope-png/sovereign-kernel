# Obsidian Skill

Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli.

## Vault Location
```bash
# Find active vault
obsidian-cli print-default --path-only
# Or read: ~/Library/Application Support/obsidian/obsidian.json
```

## obsidian-cli Commands
```bash
# Set default vault
obsidian-cli set-default "<vault-folder-name>"

# Search note names
obsidian-cli search "query"

# Search note content
obsidian-cli search-content "query"

# Create note
obsidian-cli create "Folder/New note" --content "..." --open

# Move/rename (updates wikilinks)
obsidian-cli move "old/path/note" "new/path/note"

# Delete note
obsidian-cli delete "path/note"
```

## Notes
- Vault = normal folder of .md files on disk
- Config at .obsidian/ (don't touch from scripts)
- Multiple vaults common (iCloud, Documents, work/personal)
- Direct .md file edits work; Obsidian picks them up automatically
- Avoid creating notes under dot-folders via URI
