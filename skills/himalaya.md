# Himalaya Skill

Email client and management via himalaya CLI — read, send, and manage email from the terminal.

## Use When
- Reading and sending email from the terminal
- Managing email folders and labels
- Automating email workflows

## Setup
```bash
# Install
brew install himalaya

# Configure (~/.config/himalaya/config.toml)
[accounts.personal]
email = "you@example.com"
display-name = "Your Name"
[accounts.personal.imap]
host = "imap.gmail.com"
port = 993
login = "you@example.com"
[accounts.personal.smtp]
host = "smtp.gmail.com"
port = 465
login = "you@example.com"
```

## Commands
```bash
# List messages
himalaya list

# Read message
himalaya read <id>

# Send email
himalaya send --subject "Hello" --to "user@example.com" --body "Message text"

# Reply
himalaya reply <id>

# Search
himalaya search "from:boss@company.com"

# List folders/mailboxes
himalaya folders

# Move to folder
himalaya move <id> Trash

# Flag as read
himalaya flag add <id> Seen
```

## Notes
- Supports Gmail, Fastmail, Proton Mail, and any IMAP/SMTP server
- Config file: ~/.config/himalaya/config.toml
- OAuth2 supported for Gmail
- Use app passwords for Gmail with 2FA enabled
