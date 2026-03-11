# Azure DevOps MCP Setup

This repo includes VS Code MCP config at `.vscode/mcp.json`.

## 1. Prerequisites

- VS Code with MCP support enabled in your environment
- Node.js + `npx` available
- Azure DevOps Personal Access Token (PAT)

## 2. Verify Node.js and npx in Ubuntu (WSL)

Run in your Ubuntu terminal:

```bash
node -v
npm -v
npx -v
which node
which npx
```

Expected paths should be Linux paths (for example `/usr/bin/node`), not Windows `C:` paths.

Install location guidance:

- For VS Code + WSL workflows, install Node.js in the Ubuntu distro
- Do not rely on Windows `C:` Node.js for WSL MCP workflows

If missing, install in Ubuntu:

```bash
sudo apt update
sudo apt install -y nodejs npm
node -v && npm -v && npx -v
```

## 3. Set your PAT in the terminal session

Run in your terminal before starting MCP tools:

```bash
read -s ADO_MCP_AUTH_TOKEN
export ADO_MCP_AUTH_TOKEN
```

Optional: persist in shell profile (`~/.bashrc` or `~/.zshrc`) if your security policy allows it.

## 4. Open this repo in VS Code

```bash
code .
```

When MCP starts, it will prompt for your Azure DevOps org name (`ado_org`).

## 5. Recommended PAT scopes (least privilege)

Start with:

- Project and Team: Read
- Work Items: Read
- Code: Read

Only add write scopes if you actually need create/update operations.

## 6. Troubleshooting

- `npx: command not found`: install Node.js in your environment
- Auth failures: confirm `ADO_MCP_AUTH_TOKEN` is exported in the same terminal/session VS Code uses
- Permission errors: verify PAT scopes and org access
- `cannot exec binary file` when running `node -v`:
  - Check binary and architecture:
    ```bash
    which node
    file /usr/bin/node
    dpkg --print-architecture
    uname -m
    ```
  - If architecture does not match or binary is invalid, reinstall in Ubuntu WSL:
    ```bash
    sudo apt purge -y nodejs npm
    sudo apt autoremove -y
    sudo apt update
    sudo apt install -y nodejs npm
    hash -r
    node -v
    npx -v
    ```
  - If it still fails, run deeper diagnostics:
    ```bash
    type -a node
    hash -r
    ls -l /usr/bin/node
    readlink -f /usr/bin/node
    file "$(readlink -f /usr/bin/node)"
    ldd "$(readlink -f /usr/bin/node)"
    /usr/bin/node -v
    "$(readlink -f /usr/bin/node)" -v
    ```
  - Quick interpretation:
    - `file` not showing Linux ELF x86-64: wrong binary installed
    - `ldd` showing missing libraries: broken runtime dependencies
    - direct path works but `node -v` fails: shell alias/PATH/hash issue
