# Methodology Document
## Part A — Target Company Research | DeepThought Business Analytics Assignment
### City: Hyderabad | Segments: Specialty Biotech + Defence Electronics / Precision Engineering

---

## 1. City Choice: Hyderabad

Hyderabad was selected because it concentrates two of DeepThought's strongest ICP segments in a single geography:

- **Genome Valley** (Turkapally, Shameerpet area) — One of Asia's largest life sciences clusters. Dense with specialty biotech, vaccines, biosimilars, and pharma intermediates companies. High probability of scientist-founded companies given IICT, CCMB, CSIR labs nearby that supply technical talent and founders.
- **Defence corridor** (Hyderabad–Secunderabad area) — Strong DRDO, BDL, HAL legacy creating a private defence electronics ecosystem. DT's Ananth Technologies example is the prototype here.
- **Machine tool / precision engineering** cluster — Legacy of HMT (Hindustan Machine Tools) in Hyderabad creates gen-2 and spin-off companies in CNC and precision manufacturing.

The Federer ICP's key requirement — technical decision-maker + specialty manufacturing + growth ambition — maps well to the Hyderabad profile. ISRO and DRDO alumni often become founders. Osmania, IICT, CCMB produce PhD scientists who spin out companies.

---

## 2. Segments Selected

**Primary: Specialty Biotech (Basket A)**
- Genome Valley is concentrated here. Probability of finding 10–12 qualifying companies is high.
- Strong on C3 (differentiation): biologics, vaccines, recombinant proteins are inherently niche.
- Strong on C4 (technical DM): scientist-founders are the norm, not the exception.

**Secondary: Defence Electronics + Precision Engineering (Basket A/B adjacent)**
- Hyderabad has a distinct defence electronics cluster anchored by legacy public-sector companies.
- DT's own worked examples (Ananth Technologies, Avantel) are both from this cluster — high confidence in ICP fit.

---

## 3. Research Process — How Companies Were Found

### Step 1: Anchor on DT's Worked Examples
Started with Ananth Technologies and Avantel (provided in the assignment brief) to calibrate what a strong Federer profile looks like in Hyderabad. These set the benchmark for C1–C6 evidence quality.

### Step 2: Genome Valley Directory Sweep
Genome Valley Biotech Park (Hyderabad) publishes information about tenant companies. Combined with:
- USFDA India facility database (filtered to Telangana/Hyderabad)
- WHO-GMP prequalification list (India entries)
- DSIR recognized R&D units list (filtered to Hyderabad / Telangana)

These three sources together give a pre-filtered universe of companies that are definitively manufacturers (not traders) and have third-party validation of their technical seriousness.

### Step 3: BSE SME + NSE Emerge Sweep
Filtered BSE/NSE listed companies by:
- Industry: Pharmaceuticals, Chemicals, Biotechnology, Defence & Aerospace, Industrial Machinery
- Size: Paid-up capital suggesting Rs.50Cr–Rs.500Cr revenue band
- City: Hyderabad / Telangana

This produced a list of ~40 listed companies. Public filings (annual reports) gave immediate access to revenue, leadership bios, and facility details — making criterion scoring faster and more reliable.

### Step 4: LinkedIn Founder Search
Searched for: "Founder OR MD OR CMD" + "Hyderabad" + "pharma OR biotech OR defence OR chemicals OR manufacturing" + "PhD OR IIT OR DRDO OR ISRO"

This inverted the search — finding technical founders and then verifying their companies. Effective for catching privately held companies not in BSE/NSE data.

### Step 5: Industry-Specific Sources
- **Biotech:** BioAsia Hyderabad exhibitor directories (2023, 2024, 2025)
- **Defence:** Aero India exhibitor list + DRDO spin-off tracking
- **Chemicals:** IICT Hyderabad alumni network + DSIR recognition list

### Step 6: Disqualification and Yield
Of approximately 60–70 companies investigated:
- **25 included** in final CSV (passes + documented fails)
- **~35 eliminated** before reaching full scoring:
  - Revenue too large (>Rs.500Cr): 8 companies
  - PE/institutional-owned: 4 companies
  - CRO/service (not manufacturer): 7 companies
  - Generic pharma (commodity): 6 companies
  - Wrong city (no Hyderabad operational presence): 5 companies
  - Commodity manufacturer (failed C3): 4 companies
  - No visible activity in 2 years: 3 companies

This is consistent with the assignment's stated ~30% yield rate.

---

## 4. Scoring Approach

Each company was scored against all 6 criteria using the assignment's Weak/Moderate/Strong framework. Key principles applied:

**C1 (Manufacturer):** Every company was verified to have physical manufacturing, not just services or trading. Specific watch-out: CROs (contract research organizations) in Genome Valley look like biotech manufacturers but sell services. Applied this check rigorously — Vimta Labs and Sai Life Sciences both flagged for C1 review.

**C3 (Differentiation):** ISO 9001 alone was NOT counted as differentiation. Differentiation required: patents, USFDA/EU-GMP/WHO-GMP approval, DSIR recognition, "only/first in India" status, or genuinely technical product description. Generic biotech language ("innovative solutions") was not accepted as evidence.

**C4 (Technical DM):** PhD, IIT/NIT/BITS/IISc degree, ex-ISRO/DRDO role, or publications. "Engineering background" without specific institution was scored Moderate, not Strong. MBA-only was scored Weak. Applied this strictly — several companies scored lower on C4 than they might superficially seem.

**C6 (Growth Signals):** Only signals from last 18–24 months were counted. Old press releases, unchanged websites, or facilities announced before 2023 were not counted. At least 2 of the 5 threshold signals required for Strong rating.

**Revenue ceiling:** Checked FY25 or most recent available revenue. Fast-growing defence companies (Apollo Micro Systems, Avantel) specifically checked because defence sector companies can jump past Rs.500Cr in a single year. Apollo Micro Systems disqualified for this reason.

---

## 5. Sources Used

| Source | Used For | Quality |
|--------|---------|---------|
| BSE / NSE filings (annual reports) | Revenue, leadership bios, facility details | High — audited data |
| USFDA facility database (fda.gov) | C1 (manufacturer), C3 (differentiated), C5 (export) | High — regulatory data |
| WHO-GMP prequalification list | C3, C5 for biotech/vaccine companies | High — regulatory data |
| DSIR recognized R&D units list | C3 (differentiation signal) | High — government data |
| Company websites | Products, leadership, certifications, recent news | Medium — self-reported, check recency |
| LinkedIn (founder profiles) | C4 (technical DM background), C6 (hiring signal) | Medium — self-reported |
| MCA filings (Tofler/Zauba) | Ownership structure, director details, registered office | High — regulatory data |
| BioAsia exhibitor lists | Initial company discovery in biotech segment | Medium — discovery only |
| News searches (Google News) | C6 growth signals, recent facility announcements | Medium — verify with primary |

---

## 6. AI Usage and Hallucination Control

**AI used for:** Research structuring, drafting company profiles, writing personalization hooks.

**Hallucinations caught and corrected:**

1. AI initially listed Bharat Biotech as a pass. Corrected — revenue exceeds Rs.500Cr ceiling.
2. AI scored Sai Life Sciences C1 as Strong. Corrected to Moderate — substantial CRO service revenue alongside manufacturing.
3. AI scored Mylan Laboratories as a pass. Corrected — acquired by Viatris, now a foreign-controlled subsidiary.
4. AI assumed ABR Organics had growth signals. Corrected — website staleness noted, growth signals = 0.

**Negative prompting used throughout:**
- "Do not score any C6 signal unless you can name a specific event, date, and source"
- "Do not score C3 as Strong unless there is a specific patent, regulatory approval, or 'first/only in India' status"
- "Do not assume a company is promoter-driven — verify ownership structure from MCA or BSE before scoring C4"
- "Do not include a company without verifying it produces a physical product (not services)"

---

## 7. Limitations and What I Would Do With More Time

- **Revenue verification:** Several companies have only BSE FY24 data available. FY25 data would change the picture for fast-growing defence companies.
- **Ownership depth:** For private companies, MCA data gives director names but not ownership percentages. Some of the "probable" scores on PE ownership would be stronger with more ownership data.
- **Site visits:** Growth signals sourced from web and filings. Physical verification of facility expansions is not possible remotely but would significantly increase confidence.
- **DM contact verification:** LinkedIn profiles for decision-makers are self-reported. Some DM background scores would be refined with direct verification.
