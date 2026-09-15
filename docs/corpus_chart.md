# Corpus by year

[SVG](corpus_by_year.svg) · [1400 × 1400 PNG](corpus_by_year.png)

The square chart uses horizontal stacked bars, a shared zero baseline, direct
totals, and a text breakdown beside each year. The README limits its width to
720 pixels; it scales down with the available space on smaller screens. SVG
text stays editable and the image includes a screen-reader description.

| Year | Peer-reviewed group | Preprint group | Total |
|---|---:|---:|---:|
| 2023 | 4 | 0 | 4 |
| 2024 | 6 | 10 | 16 |
| 2025 | 11 | 32 | 43 |
| 2026 | 8 | 68 | 76 |
| **Shown** | **29** | **110** | **139** |

Three of the 142 corpus records have no recorded year and are excluded:
P076, P077, and P121. These counts describe the paper's collected corpus,
not a complete census or a continuously updated publication index. The 2026
count is a corpus snapshot, not a completed calendar-year total.

## Classification and reproduction

Counts are read directly from
[coding_data_142.json](../data/stream1b_systematic_coding/coding_data_142.json).
Publication groups preserve the original chart and the repository's statistics
script: `Venue` values `arXiv`, `arXiv.org`, and blank are grouped as preprints;
other venue values are grouped as peer-reviewed. This is a venue-based coding
convention, not independent confirmation of acceptance or peer-review status.
In particular, blank and mixed venue records need that qualification when
interpreting the group labels. The redesign does not reclassify the papers.

With Python and matplotlib installed, run from the repository root:

```bash
python3 scripts/generate_corpus_chart.py
```

This generates both SVG and PNG from the same figure. For optional visual
checks at 350, 700 and 1050 pixels wide:

```bash
python3 scripts/generate_corpus_chart.py --preview-dir /tmp/corpus-chart-preview
```

Source: Tang & Lin, *Simulation as Alibi*, AIES 2026, systematic coding corpus.
