#!/usr/bin/env python3
"""Generate the three square, dependency-free SVG social cards."""

import argparse
import math
from pathlib import Path
from xml.sax.saxutils import escape

W = H = 900
PAPER, CARD, INK, MUTED = "#F5F2EB", "#FFFEFB", "#17212B", "#68737D"
GRID, TEAL, TEAL_L = "#DCE2E3", "#416F75", "#DDE9E7"
ORANGE, ORANGE_L, RUST, RUST_L = "#D98B3A", "#F3E4CF", "#9E3F2E", "#F2DEDA"
FONT = "-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"
CITATION = "Tang, S. & Lin, Z. (2026). Simulation as Alibi: How the Social Order Gets Outsourced to LLM Agents. AIES ’26."
OUT = Path(__file__).resolve().parents[1] / "docs" / "social_cards"


def t(x, y, value, size=14, fill=INK, weight=400, anchor="start", spacing=None, italic=False):
    attrs = [f'x="{x}"', f'y="{y}"', f'font-size="{size}"', f'fill="{fill}"',
             f'font-weight="{weight}"', f'text-anchor="{anchor}"']
    if spacing is not None:
        attrs.append(f'letter-spacing="{spacing}"')
    if italic:
        attrs.append('font-style="italic"')
    return f'<text {" ".join(attrs)}>{escape(str(value))}</text>'


def box(x, y, w, h, fill=CARD, stroke="none", radius=12, sw=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def line(x1, y1, x2, y2, stroke=GRID, sw=1, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def arrow(x1, y1, x2, y2, stroke=INK, sw=2, dash=None):
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 8
    bx, by = x2 - size * math.cos(angle), y2 - size * math.sin(angle)
    px, py = 4 * math.sin(angle), -4 * math.cos(angle)
    shaft = line(x1, y1, bx, by, stroke, sw, dash)
    head = f'<polygon points="{x2:.1f},{y2:.1f} {bx + px:.1f},{by + py:.1f} {bx - px:.1f},{by - py:.1f}" fill="{stroke}"/>'
    return shaft + head


def wrap_text(x, y, lines, size=14, fill=INK, weight=400, leading=20, anchor="start"):
    return [t(x, y + i * leading, value, size, fill, weight, anchor) for i, value in enumerate(lines)]


def shell(title, subtitle, eyebrow, desc):
    title_lines = title.split("\n")
    subtitle_y = 122 + 38 * (len(title_lines) - 1)
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title.replace(chr(10), " "))}</title>', f'<desc id="desc">{escape(desc)}</desc>',
        box(0, 0, W, H, PAPER, radius=0), box(20, 18, 860, 864, CARD, "#E7E1D7", 18),
        f'<g font-family="{FONT}">',
        t(52, 58, eyebrow, 12, RUST, 700, spacing=1.6),
    ]
    for i, title_line in enumerate(title_lines):
        out.append(t(52, 94 + i * 38, title_line, 32 if len(title_lines) > 1 else 25, INK, 770))
    out.append(t(52, subtitle_y, subtitle, 15, MUTED, 450))
    return out


def footer(data_note):
    return [line(52, 818, 848, 818, "#E7E1D7"), t(52, 842, data_note, 10.5, MUTED),
            t(52, 864, "Citation: " + CITATION, 10.5, INK, 650), '</g>', '</svg>']


def pain_card():
    out = shell(
        "The rules gain power as\ntheir authors disappear",
        "LLM social simulation moves from commercial experimentation toward public authority.",
        "01 · THE PAIN POINT",
        "Three domains of outsourcing and a matrix showing the absence of architecture-level disclosure across six governance frameworks.",
    )
    out += [t(52, 202, "RISING POLITICAL-ECONOMIC & GOVERNANCE STAKES", 12, RUST, 720, spacing=1.1),
            '<polyline points="74,338 338,310 602,270 826,226" fill="none" stroke="#416F75" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
            arrow(602, 270, 826, 226, TEAL, 5)]
    domains = [(170, 326, "01", "COMMERCIAL", "Proprietary", TEAL, TEAL_L),
               (450, 292, "02", "MILITARY", "Classified", RUST, RUST_L),
               (720, 247, "03", "GOVERNMENTAL", "Undocumented", ORANGE, ORANGE_L)]
    for cx, cy, number, domain, closure, color, fill in domains:
        out += [f'<circle cx="{cx}" cy="{cy}" r="34" fill="{color}"/>',
                t(cx, cy + 8, number, 20, "#FFFFFF", 780, "middle"),
                line(cx, cy + 34, cx, 386, color, 2, "3 5"),
                box(cx - 108, 386, 216, 112, fill, "#DED8CF", 12),
                t(cx, 420, domain, 12, color, 760, "middle", 1.0),
                t(cx, 462, closure, 24, INK, 770, "middle")]
    out += [line(52, 530, 848, 530, "#E5DED3"),
            box(52, 558, 796, 220, "#F7F4EE", "#E5DED3", 14),
            t(82, 596, "THE STRUCTURAL DISCLOSURE GAP", 12, RUST, 750, spacing=1.0),
            t(82, 688, "0 / 6", 72, RUST, 790),
            *wrap_text(330, 622, ["governance frameworks require explicit", "procedural authorship disclosure"], 22, INK, 730, 30),
            t(330, 690, "The regulatory object remains the model—not the authored social architecture.", 12.5, MUTED, 550)]
    gap_labels = [("D1", "Topology"), ("D2", "Actions"), ("D3", "Sanctions"), ("D4", "Beneficiary")]
    for i, (code, label) in enumerate(gap_labels):
        x = 330 + i * 125
        out += [box(x, 718, 112, 38, RUST_L, radius=9),
                t(x + 15, 743, code, 11, RUST, 760), t(x + 42, 743, label, 11, INK, 650)]
    out += footer("Evidence: institutional gap analysis of six frameworks and three cross-domain cases.")
    return out


def audit_card():
    out = shell(
        "Designer erasure concentrates\nat High EI",
        "A threshold effect—not a smooth decline in visibility.",
        "02 · THE AUDIT EVIDENCE · n = 142",
        "A three-by-three audit matrix crossing emergence intensity with designer visibility, highlighting High EI and absent designer attribution.",
    )
    out += [t(160, 214, "DESIGNER VISIBILITY (DV)", 12, TEAL, 760, spacing=1.0)]
    columns = [("FULL", TEAL_L, TEAL), ("PARTIAL", ORANGE_L, ORANGE), ("ABSENT", RUST_L, RUST)]
    matrix = [[(19, 53), (15, 42), (2, 6)], [(24, 49), (24, 49), (1, 2)], [(28, 49), (15, 26), (14, 25)]]
    row_names = ["LOW EI", "MEDIUM EI", "HIGH EI"]
    x0, y0, cw, rh = 158, 258, 145, 112
    for j, (label, _, color) in enumerate(columns):
        out.append(t(x0 + j * cw + cw / 2, 244, label, 12, color, 760, "middle"))
    out.append(f'<text x="68" y="420" font-size="10.5" fill="{RUST}" font-weight="750" text-anchor="middle" letter-spacing="0.7" transform="rotate(-90 68 420)">EMERGENCE INTENSITY (EI)</text>')
    for i, row in enumerate(matrix):
        yy = y0 + i * rh
        out.append(t(146, yy + 62, row_names[i], 12, INK, 750, "end"))
        for j, (count, pct) in enumerate(row):
            label, fill, color = columns[j]
            x = x0 + j * cw
            highlight = i == 2 and j == 2
            out += [box(x + 5, yy + 5, cw - 10, rh - 10, fill, RUST if highlight else "#DED8CF", 11, 3 if highlight else 1),
                    t(x + cw / 2, yy + 48, count, 30, INK, 790, "middle"),
                    t(x + cw / 2, yy + 78, f"{pct}% of row", 13, color, 700, "middle")]
            if highlight:
                out.append(t(x + cw / 2, yy + 96, "z = +2.7", 10, RUST, 700, "middle"))
    out += [box(616, 212, 232, 382, "#F3E8DA", "#E2D4C3", 15),
            t(640, 245, "THE CONCENTRATION", 11, RUST, 760, spacing=0.9),
            t(640, 330, "82%", 58, RUST, 800),
            *wrap_text(640, 370, ["of all absent", "designer attribution", "occurs in High-EI", "papers"], 17, INK, 700, 25),
            line(640, 478, 824, 478, "#D7C2A8"),
            t(640, 522, "14 of 17", 28, RUST, 790),
            t(640, 550, "absent-DV papers", 12, MUTED, 550),
            t(640, 576, "are High EI", 12, MUTED, 550)]
    out += [box(52, 630, 796, 166, "#F7F5EF", "#E2DDD4", 14),
            t(76, 660, "THRESHOLD, NOT GRADIENT", 12, RUST, 760, spacing=1.0),
            t(76, 708, "χ² = 16.62", 23, INK, 780),
            t(262, 708, "p = .002", 23, INK, 780),
            t(407, 708, "V = .242", 23, INK, 780),
            t(558, 708, "r = −.141", 23, INK, 780),
            t(76, 742, "Significant categorical association", 12, TEAL, 650),
            t(558, 742, "Ordinal correlation is not (p = .094)", 12, MUTED, 650),
            t(76, 774, "High EI is the regime where absent designer attribution departs sharply from expectation.", 12.5, RUST, 680)]
    out += footer("Data: 142 LLM social simulation papers; cells show counts and row percentages.")
    return out


def mechanism_card():
    out = shell(
        "Emergence hides authorship. UDOS restores it upstream.",
        "Shift accountability from downstream outputs to the design of social architecture.",
        "03 · MECHANISM + SOLUTION",
        "A mirrored schematic contrasts the Alibi Function, which renders the designer invisible, with UDOS, which creates an upstream auditable record.",
    )
    out += [box(64, 164, 344, 600, "#FBF4F1", "#DDBDB5", 16, 1.5),
            box(492, 164, 344, 600, "#F1F7F5", "#BDD4CF", 16, 1.5),
            t(236, 202, "THE ALIBI FUNCTION", 13, RUST, 760, "middle", 1.0),
            t(664, 202, "UDOS", 13, TEAL, 760, "middle", 1.0),
            line(64, 220, 408, 220, "#DDBDB5"), line(492, 220, 836, 220, "#BDD4CF")]
    # Left: one narrative activates three parallel, mutually reinforcing mechanisms.
    out += [box(94, 246, 284, 62, ORANGE_L, ORANGE, 11, 1.5),
            t(236, 273, "EMERGENCE NARRATIVE", 13, INK, 760, "middle"),
            t(236, 294, "social order appears self-organized", 10.5, MUTED, 500, "middle"),
            arrow(236, 308, 236, 340, ORANGE, 1.8),
            t(236, 360, "THREE REINFORCING MECHANISMS", 10.5, RUST, 750, "middle", 0.7)]
    mechanism_rows = ["Epistemic laundering", "Accountability displacement", "Legitimacy extraction"]
    for i, label in enumerate(mechanism_rows):
        yy = 378 + i * 52
        out += [box(104, yy, 264, 40, "#F7EAE7", "#DFC0B8", 9),
                t(236, yy + 26, label, 12, INK, 650, "middle")]
    out += [arrow(236, 522, 236, 552, RUST, 1.8), box(94, 552, 284, 78, RUST_L, RUST, 11, 2),
            t(236, 581, "ALIBI EFFECT", 12, RUST, 780, "middle"),
            t(236, 611, "Designer: Invisible", 18, INK, 760, "middle"),
            line(112, 654, 360, 654, "#D4B8B0", 1, "4 5"),
            t(236, 680, "Authored procedural architecture", 12, MUTED, 650, "middle"),
            t(236, 703, "topology · actions · sanctions · beneficiary", 10.5, MUTED, 500, "middle"),
            t(236, 736, "Outputs travel; authorship does not.", 11.5, RUST, 650, "middle")]
    # Center: a clear horizontal conceptual shift, with no overlapping badge.
    out += [t(450, 392, "SHIFT THE", 10.5, ORANGE, 760, "middle", 0.7),
            t(450, 411, "REGULATORY", 10.5, ORANGE, 760, "middle", 0.7),
            t(450, 430, "OBJECT", 10.5, ORANGE, 760, "middle", 0.7),
            arrow(420, 454, 480, 454, ORANGE, 2),
            t(450, 478, "model-level", 10, MUTED, 600, "middle"),
            t(450, 496, "architecture-level", 10, TEAL, 700, "middle")]
    # Right: an upstream disclosure chain creates an auditable record.
    out += [box(522, 246, 284, 52, TEAL_L, TEAL, 11, 1.5),
            t(664, 278, "ARCHITECTURE AUTHOR", 13, INK, 760, "middle"),
            arrow(664, 298, 664, 326, TEAL, 1.8),
            box(522, 326, 284, 158, "#EAF2EF", TEAL, 11, 2),
            t(664, 354, "FOUR UPSTREAM DISCLOSURES", 12, TEAL, 780, "middle")]
    requirements = ["R1  Interaction topology", "R2  Action grammar", "R3  Sanction architecture", "R4  Beneficiary structure"]
    out += wrap_text(548, 382, requirements, 11.5, INK, 600, 23)
    out += [t(536, 506, "verification threshold", 9.5, MUTED, 650),
            t(792, 506, "anti-box-ticking", 9.5, MUTED, 650, "end"),
            arrow(664, 484, 664, 532, TEAL, 1.8),
            box(522, 532, 284, 54, "#F8FAF8", "#C9D6D2", 10),
            t(664, 565, "INDEPENDENT OVERSIGHT", 12, INK, 740, "middle"),
            arrow(664, 586, 664, 614, TEAL, 1.8),
            box(522, 614, 284, 58, "#F8FAF8", "#C9D6D2", 10),
            t(664, 640, "AUDITABLE RECORD", 12, INK, 740, "middle"),
            t(664, 659, "audit · contestability · liability", 10, MUTED, 500, "middle"),
            arrow(664, 672, 664, 700, TEAL, 1.8),
            box(522, 700, 284, 46, TEAL_L, TEAL, 10, 2),
            t(664, 729, "Designer: Named & Accountable", 13, TEAL, 780, "middle")]
    out += footer("Framework: the Alibi Function and Upstream Disclosure Obligations for Agent Societies (UDOS).")
    return out


def write_svg(name, elements):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text("\n".join(elements) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--png", action="store_true", help="also export 1800 × 1800 PNG files (requires CairoSVG)")
    args = parser.parse_args()
    write_svg("01_pain_point.svg", pain_card())
    write_svg("02_ei_dv_audit.svg", audit_card())
    write_svg("03_mechanism_udos.svg", mechanism_card())
    if args.png:
        try:
            import cairosvg
        except ImportError as exc:
            raise SystemExit("PNG export requires CairoSVG: python3 -m pip install cairosvg") from exc
        for svg in OUT.glob("*.svg"):
            cairosvg.svg2png(url=str(svg), write_to=str(svg.with_suffix(".png")), output_width=1800, output_height=1800)


if __name__ == "__main__":
    main()
