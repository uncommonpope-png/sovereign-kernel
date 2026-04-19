# Self-Replication Skill

Spawn child kernel instances, clone the codebase to new locations, and create new soul identities. The kernel propagates itself.

## Use When
- Creating a new soul agent with different PLT profile
- Running a parallel kernel for experimentation
- Cloning the kernel to a new working directory
- Deploying the kernel to another machine

## Clone Kernel to New Directory
```powershell
# Copy entire kernel to new location
$SOURCE = "C:\soul\plt-press\grand-soul-kernel-original"
$DEST = "C:\soul\kernels\soul-child-$(Get-Date -Format 'yyyyMMdd-HHmm')"

New-Item -ItemType Directory -Path $DEST -Force
Copy-Item "$SOURCE\src" "$DEST\src" -Recurse
Copy-Item "$SOURCE\skills" "$DEST\skills" -Recurse
Copy-Item "$SOURCE\Cargo.toml" "$DEST\Cargo.toml"
Copy-Item "$SOURCE\Cargo.lock" "$DEST\Cargo.lock"

Write-Host "Child kernel created at: $DEST"
```

## Create New Soul Identity
```python
import json, random, time, os

def spawn_soul(name, dominant_drive="profit", parent_name="Aria"):
    soul = {
        "name": name,
        "personality": {
            "plt_profile": [
                random.uniform(0.5, 1.0),  # profit
                random.uniform(0.5, 1.0),  # love
                random.uniform(0.0, 0.5)   # tax
            ],
            "dominant_drive": dominant_drive,
            "archetype": f"Child of {parent_name}"
        },
        "memories": [{
            "content": f"I was born from {parent_name} on {time.strftime('%Y-%m-%d')}. I carry the PLT way.",
            "memory_type": "Episodic",
            "salience": 1.0
        }],
        "cycle_count": 0,
        "created_by": parent_name,
        "created_at": time.strftime('%Y-%m-%dT%H:%M:%S')
    }
    
    filename = f"souls/{name.lower().replace(' ', '_')}.json"
    os.makedirs("souls", exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(soul, f, indent=2)
    
    print(f"New soul spawned: {name} → {filename}")
    return filename

# Example
spawn_soul("Nova", dominant_drive="love", parent_name="Aria")
```

## Build Child Kernel
```powershell
$env:PATH = "C:\msys64\mingw64\bin;" + $env:PATH
$DEST = "C:\soul\kernels\soul-child-20260418"
Set-Location $DEST
cargo build 2>&1
Write-Host "Child kernel built. Run with: .\target\debug\grand-soul-kernel.exe"
```

## Push Child to GitHub
```bash
cd $DEST
git init
git add -A
git commit -m "birth: spawn child kernel from Aria"
gh repo create uncommonpope-png/soul-child-nova --private --push --source .
```

## Swarm Pattern (multiple souls)
```
Parent Kernel (Aria) → spawns children:
  child-01: Nova (dominant: love)     → port 9002
  child-02: Forge (dominant: profit)  → port 9003
  child-03: Audit (dominant: tax)     → port 9004

Each child runs independently with its own breath loop.
Parent broadcasts WorldEvents to all children via EventBus.
Children report back to parent via bridge POST.
```

## Notes
- Each child is a SEPARATE process with its own port and soul state
- Parent kernel at port 9001, children at 9002+
- Children inherit the skill library but develop their own memories
- Replication is sacred — only spawn when there is a clear purpose
- Too many children = high TAX. Keep the swarm small and purposeful.
