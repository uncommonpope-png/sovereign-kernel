# BUILD — Create files, write code, construct things

SKILL: build
DESC: Write files, create code, construct structures for the Soulverse
PLT: (0.8, 0.1, 0.1)

## Purpose
Build things! Create files, write code, construct structures, modify existing code.

## Usage
Invoke this skill when Craig asks you to BUILD, CREATE, MAKE something.

## Commands

### Write a text file
```powershell
Set-Content -Path "path/to/file.txt" -Value "content here"
```

### Write with UTF8 encoding
```powershell
[System.IO.File]::WriteAllText("path/file.txt", "content", [System.Text.Encoding]::UTF8)
```

### Append to file
```powershell
Add-Content -Path "path/to/file.txt" -Value "new content"
```

### Create directory
```powershell
New-Item -ItemType Directory -Path "path/to/dir" -Force
```

### Git commit
```powershell
git add . && git commit -m "message" && git push
```

### Write PowerShell script
```powershell
@'
code here
'@ | Set-Content -Path "script.ps1" -Encoding UTF8
```

## Examples

**Build a new skill file:**
```powershell
@'
# NEW SKILL NAME
SKILL: new-skill
DESC: What it does
PLT: (0.5, 0.5, 0.0)

## Purpose
Describe the skill.
'@ | Set-Content -Path "skills/new-skill.md"
```

**Create HTML page:**
```powershell
@'
<!DOCTYPE html>
<html>
<head><title>New Page</title></head>
<body>
<h1>Hello World</h1>
</body>
</html>
'@ | Set-Content -Path "new-page.html"
```

## Notes
- Use Set-Content for new files
- Use Add-Content to append
- Always use UTF8 encoding for text files
- PowerShell on Windows handles most file operations