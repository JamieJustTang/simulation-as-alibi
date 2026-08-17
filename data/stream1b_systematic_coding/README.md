# Stream 1b — Systematic Coding Corpus (142 papers)

Final coding data for the paper's systematic coding analysis.

## Files

- `coding_data_142.json` — the 142-paper dataset. Fields per record:
  - `Paper_Key`, `Paper_ID`, `Title`, `Venue`, `Year`
  - `EI` — emergence intensity (1 = Low, 2 = Medium, 3 = High)
  - `DV` — designer visibility (1 = Absent, 2 = Partial, 3 = Full)
  - `DP` — deployment proximity
  - `RT` — regulatory translatability (1–3)
  - `Designer_In_Sentence` — whether the designer appears in the emergence
    explanation sentence (yes/no)
  - `Emergence_Explanation_Quote` — verbatim emergence explanation sentence
  - `AV_Rationale` — one-line rationale for the DV code
- `cross_tabulation_ei_dv.csv` — the Table 2 cross-tabulation with row totals.
- `rationale_translation_worksheet.csv` — working sheet for the DV coding
  rationales (see note below).

## Note on coding rationales

The `AV_Rationale` field records the coding rationale in the coders' working
language (Chinese); the `Emergence_Explanation_Quote` field quotes the
verbatim English emergence explanation sentence from each paper. The
rationales are working-language records and are reproduced verbatim for
transparency; all quantitative fields (EI, DV, DP, RT, venue, year) and all
statistics derived from them are language-independent.

## Correspondence with the paper

- Table 2 (EI × DV) = counts from this data.
- χ² = 16.62, p = 0.002, V = 0.242 — see `../../scripts/reproduce_statistics.py`.
- DV is coded per the rules in `../../codebook/codebook_stream1b_v6.md`
  (emergence-explanation-sentence anchoring; risk/governance discussions do
  not count as evidence).

## Data provenance

- Corpus assembled from a 2022–2026 search of the LLM agent society and
  social simulation literature (Section 3.2 of the paper).
- DV codes are anchored on the emergence explanation sentence, produced by
  full-text reading of the papers (139 full texts; 3 papers without local
  full text coded from their emergence explanation quotes).
