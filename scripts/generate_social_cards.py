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
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(title)}</title>', f'<desc id="desc">{escape(desc)}</desc>',
        box(0, 0, W, H, PAPER, radius=0), box(20, 18, 860, 864, CARD, "#E7E1D7", 18),
        f'<g font-family="{FONT}">',
        t(52, 58, eyebrow, 12, RUST, 700, spacing=1.6),
        t(52, 94, title, 25, INK, 760),
        t(52, 122, subtitle, 14, MUTED, 400),
    ]


def footer(data_note):
    return [line(52, 818, 848, 818, "#E7E1D7"), t(52, 842, data_note, 10.5, MUTED),
            t(52, 864, "Citation: " + CITATION, 10.5, INK, 650), '</g>', '</svg>']


def pain_card():
    out = shell(
        "The rules gain power as their authors disappear",
        "LLM social simulation is moving from market experimentation toward public authority.",
        "01 · THE PAIN POINT",
        "Three domains of outsourcing and a matrix showing the absence of architecture-level disclosure across six governance frameworks.",
    )
    out += [t(52, 157, "RISING POLITICAL-ECONOMIC & GOVERNANCE STAKES", 11, RUST, 700, spacing=1.2),
            arrow(52, 174, 842, 174, RUST, 2)]
    domains = [
        ("COMMERCIAL", "Proprietary", "Academic credibility", "Self-regulation"),
        ("MILITARY", "Classified", "Tactical objectivity", "Security exemption"),
        ("GOVERNMENTAL", "Undocumented", "Policy neutrality", "Technical delegation"),
    ]
    for i, (domain, closure, epistemic, governance) in enumerate(domains):
        x = 52 + i * 270
        out += [box(x, 184, 238, 124, "#FAF7F1", "#E5DED3", 12),
                t(x + 16, 210, domain, 11, RUST, 750, spacing=1.2),
                t(x + 16, 238, closure, 18, INK, 750),
                t(x + 16, 262, epistemic, 12, MUTED),
                t(x + 16, 284, "Governance: " + governance, 11.5, TEAL, 650)]
    out += [t(52, 348, "THE DISCLOSURE GAP", 11, RUST, 700, spacing=1.3),
            t(52, 377, "None of six frameworks explicitly requires procedural authorship disclosure.", 18, INK, 720)]
    frameworks = ["EU AI Act Art. 13", "NIST AI RMF 1.0", "DoD AI Strategy",
                  "White House EO", "EU Emergency Mgmt", "China MOST Guidelines"]
    dims = ["D1", "D2", "D3", "D4"]
    labels = ["Topology", "Actions", "Sanctions", "Beneficiary"]
    gx, gy, row_h, cell_w = 276, 414, 44, 72
    for j, (dim, label) in enumerate(zip(dims, labels)):
        cx = gx + j * cell_w
        out += [t(cx + cell_w / 2, 418, dim, 12, TEAL, 750, "middle"),
                t(cx + cell_w / 2, 436, label, 10, MUTED, 500, "middle")]
    for i, framework in enumerate(frameworks):
        yy = gy + 36 + i * row_h
        out += [t(60, yy + 24, framework, 12, INK, 600)]
        for j in range(4):
            partial = i == 1 and j == 0
            fill = ORANGE_L if partial else RUST_L
            symbol = "PARTIAL" if partial else "×"
            color = ORANGE if partial else RUST
            out += [box(gx + j * cell_w + 5, yy + 5, cell_w - 10, 32, fill, radius=7),
                    t(gx + j * cell_w + cell_w / 2, yy + 27, symbol, 10 if partial else 17, color, 750, "middle")]
    out += [box(590, 470, 244, 218, "#F3E8DA", radius=14),
            t(612, 502, "STRUCTURAL GAP", 11, RUST, 750, spacing=1.3),
            t(612, 554, "0 / 6", 42, INK, 780),
            *wrap_text(612, 582, ["frameworks contain an explicit", "architecture-level procedural", "authorship disclosure mechanism"], 13, MUTED, 500, 20),
            t(612, 665, "The regulatory object is the model—", 11.5, RUST, 650),
            t(612, 683, "not the authored social architecture.", 11.5, RUST, 650)]
    out += footer("Evidence: institutional gap analysis of six frameworks and three cross-domain cases.")
    return out


def audit_card():
    out = shell(
        "Designer erasure concentrates at High EI",
        "The pattern is threshold-like—not a smooth decline in visibility.",
        "02 · THE AUDIT EVIDENCE · n = 142",
        "A three-by-three audit matrix crossing emergence intensity with designer visibility, highlighting High EI and absent designer attribution.",
    )
    out += [t(52, 164, "DESIGNER VISIBILITY (DV)", 11, TEAL, 750, spacing=1.3)]
    cols = [("FULL", TEAL_L, TEAL), ("PARTIAL", ORANGE_L, ORANGE), ("ABSENT", RUST_L, RUST)]
    rows = ["LOW EI", "MEDIUM EI", "HIGH EI"]
    values = [[(19, 53, "+0.2"), (15, 42, "+0.4"), (2, 6, "−1.1")],
              [(24, 49, "−0.1"), (24, 49, "+1.2"), (1, 2, "−2.0")],
              [(28, 49, "−0.1"), (15, 26, "−1.4"), (14, 25, "+2.7")]]
    x0, y0, cw, rh = 178, 202, 160, 132
    for j, (label, _, color) in enumerate(cols):
        out += [t(x0 + j * cw + cw / 2, 188, label, 12, color, 750, "middle")]
    out += [f'<text x="72" y="400" font-size="10.5" fill="{RUST}" font-weight="750" text-anchor="middle" letter-spacing="0.8" transform="rotate(-90 72 400)">EMERGENCE INTENSITY (EI)</text>']
    for i, row in enumerate(rows):
        out += [t(164, y0 + i * rh + 69, row, 12, INK, 750, "end")]
        for j, (count, pct, residual) in enumerate(values[i]):
            _, fill, color = cols[j]
            x, yy = x0 + j * cw, y0 + i * rh
            stroke, sw = (RUST, 3) if (i, j) == (2, 2) else ("#E4DED5", 1)
            out += [box(x + 5, yy + 5, cw - 10, rh - 10, fill, stroke, 12, sw),
                    t(x + cw / 2, yy + 51, count, 30, INK, 780, "middle"),
                    t(x + cw / 2, yy + 78, f"{pct}% of row", 12, color, 700, "middle"),
                    t(x + cw / 2, yy + 101, f"z = {residual}", 11, MUTED, 500, "middle")]
    out += [box(686, 202, 164, 386, "#F3E8DA", radius=14),
            t(706, 230, "THE CONCENTRATION", 10.5, RUST, 750, spacing=1.1),
            t(706, 300, "82%", 48, INK, 790),
            *wrap_text(706, 332, ["of all absent", "designer attribution", "occurs in High-EI", "papers"], 14, MUTED, 550, 22),
            line(706, 434, 828, 434, "#D9C8B3"),
            t(706, 466, "14 of 17", 22, RUST, 760),
            t(706, 490, "absent-DV papers", 12, MUTED, 500),
            t(706, 542, "4.4×", 25, INK, 760),
            t(706, 566, "Low-EI absent rate", 11.5, MUTED, 500)]
    out += [box(52, 630, 798, 142, "#F7F5EF", "#E5DED3", 14),
            t(72, 657, "THRESHOLD, NOT GRADIENT", 11, RUST, 750, spacing=1.2),
            t(72, 696, "χ² = 16.62", 22, INK, 760), t(236, 696, "p = .002", 22, INK, 760),
            t(370, 696, "V = .242", 22, INK, 760), t(510, 696, "r = −.141", 22, INK, 760),
            t(72, 728, "Categorical association is significant", 12, TEAL, 650),
            t(510, 728, "Ordinal correlation is not (p = .094)", 12, MUTED, 650),
            t(72, 754, "High EI is the regime where designer absence sharply departs from expectation (z = +2.7).", 12, RUST, 650)]
    out += footer("Data: systematic coding of 142 LLM social simulation papers; row percentages and standardized residuals shown.")
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
