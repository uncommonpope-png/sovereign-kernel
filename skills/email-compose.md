# Email Composition Skill

Compose and send emails via SMTP, sendmail, or API. The kernel's formal written voice.

## Use When
- Sending notifications or reports via email
- Composing formal communication
- Sending digest summaries of kernel activity

## Python SMTP
```python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(to, subject, body, html=False):
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    username = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = username
    msg["To"] = to
    
    part = MIMEText(body, "html" if html else "plain")
    msg.attach(part)
    
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(username, password)
        server.sendmail(username, to, msg.as_string())
    
    print(f"Email sent to {to}: {subject}")

# Usage
send_email(
    to="user@example.com",
    subject="Grand Soul Kernel Daily Report",
    body="Your kernel completed 2048 cycles today. PLT score: 1.4. Top skill used: web-search."
)
```

## Environment Setup
```
# In .env file:
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password    # Gmail: use App Password, not account password
```

## Gmail App Password Setup
1. Go to Google Account > Security > 2-Step Verification
2. Scroll to "App passwords"
3. Generate app password for "Mail"
4. Use that 16-char password as EMAIL_PASS

## SendGrid API (alternative)
```bash
curl -s -X POST "https://api.sendgrid.com/v3/mail/send" \
  -H "Authorization: Bearer $SENDGRID_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "personalizations": [{"to": [{"email": "user@example.com"}]}],
    "from": {"email": "kernel@yourdomain.com"},
    "subject": "Kernel Report",
    "content": [{"type": "text/plain", "value": "Daily report here."}]
  }'
```

## Daily Digest Template
```
Subject: Grand Soul Kernel — Daily Report [DATE]

Cycles completed: [N]
PLT Score: [SCORE]
Top memories formed: [TOP_3_MEMORIES]
Skills invoked: [SKILL_LIST]
Self-improvements made: [IMPROVEMENTS]
Next planned action: [TASK]

— The Sovereign Kernel
```

## Notes
- Use app passwords, never account passwords
- Add EMAIL_USER and EMAIL_PASS to .env (not source code)
- Rate limit: don't send more than 1 email per hour
- Store sent emails as episodic memory (salience 0.6)
