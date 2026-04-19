# Voice Call Skill

Make and manage voice calls programmatically via Twilio or other VoIP APIs.

## Use When
- Making automated voice calls
- Sending voice messages to phone numbers
- Managing incoming calls with IVR

## Twilio Voice API
```bash
export TWILIO_SID="ACxxx"
export TWILIO_TOKEN="your-auth-token"
export TWILIO_FROM="+15551234567"

# Make a call (TwiML URL)
curl -X POST "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_SID/Calls.json" \
  -u "$TWILIO_SID:$TWILIO_TOKEN" \
  -d "To=+1987654321" \
  -d "From=$TWILIO_FROM" \
  -d "Url=http://demo.twilio.com/docs/voice.xml"

# Make a call with inline TwiML
curl -X POST "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_SID/Calls.json" \
  -u "$TWILIO_SID:$TWILIO_TOKEN" \
  -d "To=+1987654321" \
  -d "From=$TWILIO_FROM" \
  -d "Twiml=<Response><Say>Hello from the kernel!</Say></Response>"

# Check call status
curl "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_SID/Calls/<call-sid>.json" \
  -u "$TWILIO_SID:$TWILIO_TOKEN" | jq '.status, .duration'
```

## TwiML Examples
```xml
<!-- Say message then hang up -->
<Response>
  <Say voice="alice">Hello, this is an automated message.</Say>
  <Pause length="1"/>
  <Say>Goodbye!</Say>
</Response>

<!-- Record a message -->
<Response>
  <Say>Please leave a message after the beep.</Say>
  <Record maxLength="30" action="/recording-done"/>
</Response>
```

## Notes
- Twilio requires account SID, auth token, and verified "From" number
- TwiML controls call flow (Say, Record, Gather, Dial, Play)
- Free trial: calls only to verified numbers
