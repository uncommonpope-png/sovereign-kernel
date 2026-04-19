# google-workspace

Control all Google Workspace services — Drive, Gmail, Calendar, Sheets, Docs, Chat — via the gws CLI or REST API.

## What this skill does
Manages files, emails, events, spreadsheets, and documents across Google Workspace with a single authenticated CLI or Python client.

## Setup
```bash
pip install google-auth google-auth-oauthlib google-api-python-client
# Obtain credentials.json from Google Cloud Console
# Enable: Drive API, Gmail API, Calendar API, Sheets API
```

## Authentication
```python
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
```

## Drive
```python
from googleapiclient.discovery import build
service = build('drive', 'v3', credentials=creds)
results = service.files().list(pageSize=10, fields="files(id,name)").execute()
for f in results.get('files',[]):
    print(f['name'], f['id'])
```

## Gmail — send email
```python
import base64
from email.mime.text import MIMEText
service = build('gmail', 'v1', credentials=creds)
msg = MIMEText("Body text")
msg['to'] = "recipient@example.com"
msg['subject'] = "From Sovereign Kernel"
raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
service.users().messages().send(userId='me', body={'raw': raw}).execute()
```

## Calendar — create event
```python
service = build('calendar', 'v3', credentials=creds)
event = {'summary': 'PLT Council', 'start': {'dateTime': '2026-04-19T10:00:00Z'},
         'end': {'dateTime': '2026-04-19T11:00:00Z'}}
service.events().insert(calendarId='primary', body=event).execute()
```

## Example commands
```
ACTION: List the 10 most recent files in Google Drive
ACTION: Send a Gmail summary of today's council deliberation to the configured address
```
