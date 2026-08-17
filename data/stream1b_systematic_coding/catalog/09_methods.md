# Simulation Methods & Platforms

> **Tang, S., & Lin, Z. (2026).** *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents.* Ninth AAAI/ACM Conference on Artificial Intelligence, Ethics and Society (AIES-26), camera-ready. Corresponding author: jamietang@ruc.edu.cn.

*Simulation frameworks, benchmarks, and methodological contributions*

**8 papers**

---

## Field overview

The methods category is where the designer is most legible, because the design itself is the object of study. The papers divide into two orientations. The first operationalizes theory and builds simulation infrastructure: Putnam's social capital is rendered as SOCASIM's micro-level causal chains of trust accumulation; SALM delivers a long-horizon social network simulator with hierarchical prompting and attention-based memory; online firestorms and SAPIENT's corporate-reputation monitoring model crisis and reputational dynamics; a stratified-polyamory framework pushes the approach toward social-reproductive policy questions.

The second orientation maps the design space directly. The *Silicon Society Cookbook* and the *Epi-LLM* framework systematically vary the base model and network geometry and conclude that the choice of base model — not any free parameter of the agents — is the dominant determinant of simulation outcome, with "architecture shap[ing] emergent population-level behaviour." *Socially-Weighted Alignment* makes the same point in game-theoretic form: a designer-chosen social weight induces a phase transition from congestion to stable operation near capacity, a threshold the paper derives analytically. These are papers whose central result is a design parameter, stated as such.

The audit profile confirms the inversion: 6 of 8 papers are Low-EI and 5 of 8 are DV=Full. Emergence claims are modest, and the designer is the causal subject of the explanation sentence. This category is the field's own counterpoint to the alibi — a standing demonstration that the architecture can be named, parameterized, and held to account. It is, in effect, the template for the kind of procedural disclosure the paper argues should become standard across the categories that currently do not practice it.

## Coding dimensions

- **EI — Emergence intensity** (`Low` / `Medium` / `High`, coded 1/2/3): how strongly, and with how little qualification, a paper asserts that behavior arises spontaneously. *High* asserts emergence as an established fact ("norms spontaneously emerged"); *Medium* presents it as an interpretive finding with hedging ("our results suggest the emergence of…"); *Low* mentions emergence only as a secondary observation.
- **DV — Designer visibility** (`Absent` / `Partial` / `Full`, coded 1/2/3): how explicitly a paper attributes the interaction architecture to identifiable design choices, anchored on the emergence explanation sentence. *Full* names a design choice as the causal subject ("removing memory prevents the emergence of stable cooperation"); *Partial* discloses the architecture in the methods but the explanation sentence does not return to the designer; *Absent* narrates emergence as spontaneous, self-organized, or population-level ("norms emerged naturally from interactions"). Risk, governance, and ethical discussions do not count as evidence.
- **Designer in explanation sentence** (`Yes` / `No`): whether the designer or a design choice appears in the emergence explanation sentence as a causal subject.
- **DP — Deployment proximity** (`1` = research only, `2` = deployment implied): whether emergence is discussed only in a research context, or in a deployment/policy context (commercial applications, governance recommendations, policy citations).
- **RT — Regulatory translatability** (`1` = Low, `2` = Medium, `3` = High): how readily a paper's description of emergent behavior translates into governance obligations. High is directly translatable; Medium is partially translatable but missing key information; Low is too abstract to yield concrete governance requirements.

The **emergence explanation sentence** is the sentence in which a paper explains *why* an emergent phenomenon occurs (typically Results/Discussion); DV and Designer-in-sentence codes are anchored on it. EI and DV are coded independently on distinct criteria — EI from the assertion of spontaneity, DV from the attribution of authorship — so a paper may assert strong emergence while still crediting specific design choices.

---

## From Blueprint to Reality: Modeling and Applying Putnam's Social Capital Theory with LLM-based Multi-agent Simulations [[arXiv](https://dl.acm.org/doi/10.1145/3758871.3758931)]

*arXiv · 2026 · Paper P018*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "SOCASIM uses LLM agents to reveal micro-level causal chains of how trust accumulates, norms are internalized, and decision contradictions emerge"

---

## Large Language Model-Driven Multi-Agent Simulation of Online Firestorms [[arXiv](https://arxiv.org/abs/2408.10946)]

*Applied Sciences · 2026 · Paper P062*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** While previous chapters focused on recommendation systems (RSs) based on standardized, non-verbal user feedback such as purchases, views, and clicks -- the advent of LLMs has unlocked the use of natural language (NL) interactions for recommendation. This chapter discusses how LLMs' abilities for general NL reasoning present novel opportunities to build highly personalized RSs -- which can effectively connect nuanced and diverse user preferences to items, potentially via interactive dialogues. To begin this discussion, we first present a taxonomy of the key data sources for language-driven recommendation, covering item descriptions, user-system interactions, and user profiles. We then proceed to fundamental techniques for LLM recommendation, reviewing the use of encoder-only and autoregressive LLM recommendation in both tuned and untuned settings. Afterwards, we move to multi-module recommendation architectures in which LLMs interact with components such as retrievers and RSs in multi-stage pipelines. This brings us to architectures for conversational recommender systems (CRSs), in which LLMs facilitate multi-turn dialogues where each turn presents an opportunity not only to make recommendations, but also to engage with the user in interactive preference elicitation, critiquing, and question-answering.

**Emergence explanation sentence.** "online firestorms, where crisis impact emerges from the coupling between what users express and how participation expands over time."

---

## SALM: A Multi-Agent Framework for Language Model-Driven Social Network Simulation [[arXiv](https://arxiv.org/abs/2505.09081)]

*arXiv.org · 2025 · Paper P120*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Contemporary approaches to agent-based modeling (ABM) of social systems have traditionally emphasized rule-based behaviors, limiting their ability to capture nuanced dynamics by moving beyond predefined rules and leveraging contextual understanding from LMs of human social interaction. This paper presents SALM (Social Agent LM Framework), a novel approach for integrating language models (LMs) into social network simulation that achieves unprecedented temporal stability in multi-agent scenarios. Our primary contributions include: (1) a hierarchical prompting architecture enabling stable simulation beyond 4,000 timesteps while reducing token usage by 73%, (2) an attention-based memory system achieving 80% cache hit rates (95% CI [78%, 82%]) with sub-linear memory growth of 9.5%, and (3) formal bounds on personality stability. Through extensive validation against SNAP ego networks, we demonstrate the first LLM-based framework capable of modeling long-term social phenomena while maintaining empirically validated behavioral fidelity.

**Emergence explanation sentence.** "Our framework demonstrates unprecedented capabilities in long-term social simulation through its innovative memory-centric architecture."

---

## SAPIENT: A Multi-Agent Framework for Corporate Reputation Intelligence Through Sentinel Monitoring and LLM-Based Synthetic Population Simulation [[arXiv](https://arxiv.org/abs/2607.14485)]

*Syst. · 2026 · Paper P128*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning, memory retrieval, reflection, and action selection. However, fine-grained human annotations of these intermediate steps remain scarce, and existing agents are not grounded in human preferences over such intermediate decisions. To address this gap, we introduce \method, an interactive simulation interface that enables us to collect step-level human preference supervision over agent decision trajectories, leading to a dataset of 57K fine-grained annotations. We conduct step-level preference learning on open-weight language models using supervised finetuning and direct preference optimization on this data, consistently improving simulation fidelity, coordination, and interaction quality, and inducing more socially effective agent behavior. Our results show that step-level human supervision is an effective training signal for improving both local decision quality and long-horizon agent behavior.

**Emergence explanation sentence.** "Signal conditioning improved simulation specificity (p=0.012)... credibility was sensitive to prompt wording"

---

## AI-Driven Multi-Agent Simulation of Stratified Polyamory Systems: A Computational Framework for Optimizing Social Reproductive Efficiency [[arXiv](https://arxiv.org/abs/2607.11895)]

*arXiv.org · 2026 · Paper P129*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** AI scientist systems are beginning to automate parts of scientific research, but social science poses a distinct challenge: its objects of inquiry are not merely datasets or laboratory protocols, but integrated social processes involving situated participants, interaction contexts, interventions, and outcomes. Yet a critical link is missing: existing systems either assist isolated research tasks or simulate agents as experimental subjects, leaving the research workflow and simulated society decoupled. Here we introduce AgentSociety 2, an Integrated Research Environment for executable social science. It couples two roles of LLM agents in the same runtime: AI social scientists that coordinate literature grounding, hypothesis generation, experiment design, simulation execution, result interpretation, and manuscript drafting; and silicon participants that generate behavioral responses within configurable social environments. This dual-role design turns hypotheses into auditable agent behaviors, environment rules, interventions, and measurements, thereby supporting an end-to-end workflow. Across seven illustrative studies spanning micro-level social-science laboratory experiments, meso-level dynamics in social media, and macro-level urban scenarios, we demonstrate its capacity to support diverse disciplinary questions, reproduce major qualitative patterns from prior studies, identify informative deviations, and enable large-scale simulations through optimized agent-environment interactions. By preserving human researchers' high-level agency while delegating procedural orchestration to agentic systems, it provides a human-in-the-loop and controllable infrastructure for next-generation computational social science, with broader applications in scalable computational social experimentation and AI-enabled social governance platforms.

**Emergence explanation sentence.** "the framework's viability in addressing the dual crisis of female motherhood penalties and male sexlessness, while offering a non-violent mechanism for wealth dispersion"

---

## Socially-Weighted Alignment: A Game-Theoretic Framework for Multi-Agent LLM Systems [[arXiv](https://arxiv.org/abs/2602.09877)]

*arXiv.org · 2026 · Paper P130*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** The emergence of multi-agent systems built from large language models (LLMs) offers a promising paradigm for scalable collective intelligence and self-evolution. Ideally, such systems would achieve continuous self-improvement in a fully closed loop while maintaining robust safety alignment--a combination we term the self-evolution trilemma. However, we demonstrate both theoretically and empirically that an agent society satisfying continuous self-evolution, complete isolation, and safety invariance is impossible. Drawing on an information-theoretic framework, we formalize safety as the divergence degree from anthropic value distributions. We theoretically demonstrate that isolated self-evolution induces statistical blind spots, leading to the irreversible degradation of the system's safety alignment. Empirical and qualitative results from an open-ended agent community (Moltbook) and two closed self-evolving systems reveal phenomena that align with our theoretical prediction of inevitable safety erosion. We further propose several solution directions to alleviate the identified safety concern. Our work establishes a fundamental limit on the self-evolving AI societies and shifts the discourse from symptom-driven safety patches to a principled understanding of intrinsic dynamical risks, highlighting the need for external oversight or novel safety-preserving mechanisms.

**Emergence explanation sentence.** "SWA induces a critical threshold λ* above which agents no longer have marginal incentive to increase demand under overload, yielding a phase transition from persistent congestion to stable operation near capacity."

---

## The Epi-LLM Framework: probing LLM behavioral priors through epidemiological agent-based models [[arXiv](https://arxiv.org/abs/2605.00197)]

*— · 2026 · Paper P133*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Studies attempting to simulate human behavior with $\textit{Silicon Societies}$ grow in numbers while LLM-only social networks have started appearing outside of controlled settings. However, the design space of these networks remains under-studied, which contributes to a gap in validating model realism. To enable future works to make more informed design decisions, we perform a systematic analysis of the consequences and interactions of key design choices in simulated social networks, including the choice of base model used to model individual agents, and how they are connected to each other. Using surveys as a proxy for agent opinions, our findings suggest that the geometry of the design space is non-trivial, with some parameters behaving in additive ways while others display more complex interactions. In particular, the choice of the base LLM is the most important variable impacting the simulation outcomes.

**Emergence explanation sentence.** "architecture shapes emergent population-level behaviour — with implications for the design of synthetic societies."

---

## The $\textit{Silicon Society}$ Cookbook: Design Space of LLM-based Social Simulations [[arXiv](https://arxiv.org/abs/2605.00197)]

*arXiv · 2026 · Paper P142*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Studies attempting to simulate human behavior with $\textit{Silicon Societies}$ grow in numbers while LLM-only social networks have started appearing outside of controlled settings. However, the design space of these networks remains under-studied, which contributes to a gap in validating model realism. To enable future works to make more informed design decisions, we perform a systematic analysis of the consequences and interactions of key design choices in simulated social networks, including the choice of base model used to model individual agents, and how they are connected to each other. Using surveys as a proxy for agent opinions, our findings suggest that the geometry of the design space is non-trivial, with some parameters behaving in additive ways while others display more complex interactions. In particular, the choice of the base LLM is the most important variable impacting the simulation outcomes.

**Emergence explanation sentence.** "simulation behavior cannot be...model-dependent and scale-dependent...The specific way in which this is done depends on the simulation parameters."

---
