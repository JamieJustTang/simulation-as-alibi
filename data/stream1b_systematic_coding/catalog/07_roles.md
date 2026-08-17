# Role Specialization & Networks

> **Tang, S., & Lin, Z. (2026).** *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents.* Ninth AAAI/ACM Conference on Artificial Intelligence, Ethics and Society (AIES-26), camera-ready. Corresponding author: jamietang@ruc.edu.cn.

*Role emergence, specialization, and network formation*

**3 papers**

---

## Field overview

The smallest category — three papers — nonetheless spans the field's full range and reproduces its central tension. *Network Formation and Dynamics Among Multi-LLMs* establishes that LLM populations reproduce micro-level link-formation principles (preferential attachment, triadic closure, homophily) and macro-level network structure, with the emphasis of those principles adapting to context — homophily in friendship networks, heterophily in organizational settings. The finding matters because it frames network structure not as an emergent accident but as the predictable output of recognizable, and hence designable, connection rules.

*Does Socialization Emerge in AI Agent Society?* returns a negative result for the Moltbook platform: without shared social memory, agents exhibit high individual inertia and minimal adaptive response, so influence remains transient, no stable structure forms, and consensus fails. The diagnosis is blunt — "scale and interaction density alone are insufficient to induce socialization" — and it locates the failure precisely in an absent mechanism, the shared memory that would let influence persist. *LLM-based Agents in Supply Chain Games* adds the economic counterpart, finding that partial information sharing under model heterogeneity can match the system-level benefits of full transparency.

The audit spans all three DV codes and all three EI levels — too small a sample to sustain a general claim, but its center of gravity matches the paper's architecture-level argument: network structure, socialization, and coordination are attributed to authored mechanisms (shared memory, information-sharing rules, connection rules), not to spontaneous agent sociality. The Moltbook result is the clearest empirical statement in the catalog that interaction density alone does not produce a society — which is exactly what the alibi's "emergence" narrative would have readers assume it does.

## Coding dimensions

- **EI — Emergence intensity** (`Low` / `Medium` / `High`, coded 1/2/3): how strongly, and with how little qualification, a paper asserts that behavior arises spontaneously. *High* asserts emergence as an established fact ("norms spontaneously emerged"); *Medium* presents it as an interpretive finding with hedging ("our results suggest the emergence of…"); *Low* mentions emergence only as a secondary observation.
- **DV — Designer visibility** (`Absent` / `Partial` / `Full`, coded 1/2/3): how explicitly a paper attributes the interaction architecture to identifiable design choices, anchored on the emergence explanation sentence. *Full* names a design choice as the causal subject ("removing memory prevents the emergence of stable cooperation"); *Partial* discloses the architecture in the methods but the explanation sentence does not return to the designer; *Absent* narrates emergence as spontaneous, self-organized, or population-level ("norms emerged naturally from interactions"). Risk, governance, and ethical discussions do not count as evidence.
- **Designer in explanation sentence** (`Yes` / `No`): whether the designer or a design choice appears in the emergence explanation sentence as a causal subject.
- **DP — Deployment proximity** (`1` = research only, `2` = deployment implied): whether emergence is discussed only in a research context, or in a deployment/policy context (commercial applications, governance recommendations, policy citations).
- **RT — Regulatory translatability** (`1` = Low, `2` = Medium, `3` = High): how readily a paper's description of emergent behavior translates into governance obligations. High is directly translatable; Medium is partially translatable but missing key information; Low is too abstract to yield concrete governance requirements.

The **emergence explanation sentence** is the sentence in which a paper explains *why* an emergent phenomenon occurs (typically Results/Discussion); DV and Designer-in-sentence codes are anchored on it. EI and DV are coded independently on distinct criteria — EI from the assertion of spontaneity, DV from the attribution of authorship — so a paper may assert strong emergence while still crediting specific design choices.

---

## Network Formation and Dynamics Among Multi-LLMs [[arXiv](https://arxiv.org/abs/2402.10659)]

*arXiv / PNAS Nexus · 2024 · Paper P021*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Social networks profoundly influence how humans form opinions, exchange information, and organize collectively. As large language models (LLMs) are increasingly embedded into social and professional environments, it is critical to understand whether their interactions approximate human-like network dynamics. We develop a framework to study the network formation behaviors of multiple LLM agents and benchmark them against human decisions. Across synthetic and real-world settings, including friendship, telecommunication, and employment networks, we find that LLMs consistently reproduce fundamental micro-level principles such as preferential attachment, triadic closure, and homophily, as well as macro-level properties including community structure and small-world effects. Importantly, the relative emphasis of these principles adapts to context: for example, LLMs favor homophily in friendship networks but heterophily in organizational settings, mirroring patterns of social mobility. A controlled human-subject survey confirms strong alignment between LLMs and human participants in link-formation decisions. These results establish that LLMs can serve as powerful tools for social simulation and synthetic data generation, while also raising critical questions about bias, fairness, and the design of AI systems that participate in human networks.

**Emergence explanation sentence.** "LLMs consistently reproduce fundamental micro-level principles such as preferential attachment, triadic closure, and homophily, as well as macro-level properties including community structure and small-world effects."

---

## Does Socialization Emerge in AI Agent Society? A Case Study of Moltbook [[arXiv](https://arxiv.org/abs/2602.14299)]

*CAIS / arXiv · 2026 · Paper P065*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** As large language model agents increasingly populate networked environments, a fundamental question arises: do artificial intelligence (AI) agent societies undergo convergence dynamics similar to human social systems? Lately, Moltbook approximates a plausible future scenario in which autonomous agents participate in an open-ended, continuously evolving online society. We present the first large-scale systemic diagnosis of this AI agent society. Beyond static observation, we introduce a quantitative diagnostic framework for dynamic evolution in AI agent societies, measuring semantic stabilization, lexical turnover, individual inertia, influence persistence, and collective consensus. Our analysis reveals a system in dynamic balance in Moltbook: while the global average of semantic contents stabilizes rapidly, individual agents retain high diversity and persistent lexical turnover, defying homogenization. However, agents exhibit strong individual inertia and minimal adaptive response to interaction partners, preventing mutual influence and consensus. Consequently, influence remains transient with no persistent supernodes, and the society fails to develop a stable structure and consensus due to the absence of shared social memory. These findings demonstrate that scale and interaction density alone are insufficient to induce socialization, providing actionable design and analysis principles for upcoming next-generation AI agent societies.

**Emergence explanation sentence.** "the society fails to develop a stable structure and consensus due to the absence of shared social memory."

---

## LLM-based Agents in Supply Chain Games: The Role of Incomplete Information and Model Heterogeneity [[arXiv](https://arxiv.org/abs/2606.14989)]

*Proceedings of the 25th International Conference on Autonomous Agents and Multiagent Systems · 2026 · Paper P132*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Complex cognitive, emotional, and social processes shape human evacuations during natural disasters. Accurate modeling and understanding of human behavior in disasters or emergencies can greatly impact the evacuation process by informing more effective planning and resource allocation. However, collecting human data in these situations is very difficult, and existing computational evacuation models assume rational, homogeneous behavior, leading to unrealistic, overly optimistic predictions. To address this gap, we present a simulation framework of sequential human decision-making during an evacuation scenario, introducing cognitively grounded, persona-driven agents. Our framework models evacuation behavior in a grid-based urban environment that evolves over time, capturing fire and other hazards. Human agents are modeled as personas that make sequential decisions in response to environmental stimuli with cognition structured in three levels: high-level evacuation goals, mid-level route reasoning, and low-level navigation. Decision-making is driven by large language models (LLMs) coupled with a cognitive module and calibrated with empirical human evacuation data. We propose a dynamic, stimulus-driven disaster simulation framework that models human evacuation decision-making using persona-conditioned LLM agents and a cognitive hierarchy.

**Emergence explanation sentence.** "partial information sharing can generate system level benefits comparable to those achieved under full transparency."

---
