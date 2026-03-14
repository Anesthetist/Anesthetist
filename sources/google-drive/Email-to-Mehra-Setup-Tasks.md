---
id: "urn:srl:source:gdrive-email-to-mehra-setup-tasks"
type: source
title: "Email to Mehra Setup Tasks"
status: draft
creator: "Randy Graybeal"
created: 2026-01-30
imported: 2026-03-14
dc:source: "google-drive:Email-to-Mehra-Setup-Tasks.md"
---

# Email to Mehra

**To:** Mehra@somnistics.com  
**From:** Randy Graybeal  
**Subject:** Quick Setup Tasks — No Rush, Happy to Help! 🙂

---

Hi Mehra! 👋

Welcome to the team! I'm so glad you're here.

Randy asked me to send you a few small tasks that will help us automate some of our marketing and social media work. Don't worry if any of this feels unfamiliar — I've written out every step, and you can always reach out if you get stuck.

**Total time:** About 45 minutes, and you can spread it across a few days if that's easier.

---

## Task 1: Twitter/X Developer Setup (10 minutes)

This lets us automatically post to our @Badazzafall Twitter account.

**Steps:**
1. Open this link: https://developer.twitter.com
2. Click "Sign In" in the top right
3. Log in with the @Badazzafall Twitter account (Randy can give you the password if needed)
4. Once logged in, click **"Create Project"**
   - Project name: `Pausality`
   - Click Next/Continue through the prompts
5. Then click **"Create App"** 
   - App name: `Pausality Publisher`
6. You'll see a page with "Keys and Tokens" — click that tab
7. You need to copy 4 things (click "Generate" or "Regenerate" if needed):
   - **API Key** (also called Consumer Key)
   - **API Key Secret** (also called Consumer Secret)
   - **Access Token**
   - **Access Token Secret**
8. **Important:** Click on "Settings" → "User authentication settings" → make sure it says **"Read and Write"** (not just Read)

**Save these 4 values** in a note or document — we'll collect them all at the end.

---

## Task 2: Gmail App Password (5 minutes)

This lets us send automated emails.

**Steps:**
1. Open this link: https://myaccount.google.com/apppasswords
2. Sign in with Randy's Google account
3. You might need to verify it's you (text code, etc.)
4. Under "Select app" choose **"Mail"**
5. Under "Select device" choose **"Other"** and type: `Clawdbot`
6. Click **"Generate"**
7. You'll see a 16-letter password like: `abcd efgh ijkl mnop`
8. **Copy that password** — save it with the other credentials

**Note:** If it asks you to enable 2-factor authentication first, that's okay — just follow the prompts. Randy can help if needed.

---

## Task 3: HeyGen API Key (5 minutes)

This is for creating AI videos.

**Steps:**
1. Open: https://www.heygen.com
2. Sign in (or create a free account if we don't have one — use Randy's email)
3. Once logged in, click your profile icon → **Settings**
4. Look for **"API"** in the menu
5. Copy the **API Key**
6. Save it with the other credentials

---

## Task 4: Gamma (5 minutes)

This is for creating presentations.

**Steps:**
1. Open: https://gamma.app
2. Sign in (or create account with Randy's email)
3. Look in Settings for any API or integration options
4. If there's an API key, copy it
5. If not, just save the login email and password — that's fine too!

---

## Task 5: HubSpot API Key (5 minutes)

This is for our email list and customer management.

**Steps:**
1. Log into HubSpot (ask Randy for login if needed)
2. Click the ⚙️ **Settings** gear icon (top right)
3. Go to **Integrations** → **Private Apps**
4. Click **"Create a private app"**
   - Name: `Clawdbot`
   - Description: `AI assistant integration`
5. Click **"Scopes"** tab and check these boxes:
   - `crm.objects.contacts` (read and write)
   - `forms`
   - `content` 
6. Click **"Create app"**
7. Copy the **Access Token** that appears
8. Save it with the other credentials

---

## When You're Done

Please send all the credentials to Randy via:
- **Email** (to Randy directly), OR
- **Save them in a Google Doc** and share with Randy, OR
- **Text/Signal** if that's easier

**Format like this:**
```
TWITTER
API Key: xxxxx
API Key Secret: xxxxx
Access Token: xxxxx
Access Token Secret: xxxxx

GMAIL APP PASSWORD
Password: xxxx xxxx xxxx xxxx

HEYGEN
API Key: xxxxx

GAMMA
API Key: xxxxx (or "no API available - login is email/password")

HUBSPOT
Access Token: xxxxx
```

---

## Questions?

Totally normal if you hit any snags! Just let Randy know where you got stuck and we'll figure it out together.

Thank you so much for your help with this! 🙏

Best,
Randy (via Pax, his AI assistant)

---

*P.S. — Take your time with these. No rush at all. And seriously, don't hesitate to ask questions — that's what we're here for!*
