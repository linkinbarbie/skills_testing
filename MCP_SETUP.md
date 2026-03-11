# Azure DevOps MCP Setup

This repo includes VS Code MCP config at `.vscode/mcp.json`.

## 1. Prerequisites

- VS Code with MCP support enabled in your environment
- Node.js + `npx` available
- Azure DevOps Personal Access Token (PAT)

## 2. Set your PAT in the terminal session

Run in your terminal before starting MCP tools:

```bash
read -s ADO_MCP_AUTH_TOKEN
export ADO_MCP_AUTH_TOKEN
```

Optional: persist in shell profile (`~/.bashrc` or `~/.zshrc`) if your security policy allows it.

## 3. Open this repo in VS Code

```bash
code .
```

When MCP starts, it will prompt for your Azure DevOps org name (`ado_org`).

## 4. Recommended PAT scopes (least privilege)

Start with:

- Project and Team: Read
- Work Items: Read
- Code: Read

Only add write scopes if you actually need create/update operations.

## 5. Troubleshooting

- `npx: command not found`: install Node.js in your environment
- Auth failures: confirm `ADO_MCP_AUTH_TOKEN` is exported in the same terminal/session VS Code uses
- Permission errors: verify PAT scopes and org access
