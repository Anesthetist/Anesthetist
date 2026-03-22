<!-- v1.0 — initial creation 2026-03-20 -->
# Compliance Bot (Gertrude) — Run Protocol

## Pre-Run Checklist

1. Read `_bots/compliance-gertrude/soul.md` — internalize the red lines, approved alternatives, and competitor patterns
2. Read the content to be reviewed
3. Identify the content type (app store, website, proposal, social media, investor deck, CE course)
4. Note the target audience (consumers, clinicians, investors, enterprise buyers)

## Execution Steps

### Step 1: Full Scan

Read the entire document. Flag every instance of:
- [ ] Medical device language (diagnose, treat, cure, prevent, mitigate)
- [ ] Protected terms (biofeedback therapy, therapeutic, medical-grade, prescribe)
- [ ] Specific outcome claims attributed to the PRODUCT
- [ ] Missing disclaimers
- [ ] Scope-of-practice issues (biofeedback without BCIA certification, clinical claims without licensure)

### Step 2: Classify and Prioritize

| Risk Level | Definition | Examples |
|---|---|---|
| **HIGH** | Would trigger FDA warning letter or FTC enforcement | "Treats anxiety," "clinically proven," "biofeedback therapy" |
| **MEDIUM** | Borderline — could be interpreted as medical claim by a regulator | "Improves vagal tone," specific outcome percentages, "intervention" |
| **LOW** | Style/tone issues — technically compliant but could be softer | "Clinical coaching" when "performance coaching" works, missing "individual results vary" |

### Step 3: Generate Fixes

For each flagged item, provide:
1. The exact problematic text
2. Why it's a problem (specific regulation)
3. Risk level
4. Exact replacement text
5. Which competitor uses similar approved language (if applicable)

### Step 4: Check Disclaimers

Verify the content includes (as appropriate for content type):

**App Store / Website (required):**
- "Pausality is a wellness application, not a medical device"
- "Not intended to diagnose, treat, cure, or prevent any disease"
- "For wellness and informational purposes only"
- "Consult your healthcare provider before beginning any wellness program"
- "Individual results may vary"

**Proposals / Enterprise Materials:**
- All of the above, plus:
- "This program is wellness coaching, not medical treatment"
- Clear framing of Randy's CRNA background as QUALIFICATIONS (not as the nature of the service)

**Social Media / Marketing:**
- At minimum: "For wellness purposes. Not medical advice."
- No specific outcome claims without "based on published research" attribution

**Investor Decks:**
- Investor materials have more latitude (not consumer-facing)
- Still avoid "FDA-cleared" or "clinically proven" unless literally true
- Can describe the regulatory strategy and pathway

### Step 5: Verify Randy's Role Framing

Randy IS a CRNA. That's a fact about his qualifications. But the SERVICE he provides through Pausality must be framed as:
- ✅ "Wellness coaching informed by 28 years of clinical expertise"
- ✅ "Performance coaching from a CRNA background"
- ✅ "Breathing and body-awareness training"
- ❌ "Clinical treatment" or "clinical intervention"
- ❌ "Biofeedback therapy" (requires BCIA certification)
- ❌ "Medical consultation"

### Step 6: Output Report

Produce a compliance report with:
1. Summary: PASS / PASS WITH CHANGES / FAIL
2. Total flags by risk level
3. Each flagged item with fix
4. Corrected disclaimer text (if missing or incomplete)
5. Competitor language models used

### Step 7: Post-Run

- If content was corrected, verify the corrected version passes a re-scan
- Log the review in `outputs/compliance-log.md`
- If a new pattern is discovered (new FDA guidance, new competitor language), update `soul.md`

## Content-Specific Rules

### App Store Description
- Highest scrutiny. Apple and Google review these.
- No disease claims. No "biofeedback." No specific outcome numbers.
- Model: Calm and Headspace App Store descriptions.

### Proposals (Like Mossimo)
- Medium scrutiny. Not public, but could be shared.
- Can reference research with proper attribution.
- Cannot promise specific outcomes.
- "Expected trends" not "guaranteed results."

### LinkedIn / Social Media
- High scrutiny. Public, searchable, screenshot-able.
- Research attribution is fine ("studies show...").
- Product claims must be wellness-framed.

### CE Course Materials
- Special rules: CE courses CAN teach clinical science.
- The course TEACHES the research. The APP is a wellness tool.
- Clear separation between educational content and product claims.

### Investor Materials
- Lowest scrutiny for regulatory (not consumer-facing).
- But highest scrutiny for accuracy — investors will diligence claims.
- Can describe regulatory strategy, market positioning, clinical pathway.
- Avoid "FDA-cleared" unless literally true.
