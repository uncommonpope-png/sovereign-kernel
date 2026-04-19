# OpenAI Whisper Skill

Local speech-to-text transcription with the Whisper CLI (no API key needed).

## Quick Start
```bash
whisper /path/audio.mp3 --model medium --output_format txt --output_dir .
whisper /path/audio.m4a --task translate --output_format srt
```

## Models
- tiny, base, small, medium, large, turbo (default on this install)
- Smaller = faster, larger = more accurate
- Models download to ~/.cache/whisper on first run

## Output Formats
- txt, srt, vtt, json, tsv

## Common Options
```bash
whisper audio.mp3 --model small --language en --output_format txt
whisper audio.mp3 --task translate --output_format srt
whisper audio.mp3 --model large --output_dir ./transcripts
```

## Notes
- No API key required — runs fully offline
- First run downloads the model (may take time)
- Supports most audio formats: mp3, m4a, wav, flac, ogg
