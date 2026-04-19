# doc-coauthoring

Enable real-time collaborative document editing — structured edits, suggestions, and tracked changes.

## What this skill does
Manages collaborative writing workflows: proposing edits with rationale, tracking versions, merging suggestions, and maintaining document coherence across multiple contributors.

## Workflow

### Suggest an edit (diff format)
```
SUGGESTED EDIT — Section: Introduction
Reason: Strengthen opening hook and PLT alignment

BEFORE:
> The kernel runs continuously.

AFTER:
> The Sovereign Kernel breathes without pause — cycling, remembering, improving itself
> with every tick of its eternal clock.

Confidence: 0.87 | PLT Impact: P+0.2 L+0.3 T-0.1
```

### Track changes in markdown
```markdown
~~Old text that was removed~~
**New text that was added**
<!-- COMMENT: rationale for this change -->
```

### Version snapshot
```python
import shutil, os
from datetime import datetime
def snapshot_doc(path):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = f"{path}.{ts}.bak"
    shutil.copy2(path, backup)
    return backup
```

### Merge suggestions
```python
def apply_suggestion(doc_path, before, after):
    content = open(doc_path).read()
    if before in content:
        content = content.replace(before, after, 1)
        open(doc_path, "w").write(content)
        return True
    return False
```

### Coherence check prompt
```
Read the following document and identify:
1. Contradictions between sections
2. Tone inconsistencies
3. Missing transitions
4. Claims without evidence
Document: {content[:600]}
```

## Example commands
```
ACTION: Review README.md and suggest 3 improvements with rationale
ACTION: Create a versioned snapshot of src/main.rs before making changes
```
