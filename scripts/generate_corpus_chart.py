#!/usr/bin/env python3
"""Render the README corpus chart from the recorded coding data (matplotlib).

Run from any directory. --preview-dir exports 350/700/1050 px QA views.
Publication groups preserve the repository's existing venue-based coding;
this script does not independently verify publication or peer-review status.
"""

import argparse
from collections import Counter
from html import escape
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
INK, MUTED, GRID = '#17252B', '#47585E', '#DDE4E5'
PEER, PREPRINT = '#24666C', '#C85B37'


def load_counts():
    records = json.loads((ROOT / 'data/stream1b_systematic_coding/coding_data_142.json').read_text())
    counts = Counter()
    omitted = 0
    for row in records:
        year = str(row.get('Year', '')).strip()
        if not year.isdigit():
            omitted += 1
            continue
        venue = str(row.get('Venue', '')).strip()
        group = 'preprint' if venue in {'arXiv', 'arXiv.org', ''} else 'peer'
        counts[int(year), group] += 1
    years = sorted({year for year, _ in counts})
    return records, years, counts, omitted


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--preview-dir', type=Path)
    parser.add_argument('--lang', choices=('en', 'zh'), default='en')
    args = parser.parse_args()
    zh = args.lang == 'zh'
    records, years, counts, omitted = load_counts()
    if len(years) != 4:
        raise ValueError('This four-year layout needs adjustment for the updated corpus.')
    totals = [counts[y, 'peer'] + counts[y, 'preprint'] for y in years]
    peer = sum(counts[y, 'peer'] for y in years)
    preprint = sum(counts[y, 'preprint'] for y in years)
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'none',
                         'svg.hashsalt': 'simulation-as-alibi-corpus',
                         'text.color': INK})
    if zh:
        for family in ('Heiti SC', 'Noto Sans CJK SC', 'Microsoft YaHei', 'SimHei'):
            try:
                font_manager.findfont(family, fallback_to_default=False)
                break
            except ValueError:
                continue
        else:
            raise RuntimeError('Chinese export requires Heiti SC, Noto Sans CJK SC, Microsoft YaHei or SimHei.')
        plt.rcParams.update({'font.family': family, 'svg.fonttype': 'path'})
    title = '新增研究以预印本为主' if zh else 'Growth led by preprints'
    fig = plt.figure(figsize=(7, 7), facecolor='white')

    def text(x, y, s, size=16, color=INK, weight='normal', **kw):
        return fig.text(x, y, s, fontsize=size, color=color, weight=weight, **kw)

    text(.07, .936, '研究样本概览' if zh else 'THE RESEARCH CORPUS', 13, PEER, 'bold')
    text(.07, .855, title, 25, INK, 'bold')
    text(.07, .806, 'LLM 社会模拟 · 各年收录论文数量' if zh else 'LLM social simulation · papers by year', 15, MUTED)
    for x, color, label in [(.07, PEER, f'{peer} 篇经同行评审' if zh else f'{peer} peer-reviewed'), (.52, PREPRINT, f'{preprint} 篇预印本' if zh else f'{preprint} preprints')]:
        fig.add_artist(Rectangle((x, .741), .023, .023, transform=fig.transFigure,
                                 facecolor=color, edgecolor='none'))
        text(x + .035, .742, label, 16, weight='bold')

    ax = fig.add_axes([.205, .24, .68, .405])
    scale_max = ((max(totals) + 19) // 20) * 20
    ax.set_xlim(0, scale_max)
    ax.set_ylim(-.4, 3.8)
    ax.set_yticks([])
    ax.set_xticks(range(0, scale_max + 1, 20))
    ax.tick_params(axis='x', colors=MUTED, labelsize=13, length=0, pad=8)
    ax.set_axisbelow(True)
    ax.grid(axis='x', color=GRID, linewidth=.7)
    for spine in ax.spines.values():
        spine.set_visible(False)
    for i, (year, total) in enumerate(zip(years, totals)):
        yy = 3.25 - i
        a, b = counts[year, 'peer'], counts[year, 'preprint']
        ax.barh(yy, a, height=.27, color=PEER)
        ax.barh(yy, b, left=a, height=.27, color=PREPRINT)
        ax.text(-.07, yy, str(year), transform=ax.get_yaxis_transform(),
                ha='right', va='center', fontsize=17, weight='bold', color=INK)
        ax.text(total + 1.5, yy, str(total), va='center', fontsize=17,
                weight='bold', clip_on=False, color=INK)
        ax.text(0, yy - .40, f'同行评审 {a} 篇 + 预印本 {b} 篇' if zh else f'{a} peer-reviewed + {b} preprints',
                fontsize=16, color=MUTED, va='center')
    text(.205, .165, '论文数量（篇）' if zh else 'Number of papers', 13, MUTED)
    fig.add_artist(plt.Line2D([.07, .94], [.133, .133], transform=fig.transFigure,
                              color=GRID, linewidth=1))
    text(.07, .098, f'共 {len(records)} 篇；{omitted} 篇缺少年份，未纳入图中。' if zh else f'{len(records)} papers; {omitted} without a year omitted.', 14, MUTED)
    text(.07, .058, '仅反映本文收录样本，不代表全领域总量。' if zh else 'Corpus snapshot, not a full-field census.', 14, MUTED)
    text(.07, .018, 'Tang & Lin · Simulation as Alibi · AIES 2026', 12, MUTED)

    target = ROOT / ('docs/corpus_by_year_zh' if zh else 'docs/corpus_by_year')
    description = (f'Corpus snapshot with {len(records)} papers, {omitted} missing years excluded. '
                   f'Publication groups follow recorded venue coding. ' + '; '.join(
                       f'{year}: {counts[year, "peer"]} peer-reviewed, '
                       f'{counts[year, "preprint"]} preprints, total {total}'
                       for year, total in zip(years, totals)))
    if zh:
        description = (f'本文收录 {len(records)} 篇论文，其中 {omitted} 篇缺少年份，未纳入图中。分类沿用仓库的发表渠道编码。' + '；'.join(
            f'{year} 年：同行评审 {counts[year, "peer"]} 篇，预印本 {counts[year, "preprint"]} 篇，共 {total} 篇'
            for year, total in zip(years, totals)))
    fig.savefig(target.with_suffix('.svg'), metadata={'Date': None, 'Description': description})
    svg_path = target.with_suffix('.svg')
    svg = svg_path.read_text()
    # Keep both SVGs scalable and accessible; Chinese glyphs use portable outlines.
    svg = svg.replace('<svg ', '<svg role="img" aria-labelledby="chart-title chart-desc" ', 1)
    start = svg.index('>', svg.index('<svg ')) + 1
    svg = (svg[:start] + f'\n<title id="chart-title">{escape(title)}</title>'
           + f'\n<desc id="chart-desc">{escape(description)}</desc>' + svg[start:])
    svg_path.write_text("\n".join(line.rstrip() for line in svg.splitlines()) + "\n")
    fig.savefig(target.with_suffix('.png'), dpi=200, metadata={'Description': description})
    if args.preview_dir:
        args.preview_dir.mkdir(parents=True, exist_ok=True)
        for pixels in (350, 700, 1050):
            fig.savefig(args.preview_dir / f'corpus-{args.lang}-{pixels}.png', dpi=pixels / 7)
    print(description)
    plt.close(fig)


if __name__ == '__main__':
    main()
