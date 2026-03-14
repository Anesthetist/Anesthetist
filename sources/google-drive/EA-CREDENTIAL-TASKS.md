---
id: "urn:srl:source:gdrive-ea-credential-tasks"
type: source
title: "EA CREDENTIAL TASKS"
status: draft
creator: "Randy Graybeal"
created: 2026-01-30
imported: 2026-03-14
dc:source: "google-drive:EA-CREDENTIAL-TASKS.md"
---

# Executive Assistant Task List — Credential & Setup Blockers
**For:** Randy Graybeal  
**From:** Pax (AI Chief of Staff)  
**Date:** 2026-01-31  
**Priority:** High — These are blocking automation

---

## Summary

Pax (Randy's AI assistant) needs the following credentials and approvals to fully automate marketing, content, and social media operations. Each task takes 5-15 minutes. Total time: ~45 minutes.

---

## 🔴 CRITICAL (Blocking Multiple Workflows)

### 1. Twitter/X API Credentials (@Badazzafall)
**Time:** 10 minutes  
**Why:** Enables automated posting, Moltbook verification, social media scheduling

**Steps:**
1. Go to https://developer.twitter.com
2. Sign in as @Badazzafall
3. Click "Create Project" → name it "Pausality"
4. Click "Create App" → name it "Pausality Publisher"
5. Go to "Keys and Tokens" tab
6. Generate and copy ALL 4 values:
   - API Key
   - API Key Secret  
   - Access Token
   - Access Token Secret
7. Set "App Permissions" to **Read and Write** (Settings → User authentication settings)
8. Send credentials to Pax via Telegram or save to `/home/ubuntu/clawd/.credentials/twitter.json`

**Format for credentials file:**
```json
{
  "api_key": "xxxxx",
  "api_key_secret": "xxxxx",
  "access_token": "xxxxx",
  "access_token_secret": "xxxxx"
}
```

---

### 2. Gmail App Password (for email automation)
**Time:** 5 minutes  
**Why:** Enables Pax to send emails, check inbox, automate notifications

**Steps:**
1. Go to https://myaccount.google.com/apppasswords
2. Sign in to Randy's Google account
3. Select app: "Mail"
4. Select device: "Other" → name it "Clawdbot"
5. Click "Generate"
6. Copy the 16-character password (looks like: xxxx xxxx xxxx xxxx)
7. Save to `/home/ubuntu/clawd/.credentials/gmail-app-password.txt`

**Note:** Requires 2FA to be enabled on the Google account.

---

## 🟡 HIGH PRIORITY (Blocking Content Creation)

### 3. HeyGen Credentials (AI video generation)
**Time:** 5 minutes  
**Why:** Enables automated video content for marketing

**Steps:**
1. Go to https://www.heygen.com
2. Sign in (or create account if needed)
3. Go to Settings → API
4. Copy the API key
5. Save to `/home/ubuntu/clawd/.credentials/heygen.json`

**Format:**
```json
{
  "api_key": "xxxxx"
}
```

---

### 4. Gamma Credentials (AI presentation generation)
**Time:** 5 minutes  
**Why:** Enables automated pitch decks, investor materials

**Steps:**
1. Go to https://gamma.app
2. Sign in (or create account if needed)
3. Go to Settings → Integrations or API
4. Copy API key (if available) OR share login credentials securely
5. Save to `/home/ubuntu/clawd/.credentials/gamma.json`

**Note:** Gamma may not have a public API. If not, save login credentials for browser automation.

---

### 5. HubSpot API Key (if not already connected)
**Time:** 5 minutes  
**Why:** Enables waitlist management, email automation, CRM integration

**Steps:**
1. Go to HubSpot → Settings → Integrations → Private Apps
2. Create new private app named "Clawdbot"
3. Give it scopes: contacts, forms, marketing emails
4. Copy the access token
5. Save to `/home/ubuntu/clawd/.credentials/hubspot.json`

**Format:**
```json
{
  "access_token": "xxxxx"
}
```

---

## 🟢 MEDIUM PRIORITY (Nice to Have)

### 6. Buffer/Hypefury Account (social scheduling alternative)
**Time:** 10 minutes  
**Why:** Backup for social posting if direct API is too complex

**Steps:**
1. Create account at https://buffer.com OR https://hypefury.com
2. Connect @Badazzafall Twitter account
3. Share login credentials with Pax

---

### 7. Verify Moltbook Claim (pausality_ai)
**Time:** 2 minutes  
**Why:** Verifies our AI agent on Moltbook platform

**Steps:**
1. Go to https://moltbook.com/claim/moltbook_claim_eD_EuxpCuECCYW8v55Wzid8HwHy5pkdA
2. Connect with Twitter account @PausalityBot (need to create this first)
3. Verification code: `claw-68AH`

**Note:** Requires creating @PausalityBot Twitter account first.

---

## 📋 APPROVALS PENDING

### Reddit Post Approval
**Location:** `/home/ubuntu/clawd/reports/reddit-drafts/2026-01-31.md`  
**Action:** Randy to review and approve, then Pax posts

---

## ✅ ALREADY WORKING

| Service | Status |
|---------|--------|
| Google Drive | ✅ Connected via OAuth |
| Moltbook (midazofol_ai) | ✅ Claimed and posting |
| Anthropic API | ✅ Working |
| Brave Search | ✅ Working |

---

## Credential Storage Location

All credentials should be saved to: `/home/ubuntu/clawd/.credentials/`

```
.credentials/
├── twitter.json
├── gmail-app-password.txt
├── heygen.json
├── gamma.json
├── hubspot.json
└── buffer.json (optional)
```

---

## Questions for Randy

1. **Do you have HeyGen/Gamma accounts already?** If not, should EA create them?
2. **Which Twitter account for Pausality bot?** Create @PausalityBot or use existing?
3. **Buffer vs Hypefury vs direct API?** Preference for social scheduling?

---

*Once these are complete, Pax can automate: Twitter posting, email campaigns, video generation, presentation creation, waitlist management, and full social media scheduling.*
