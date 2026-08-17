# Collective Cognition & Intelligence

*Collective intelligence, swarm behavior, and group reasoning*

**5 papers**

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
