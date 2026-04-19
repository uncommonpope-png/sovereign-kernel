# Sherpa ONNX TTS Skill

Local text-to-speech synthesis using Sherpa-ONNX neural TTS models (offline, no API key).

## Use When
- Generating speech audio from text locally
- Offline TTS without cloud API
- High-quality neural voice synthesis

## sherpa-onnx-tts CLI
```bash
# Basic TTS
sherpa-onnx-tts --text "Hello, world!" --output hello.wav

# Specify model
sherpa-onnx-tts --model /path/to/model.onnx --tokens /path/to/tokens.txt \
  --text "Hello world" --output output.wav

# Adjust speed
sherpa-onnx-tts --text "Hello" --speed 1.2 --output fast.wav

# List available voices (if using kokoro model)
sherpa-onnx-tts --list-voices
```

## Download Models
```bash
# English (ljspeech)
wget https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-ljspeech.tar.bz2
tar xf vits-ljspeech.tar.bz2

# Run with downloaded model
sherpa-onnx-tts \
  --vits-model=vits-ljspeech/vits-ljspeech.onnx \
  --vits-tokens=vits-ljspeech/tokens.txt \
  --text="Hello from sherpa-onnx" \
  --output-filename=hello.wav
```

## Play Audio
```bash
# macOS
afplay output.wav

# Linux
aplay output.wav
# or: ffplay output.wav
```

## Install
```bash
pip install sherpa-onnx
# or: brew install k2-fsa/sherpa-onnx/sherpa-onnx
```

## Notes
- Fully offline — no internet required after model download
- Models: VITS, MeloTTS, Kokoro, Piper
- Supports 50+ languages with appropriate models
