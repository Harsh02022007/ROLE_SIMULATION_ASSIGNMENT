# Part B: Sourcing Strategy + 1000-Company Scale-Up Proposal
## DeepThought Business Analytics Assignment
### Submitted by: Harsh Bujade

---

# Question 1: How Else Would You Find Federer Companies Across India?

---

## Method 1: DSIR Recognized R&D Units List

**What it is:** The Department of Scientific and Industrial Research publishes a public list of Indian companies with approved in-house R&D units. ~3,000+ companies nationally.

**Why it works for this ICP specifically:**
- DSIR recognition requires an R&D application with facility documentation — so by definition you get manufacturers (not traders).
- Signals C3 (differentiation — they invested in R&D) and C4 (technical DM — someone built and runs an R&D function).
- Government-verified, so C1 and C3 evidence is pre-confirmed rather than self-reported.
- Free to access from dsir.gov.in. Downloadable as a structured list.

**Limitation:** Skews toward established companies. Newer companies (<5 years old) may not have applied yet even if they're excellent ICP fits.

---

## Method 2: Regulatory Approval Databases

**What it is:**
- USFDA Establishment Inspection Database (fda.gov) — filters to India, then by product type
- EU-GMP approved sites (EMA database)
- WHO Prequalification list
- CDSCO GMP approval database (India-specific)

**Why it works:**
- Regulatory approval is *the* strongest single signal for C3 (differentiated, not commodity). Commodity manufacturers don't spend Rs.1–5Cr to get USFDA approved.
- Directly evidences C1 (physical manufacturing facility — you must have one to get approved).
- The USFDA database gives facility address — filtering to target cities is trivial.
- Cross-referencing WHO-GMP + USFDA gives a Venn diagram of companies with maximum regulatory moat.

**Limitation:** Heavy pharma/chemicals bias. Defence, agri, industrial segments are not captured. Misses companies that have differentiated products but haven't pursued international regulatory approvals yet.

---

## Method 3: Trade Expo Exhibitor Directories

**Target expos:**
| Expo | Segment | Frequency |
|------|---------|-----------|
| CPHI India | Pharma intermediates, APIs | Annual |
| BioAsia Hyderabad | Biotech, vaccines, life sciences | Annual |
| Aero India | Defence, aerospace | Biennial |
| IMTEX Bangalore | Machine tools, precision engineering | Biennial |
| PackEx / IndiaPlas | Specialty materials, polymer | Annual |
| Agri Intex Coimbatore | Agri-inputs, seeds, biopesticides | Annual |
| Analytica India | Diagnostics, lab instruments, sensors | Annual |

**Why it works:**
- Exhibitors self-select for growth intent — paying Rs.2–10L for an exhibition booth is a strong C6 (growth signal).
- Expo categories map directly to ICP segments.
- Exhibitor directories typically include company name, website, and product category — enough for initial filtering.
- For past expos, archived exhibitor lists are often available via Wayback Machine.

**Limitation:** Biased toward companies with marketing budgets. Bootstrapped technical founders sometimes skip expos even if their products are excellent.

---

## Method 4: Industry Association Membership Directories

**Target associations:**
- **IDMA** (Indian Drug Manufacturers' Association) — pharma intermediates
- **BDMA** (Bulk Drug Manufacturers' Association of India) — APIs, Hyderabad-heavy
- **ACMA** (Automotive Component Manufacturers Association) — precision engineering
- **ELCINA** (Electronic Industries Association of India) — defence electronics, sensors
- **Seed Association of India** — hybrid seeds, agri-inputs
- **Indian Chemical Council** — specialty and performance chemicals
- **FICCI Health Services** — diagnostics, medical devices

**Why it works:**
- Active association membership signals an operating company in the segment.
- Directories often include company size, product range, and direct contact.
- BDMA is particularly valuable — it's Hyderabad-centric and focuses specifically on bulk drug and specialty API manufacturers.

**Limitation:** Overlaps heavily with DSIR and expo lists. Directories vary in quality — some are updated annually, others haven't changed in 5 years.

---

## Method 5: MCA (Ministry of Corporate Affairs) by NIC Code

**What it is:** Every Indian registered company has an NIC (National Industrial Classification) code. MCA filings are public. Can filter by NIC code + state + paid-up capital range.

**Why it works:**
- NIC code filtering allows targeting specific manufacturing sub-segments at national scale.
- Paid-up capital gives a rough size proxy for revenue band filtering.
- Director details (DIN — Director Identification Number) give decision-maker names for C4 evaluation.
- Ownership percentage data available for listed companies — helps identify PE-controlled vs. promoter-driven.

**Key NIC codes for target segments:**
```
21001 — Manufacture of basic pharmaceutical products
21002 — Pharma intermediates, APIs
26600 — Medical devices and instruments
26209 — Electronic components (defence, sensors)
20119 — Specialty chemicals
01130 — Hybrid seeds and planting material
32502 — Surgical instruments, implants
```

**Tool to use:** Tofler.in, Zauba Corp, or direct MCA portal for structured query.

**Limitation:** Very noisy — NIC codes are self-reported and frequently wrong. A trading company can claim a manufacturing NIC code. Requires heavy manual filtering downstream. No website URL in MCA data — needs Google search enrichment.

---

## Method 6: LinkedIn Sales Navigator — Inverted Founder Search

**What it is:** Instead of finding companies then checking their founder, find technical founders and trace back to their companies.

**Search parameters:**
- Seniority: Owner, CXO, Founder, Managing Director
- Industry: Manufacturing sub-sectors (life sciences, chemicals, defence, industrial machinery)
- Keywords: "PhD" OR "IIT" OR "DRDO" OR "ISRO" OR "BITS" OR "NIT"
- Geography: Target city

**Why it works:**
- Directly surfaces C4 (technical decision-maker) as the entry point
- Strong for finding privately held companies not listed on BSE/NSE
- ISRO and DRDO alumni are very active on LinkedIn — this captures the ex-government-scientist-turned-founder profile that is DT's ideal C4

**Limitation:** Self-reported data — headcount and industry tags are frequently wrong for Indian MSMEs. Some promoters have minimal LinkedIn presence.

---

## Method 7: State Industrial Development Corporation Directories

**Target SDCs:**
- **TSIIC** (Telangana State Industrial Infrastructure Corporation) — Hyderabad
- **MIDC** (Maharashtra Industrial Development Corporation) — Pune, Nashik, Aurangabad
- **GIDC** (Gujarat Industrial Development Corporation) — Ahmedabad, Vadodara, Surat
- **TIDCO** (Tamil Nadu Industrial Development Corporation) — Chennai, Coimbatore

**Why it works:**
- SDCs maintain lists of companies operating in their industrial estates.
- Industrial estates (pharma parks, biotech zones, electronics parks) are already segment-filtered.
- Hyderabad's Genome Valley is a TSIIC cluster — its tenant list is a near-complete inventory of Hyderabad biotech manufacturers.
- Some SDCs publish online directories; others require RTI (Right to Information) applications.

**Limitation:** Data quality varies widely by state. Some directories are years out of date. Online access is inconsistent.

---

---

# Question 2: The 1000-Company Proposal

## Building a Verified List of 1000 Federer Companies in 30 Days

---

## Goal

1000 companies that are genuinely ICP-qualified — Indian specialty manufacturers, Rs.50Cr–Rs.500Cr, promoter-driven, differentiated product, technical decision-maker, active growth signals — with evidence-backed Federer scores on all 6 criteria.

Not 5,000 names from a database dump. 1,000 verified companies.

---

## The Core Constraint: Yield

From Part A, ~30% of investigated companies will pass. To get 1,000 passes, I need to investigate 3,300–3,500 companies. That's the primary planning constraint.

---

## The Funnel

```
RAW UNIVERSE: 5,000–6,000 company names
         ↓  Hard pre-filters (auto-disqualify on name/segment/size)
SCREENED POOL: 3,300–3,500 companies
         ↓  AI-assisted ICP scoring (website scrape + Claude)
FIRST-PASS: ~1,200–1,400 companies (score ≥ 40)
         ↓  Human QA on borderline + low-confidence flags
VERIFIED LIST: 1,000 companies (score ≥ 60, human-verified)
```

---

## Week 1: Build the Universe (Days 1–7)

**Goal:** 5,000–6,000 unique company names with website URL and rough segment tag.

**Day 1–2: Structured data sources (fastest, cleanest)**
- Download DSIR recognized R&D units list → ~800–1,000 companies after filtering to target segments
- Download BSE SME + NSE Emerge listed companies by sector → ~500 companies
- Pull USFDA India facility database + WHO-GMP list → ~400 companies
- These three alone give ~1,500–1,700 companies with high-quality pre-signals on C1 and C3

**Day 2–3: Expo scraping**
- Write Python (Playwright/BeautifulSoup) scrapers for 8 target expo exhibitor directories: CPHI, BioAsia, Aero India, IMTEX, Agri Intex, Analytica India, PackEx, ELCIMA (electrical/industrial)
- Expected: ~800–1,000 companies after deduplication across expos

**Day 3–4: MCA extraction**
- Use Tofler/Zauba to query by NIC code + state + paid-up capital range
- Target NIC codes: 21001, 21002, 26600, 26209, 20119, 01130, 32502 across 8 target cities
- Expected: ~1,500 companies, but ~40% will be dormant or non-manufacturing — filter to companies with website

**Day 4–5: Industry association directories**
- Extract BDMA, IDMA, ACMA, ELCINA, Seed Association member lists
- Expected: ~600–800 companies, heavily overlapping with DSIR/expo lists

**Day 5–6: LinkedIn Sales Navigator**
- Run founder/MD search in each target city with technical background keywords
- Extract ~500–700 profiles → ~400–500 unique companies
- Particularly valuable for finding private companies not in any public registry

**Day 6–7: Deduplication and enrichment**
- Fuzzy name matching (Python `fuzzywuzzy` library) to deduplicate across sources
- For ~30% of companies without a website URL: Google search automation (`{company name} {city} site:.in OR site:.com`)
- Target: **5,000–6,000 unique companies** with name + city + rough segment + website URL

**Week 1 Output:** Master universe spreadsheet, 5,000–6,000 rows, hosted on GitHub.

---

## Week 2: Hard Pre-Filters + Automated Scoring (Days 8–17)

**Day 8: Hard pre-filter pass (eliminates ~1,500–2,000 before AI scoring)**

Automated rules (no AI needed — string matching and size data):
```python
DISQUALIFY_IF:
  - No website found after 2 Google search attempts
  - Company name contains "Trading", "Imports", "Distributors", "Solutions Pvt", "Services Ltd"
  - Revenue > Rs.500Cr (from BSE/NSE data)
  - Known PE-owned (from a maintained PE-owned companies list)
  - Generic pharma NIC code 21001 alone (bulk APIs, branded generics)
```
After this pass: ~3,300–3,500 companies remain.

**Day 8–9: Build and calibrate the scoring pipeline**

Tech stack:
- **Playwright (Python)** — for JavaScript-rendered website scraping
- **Claude Haiku API** — first-pass ICP scoring (cheap, fast)
- **Claude Sonnet API** — borderline re-scoring (higher accuracy)

Calibration: Run on all 28 companies from Part A. Tune prompt until ≥ 23/28 match my hand-scored verdicts. If below, adjust prompt and re-run.

**The scoring prompt (system message to Claude Haiku):**
```
You are scoring Indian manufacturing companies against the DeepThought Federer ICP.
Score C1–C6 as Strong / Moderate / Weak based on the website content provided.
Rules:
- C1 (Manufacturer): Score Fail if the company provides services not physical products.
  CROs, testing labs, analytical services, logistics = Fail.
- C3 (Differentiated): ISO 9001 alone is NOT differentiation. Require: patents, 
  USFDA/WHO/EU-GMP approval, DSIR recognition, or "first/only in India" language.
- C4 (Technical DM): Require PhD, IIT/IISc/BITS/NIT degree, ex-ISRO/DRDO — 
  not just "engineering background". MBA only = Weak.
- C6 (Growth): Only count signals from 2023 onwards. Old news = 0 signals.
Return JSON only: {C1, C2, C3, C4, C5, C6, verdict, confidence, evidence_notes}
```

**Day 10–14: Scraping + Haiku scoring**
- Scrape 5 pages per company (homepage, /about, /products, /leadership, /news)
- Target: 30 seconds/company with politeness delays; 4 parallel workers
- 3,300 companies × 30s ÷ 4 workers = ~7 hours scraping time
- Send each scrape to Claude Haiku: ~3 seconds/company = ~3 hours
- Cost estimate: Haiku at ~$0.001/1K tokens × 8K tokens × 3,300 = ~$26

**Day 14–17: Sonnet re-scoring of borderlines**
- Borderline = score 40–65 = ~700 companies
- Re-score with Claude Sonnet for higher judgment accuracy
- Cost: ~$0.01/1K tokens × 12K tokens × 700 = ~$84

**Expected end of Week 2:** ~1,200–1,400 companies with Haiku-scored verdict ≥ 60.

---

## Week 3: Human QA (Days 18–24)

**Why QA is necessary — the main AI failure modes:**
1. **C3 inflation** — Haiku reads "ISO 9001" and scores differentiation as Moderate. ISO 9001 is a baseline, not a differentiator.
2. **C4 false positives** — Haiku interprets any "B.Tech" as technical. A B.Tech from a tier-3 college running a commodity business ≠ IIT PhD scientist.
3. **C6 false positives** — Haiku reads 2019 press releases and scores growth as Moderate. No activity since 2022 = C6 Weak.
4. **C1 false negatives** — Website uses "solutions" language but actually manufactures — Haiku takes the language literally.

**Day 18: Auto-QA flags (programmatic — no human)**
```python
FLAG_FOR_HUMAN_QA_IF:
  - C3 evidence mentions only ISO 9001 or ISO 14001 AND C3 = Strong
  - C6 evidence references any news older than January 2023 AND C6 = Strong
  - C1 evidence contains "services", "solutions", "consulting" language AND C1 = Strong
  - Total score = 60–65 (high borderline — these have highest false positive risk)
```
Expected flagged: ~400–500 companies.

**Day 18–24: Human QA (2–3 hours/day)**
- For each flagged company: open website, verify 2–3 key claims, adjust scores if needed
- Estimate: 3–4 minutes per company × 400 companies = ~25 hours total = ~4 hours/day for 6 days
- Spot-check 50 random "strong pass" companies (should be correct but verify ~10%)

**Expected end of Week 3:** ~1,100–1,200 verified companies at score ≥ 60.

---

## Week 4: Final Assembly + Personalization (Days 25–30)

**Day 25–26:** Drop companies that failed QA. Merge clean passes + QA-verified passes. Deduplicate final list. Verify count ≥ 1,000.

**Day 26–28:** Add personalization hooks to the top 200 by score (Priority tier). Format: one specific, recent, true detail per company that can be used in line 1 of an outreach email. This tier is ready for immediate BD outreach.

**Day 28–29:** Format final deliverable:
- **Master CSV** (1,000+ companies, all fields, all scores, all evidence)
- **Priority-200 list** (personalization hooks ready)
- **Source breakdown CSV** (which source contributed how many final companies — informs future sourcing investment)

**Day 30:** Buffer. Overruns happen.

---

## Weekly Summary

| Week | Focus | Output |
|------|-------|--------|
| 1 | Universe building | 5,000–6,000 companies with names, cities, segment tags, websites |
| 2 | Scraping + AI scoring | All 3,300+ screened companies scored. First-pass: ~1,200–1,400. |
| 3 | Human QA | Borderlines re-verified. Target: 1,100–1,200 verified passes. |
| 4 | Assembly + personalization | 1,000+ final companies in master CSV. Top 200 with outreach hooks. |

---

## Risk Table

| Risk | Mitigation |
|------|-----------|
| Yield < 25% | Expand universe: add 3 more expo lists, state SDC directories, Google Maps scraping of industrial zones in target cities |
| Scraper blocked | Rotate user agents + delays. Residential proxy for critical sites. Fall back to manual research for top-priority flagged companies. |
| AI scoring accuracy < 80% | Retune prompt on calibration set. Split scoring: Haiku for C1/C2/C5 (factual), Sonnet for C3/C4/C6 (judgment). |
| QA bottleneck | Tighten auto-QA rules to reduce human review load. Recruit a second QA reviewer. |
| Deduplication errors | Fuzzy matching (Levenshtein distance) + CIN number cross-match for listed companies |

---

## Tools and Cost Estimate

| Tool | Purpose | Cost |
|------|---------|------|
| Claude Haiku API | First-pass scoring (3,300 companies) | ~$26 |
| Claude Sonnet API | Borderline re-scoring (700 companies) | ~$84 |
| Playwright + Python | Website scraping (open source) | Free |
| Tofler / Zauba | MCA data extraction | ~$20–50/month |
| LinkedIn Sales Navigator | Technical DM discovery | License provided |
| GitHub + GitHub Actions | Pipeline orchestration and storage | Free |
| Google Sheets / PostgreSQL | Master data tracking | Free |
| **Total AI + data** | | **~$150–200** |

---

## Realistic Yield Expectation

Based on Part A research yield (~43% of investigated companies passed), and accounting for AI scoring being somewhat noisier than manual:

| Stage | Count | Notes |
|-------|-------|-------|
| Raw universe | 5,500 | Before any filtering |
| After hard pre-filters | 3,300 | Auto-disqualify rules |
| After AI first-pass (score ≥ 40) | 1,300 | ~39% pass |
| After Sonnet re-score + QA | 1,050 | Human QA tightens to ~32% net |
| **Final verified list** | **1,000+** | Meets target |

---

*[Hand-drawn diagram of this funnel submitted separately in Internshala chat as required]*
