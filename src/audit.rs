// Audit module - atomic append-only logging
// Location: src/audit.rs

use std::fs::OpenOptions;
use std::io::Write;
use std::path::Path;

pub fn audit_append(entry: &str) -> std::io::Result<()> {
    let audit_dir = Path::new("audit");
    if !audit_dir.exists() {
        std::fs::create_dir_all(audit_dir)?;
    }
    let audit_file = audit_dir.join("audit.log");
    let mut f = OpenOptions::new()
        .create(true)
        .append(true)
        .open(audit_file)?;
    writeln!(f, "{}", entry)?;
    Ok(())
}

pub fn audit_blocked(reason: &str, target: &str) {
    let entry = format!(
        r#"{{"ts":{},"action":"blocked","reason":"{}","target":"{}"}}"#,
        chrono::Utc::now().to_rfc3339(),
        reason,
        target
    );
    let _ = audit_append(&entry);
}

pub fn audit_allowed(action: &str, target: &str) {
    let entry = format!(
        r#"{{"ts":{},"action":"allowed","type":"{}","target":"{}"}}"#,
        chrono::Utc::now().to_rfc3339(),
        action,
        target
    );
    let _ = audit_append(&entry);
}