# Stream 1a — CDA Corpus (20 papers + 5 platform documents)

As declared in the paper (Section 3.2, Data Streams): *"Stream 1a (critical
discourse analysis) comprises 20 papers on LLM agent societies (2023–2026)
from AAMAS, NeurIPS, ICML, Nature Computational Science, and arXiv, reporting
emergent social phenomena in multi-agent LLM systems."*

## Scope

Stream 1a is the **qualitative** component of the study: critical discourse
analysis aimed at interpretive depth, identifying the rhetorical mechanisms
through which emergence discourse erases the designer (passive constructions,
nominalization, recontextualization, legitimacy nesting). The findings are
reported in Section 4.1 of the paper.

Consistent with the paper, this directory does not publish a per-paper CDA
corpus or a CDA cross-tabulation. The qualitative claims are supported by the
analysis narrative and the sources cited in the paper's bibliography; no
quantitative statistic in the paper depends on this stream.

The paper's quantitative results (Table 2, χ² = 16.62) come exclusively from
the Stream 1b systematic coding and are fully reproducible from
`../../data/stream1b_systematic_coding/coding_data_142.json` via
`../../scripts/reproduce_statistics.py`.

## Note on the two 82% figures in the paper

- Section 4.1: "passive and subjectless constructions... appearing in 82% of
  high-emergence-intensity documents" — a qualitative descriptive observation
  from the CDA reading.
- Section 4.2: "High-EI papers constitute 40% of the corpus yet account for
  82% of all absent designer attribution" — a statistic of the 142-paper
  coding (14 of 17 Absent-DV papers are High-EI), verified by
  `reproduce_statistics.py`.

## Coding instrument

The DV (designer visibility) coding rules used for the qualitative reading of
these papers follow the same emergence-explanation-sentence anchoring
described in `../../codebook/codebook_stream1b_v6.md`.
