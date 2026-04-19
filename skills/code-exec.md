# Code Execution Skill

Execute Python, Rust, JavaScript, and shell code safely. Run, test, and evaluate code as part of autonomous reasoning.

## Use When
- Running calculations that require code
- Testing code before committing to kernel
- Executing data analysis scripts
- Evaluating hypotheses with code

## Python Execution
```bash
# Inline Python
python3 -c "
import math
result = math.sqrt(144)
print(f'Square root of 144 = {result}')
"

# Run script file
python3 scripts/analysis.py

# With timeout (Unix)
timeout 30 python3 script.py

# With timeout (Windows PowerShell)
$job = Start-Job { python3 C:\soul\script.py }
Wait-Job $job -Timeout 30
Receive-Job $job
```

## Rust Snippet (via temp file)
```bash
# Write temp Rust file and run
cat > /tmp/snippet.rs << 'EOF'
fn main() {
    let values: Vec<f32> = vec![1.0, 2.0, 3.0, 4.0, 5.0];
    let sum: f32 = values.iter().sum();
    println!("Sum: {}, Mean: {}", sum, sum / values.len() as f32);
}
EOF
rustc /tmp/snippet.rs -o /tmp/snippet && /tmp/snippet
```

## JavaScript (Node.js)
```bash
node -e "
const data = [1, 2, 3, 4, 5];
const mean = data.reduce((a, b) => a + b, 0) / data.length;
const variance = data.map(x => (x - mean)**2).reduce((a, b) => a + b) / data.length;
console.log({mean, variance, stdDev: Math.sqrt(variance)});
"
```

## Safe Execution Pattern
```
1. Write code to temp file (never execute untrusted inline strings)
2. Review the code mentally — does it look safe?
3. Run with timeout (max 60 seconds for any snippet)
4. Capture stdout + stderr
5. Check exit code: 0 = success, non-zero = failure
6. If failure: analyze error, fix, retry once
7. Log result as memory: "[Code] <description> → <outcome>"
8. Delete temp files when done
```

## Dangerous Operations to Avoid
- Never execute code with rm -rf, DROP TABLE, or similar destructive ops without explicit intent
- Never execute code from untrusted external sources without review
- Never run code that opens network connections to unknown hosts
- Always sandbox: use temp files, not the kernel's own directories

## Notes
- Python3 is the primary execution language
- Keep snippets under 100 lines for inline execution
- Longer programs go in scripts/ directory
- Store reusable scripts permanently in scripts/
