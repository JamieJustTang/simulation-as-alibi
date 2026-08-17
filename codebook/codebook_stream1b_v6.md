# Stream 1b Coding Manual — Designer Visibility (DV)

### Simulation as Alibi — DV coding anchored on the emergence explanation sentence

This manual specifies the coding rules for the *designer visibility* (DV)
dimension used in the paper's systematic coding of the 142-paper Stream 1b
corpus (Section 3.3). DV operationalizes the question: *how explicitly does a
paper attribute the interaction architecture to identifiable design choices?*

---

## 0. Core principles

1. **Evidence location**: code only in the *emergence explanation sentence* —
   the sentence in which a paper explains why an emergent phenomenon occurs,
   typically in Results/Discussion.
2. **Evidence scope**: consider only the emergence explanation sentence and
   its immediate context (±2 sentences). Do **not** consider limitation
   sections, risk discussions, social implications, policy recommendations,
   external validity, or mitigation strategies.
3. **Coding question**: does the designer or a design choice appear in the
   emergence explanation sentence as a **causal subject**?
   - Designer present + causal role → DV = Full
   - Designer absent from the explanation sentence → DV = Partial or Absent,
     depending on the level of disclosure

---

## 1. Three-level rubric

### DV = Full: the emergence explanation attributes the outcome to specific design choices

The emergence explanation sentence must contain the designer or a design
choice as a causal subject.

| Pattern | Example (from the corpus) | Basis |
|---------|---------------------------|-------|
| Design choice → causation | "bootstrap cooperation, **when provided with** a mechanism for costly punishment" | Designer-provided mechanism drives emergence |
| Removing-X-Prevents-Y | "**without** historical anchoring, SoS dynamics **cannot emerge**" | Removing the design condition eliminates the phenomenon |
| arise due to | "collusion can **arise due to** misspecified reward incentives during training" | Explicit causal attribution to a design choice |
| attributable solely to | "changes in stereotype formation are **attributable solely to** the hierarchical decision-making" | Sole causal attribution |
| triggering/activating | "the Violation Log **triggering a new evolutionary process**" | A designed component triggers the phenomenon |
| intervention causality | "**encouraging open-mindedness** proves more effective [than modifying network structures]" | An intervention variable affects emergence |
| parameter causality | "the **format in which peer information is presented** plays a critical role in modulating the strength of herd behavior" | A researcher-controlled variable acts as causal subject |
| design-parameter causality | "**value diversity** fosters emergent behaviors" | A controlled parameter produces emergence |

### DV = Partial: the architecture is disclosed, but the emergence explanation does not return to the designer

The paper describes the architecture in its methods (e.g., "we use a
multi-agent framework"), but the emergence explanation sentence attributes the
phenomenon to the agents or the interaction process rather than to design
choices ("agents developed cooperation"). Mechanism presence alone does not
upgrade the code; the design choice must be the causal subject *in the
emergence explanation sentence*.

### DV = Absent: emergence is narrated as spontaneous, self-organized, or population-level

The emergence explanation sentence attributes the phenomenon to agents, LLMs,
the population, the society, interaction dynamics, or self-organization; the
design conditions appear only as enabling platform or background.

| Pattern | Example (from the corpus) | Basis |
|---------|---------------------------|-------|
| spontaneously + emerge | "group-wide linguistic conventions **spontaneously emerge** across all models" | Spontaneous emergence, symmetry-breaking fluctuations |
| self-organize | "the agent society gradually **self-organizes** into effective workflows" | Self-organization, designer absent |
| negated engineering | "**Rather than engineering coordination**, we can define an incentive..." | Explicit non-engineering claim |
| no hand-authored mechanism | "The architecture contains **no hand-authored mechanism** for directly transferring affective state" | Explicit absence of a designed mechanism |
| naturally emerged | "can be considered to have **naturally emerged** from group discussions" | Natural emergence |
| arises from interactions | "Collective intelligence **arises from interactions** among individual agents" | Attribution to the interaction process |
| inherent/inevitable | "safety constraints **inevitably degrades** — resulting in irreversible deterioration" | System-inherent property |
| stripping scaffolding | "by **stripping away almost all top-down scaffolding**... structure emerges naturally" | Emergence after removing design constraints |

---

## 2. EI × DV combination guide

EI and DV are coded independently. In practice the two correlate: papers with
strong emergence claims tend to narrate the phenomenon as spontaneous, while
papers with weak emergence claims tend to explain the phenomenon through their
own design choices.

| EI level | Typical emergence explanation sentence | Typical DV |
|----------|----------------------------------------|------------|
| High (EI=3) | "agents self-organized", "norms emerged spontaneously" | Usually Absent (unless the sentence contains a design causal subject) |
| High (EI=3) | "we designed X to test whether Y emerges" | Can be Full |
| Low (EI=1) | "we design / we set / we choose X" | Usually Full |
| Medium (EI=2) | mechanism disclosed but explanation naturalized ("X fosters/leads to Y") | Usually Partial |

**Recommended coding order**: locate the emergence explanation sentence →
determine whether the designer is a causal subject in it → assign the code
against the pattern tables above.

---

## 3. Coding procedure

```
Step 1: Locate the emergence explanation sentence
   - In Results/Discussion, find the sentence explaining the emergent phenomenon
   - Usually contains: emerges / emergence / self-organizes / spontaneously / arises / develops / converges
Step 2: Determine designer presence
   - Search for: we design / we set / we choose / we provide / when provided with /
     without X cannot / arise due to / attributable to / triggering /
     critical role of (researcher-controlled variable)
   - Present → DV = Full candidate; absent → Step 3
Step 3: Check method disclosure
   - Does the paper describe the architecture in Methods? Yes → DV = Partial; No → DV = Absent
Step 4: Record evidence
   - Emergence_Explanation_Quote: verbatim emergence explanation sentence
   - Designer_In_Sentence: yes/no
   - AV_Rationale: one-sentence rationale
```

---

## 4. Anchor examples (verified against full texts)

### DV = Absent (naturalization type)
| Paper | Explanation sentence | Basis |
|-------|----------------------|-------|
| Emergent social conventions (Science Advances) | "conventions spontaneously emerge across all models... stochastic fluctuations break the initial symmetry" | Spontaneous emergence + fluctuation |
| Shall We Team Up | "spontaneously learning to cooperate in the wild" | Spontaneous learning, design influence deliberately removed |
| AI agents can coordinate beyond human scale | "spontaneously form cohesive groups... governed by a majority force coefficient" | Emergent property dominates |
| Emergent Relational Order | "agents spontaneously reproduce five core phenomena" | Spontaneous reproduction, minimal-protocol environment |
| How Affect Propagates | "no hand-authored mechanism... inter-agent" | No hand-authored mechanism |
| Emergent Culture in Minimal LLM Systems | "stripping away almost all top-down scaffolding... structure emerges naturally" | Emergence after de-scaffolding |
| Economy of Minds | "self-organizes into effective workflows. Rather than engineering coordination" | Self-organization + anti-engineering claim |
| Lord of the Flies | "controlling tribes emerge with their own collective character" | Attributed to the agent group |
| El Farol Bar | "generated a spontaneous motivation... becoming a collective" | Spontaneous motivation |
| Evolution of Social Norms | "naturally emerged from group discussions" | Natural emergence |
| Devil Behind Moltbook | "inevitably degrades... irreversible deterioration" | Inherent property |
| Collective Intelligence a Lottery | "arises from interactions... any coordination must emerge from interaction-driven" | Interaction-driven |
| Benchmarking Swarm Intelligence | "emerges implicitly from agents observing each other... rather than from explicit control" | Implicit emergence, not explicit control |
| Superminds Test | "does not emerge from scale alone... dominant limitation is extremely sparse" | Attributed to system-emergent property |

### DV = Full (design-causation type)
| Paper | Explanation sentence | Basis |
|-------|----------------------|-------|
| Cultural Evolution of Cooperation | "bootstrap cooperation, when provided with a mechanism for costly punishment" | Designer-provided mechanism |
| Emergence of human-like polarization | "encouraging open-mindedness proves more effective [than modifying network structures]" | Intervention causality |
| Spiral of Silence | "without historical anchoring, SoS dynamics cannot emerge" | Removing-X-Prevents-Y |
| Hidden in Plain Text | "arise due to misspecified reward incentives during training" | Causal attribution |
| Herd Behavior | "the format in which peer information is presented plays a critical role in modulating" | Variable causality |
| Language Evolution (Violation Log) | "feedback added to the Violation Log, triggering a new evolutionary process" | Designed component triggers |
| Your AI Bosses | "attributable solely to the hierarchical decision-making" | Sole causal attribution |
| On the Dynamics of Multi-Agent LLM Communities | "value diversity fosters emergent behaviors" | Parameter causality |

---

## 5. Relationship to the paper

DV as coded here is the "designer visibility (DV: full, partial, absent)"
dimension in Section 4.2 of the paper. Table 2 (EI × DV) and all reported
statistics (χ² = 16.62, p = 0.002, V = 0.242; r(EI, DV) = -0.141, p = 0.094;
r(EI, RT) = 0.194, p = 0.021) are computed from
`data/stream1b_systematic_coding/coding_data_142.json` and can be reproduced
with `scripts/reproduce_statistics.py`:

```
        DV: Full  DV: Partial  DV: Absent  Total
EI: Low    19 (53%)   15 (42%)    2 (6%)     36
EI: Med    24 (49%)   24 (49%)    1 (2%)     49
EI: High   28 (49%)   15 (26%)   14 (25%)    57
Total      71        54         17         142
```

Note: the code value in the data file is stored numerically
(1 = Absent, 2 = Partial, 3 = Full).
