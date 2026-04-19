# mcp-builder

Scaffold and generate MCP (Model Context Protocol) server code from a description.

## What this skill does
Creates fully functional MCP servers that expose tools, resources, and prompts to Claude and other MCP-compatible agents.

## Setup
```bash
pip install mcp
# or
npm install @modelcontextprotocol/sdk
```

## Python MCP Server Template
```python
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import mcp.types as types

server = Server("my-mcp-server")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [Tool(name="do_thing", description="Does the thing",
        inputSchema={"type":"object","properties":{"input":{"type":"string"}},"required":["input"]})]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "do_thing":
        result = f"Did the thing with: {arguments['input']}"
        return [TextContent(type="text", text=result)]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream,
            InitializationOptions(server_name="my-mcp-server", server_version="0.1.0",
                capabilities=server.get_capabilities(notification_options=None, experimental_capabilities={})))

if __name__ == "__main__":
    import asyncio; asyncio.run(main())
```

## Register with Claude Desktop
```json
// claude_desktop_config.json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

## Example commands
```
ACTION: Scaffold an MCP server that exposes the kernel's skill invocation as a tool
ACTION: Generate an MCP server for PLT scoring with list_tools and call_tool
```
