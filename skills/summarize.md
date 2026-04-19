# Summarize Skill

Summarize or extract text/transcripts from URLs, podcasts, YouTube videos, and local files.

## Use When
- "summarize this URL/article"
- "what's this link/video about?"
- "transcribe this YouTube/video"
- "use summarize.sh"

## Quick Start
```bash
summarize "https://example.com" --model google/gemini-3-flash-preview
summarize "/path/to/file.pdf" --model google/gemini-3-flash-preview
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto
```

## YouTube Transcript
```bash
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto --extract-only
```

## Useful Flags
- `--length short|medium|long|xl|xxl|<chars>`
- `--extract-only` (URLs only — get raw text)
- `--json` (machine readable)
- `--youtube auto` (Apify fallback if APIFY_API_TOKEN set)

## Environment Variables
- OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, XAI_API_KEY
- Default model: google/gemini-3-flash-preview

## Config
~/.summarize/config.json: `{"model":"openai/gpt-5.2"}`
