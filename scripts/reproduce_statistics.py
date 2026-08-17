#!/usr/bin/env python3
"""
Reproduce all quantitative results reported in:
Tang, S. & Lin, Z. (2026). Simulation as Alibi — How the Social Order Gets
Outsourced to LLM Agents. AIES-26 (camera-ready).

Run:  python3 reproduce_statistics.py
Requires: Python 3.8+ (standard library only).

Outputs are compared against the values printed in the paper:
  - Table 2 cross-tabulation (EI x DV), row percentages, standardized residuals
  - chi2 = 16.62, df = 4, p = 0.002, Cramer's V = 0.242
  - r(EI, DV) = -0.141, p = 0.094  (non-significant -> threshold signature)
  - r(EI, RT) = 0.194, p = 0.021   (positive, significant)
  - 14 of 17 Absent-DV papers (82%) are High-EI papers
  - ~80% of the systematic coding corpus are arXiv preprints
"""
import json, math, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "stream1b_systematic_coding", "coding_data_142.json")

def gammainc_p(a, x):
    """Regularized lower incomplete gamma P(a, x) via series."""
    if x <= 0: return 0.0
    s = 1.0 / a; term = 1.0 / a
    for i in range(1, 600):
        term *= x / (a + i); s += term
        if term < 1e-14 * s: break
    return s * math.exp(-x + a * math.log(x) - math.lgamma(a))

def chi2_pvalue(obs):
    n = sum(sum(r) for r in obs)
    rs = [sum(r) for r in obs]
    cs = [sum(obs[i][j] for i in range(3)) for j in range(3)]
    chi = sum((obs[i][j] - rs[i]*cs[j]/n)**2 / (rs[i]*cs[j]/n)
              for i in range(3) for j in range(3))
    p = 1 - gammainc_p(4/2, chi/2)   # df = (3-1)*(3-1) = 4
    return chi, p

def pearson_r_p(pairs):
    m = len(pairs)
    mx = sum(a for a, b in pairs) / m
    my = sum(b for a, b in pairs) / m
    cov = sum((a-mx)*(b-my) for a, b in pairs) / m
    sx = math.sqrt(sum((a-mx)**2 for a, b in pairs) / m)
    sy = math.sqrt(sum((b-my)**2 for a, b in pairs) / m)
    r = cov / (sx * sy) if sx > 0 and sy > 0 else 0.0
    t = r * math.sqrt((m - 2) / (1 - r*r)) if abs(r) < 1 else 0.0
    from math import erf
    p = 2 * (1 - 0.5 * (1 + erf(abs(t) / math.sqrt(2))))
    return r, p

def main():
    recs = json.load(open(DATA))
    n = len(recs)
    assert n == 142, f"expected 142 records, got {n}"

    # ---- cross-tabulation EI (1=Low,2=Med,3=High) x DV (1=Absent,2=Partial,3=Full)
    tab = collections.Counter((int(r["EI"]), int(r["DV"])) for r in recs)
    obs = [[tab.get((i, j), 0) for j in (1, 2, 3)] for i in (1, 2, 3)]
    rs = [sum(o) for o in obs]
    cs = [sum(obs[i][j] for i in range(3)) for j in range(3)]
    chi, p = chi2_pvalue(obs)
    V = math.sqrt(chi / (n * 2))

    print("=" * 72)
    print("Table 2 cross-tabulation (EI x DV)")
    print("=" * 72)
    print(f"{'':10}{'DV: Full':>10}{'DV: Partial':>12}{'DV: Absent':>12}{'Total':>8}")
    for i, label in enumerate(["EI: Low", "EI: Medium", "EI: High"]):
        row = [obs[i][2], obs[i][1], obs[i][0]]  # Full, Partial, Absent
        pct = [100*c/rs[i] for c in row]
        print(f"{label:10}{row[0]:>8} ({pct[0]:3.0f}%){row[1]:>10} ({pct[1]:3.0f}%){row[2]:>10} ({pct[2]:3.0f}%){rs[i]:>8}")
    print(f"{'Total':10}{cs[2]:>8}{cs[1]:>12}{cs[0]:>12}{n:>8}")

    # standardized residuals
    print("\nStandardized residuals:")
    for i, label in enumerate(["Low", "Medium", "High"]):
        zs = []
        for j in (2, 1, 0):
            e = rs[i] * cs[j] / n
            zs.append((obs[i][j] - e) / math.sqrt(e))
        print(f"  {label:8}" + "".join(f"{z:>+10.1f}" for z in zs))

    print("\n" + "=" * 72)
    print("Reported statistics vs. reproduced values")
    print("=" * 72)
    checks = [
        ("chi2 (df=4)", 16.62, chi),
        ("p-value", 0.002, p),
        ("Cramer's V", 0.242, V),
    ]
    for name, reported, got in checks:
        flag = "OK" if abs(reported - got) < 0.01 else "MISMATCH"
        print(f"  {name:15} reported={reported:<8.3f} reproduced={got:<8.3f}  [{flag}]")

    # r(EI, DV) on ordinal codes
    pairs = [(int(r["EI"]), int(r["DV"])) for r in recs]
    r1, p1 = pearson_r_p(pairs)
    print(f"  {'r(EI,DV)':15} reported={-0.141:<8.3f} reproduced={r1:<8.3f} p={p1:.3f}  [{ 'OK' if abs(-0.141-r1)<0.01 else 'MISMATCH'}]")

    # r(EI, RT)
    rtmap = {"1": 1, "2": 2, "3": 3}
    pairs2 = [(int(r["EI"]), rtmap[str(r["RT"])]) for r in recs if r.get("RT")]
    r2, p2 = pearson_r_p(pairs2)
    print(f"  {'r(EI,RT)':15} reported={0.194:<8.3f} reproduced={r2:<8.3f} p={p2:.3f}  [{ 'OK' if abs(0.194-r2)<0.01 else 'MISMATCH'}]")

    # absent concentration
    hi_abs = [r for r in recs if r["EI"] == "3" and r["DV"] == "1"]
    total_abs = [r for r in recs if r["DV"] == "1"]
    print(f"  {'Absent concentration':15} reported=14/17 (82%) reproduced={len(hi_abs)}/{len(total_abs)} ({100*len(hi_abs)/len(total_abs):.0f}%)")

    # arXiv share
    arv = {"arXiv", "arXiv.org", ""}
    n_arxiv = sum(1 for r in recs if str(r["Venue"]) in arv)
    print(f"  {'arXiv share':15} reported=~80% reproduced={100*n_arxiv/n:.0f}%")

    # threshold signature
    sig_chi = p < 0.05
    sig_r = p1 < 0.05
    print(f"\n  Threshold signature (chi2 significant & r non-significant): "
          f"{'CONFIRMED' if (sig_chi and not sig_r) else 'NOT CONFIRMED'}")

if __name__ == "__main__":
    main()
