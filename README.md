# Simulation as Alibi — Audit & Supporting Materials

Supporting materials for:

> Tang, S., & Lin, Z. (2026). *Simulation as Alibi — How the Social Order Gets
> Outsourced to LLM Agents*. Ninth AAAI/ACM Conference on Artificial
> Intelligence, Ethics and Society (AIES-26), camera-ready version.

This repository provides the coding data, codebook, audit materials, and
analysis scripts behind the paper's systematic coding analysis (Stream 1b),
together with documentation of the other data streams.

---

## Repository structure

```
simulation-as-alibi/
├── README.md                      # this file
├── data/
│   ├── stream1b_systematic_coding/
│   │   ├── coding_data_142.json   # 142-paper coding data (EI, DV, DP, RT, evidence quotes)
│   │   └── cross_tabulation_ei_dv.csv
│   ├── stream1a_cda/              # CDA corpus: audit extract + rationale (no data published)
│   ├── stream2_platforms/         # 5 platforms: case audit + Artificial Societies snapshot
│   └── stream3_governance/        # 6 governance frameworks: list + official sources
├── codebook/
│   └── codebook_stream1b_v6.md    # DV coding rules (emergence-explanation-sentence anchoring)
├── analysis/
│   └── statistics_summary.json    # all statistics reported in the paper
└── scripts/
    └── reproduce_statistics.py    # reproduce every number in Table 2 & Section 4.2
```

## Quick start

```bash
python3 scripts/reproduce_statistics.py
```

This reproduces, from `data/stream1b_systematic_coding/coding_data_142.json`:

| Statistic | Paper reports | Script reproduces |
|-----------|---------------|-------------------|
| χ² (df=4) | 16.62 | 16.622 |
| p | 0.002 | 0.002 |
| Cramér's V | 0.242 | 0.242 |
| r(EI, DV) | -0.141 (p = 0.094) | -0.141 (p = 0.092) |
| r(EI, RT) | 0.194 (p = 0.021) | 0.194 (p = 0.019) |
| Absent concentration | 14/17 (82%) in High EI | 14/17 (82%) |
| arXiv share | ~80% | 80% |

*The correlation p-values in the paper are exact two-tailed values; the
script uses a normal approximation to the t-distribution, which accounts for
the third-decimal differences (0.094 vs. 0.092; 0.021 vs. 0.019). All point
estimates match exactly.*

## What the paper claims, and where it is backed here

1. **142-paper systematic coding corpus (Stream 1b)** — `coding_data_142.json`.
   Each record contains: Paper ID, title, venue, year, and the four coded
   dimensions used in the paper — emergence intensity (EI), designer
   visibility (DV), deployment proximity (DP), regulatory translatability (RT)
   — plus the verbatim emergence-explanation sentence (English) and the coding
   rationale (recorded in the coders' working language, Chinese; see the
   Stream 1b README). All quantitative fields and statistics are
   language-independent.
2. **DV coding is anchored in the emergence-explanation sentence** —
   `codebook/codebook_stream1b_v6.md` (Section 3.3 of the paper).
3. **Table 2 cross-tabulation and all statistics in Section 4.2** —
   `reproduce_statistics.py`, `cross_tabulation_ei_dv.csv`,
   `statistics_summary.json`.
4. **The threshold signature** — significant χ² alongside a non-significant
   ordinal correlation — is confirmed by the script (`THRESHOLD CONFIRMED`).
5. **~80% arXiv preprint share** — computed from the `Venue` field
   (Section 8 limitation discussion).
6. **Stream 2 (5 platforms) and Stream 3 (6 governance frameworks)** —
   documented in `data/stream2_platforms/README.md` and
   `data/stream3_governance/README.md`, including the full case audit
   (`case_audit.md`) and official source links.
7. **Stream 1a (CDA, 20 papers)** — `data/stream1a_cda/README.md`. Stream 1a
   is the qualitative component of the study; consistent with the paper, no
   per-paper CDA corpus or cross-tabulation is published, and no quantitative
   statistic in the paper depends on this stream.

## Coding protocol summary (DV)

The DV code is assigned by locating the paper's *emergence explanation
sentence* — the sentence in which the paper explains why an emergent
phenomenon occurs — and asking whether the designer or design choices appear
in that sentence as a causal subject:

- **DV = Full**: the emergence explanation attributes the outcome to specific
  design choices (e.g., "removing memory prevents the emergence of stable
  cooperation").
- **DV = Partial**: the architecture is disclosed in the methods but the
  emergence explanation does not return to those design choices.
- **DV = Absent**: emergence is narrated as spontaneous, self-organized, or
  population-level (e.g., "norms emerged naturally from interactions").

Risk, governance, and ethical discussions do **not** count as evidence of
designer visibility.

## Notes on scope

- The quantitative analysis (Stream 1b) covers 142 papers spanning the full
  publication spectrum (peer-reviewed venues and arXiv preprints alike),
  because the central debates over emergent behavior are currently unfolding
  in the preprint literature; ~80% of the corpus are preprints (see the
  paper's limitation discussion).
- Case studies (Section 6) are document-based pattern inference, as stated
  in the paper.

## License & contact

Materials are released for transparency and audit. Please cite the AIES-26
paper. For questions: jamietang@ruc.edu.cn.
