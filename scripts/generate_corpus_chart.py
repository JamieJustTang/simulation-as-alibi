#!/usr/bin/env python3
"""Generate the editorial-style, dependency-free SVG used in the README."""

from pathlib import Path

YEARS = (2023, 2024, 2025, 2026)
PEER_REVIEWED = (4, 6, 11, 8)
PREPRINTS = (0, 10, 32, 68)
TOTALS = tuple(a + b for a, b in zip(PEER_REVIEWED, PREPRINTS))
WIDTH, HEIGHT = 900, 570
LEFT, RIGHT, TOP, BASELINE = 82, 42, 180, 484
PLOT_WIDTH, PLOT_HEIGHT = WIDTH - LEFT - RIGHT, BASELINE - TOP
MAX_VALUE = 80
INK, MUTED, GRID = "#17212B", "#68737D", "#DCE2E3"
PAPER, CARD = "#F5F2EB", "#FFFEFB"
PEER, PREPRINT, ACCENT = "#416F75", "#D98B3A", "#9E3F2E"


def y(value: int) -> float:
    return BASELINE - PLOT_HEIGHT * value / MAX_VALUE


def main() -> None:
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="chart-title chart-desc">',
        '<title id="chart-title">The field is expanding faster than peer review</title>',
        '<desc id="chart-desc">Stacked bars show 29 peer-reviewed papers and 110 arXiv preprints from 2023 to 2026. The 2026 bar contains 8 peer-reviewed papers and 68 preprints.</desc>',
        f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{PAPER}"/>',
        f'<rect x="20" y="18" width="860" height="534" rx="18" fill="{CARD}" stroke="#E7E1D7"/>',
        '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif">',
        f'<text x="52" y="58" font-size="12" font-weight="700" letter-spacing="1.7" fill="{ACCENT}">FIELD OVERVIEW · 2023–2026</text>',
        f'<text x="52" y="92" font-size="25" font-weight="750" fill="{INK}">The field is expanding faster than peer review</text>',
        f'<text x="52" y="120" font-size="15" fill="{MUTED}">Annual papers in the systematic coding corpus, by publication status</text>',
        f'<rect x="638" y="42" width="212" height="92" rx="12" fill="#F3E8DA"/>',
        f'<text x="656" y="66" font-size="11" font-weight="700" letter-spacing="1.15" fill="{ACCENT}">2026 PREPRINT SURGE</text>',
        f'<text x="656" y="108" font-size="38" font-weight="760" fill="{INK}">68</text>',
        f'<text x="714" y="96" font-size="13" font-weight="650" fill="{INK}">preprints</text>',
        f'<text x="714" y="116" font-size="12" fill="{MUTED}">89% of 2026 output</text>',
        f'<circle cx="58" cy="151" r="5" fill="{PEER}"/>',
        f'<text x="70" y="156" font-size="13" fill="{INK}">Peer-reviewed</text>',
        f'<text x="169" y="156" font-size="13" font-weight="700" fill="{PEER}">29</text>',
        f'<circle cx="208" cy="151" r="5" fill="{PREPRINT}"/>',
        f'<text x="220" y="156" font-size="13" fill="{INK}">arXiv preprint</text>',
        f'<text x="310" y="156" font-size="13" font-weight="700" fill="{PREPRINT}">110</text>',
        f'<text x="850" y="156" text-anchor="end" font-size="12" fill="{MUTED}">n = 139 with complete chart metadata</text>',
        f'<rect x="666" y="{TOP - 8}" width="142" height="{PLOT_HEIGHT + 24}" rx="12" fill="#FBF4E9"/>',
    ]
    for tick in range(0, MAX_VALUE + 1, 20):
        ty = y(tick)
        out += [
            f'<line x1="{LEFT}" y1="{ty:.1f}" x2="{WIDTH - RIGHT}" y2="{ty:.1f}" stroke="{GRID}" stroke-width="1"/>',
                f'<text x="{LEFT - 15}" y="{ty + 5:.1f}" text-anchor="end" font-size="13" fill="{MUTED}">{tick}</text>',
        ]
    centers, bar_width = (150, 346, 542, 738), 76
    for year, peer, preprint, total, center in zip(YEARS, PEER_REVIEWED, PREPRINTS, TOTALS, centers):
        x, peer_h, preprint_h = center - bar_width / 2, PLOT_HEIGHT * peer / MAX_VALUE, PLOT_HEIGHT * preprint / MAX_VALUE
        total_y = y(total)
        out.append(f'<rect x="{x:.1f}" y="{TOP:.1f}" width="{bar_width}" height="{PLOT_HEIGHT}" rx="8" fill="#F1F1ED"/>')
        if preprint:
            out.append(f'<path d="M{x:.1f},{total_y + 8:.1f} Q{x:.1f},{total_y:.1f} {x + 8:.1f},{total_y:.1f} H{x + bar_width - 8:.1f} Q{x + bar_width:.1f},{total_y:.1f} {x + bar_width:.1f},{total_y + 8:.1f} V{BASELINE - peer_h:.1f} H{x:.1f} Z" fill="{PREPRINT}"/>')
        out.append(f'<rect x="{x:.1f}" y="{BASELINE - peer_h:.1f}" width="{bar_width}" height="{peer_h:.1f}" fill="{PEER}"/>')
        out.append(f'<text x="{center}" y="{total_y - 12:.1f}" text-anchor="middle" font-size="19" font-weight="750" fill="{INK}">{total}</text>')
        out.append(f'<text x="{center}" y="517" text-anchor="middle" font-size="15" font-weight="650" fill="{INK}">{year}</text>')
        if peer >= 6:
            out.append(f'<text x="{center}" y="{BASELINE - peer_h / 2 + 5:.1f}" text-anchor="middle" font-size="13" font-weight="700" fill="#FFFFFF">{peer}</text>')
        if preprint >= 10:
            out.append(f'<text x="{center}" y="{total_y + preprint_h / 2 + 5:.1f}" text-anchor="middle" font-size="13" font-weight="700" fill="#4D2C12">{preprint}</text>')
    out += [
        f'<text x="35" y="340" text-anchor="middle" font-size="12" fill="{MUTED}" transform="rotate(-90 35 340)">NUMBER OF PAPERS</text>',
        f'<path d="M385 240 C455 216, 565 211, 654 225" fill="none" stroke="{ACCENT}" stroke-width="1.5" stroke-dasharray="4 5"/>',
        f'<path d="M645 218 L656 225 L645 231" fill="none" stroke="{ACCENT}" stroke-width="1.5"/>',
        f'<text x="520" y="207" text-anchor="middle" font-size="12" font-weight="700" fill="{ACCENT}">4.8× MORE PAPERS THAN 2024</text>',
        f'<text x="52" y="540" font-size="11.5" fill="{MUTED}">Source: systematic coding data. Three corpus records without a year are excluded from the chart.</text>',
        '</g>', '</svg>',
    ]
    target = Path(__file__).resolve().parents[1] / "docs" / "corpus_by_year.svg"
    target.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
