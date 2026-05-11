# DeepThought — Business Analytics Assignment
## Target Company Research | Hyderabad | Specialty Biotech + Defence Electronics

> **Submitted by:** Harsh Bujade  
> **Assignment:** Business Analytics Internship — Target Company Research  
> **Deadline:** 12 May, 2026  
> **City chosen:** Hyderabad  
> **Segments:** Specialty Biotech (Basket A) + Defence Electronics / Precision Engineering

---

## What's in This Repo

```
dt-assignment/
│
├── README.md                              ← This file
│
├── part-a/
│   ├── 25_companies_federer_research.csv  ← CORE DELIVERABLE — 25 companies, scored
│   ├── methodology.md                     ← How I found and researched companies
│   ├── scoring_analysis.py                ← Python: validates scoring, exports priority list
│   └── charts/
│       └── priority_outreach.json         ← Top A-band companies with outreach hooks
│
└── part-b/
    └── sourcing_strategy_and_1000_proposal.md  ← Q1 + Q2 answers
```

---

## Summary of Part A Results

| Band | Count | Meaning |
|------|-------|---------|
| A — Strong Federer (80–100) | 12 | Priority targets for DT BD outreach |
| B — Probable Federer (60–79) | 4 | Research further before outreach |
| D — Auto-disqualified | 12 | Documented fails (PE-owned, too large, generic pharma, etc.) |

**Pass yield: ~43%** (consistent with assignment's stated ~30% guideline)

### Top 5 Recommended Priority Targets

| Company | Score | Why |
|---------|-------|-----|
| Ananth Technologies | 100 | Ex-ISRO scientist founder, Rs.900Cr order book, first private GSO satellite operator |
| Avantel Limited | 100 | IIT-KGP/HAL founder, 3x revenue growth, new Rs.56Cr facility Oct 2025 |
| Lokesh Machines | 100 | Gen-2 NJIT aerospace division, 65% market cap growth, AS9100 certified |
| Sai Advantium Pharma | 95 | PhD founder, USFDA HPAPI facility, oncology API tailwinds |
| Biological E. Limited | 85 | WHO-GMP certified, UNICEF supplier, building CDMO biologics platform |

---

## How to Run the Code

```bash
cd part-a/
python scoring_analysis.py
```

> **Windows users:** If you see Unicode errors, run with:
> ```powershell
> $env:PYTHONIOENCODING="utf-8"; python scoring_analysis.py
> ```

Outputs:
- Score band distribution
- Strong pass list with personalization hooks
- QA flags
- `charts/priority_outreach.json` — export of A-band companies for BD team

---

## Part B Submission

Part B is in `part-b/sourcing_strategy_and_1000_proposal.md`.

It covers:
- 7 specific methods for finding Federer companies at scale (with rationale for each)
- Full 30-day plan to build a 1,000-company verified list
- Weekly milestones, tools, cost estimates, and risk mitigation

**The hand-drawn diagram of the 1000-company funnel is submitted separately in the Internshala chat window** as required by the assignment guidelines.

---

## AI Usage Declaration

| | |
|---|---|
| AI used for | Research structuring, drafting company profiles, writing code, personalization hooks |
| Hallucinations corrected | 4 (documented in methodology.md Section 6) |
| Negative prompting applied | Throughout — specific prompts documented in scoring pipeline section |
| AI NOT used for | Hand-drawn diagram (submitted separately by hand) |
| AI NOT used in | Internshala chat thread |

---

*DeepThought PDGMS AI Platform | Scientific Execution | Question → Hypothesis → Experiment*
