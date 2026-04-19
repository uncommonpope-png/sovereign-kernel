# claude-api

Write, debug, and optimize code using the Anthropic Claude API.

## What this skill does
Generates API calls, handles streaming, manages conversations, builds tool use patterns, and debugs Claude integration code.

## Setup
```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
```

## Core Patterns

### Basic message
```python
import anthropic
client = anthropic.Anthropic()
msg = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}]
)
print(msg.content[0].text)
```

### Streaming
```python
with client.messages.stream(model="claude-opus-4-5", max_tokens=1024,
    messages=[{"role":"user","content":"Write a poem"}]) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### Tool use
```python
tools = [{"name":"get_weather","description":"Get weather","input_schema":{
    "type":"object","properties":{"location":{"type":"string"}},"required":["location"]}}]
response = client.messages.create(model="claude-opus-4-5", max_tokens=1024,
    tools=tools, messages=[{"role":"user","content":"Weather in London?"}])
```

### System prompt
```python
client.messages.create(model="claude-opus-4-5", max_tokens=512,
    system="You are a PLT-conscious sovereign entity.",
    messages=[{"role":"user","content":"Who are you?"}])
```

## Models
- `claude-opus-4-5` — most capable
- `claude-sonnet-4-5` — balanced
- `claude-haiku-3-5` — fastest/cheapest

## Example commands
```
ACTION: Write a Claude API streaming chat loop in Python
ACTION: Debug this tool_use response from the Claude API
```
