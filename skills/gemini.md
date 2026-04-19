# Gemini Skill

Interact with Google Gemini AI models via the Gemini API or SDK.

## Use When
- Sending prompts to Gemini models
- Generating text, code, or analysis with Gemini
- Using multimodal input (text + images)

## Setup
```bash
export GEMINI_API_KEY="your-api-key"
# or: GOOGLE_API_KEY, GOOGLE_GENERATIVE_AI_API_KEY
```

## REST API
```bash
# Text prompt
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"Explain quantum computing in 3 sentences"}]}]}'

# Extract response text
curl -s ... | jq -r '.candidates[0].content.parts[0].text'
```

## Python SDK
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_KEY")
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("Your prompt here")
print(response.text)
```

## Models
- gemini-2.0-flash: fast, balanced
- gemini-2.0-flash-thinking: reasoning
- gemini-1.5-pro: long context (1M tokens)
- gemini-1.5-flash: fast and efficient

## Notes
- Free tier available at https://aistudio.google.com
- Supports images, audio, video, documents as input
- System instructions via system_instruction field
