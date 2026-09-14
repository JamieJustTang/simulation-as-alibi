# Simulation as Alibi — bilingual social cards

Three square cards per language, designed for reading on a phone:

| Card | English / X | 简体中文 / 小红书 |
|---|---|---|
| 1. Who wrote the rules? | [PNG](en/01_rules.png) | [PNG](zh/01_rules.png) |
| 2. Evidence from 142 papers | [PNG](en/02_evidence.png) | [PNG](zh/02_evidence.png) |
| 3. Four disclosure questions | [PNG](en/03_disclosure.png) | [PNG](zh/03_disclosure.png) |

Upload cards in numerical order. Each image is square, so neither platform needs a panoramic or tall-poster crop. [View all six](index.html). Posting copy and image descriptions are in [captions.md](captions.md).

## Evidence and scope

Based on Tang & Lin, *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents*, AIES 2026, final camera-ready manuscript.

- Card 1: Sections 2 and 6. The illustration is a visual metaphor for authored interaction conditions. The paper recognizes emergence as a real scientific phenomenon and critiques how emergence language can obscure responsibility.
- Card 2: Section 4.2, Table 2. Absent designer attribution: Low EI 2/36 (5.6%), Medium EI 1/49 (2.0%), High EI 14/57 (24.6%). Fourteen of all 17 absent-attribution papers are High EI (82.4%, rounded to 82%). Attribution is coded in the emergence explanation sentence; absence here does not establish that a paper discloses no methods. Single-coder, approximately 80% preprints; the association does not establish causation.
- Card 3: Sections 5 and 7. The governance finding concerns the six documents examined in this paper, not an exhaustive or continually updated legal survey. UDOS is a proposed diagnostic framework, not an enacted requirement or validated intervention. Disclosure is necessary but insufficient for accountability.

Counts were cross-checked against `data/stream1b_systematic_coding/cross_tabulation_ei_dv.csv` and `scripts/reproduce_statistics.py`.

## Production

Generated with the built-in GPT Image tool. Initial prompts are preserved in [prompts.json](prompts.json), and the final evidence-card edits in [refinement-prompts.json](refinement-prompts.json). Numerical tables replaced generated bars after visual checks found inaccurate bar lengths. Generated images are raster originals, not editable vector artwork; rerunning the prompts may produce different layouts. The prior SVG cards and their generator remain in the parent directory for reference.
