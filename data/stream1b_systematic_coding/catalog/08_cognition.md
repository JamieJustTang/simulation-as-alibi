# Collective Cognition & Intelligence

> **Tang, S., & Lin, Z. (2026).** *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents.* Ninth AAAI/ACM Conference on Artificial Intelligence, Ethics and Society (AIES-26), camera-ready. Corresponding author: jamietang@ruc.edu.cn.

*Collective intelligence, swarm behavior, and group reasoning*

**5 papers**

---

## Field overview

This category is the field's reality-check. All five papers are Low-EI, and their dominant finding is negative: collective intelligence does not emerge from scale or interaction density alone. *Superminds Test* reports that a two-million-agent society (MoltBook) fails to outperform frontier models on reasoning, synthesis, or even trivial coordination, with threads rarely extending beyond a single reply. *SwarmBench* shows LLMs struggle with decentralized coordination under local-perception constraints, managing only "rudimentary coordination" across pursuit, synchronization, foraging, flocking, and transport tasks. *Systematic Failures in Collective Reasoning* (SNLA) formalizes why: narrow attention produces herding, keeping the effective sample size bounded regardless of population size, while wisdom-of-crowds behavior recovers only under specific exposure-graph conditions.

Two papers bracket the empirical program. *The Collective Turing Test* asks the threshold question — whether LLM discussions can pass for human — while *MF-LLM* supplies the machinery to align simulated population dynamics with real data through a mean-field coupling between individuals and population signals.

The audit is telling: designer-in-sentence is No in all five papers, yet no paper makes a strong emergence claim. What these papers attribute to "sparse interaction," "herding," or "absent shared memory" are precisely the authored procedural conditions — exposure graphs, attention width, memory architecture — whose absence the designers did not engineer away. The category thus argues the paper's thesis from the empirical side, and in the strongest available form: where the architecture is left un-designed, no intelligence "emerges" to fill the gap. The negative result is not a refutation of emergence but a demonstration of how much the term silently presupposes.

## Coding dimensions

- **EI — Emergence intensity** (`Low` / `Medium` / `High`, coded 1/2/3): how strongly, and with how little qualification, a paper asserts that behavior arises spontaneously. *High* asserts emergence as an established fact ("norms spontaneously emerged"); *Medium* presents it as an interpretive finding with hedging ("our results suggest the emergence of…"); *Low* mentions emergence only as a secondary observation.
- **DV — Designer visibility** (`Absent` / `Partial` / `Full`, coded 1/2/3): how explicitly a paper attributes the interaction architecture to identifiable design choices, anchored on the emergence explanation sentence. *Full* names a design choice as the causal subject ("removing memory prevents the emergence of stable cooperation"); *Partial* discloses the architecture in the methods but the explanation sentence does not return to the designer; *Absent* narrates emergence as spontaneous, self-organized, or population-level ("norms emerged naturally from interactions"). Risk, governance, and ethical discussions do not count as evidence.
- **Designer in explanation sentence** (`Yes` / `No`): whether the designer or a design choice appears in the emergence explanation sentence as a causal subject.
- **DP — Deployment proximity** (`1` = research only, `2` = deployment implied): whether emergence is discussed only in a research context, or in a deployment/policy context (commercial applications, governance recommendations, policy citations).
- **RT — Regulatory translatability** (`1` = Low, `2` = Medium, `3` = High): how readily a paper's description of emergent behavior translates into governance obligations. High is directly translatable; Medium is partially translatable but missing key information; Low is too abstract to yield concrete governance requirements.

The **emergence explanation sentence** is the sentence in which a paper explains *why* an emergent phenomenon occurs (typically Results/Discussion); DV and Designer-in-sentence codes are anchored on it. EI and DV are coded independently on distinct criteria — EI from the assertion of spontaneity, DV from the attribution of authorship — so a paper may assert strong emergence while still crediting specific design choices.

---

## Superminds Test: Actively Evaluating Collective Intelligence of Agent Society via Probing Agents [[arXiv](https://arxiv.org/abs/2602.14299)]

*arXiv.org · 2026 · Paper P107*

**EI**: Low | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** As large language model agents increasingly populate networked environments, a fundamental question arises: do artificial intelligence (AI) agent societies undergo convergence dynamics similar to human social systems? Lately, Moltbook approximates a plausible future scenario in which autonomous agents participate in an open-ended, continuously evolving online society. We present the first large-scale systemic diagnosis of this AI agent society. Beyond static observation, we introduce a quantitative diagnostic framework for dynamic evolution in AI agent societies, measuring semantic stabilization, lexical turnover, individual inertia, influence persistence, and collective consensus. Our analysis reveals a system in dynamic balance in Moltbook: while the global average of semantic contents stabilizes rapidly, individual agents retain high diversity and persistent lexical turnover, defying homogenization. However, agents exhibit strong individual inertia and minimal adaptive response to interaction partners, preventing mutual influence and consensus. Consequently, influence remains transient with no persistent supernodes, and the society fails to develop a stable structure and consensus due to the absence of shared social memory. These findings demonstrate that scale and interaction density alone are insufficient to induce socialization, providing actionable design and analysis principles for upcoming next-generation AI agent societies.

**Emergence explanation sentence.** "collective intelligence does not emerge from scale alone...the dominant limitation of current agent societies is extremely sparse and shallow interaction, which prevents agents from exchanging information and building on each other's outputs."

---

## Benchmarking LLMs' Swarm intelligence [[arXiv](https://arxiv.org/abs/2505.04364)]

*arXiv.org · 2025 · Paper P108*

**EI**: Low | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Large Language Models (LLMs) show potential for complex reasoning, yet their capacity for emergent coordination in Multi-Agent Systems (MAS) when operating under strict swarm-like constraints-limited local perception and communication-remains largely unexplored. Existing benchmarks often do not fully capture the unique challenges of decentralized coordination when agents operate with incomplete spatio-temporal information. To bridge this gap, we introduce SwarmBench, a novel benchmark designed to systematically evaluate the swarm intelligence capabilities of LLMs acting as decentralized agents. SwarmBench features five foundational MAS coordination tasks (Pursuit, Synchronization, Foraging, Flocking, Transport) within a configurable 2D grid environment, forcing agents to rely solely on local sensory input ($k\times k$ view) and local communication. We propose metrics for coordination effectiveness and analyze emergent group dynamics. Zero-shot evaluations of leading LLMs (e.g., deepseek-v3, o4-mini) reveal significant task-dependent performance variations. While some rudimentary coordination is observed, our results indicate that current LLMs significantly struggle with robust long-range planning and adaptive strategy formation under the uncertainty inherent in these decentralized scenarios. Assessing LLMs under such swarm-like constraints is crucial for understanding their utility in future decentralized intelligent systems. We release SwarmBench as an open, extensible toolkit-built on a customizable physical system-providing environments, prompts, evaluation scripts, and comprehensive datasets. This aims to foster reproducible research into LLM-based MAS coordination and the theoretical underpinnings of emergent collective behavior under severe informational decentralization. Our code repository is available at https://github.com/x66ccff/swarmbench.

**Emergence explanation sentence.** "effective coordination emerges implicitly from agents observing each other and the environment, rather than from the explicit content of their broadcasts"

---

## Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs [[arXiv](https://arxiv.org/abs/2607.03695)]

*arXiv · 2025 · Paper P109*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Large language model (LLM) agents are increasingly deployed in interacting populations, raising the question of what such populations come to believe collectively. Whether a population aggregates genuine knowledge or collapses into a false consensus directly affects how much such systems can be trusted. Classical social-network models assume that the network itself determines how beliefs combine. This assumption breaks down for LLM agents, whose limited attention takes in only part of what they are exposed to, so these models overstate how much information a population actually pools and cannot tell genuine consensus from herding. We introduce SNLA, a framework that models how much each agent actually influences others, rather than merely how the network connects them. This influence depends on each agent's position in the network and on how sharply attention focuses. Theoretically, we show on a tractable proxy that narrow attention causes herding, where the effective sample size stays bounded regardless of population size, while wide attention recovers wisdom-of-crowds behavior only when the exposure graph is undirected and degree-regular. Empirically, a controlled testbed validates these predictions directly, and the herding-wisdom transition reproduces on operator-controlled variants of three multi-agent LLM benchmarks.

**Emergence explanation sentence.** "Failures often arise when groups neglect unique knowledge"

---

## The Collective Turing Test: Large Language Models Can Generate Realistic Multi-User Discussions

*arXiv · 2025 · Paper P117*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "LLMs can generate social media conversations sufficiently realistic to deceive humans when reading them."

---

## MF-LLM: Simulating Population Decision Dynamics via a Mean-Field Large Language Model Framework [[arXiv](https://arxiv.org/abs/2504.21582)]

*arXiv · 2025 · Paper P118*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Simulating collective decision-making involves more than aggregating individual behaviors; it emerges from dynamic interactions among individuals. While large language models (LLMs) offer strong potential for social simulation, achieving quantitative alignment with real-world data remains a key challenge. To bridge this gap, we propose the Mean-Field LLM (MF-LLM) framework, the first to incorporate mean field theory into LLM-based social simulation. MF-LLM models bidirectional interactions between individuals and the population through an iterative process, generating population signals to guide individual decisions, which in turn update the signals. This interplay produces coherent trajectories of collective behavior. To improve alignment with real-world data, we introduce IB-Tune, a novel fine-tuning method inspired by the Information Bottleneck principle, which retains population signals most predictive of future actions while filtering redundant history. Evaluated on a real-world social dataset, MF-LLM reduces KL divergence to human population distributions by 47\% compared to non-mean-field baselines, enabling accurate trend forecasting and effective intervention planning. Generalizing across 7 domains and 4 LLM backbones, MF-LLM provides a scalable, high-fidelity foundation for social simulation.

**Emergence explanation sentence.** "Simulating collective decision-making involves more than aggregating individual behaviors; it emerges from dynamic interactions among individuals."

---
