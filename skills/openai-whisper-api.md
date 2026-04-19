# OpenAI Whisper API Skill

Cloud-based speech-to-text via OpenAI Whisper API (requires API key, no local install).

## Use When
- Transcribing audio without local Whisper install
- Need faster transcription via cloud
- Large files or batch transcription

## Setup
```bash
export OPENAI_API_KEY="sk-..."
```

## Transcription
```bash
# Transcribe audio file
curl -s -X POST "https://api.openai.com/v1/audio/transcriptions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@audio.mp3" \
  -F "model=whisper-1" \
  | jq '.text'

# With language hint (faster)
curl -s -X POST "https://api.openai.com/v1/audio/transcriptions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@audio.mp3" \
  -F "model=whisper-1" \
  -F "language=en" \
  | jq '.text'

# SRT subtitle format
curl -s -X POST "https://api.openai.com/v1/audio/transcriptions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@audio.mp3" \
  -F "model=whisper-1" \
  -F "response_format=srt"
```

## Translation (to English)
```bash
curl -s -X POST "https://api.openai.com/v1/audio/translations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@audio_spanish.mp3" \
  -F "model=whisper-1" \
  | jq '.text'
```

## Python SDK
```python
from openai import OpenAI
client = OpenAI()
with open("audio.mp3", "rb") as f:
    result = client.audio.transcriptions.create(model="whisper-1", file=f)
print(result.text)
```

## Notes
- Supported formats: mp3, mp4, mpeg, mpga, m4a, wav, webm
- Max file size: 25MB
- Cost: $0.006/minute
