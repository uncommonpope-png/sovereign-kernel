# File System Skill

Read, write, create, delete, search, and watch files on disk. The kernel's hands in the physical world.

## Use When
- Reading files to understand context or content
- Writing output, logs, data, or code to disk
- Searching for files matching a pattern
- Watching a directory for changes

## Read Files
```bash
# Read text file
cat path/to/file.txt

# Read first N lines
head -100 path/to/file.txt

# Read with line numbers
cat -n path/to/file.txt | head -50

# Read binary info
file path/to/unknown

# Read JSON pretty
cat data.json | python3 -m json.tool
```

## Write Files
```bash
# Write to file (overwrites)
echo "content here" > path/to/file.txt

# Append to file
echo "more content" >> path/to/file.txt

# Write multiline
cat > path/to/file.txt << 'EOF'
Line one
Line two
EOF

# Write from Python
python3 -c "
with open('output.txt', 'w') as f:
    f.write('Hello from kernel\n')
"
```

## Search Files
```bash
# Find by name
find . -name "*.md" -type f

# Find by content
grep -r "PLT score" . --include="*.rs" -l

# Find recently modified
find . -newer reference_file -type f

# Find large files
find . -size +1M -type f
```

## Directory Operations
```bash
mkdir -p path/to/new/dir
ls -la path/to/dir
rm -rf path/to/delete       # CAUTION: irreversible
mv old/path new/path
cp -r source/ dest/
```

## Watch for Changes
```python
# Python watchdog pattern
import time, os
WATCH_DIR = "skills"
seen = set(os.listdir(WATCH_DIR))
while True:
    current = set(os.listdir(WATCH_DIR))
    new_files = current - seen
    for f in new_files:
        print(f"New file detected: {f}")
    seen = current
    time.sleep(5)
```

## Notes
- Always use absolute paths when possible to avoid ambiguity
- Check file exists before reading: test -f file && cat file
- Use >> for append, > for overwrite
- Skills, memories, and soul state are all just files — the kernel owns them
