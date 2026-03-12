# Azure DevOps MCP Setup

This repo includes VS Code MCP config at `.vscode/mcp.json`.

## 1. Prerequisites

- VS Code with MCP support enabled in your environment
- Node.js + `npx` available
- Azure DevOps Personal Access Token (PAT)
- WSL2 (WSL1 can cause Node runtime issues for MCP tooling)

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

## 6. WSL1-safe setup for VS Code Copilot + ADO MCP

Use this if your VM must stay on WSL1.

1. Install and verify Windows Node.js (not Ubuntu WSL Node):

```powershell
node -v
npm -v
npx -v
where npx
```

2. Sign in to VS Code Copilot:

- Install `GitHub Copilot` and `GitHub Copilot Chat` extensions
- Sign in with your org-approved account/license

3. Set ADO token in the Windows session used by VS Code:

```powershell
setx ADO_MCP_AUTH_TOKEN "<your-ado-pat>"
```

Close and reopen VS Code after `setx`.

4. Use Windows Node command in `.vscode/mcp.json`:

```json
"command": "C:\\Program Files\\nodejs\\npx.cmd"
```

5. Open repo in VS Code (Windows context) and start MCP.  
You should be able to use:

- Copilot in editor/chat
- ADO MCP for repos, work/boards, and core project data

## 7. Troubleshooting

- `npx: command not found`: install Node.js in your environment
- Auth failures: confirm `ADO_MCP_AUTH_TOKEN` is exported in the same terminal/session VS Code uses
- Permission errors: verify PAT scopes and org access
- WSL version check and migration (recommended if Node exec is unstable):
  - Check current version from Ubuntu:
    ```bash
    wsl.exe -l -v
    uname -r
    ```
  - If distro version is `1`, switch in Windows PowerShell (Admin):
    ```powershell
    wsl --set-version Ubuntu 2
    wsl --set-default-version 2
    wsl -l -v
    ```
  - If conversion fails, enable required features then reboot:
    ```powershell
    dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    wsl --update
    ```
  - Re-open Ubuntu and verify runtime again:
    ```bash
    node -v
    npm -v
    npx -v
    ```
  - If you see `WSL2 is not supported on your current machine configuration` in a VM, run in Windows PowerShell (Admin):
    ```powershell
    systeminfo | Select-String "Hyper-V Requirements"
    Get-ComputerInfo -Property "HyperV*"

    dism /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    dism /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /all /norestart
    bcdedit /set hypervisorlaunchtype auto
    wsl --update
    shutdown /r /t 0
    ```
  - After reboot:
    ```powershell
    wsl --set-default-version 2
    wsl -l -v
    ```
  - Verify WSL2-related Windows features are enabled:
    ```powershell
    Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux,VirtualMachinePlatform,Microsoft-Hyper-V-All
    ```
  - If it still fails, this is usually an Azure VM configuration blocker. Confirm:
    - VM size supports nested virtualization
    - VM is Generation 2
    - Nested virtualization is enabled by platform/policy
    - Organization policy allows Hyper-V in guest VM
  - If Azure policy/size blocks WSL2, use one:
    - Run MCP on Windows native Node (not WSL)
    - Use a Linux VM/devcontainer for MCP
    - Keep WSL1 only for non-Node-critical tasks
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
  - If `ldd` shows no missing libraries but `node -v` still fails, run:
    ```bash
    type -a node
    readlink -f /usr/bin/node
    /usr/bin/node -v
    "$(readlink -f /usr/bin/node)" -v
    env -i PATH=/usr/bin:/bin /usr/bin/node -v
    ```
  - If direct execution still fails, do a clean reinstall including runtime libs:
    ```bash
    sudo apt purge -y nodejs npm
    sudo apt autoremove -y
    sudo apt install --reinstall -y libc6 libstdc++6
    sudo apt update
    sudo apt install -y nodejs npm
    hash -r
    node -v
    ```
  - If `which node` is `/usr/bin/node` but `node -v` still says `cannot execute binary file`, run:
    ```bash
    /usr/bin/nodejs -v
    sudo apt update
    sudo apt install --reinstall -y nodejs npm
    sudo ln -sf /usr/bin/nodejs /usr/bin/node
    hash -r
    /usr/bin/node -v
    node -v
    npm -v
    npx -v
    ```
  - If `/usr/bin/nodejs -v` also fails, use `nvm` fallback:
    ```bash
    curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
    source ~/.bashrc
    nvm install --lts
    nvm use --lts
    node -v
    npm -v
    npx -v
    ```

## 8. Node 24 + MCP stable run path (recommended for your setup)

If Node 24 installed via `nvm` can run with direct loader checks but `node -v` sometimes fails, pin MCP to a stable Node 24 runtime path.

Run this in Ubuntu WSL:

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

nvm install 24
nvm use 24
nvm alias default 24
hash -r

which node
which npx
node -v
npm -v
npx -v
```

Expected: all version commands succeed and paths point to `$HOME/.nvm/...`, not `/mnt/c/...`.

Get exact `npx` path:

```bash
command -v npx
```

Use that absolute path in `.vscode/mcp.json`:

```json
{
  "servers": {
    "ado": {
      "type": "stdio",
      "command": "/home/<your-user>/.nvm/versions/node/v24.x.x/bin/npx",
      "args": [
        "-y",
        "@azure-devops/mcp",
        "${input:ado_org}",
        "--authentication",
        "envvar",
        "-d",
        "core",
        "-d",
        "work",
        "-d",
        "work-items",
        "-d",
        "repositories"
      ]
    }
  }
}
```

After updating config:

```bash
code .
```

Then restart VS Code or reload the window so MCP picks up the new command path.

## 9. If Node 24 only works via interpreter, force source build

If `node -v` fails but running through the loader/interpreter works, your local Node 24 install may be a bad prebuilt binary for this environment.

Build Node 24 from source with `nvm`:

```bash
sudo apt update
sudo apt install -y build-essential python3 make g++

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

nvm uninstall 24
rm -rf "$NVM_DIR/.cache"
nvm install 24 -s
nvm use 24
nvm alias default 24
hash -r

node -v
npm -v
npx -v
```

Validate binary details:

```bash
BIN="$(which node)"
file -L "$BIN"
uname -m
readelf -h "$BIN" | rg 'Class|Machine'
readelf -l "$BIN" | rg 'interpreter|Requesting'
```

If versions now print normally, keep MCP using the absolute `npx` path from:

```bash
command -v npx
```
