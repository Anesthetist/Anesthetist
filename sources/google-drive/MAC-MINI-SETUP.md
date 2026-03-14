---
id: "urn:srl:source:gdrive-mac-mini-setup"
type: source
title: "MAC MINI SETUP"
status: draft
creator: "Randy Graybeal"
created: 2026-01-30
imported: 2026-03-14
dc:source: "google-drive:MAC-MINI-SETUP.md"
---

# Mac Mini Clawdbot Setup Guide

**Machine:** Mac Mini M4 (16GB / 512GB)
**Purpose:** Dedicated, secure Clawdbot instance
**Date:** 2026-01-30

---

## Phase 1: macOS Initial Setup

### 1.1 First Boot
- Create a **dedicated admin account** (not your personal one)
  - Suggested: `clawdadmin` or `somnistics-admin`
  - Strong password (20+ chars, store in 1Password/Bitwarden)
- Skip Apple ID sign-in (or use a dedicated Apple ID for this machine)
- Enable FileVault encryption when prompted

### 1.2 System Hardening
```bash
# Enable firewall
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setglobalstate on

# Enable stealth mode (don't respond to pings)
sudo /usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on

# Disable remote login until needed
sudo systemsetup -setremotelogin off

# Require password immediately after sleep
sudo pmset -a destroyfvsleepkey 1
```

### 1.3 Create Dedicated Bot User
```bash
# Create a non-admin user for running Clawdbot
sudo dscl . -create /Users/clawdbot
sudo dscl . -create /Users/clawdbot UserShell /bin/zsh
sudo dscl . -create /Users/clawdbot RealName "Clawdbot Service"
sudo dscl . -create /Users/clawdbot UniqueID 502
sudo dscl . -create /Users/clawdbot PrimaryGroupID 20
sudo dscl . -create /Users/clawdbot NFSHomeDirectory /Users/clawdbot
sudo mkdir /Users/clawdbot
sudo chown clawdbot:staff /Users/clawdbot
```

---

## Phase 2: Development Environment

### 2.1 Install Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add to path (Apple Silicon)
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### 2.2 Install Node.js (via nvm)
```bash
brew install nvm
mkdir ~/.nvm

# Add to shell config
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.zshrc
echo '[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"' >> ~/.zshrc
source ~/.zshrc

# Install Node 22 LTS
nvm install 22
nvm use 22
nvm alias default 22
```

### 2.3 Install Git & Essential Tools
```bash
brew install git gh jq curl wget
```

---

## Phase 3: Clawdbot Installation

### 3.1 Install Clawdbot
```bash
npm install -g clawdbot
```

### 3.2 Initialize Workspace
```bash
mkdir -p ~/clawd
cd ~/clawd
clawdbot init
```

### 3.3 Configure API Keys
```bash
# Create secure config
clawdbot config

# You'll need:
# - Anthropic API key
# - Telegram bot token (create new bot via @BotFather)
```

---

## Phase 4: Security Best Practices

### 4.1 Secrets Management
```bash
# Option A: Use macOS Keychain
security add-generic-password -a "clawdbot" -s "anthropic-api-key" -w "YOUR_KEY"

# Option B: Use environment file with restricted permissions
touch ~/.clawdbot/.env
chmod 600 ~/.clawdbot/.env
# Add keys to .env file
```

### 4.2 Network Security
```bash
# If exposing to internet, use Cloudflare Tunnel (zero trust)
brew install cloudflared
cloudflared tunnel login
cloudflared tunnel create clawdbot-mac
```

### 4.3 Automatic Updates
```bash
# Create update script
cat > ~/clawd/update.sh << 'EOF'
#!/bin/bash
npm update -g clawdbot
cd ~/clawd && git pull
EOF
chmod +x ~/clawd/update.sh
```

### 4.4 Backup Strategy
```bash
# Daily backup to iCloud or external
# Add to crontab:
# 0 3 * * * tar -czf ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd-backup-$(date +\%Y\%m\%d).tar.gz ~/clawd
```

---

## Phase 5: New Bot Identity

### 5.1 Create Unique Persona
The new instance should have its own:
- `SOUL.md` — Different name, personality, purpose
- `AGENTS.md` — Specific operating procedures
- `USER.md` — Who it serves (same or different?)

**Suggested personas:**
- **Marketing Bot** — Dedicated to GTM execution
- **Research Bot** — Competitive intel & analysis
- **Dev Bot** — Code, automation, infrastructure

### 5.2 Separate Telegram Bot
1. Message @BotFather on Telegram
2. `/newbot`
3. Name it (e.g., "Pausality Marketing Bot")
4. Get the token
5. Configure in new Clawdbot instance

---

## Phase 6: Run as Service

### 6.1 Create LaunchAgent (auto-start)
```bash
cat > ~/Library/LaunchAgents/com.somnistics.clawdbot.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.somnistics.clawdbot</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/node</string>
        <string>/opt/homebrew/bin/clawdbot</string>
        <string>gateway</string>
        <string>start</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/clawdbot/clawd</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/clawdbot/clawd/logs/stdout.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/clawdbot/clawd/logs/stderr.log</string>
</dict>
</plist>
EOF

launchctl load ~/Library/LaunchAgents/com.somnistics.clawdbot.plist
```

---

## Quick Start Checklist

- [ ] Unbox and first boot
- [ ] Create admin account (not personal)
- [ ] Enable FileVault
- [ ] Enable Firewall
- [ ] Install Homebrew
- [ ] Install Node.js via nvm
- [ ] Install Clawdbot
- [ ] Create new Telegram bot
- [ ] Configure API keys securely
- [ ] Create SOUL.md for new persona
- [ ] Test manually
- [ ] Set up LaunchAgent for auto-start
- [ ] Configure backups

---

## Questions to Decide

1. **What's this bot's purpose?** (Marketing? Research? General assistant?)
2. **Same Telegram channel or separate?**
3. **Shared workspace with EC2 or independent?**
4. **What should its name/personality be?**

---

*Guide created by Pax 🦾*
