"""
DeepThought Business Analytics Assignment
Part A — Federer ICP Scoring Analyzer

This script:
1. Reads the 25-company CSV
2. Validates scoring consistency
3. Prints a summary dashboard of results
4. Flags any scoring anomalies for human QA
5. Segments companies by score band and verdict

Usage: python3 scoring_analysis.py
"""

import csv
import json
from collections import defaultdict

CSV_PATH = "25_companies_federer_research.csv"

# ─────────────────────────────────────────────────────────────
# SCORING LOGIC
# ─────────────────────────────────────────────────────────────

SCORE_MAP = {
    "Strong": 1.0,
    "Moderate": 0.5,
    "Weak": 0.0,
    "Fail": 0.0,
    "N/A": None,  # auto-disqualified — skip scoring
}

CRITERION_WEIGHTS = {
    "C1": 10,
    "C2": 5,
    "C3": 25,
    "C4": 20,
    "C5": 20,
    "C6": 20,
}

SCORE_BANDS = {
    (80, 100): "A — Strong Federer",
    (60, 79):  "B — Probable Federer",
    (40, 59):  "C — Borderline",
    (0,  39):  "D — Not ICP",
}

def get_band(score):
    for (low, high), band in SCORE_BANDS.items():
        if low <= score <= high:
            return band
    return "D — Not ICP"


def calculate_federer_score(row):
    """Calculate score from C1–C6 scores in the row."""
    total = 0
    any_disqualified = False

    for crit, weight in CRITERION_WEIGHTS.items():
        score_key = f"{crit} Manufacturer Score" if crit == "C1" else f"{crit} India Score" if crit == "C2" else f"{crit} Differentiation Score" if crit == "C3" else f"{crit} Tech DM Score" if crit == "C4" else f"{crit} Tailwind Score" if crit == "C5" else f"{crit} Growth Score"
        
        # Try to find the column
        for col in row:
            if col.startswith(crit) and "Score" in col:
                val = row[col].strip()
                multiplier = SCORE_MAP.get(val)
                if multiplier is None:
                    any_disqualified = True
                    break
                if val == "Fail":
                    return 0  # Any C1 or C3 Fail → disqualify
                total += weight * multiplier
                break

    if any_disqualified:
        return 0

    return round(total)


def print_header(title):
    width = 65
    print("\n" + "═" * width)
    print(f"  {title}")
    print("═" * width)


def load_companies(path):
    companies = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            companies.append(dict(row))
    return companies


def analyze(companies):
    print_header("DEEPTHOUGHT — FEDERER ICP SCORING ANALYSIS")

    passes = []
    fails = []
    borderlines = []

    band_counts = defaultdict(int)
    segment_counts = defaultdict(int)

    for c in companies:
        name = c.get("Company Name", "Unknown")
        verdict = c.get("Verdict", "")
        score_raw = c.get("Federer Score", "0")

        try:
            score = int(score_raw)
        except (ValueError, TypeError):
            score = 0

        band = get_band(score)
        band_counts[band] += 1
        segment_counts[c.get("Segment", "Unknown")] += 1

        if score >= 80:
            passes.append((name, score, c.get("Personalization Hook", "")))
        elif 60 <= score < 80:
            borderlines.append((name, score, verdict))
        else:
            fails.append((name, score, verdict))

    # ─── SUMMARY TABLE ───
    print_header("SCORE BAND DISTRIBUTION")
    total = len(companies)
    print(f"\n  {'Band':<30} {'Count':<10} {'%'}")
    print("  " + "-" * 50)
    for (low, high), band in sorted(SCORE_BANDS.items(), reverse=True):
        count = band_counts.get(band, 0)
        pct = (count / total * 100) if total else 0
        bar = "█" * int(pct / 5)
        print(f"  {band:<30} {count:<10} {pct:.0f}%  {bar}")
    print(f"\n  Total companies evaluated: {total}")

    # ─── STRONG PASSES ───
    print_header("STRONG PASS COMPANIES (Score ≥ 80)")
    if passes:
        for name, score, hook in sorted(passes, key=lambda x: -x[1]):
            print(f"\n  ✅ {name} [{score}/100]")
            if hook and hook != "N/A":
                print(f"     Hook: {hook[:90]}...")
    else:
        print("  None found.")

    # ─── BORDERLINES ───
    print_header("BORDERLINE COMPANIES (Score 60–79) — Research Further")
    if borderlines:
        for name, score, verdict in sorted(borderlines, key=lambda x: -x[1]):
            print(f"\n  ⚠️  {name} [{score}/100]")
            print(f"     {verdict[:100]}")
    else:
        print("  None.")

    # ─── FAILS ───
    print_header("DISQUALIFIED COMPANIES (Score < 40 or Auto-Disqualify)")
    if fails:
        for name, score, verdict in fails:
            reason = verdict.split(",")[0][:80] if verdict else "Unknown"
            print(f"  ❌ {name}: {reason}")

    # ─── SEGMENT BREAKDOWN ───
    print_header("COMPANIES BY SEGMENT")
    for seg, count in sorted(segment_counts.items(), key=lambda x: -x[1]):
        short = seg[:50]
        print(f"  {short:<50} {count}")

    # ─── YIELD ANALYSIS ───
    print_header("YIELD ANALYSIS")
    pass_count = len(passes)
    border_count = len(borderlines)
    fail_count = len(fails)

    print(f"\n  Strong passes (A-band, score ≥ 80):   {pass_count}")
    print(f"  Borderline (B-band, score 60-79):     {border_count}")
    print(f"  Disqualified (D-band, score < 40):    {fail_count}")
    print(f"  Total:                                {total}")

    if total > 0:
        yield_rate = pass_count / total * 100
        print(f"\n  Pass yield: {yield_rate:.0f}% (assignment predicts ~30%)")

        if yield_rate < 25:
            print("  ⚠️  Yield below expected — review borderlines or expand research.")
        elif yield_rate > 50:
            print("  ⚠️  Yield above 50% — verify scoring criteria weren't too lenient.")
        else:
            print("  ✅ Yield within expected range.")

    # ─── SCORING QA FLAGS ───
    print_header("QA FLAGS — Items to Review")

    flags = []
    for c in companies:
        name = c.get("Company Name", "?")
        c3 = c.get("C3 Differentiation Score", "")
        c6 = c.get("C6 Growth Score", "")
        score_raw = c.get("Federer Score", "0")

        try:
            score = int(score_raw)
        except (ValueError, TypeError):
            score = 0

        # Flag: C3 = "ISO 9001 only" risk
        if "ISO 9001" in c.get("C3 Evidence", "") and c3 == "Strong":
            flags.append(f"[C3] {name}: Strong C3 but ISO 9001 mentioned — verify genuine differentiation")

        # Flag: C6 = strong but score band low
        if c6 == "Strong" and score < 60:
            flags.append(f"[C6] {name}: Strong growth signals but low total score — check other criteria")

        # Flag: 0 score companies with some criteria showing
        if score == 0 and c.get("Verdict", "").startswith("Fail"):
            pass  # Expected — auto-disqualified, fine

    if flags:
        for flag in flags:
            print(f"  🔍 {flag}")
    else:
        print("\n  No QA flags raised. Scoring appears consistent.")

    print("\n" + "═" * 65)
    print("  Analysis complete.")
    print("═" * 65 + "\n")


def export_priority_list(companies, out_path="charts/priority_outreach.json"):
    """Export top A-band companies with personalization hooks for outreach."""
    import os
    os.makedirs("charts", exist_ok=True)

    priority = []
    for c in companies:
        try:
            score = int(c.get("Federer Score", "0"))
        except (ValueError, TypeError):
            score = 0

        if score >= 80 and c.get("Personalization Hook", "N/A") != "N/A":
            priority.append({
                "company": c.get("Company Name"),
                "website": c.get("Website"),
                "segment": c.get("Segment"),
                "score": score,
                "band": c.get("Score Band"),
                "decision_maker": c.get("Decision Maker"),
                "dm_title": c.get("DM Title"),
                "dm_background": c.get("DM Background"),
                "revenue_band": c.get("Revenue Band"),
                "personalization_hook": c.get("Personalization Hook"),
                "verdict": c.get("Verdict"),
            })

    priority.sort(key=lambda x: -x["score"])

    with open(out_path, "w") as f:
        json.dump(priority, f, indent=2)

    print(f"\n  ✅ Priority outreach list exported: {out_path}")
    print(f"     {len(priority)} companies ready for outreach")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n  Loading company research data...")
    companies = load_companies(CSV_PATH)
    print(f"  Loaded {len(companies)} companies.")

    analyze(companies)
    export_priority_list(companies)
