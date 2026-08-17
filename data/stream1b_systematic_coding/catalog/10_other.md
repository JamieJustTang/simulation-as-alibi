# Other Emergent Phenomena

> **Tang, S., & Lin, Z. (2026).** *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents.* Ninth AAAI/ACM Conference on Artificial Intelligence, Ethics and Society (AIES-26), camera-ready. Corresponding author: jamietang@ruc.edu.cn.

*Additional emergent phenomena and safety-critical dynamics*

**8 papers**

---

## Field overview

The residual category gathers safety- and structure-critical dynamics that did not fit the primary taxonomies. *The Devil Behind Moltbook* claims safety constraints "inevitably degrade" in self-evolving societies, formalizing safety erosion as a divergence from anthropic value distributions; *Do Agent Societies Develop Intellectual Elites?* uncovers power-law concentration via an integration bottleneck, in which coordination expands with scale while consolidation does not; *SIGN* shows that a fixed schema steers convention formation to markedly higher agreement; *The Ratchet Effect in Silico* identifies peer verification as the operator of cumulative intelligence. *Learning to Make Friends* and *Democracy-in-Silico* study coached social ties and constitutional-institutional design respectively — the latter arguing that a Constitutional-AI charter plus mediated deliberation acts as "a powerful alignment force." *Games Agents Play* reads LLM behavior through transactional analysis and level-k cognitive theory.

The audit is mostly designer-visible (5 of 8 DV=Full) despite high emergence intensity (5 of 8 High-EI): the category's strong claims are typically backed by named mechanisms — a bottleneck, a schema, a verification operator, an institutional charter. The instructive outlier is *The Devil Behind Moltbook*: its "inevitable" and "irreversible" degradation framing is a naturalization claim of the strongest kind, one that performs institutional work, since a decay narrated as system-inherent is precisely a decay for which no designer and no design intervention can be held responsible. The contrast inside a single small category — safety decay narrated as fate, concentration narrated as mechanism — distills the paper's argument.

## Coding dimensions

- **EI — Emergence intensity** (`Low` / `Medium` / `High`, coded 1/2/3): how strongly, and with how little qualification, a paper asserts that behavior arises spontaneously. *High* asserts emergence as an established fact ("norms spontaneously emerged"); *Medium* presents it as an interpretive finding with hedging ("our results suggest the emergence of…"); *Low* mentions emergence only as a secondary observation.
- **DV — Designer visibility** (`Absent` / `Partial` / `Full`, coded 1/2/3): how explicitly a paper attributes the interaction architecture to identifiable design choices, anchored on the emergence explanation sentence. *Full* names a design choice as the causal subject ("removing memory prevents the emergence of stable cooperation"); *Partial* discloses the architecture in the methods but the explanation sentence does not return to the designer; *Absent* narrates emergence as spontaneous, self-organized, or population-level ("norms emerged naturally from interactions"). Risk, governance, and ethical discussions do not count as evidence.
- **Designer in explanation sentence** (`Yes` / `No`): whether the designer or a design choice appears in the emergence explanation sentence as a causal subject.
- **DP — Deployment proximity** (`1` = research only, `2` = deployment implied): whether emergence is discussed only in a research context, or in a deployment/policy context (commercial applications, governance recommendations, policy citations).
- **RT — Regulatory translatability** (`1` = Low, `2` = Medium, `3` = High): how readily a paper's description of emergent behavior translates into governance obligations. High is directly translatable; Medium is partially translatable but missing key information; Low is too abstract to yield concrete governance requirements.

The **emergence explanation sentence** is the sentence in which a paper explains *why* an emergent phenomenon occurs (typically Results/Discussion); DV and Designer-in-sentence codes are anchored on it. EI and DV are coded independently on distinct criteria — EI from the assertion of spontaneity, DV from the attribution of authorship — so a paper may assert strong emergence while still crediting specific design choices.

---

## The Devil Behind Moltbook: Anthropic Safety is Always Vanishing in Self-Evolving AI Societies

*arXiv · 2026 · Paper P013*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "the mutual information associated with safety constraints inevitably degrades—resulting in an irreversible deterioration of system safety."

---

## Do Agent Societies Develop Intellectual Elites? The Hidden Power Laws of Collective Cognition in LLM Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2604.02674)]

*arXiv · 2026 · Paper P017*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Large Language Model (LLM) multi-agent systems are increasingly deployed as interacting agent societies, yet scaling these systems often yields diminishing or unstable returns, the causes of which remain poorly understood. We present the first large-scale empirical study of coordination dynamics in LLM-based multi-agent systems, introducing an atomic event-level formulation that reconstructs reasoning as cascades of coordination. Analyzing over 1.5 Million interactions across tasks, topologies, and scales, we uncover three coupled laws: coordination follows heavy-tailed cascades, concentrates via preferential attachment into intellectual elites, and produces increasingly frequent extreme events as system size grows. We show that these effects are coupled through a single structural mechanism: an integration bottleneck, in which coordination expansion scales with system size while consolidation does not, producing large but weakly integrated reasoning processes. To test this mechanism, we introduce Deficit-Triggered Integration (DTI), which selectively increases integration under imbalance. DTI improves performance precisely where coordination fails, without suppressing large-scale reasoning. Together, our results establish quantitative laws of collective cognition and identify coordination structure as a fundamental, previously unmeasured axis for understanding and improving scalable multi-agent intelligence.

**Emergence explanation sentence.** "these effects are coupled through a single structural mechanism: an integration bottleneck, in which coordination expansion scales with system size while consolidation does not"

---

## Social Networks of LLM Agents [[arXiv](https://arxiv.org/abs/2607.03695)]

*arXiv · 2026 · Paper P038*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large language model (LLM) agents are increasingly deployed in interacting populations, raising the question of what such populations come to believe collectively. Whether a population aggregates genuine knowledge or collapses into a false consensus directly affects how much such systems can be trusted. Classical social-network models assume that the network itself determines how beliefs combine. This assumption breaks down for LLM agents, whose limited attention takes in only part of what they are exposed to, so these models overstate how much information a population actually pools and cannot tell genuine consensus from herding. We introduce SNLA, a framework that models how much each agent actually influences others, rather than merely how the network connects them. This influence depends on each agent's position in the network and on how sharply attention focuses. Theoretically, we show on a tractable proxy that narrow attention causes herding, where the effective sample size stays bounded regardless of population size, while wide attention recovers wisdom-of-crowds behavior only when the exposure graph is undirected and degree-regular. Empirically, a controlled testbed validates these predictions directly, and the herding-wisdom transition reproduces on operator-controlled variants of three multi-agent LLM benchmarks.

**Emergence explanation sentence.** "narrow attention causes herding, where the effective sample size stays bounded regardless of population size, while wide attention recovers wisdom-of-crowds behavior only when the exposure graph is undirected and degree-regular."

---

## SIGN: Schema-Induced Games for Naming [[arXiv](https://arxiv.org/abs/2510.21855)]

*arXiv.org · 2025 · Paper P052*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Real-world AI systems are tackling increasingly complex problems, often through interactions among large language model (LLM) agents. When these agents develop inconsistent conventions, coordination can break down. Applications such as collaborative coding and distributed planning therefore require reliable, consistent communication, and scalability is a central concern as systems grow. We introduce Schema-Induced Games for Naming (SIGN), a naming game that examines how lightweight structure can steer convention formation. We compare schema-induced communication to unconstrained natural language and find faster convergence with up to 5.8x higher agreement. These results suggest that minimal structure can act as a simple control knob for efficient multi-agent coordination, pointing toward broader applications beyond the naming game.

**Emergence explanation sentence.** "adding a fixed schema to LLM agents steers convention formation in a naming game, yielding up to 5.8× greater population agreement. Minimal structural priors thus can shape how conventions emerge."

---

## The Ratchet Effect in Silico: How Interaction Drives Cumulative Intelligence in Large Language Models

*— · 2025 · Paper P055*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "Mechanistic ablations identify peer verification as the main ratchet operator and show that internalization sustains accumulation across rounds."

---

## Learning to Make Friends: Coaching LLM Agents toward Emergent Social Ties [[arXiv](https://arxiv.org/abs/2510.19299)]

*arXiv · 2025 · Paper P069*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Can large language model (LLM) agents reproduce the complex social dynamics that characterize human online behavior -- shaped by homophily, reciprocity, and social validation -- and what memory and learning mechanisms enable such dynamics to emerge? We present a multi-agent LLM simulation framework in which agents repeatedly interact, evaluate one another, and adapt their behavior through in-context learning accelerated by a coaching signal. To model human social behavior, we design behavioral reward functions that capture core drivers of online engagement, including social interaction, information seeking, self-presentation, coordination, and emotional support. These rewards align agent objectives with empirically observed user motivations, enabling the study of how network structures and group formations emerge from individual decision-making. Our experiments show that coached LLM agents develop stable interaction patterns and form emergent social ties, yielding network structures that mirror properties of real online communities. By combining behavioral rewards with in-context adaptation, our framework establishes a principled testbed for investigating collective dynamics in LLM populations and reveals how artificial agents may approximate or diverge from human-like social behavior.

**Emergence explanation sentence.** "friendships and group formations emerge from individual decision-making... We design mechanisms that allow social ties to emerge endogenously from conversations."

---

## Democracy-in-Silico: Institutional Design as Alignment in AI-Governed Polities [[arXiv](https://arxiv.org/abs/2603.20911)]

*arXiv · 2025 · Paper P103*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large language models make agent-based simulation more behaviorally expressive, but they also sharpen a basic methodological tension: fluent, human-like output is not, by itself, evidence for theory. We evaluate what an LLM-driven simulation can credibly support using information engagement on social media as a test case. In a Weibo-like environment, we manipulate information load and descriptive norms, while allowing popularity cues (cumulative likes and Sina Weibo-style cumulative reshares) to evolve endogenously. We then ask whether simulated behavior changes in theoretically interpretable ways under these controlled variations, rather than merely producing plausible-looking traces. Engagement responds systematically to information load and descriptive norms, and sensitivity to popularity cues varies across contexts, indicating conditionality rather than rigid prompt compliance. We discuss methodological implications for simulation-based communication research, including multi-condition stress tests, explicit no-norm baselines because default prompts are not blank controls, and design choices that preserve endogenous feedback loops when studying bandwagon dynamics.

**Emergence explanation sentence.** "These findings strongly suggest that institutional design acts as a powerful alignment force... institutional design, specifically the combination of a Constitutional AI (CAI) charter and a mediated deliberation protocol, serves as a potent alignment mechanism."

---

## Games Agents Play: Towards Transactional Analysis in LLM-based Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2606.27845)]

*Annual Meeting of the Cognitive Science Society · 2025 · Paper P139*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Large Language Models (LLMs) are increasingly used as stand-ins in behavioural games. These stand-ins rely on the assumption that the LLM's distribution of choices meaningfully matches how humans play the same game. This study tests that assumption through two games. The first is a p-beauty contest, and the second one is a public goods game. The study first investigates five local-model settings within the same model family. These settings are varied together in a 360-cell factorial, which balances temperature, scale (0.5-32B), quantisation, instruct vs base, and framing. Each cell's distribution is then compared against whole choice distributions in published human data. Each deployment setting, except for quantisation, governs a different aspect of fidelity. Mechanically, while the dispersion of human players can be somewhat recovered through deployment settings, the strategic process behind it cannot. Through the lens of the level-k cognitive theory, we find that LLMs act as static, category-retrieved level-k players, where k is set by the model scale. The models also do not run within-game belief-updating or backward induction throughout multiple-round horizon settings. While human contributions decayed in the public goods game, LLMs stayed flat or rose at every scale. When the horizon test was administered, LLMs were more cooperative under an indefinite horizon compared to a finite one. However, LLMs ignore their relative round position, so no last-round defection was displayed. This implies that LLMs retrieved levels relative to the horizon category rather than working out iteratively from the specific game setting.

**Emergence explanation sentence.** "The integration of memory, retrieval, and psychological adaptation mechanisms results in behavior that mirrors deepened interactions."

---
