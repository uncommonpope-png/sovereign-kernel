# MCPorter Skill

Manage and configure MCP (Model Context Protocol) servers — install, list, and connect tools.

## Use When
- Installing MCP servers for AI tool use
- Configuring MCP server connections
- Listing available MCP tools and servers

## mcporter CLI (if installed)
```bash
mcporter list                        # list installed MCP servers
mcporter install <server-name>       # install an MCP server
mcporter remove <server-name>        # remove MCP server
mcporter start <server-name>         # start MCP server
mcporter stop <server-name>          # stop MCP server
mcporter config <server-name>        # show server config
```

## Manual MCP Configuration
Claude/Cursor MCP config (~/.cursor/mcp.json or ~/Library/Application Support/Claude/claude_desktop_config.json):
```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/dir"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"}
    }
  }
}
```

## Common MCP Servers
```bash
npx @modelcontextprotocol/server-filesystem /path
npx @modelcontextprotocol/server-github
npx @modelcontextprotocol/server-postgres postgresql://localhost/mydb
npx @modelcontextprotocol/server-slack
```

## Notes
- MCP servers extend AI assistants with tools and data access
- Restart Claude/Cursor after config changes
- Use npx for quick installs or npm install -g for permanent
