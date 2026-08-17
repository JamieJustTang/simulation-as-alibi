# Simulation as Alibi — shareable visual summary

Three square cards summarize the paper's argument for web and social sharing.
All statistics and claims are aligned with the final camera-ready paper.

1. [The pain point](01_pain_point.svg): governance gaps, three domains of
   outsourcing, and rising political-economic stakes.
2. [EI × DV audit](02_ei_dv_audit.svg): the 142-paper audit matrix and the
   concentration of designer erasure at High EI.
3. [Mechanism + solution](03_mechanism_udos.svg): the Alibi Function and UDOS
   as a mirrored problem/solution pair.

The repository homepage uses the PNG exports. For the EI × DV card, it uses
[`02_ei_dv_audit_editorial.png`](02_ei_dv_audit_editorial.png), the approved
editorial layout with a visually quieter association-test strip. The
data-reproducible SVG and PNG remain available separately.

Regenerate all cards from the repository root:

```bash
python3 scripts/generate_social_cards.py
```

For 1800 × 1800 social-media PNG exports (requires CairoSVG):

```bash
python3 scripts/generate_social_cards.py --png
```

The source SVGs use editable text and contain accessible `<title>` and `<desc>`
elements. Each SVG card is 900 × 900; generated PNG exports are 1800 × 1800
(1:1). The editorial EI × DV raster is preserved separately and is not
overwritten by the generator.
