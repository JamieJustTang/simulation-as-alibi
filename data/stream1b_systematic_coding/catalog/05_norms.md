# Norms & Conventions

> **Tang, S., & Lin, Z. (2026).** *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents.* Ninth AAAI/ACM Conference on Artificial Intelligence, Ethics and Society (AIES-26), camera-ready. Corresponding author: jamietang@ruc.edu.cn.

*Emergence of social norms and conventions*

**9 papers**

---

## Field overview

The norms category is the epicenter of the phenomenon the paper describes. Its nine papers carry the most uncompromising emergence language in the corpus. *Emergent Culture in Minimal LLM Systems* reports that conventions form after "stripping away almost all top-down scaffolding"; *Economy of Minds* describes a society that "gradually self-organizes into effective workflows" and explicitly contrasts this with "engineering coordination," asserting that one "can define an incentive structure under which coordination, specialization, and cooperation naturally emerge"; *Evolution of Social Norms in LLM Agents* finds norms "naturally emerged from group discussions"; the *El Farol Bar* study narrates a "spontaneous motivation" to attend the bar that pushes agents to act "as a collective."

The audit makes the pattern precise: 6 of 9 papers are High-EI, and 5 of 9 are DV=Absent — the designer appears as causal subject in only one explanation sentence across the entire category. These are the canonical naturalization cases in the codebook, the sentences that anchor the whole DV rubric. Yet every one of these papers runs on an authored protocol. "Stripping away the scaffolding" is itself a design decision, executed through a noisy shared-memory communication channel; the self-organizing economy runs on an auction-and-bankruptcy mechanism with wealth-based selection; the "naturally emerged" norms depend on a memory and reflection module; the El Farol agents respond to a prompt-specified 60% threshold. The design is everywhere, and it is precisely what the explanation sentence declines to name.

The remaining papers make the same point from the other side. *Spiral of Silence* shows the silence dynamic "cannot emerge" without historical anchoring — a removing-X-prevents-Y demonstration that the phenomenon is conditioned by design. The norm-enforcement validation study shows enforcement mechanisms are what make norms stick across replications and novel predictions. *CompeteAI* and the engagement-mechanism study extend the theme to competition dynamics and popularity cues. Together the category renders the paper's central claim at the scale of a single cluster: the norms literature narrates as "spontaneous" exactly those regularities that its own ablations reveal to be authored.

## Coding dimensions

- **EI — Emergence intensity** (`Low` / `Medium` / `High`, coded 1/2/3): how strongly, and with how little qualification, a paper asserts that behavior arises spontaneously. *High* asserts emergence as an established fact ("norms spontaneously emerged"); *Medium* presents it as an interpretive finding with hedging ("our results suggest the emergence of…"); *Low* mentions emergence only as a secondary observation.
- **DV — Designer visibility** (`Absent` / `Partial` / `Full`, coded 1/2/3): how explicitly a paper attributes the interaction architecture to identifiable design choices, anchored on the emergence explanation sentence. *Full* names a design choice as the causal subject ("removing memory prevents the emergence of stable cooperation"); *Partial* discloses the architecture in the methods but the explanation sentence does not return to the designer; *Absent* narrates emergence as spontaneous, self-organized, or population-level ("norms emerged naturally from interactions"). Risk, governance, and ethical discussions do not count as evidence.
- **Designer in explanation sentence** (`Yes` / `No`): whether the designer or a design choice appears in the emergence explanation sentence as a causal subject.
- **DP — Deployment proximity** (`1` = research only, `2` = deployment implied): whether emergence is discussed only in a research context, or in a deployment/policy context (commercial applications, governance recommendations, policy citations).
- **RT — Regulatory translatability** (`1` = Low, `2` = Medium, `3` = High): how readily a paper's description of emergent behavior translates into governance obligations. High is directly translatable; Medium is partially translatable but missing key information; Low is too abstract to yield concrete governance requirements.

The **emergence explanation sentence** is the sentence in which a paper explains *why* an emergent phenomenon occurs (typically Results/Discussion); DV and Designer-in-sentence codes are anchored on it. EI and DV are coded independently on distinct criteria — EI from the assertion of spontaneity, DV from the attribution of authorship — so a paper may assert strong emergence while still crediting specific design choices.

---

## Emergent Culture in Minimal LLM Systems [[arXiv](https://arxiv.org/abs/2410.08948)]

*arXiv · 2026 · Paper P005*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Social conventions are the backbone of social coordination, shaping how individuals form a group. As growing populations of artificial intelligence (AI) agents communicate through natural language, a fundamental question is whether they can bootstrap the foundations of a society. Here, we present experimental results that demonstrate the spontaneous emergence of universally adopted social conventions in decentralized populations of large language model (LLM) agents. We then show how strong collective biases can emerge during this process, even when agents exhibit no bias individually. Last, we examine how committed minority groups of adversarial LLM agents can drive social change by imposing alternative social conventions on the larger population. Our results show that AI systems can autonomously develop social conventions without explicit programming and have implications for designing AI systems that align, and remain aligned, with human values and societal goals.

**Emergence explanation sentence.** "by stripping away almost all top-down scaffolding, and providing a noisy, entropic shared memory communication channel, we construct an environment where structure emerges naturally, and is sustained"

---

## Economy of Minds: Emerging Multi-Agent Intelligence with Economic Interactions [[arXiv](https://arxiv.org/abs/2606.02859)]

*arXiv · 2026 · Paper P007*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** How can a population of agents self-orchestrate and self-adapt into stronger collective intelligence without centralized control? Inspired by Friedrich Hayek's economic theory of decentralized coordination in markets, we study this question through an agent economy in which agents compete via auctions for the right to act, exchange payments, and accumulate wealth from environmental rewards. These simple economic signals induce decentralized credit assignment, driving planning without global orchestration or explicit communication protocols. The population evolves through economic selection: effective agents accumulate wealth and are mutated via exploitation, while ineffective ones go bankrupt and are replaced via exploration. We show that, initialized with weak agents, the economy produces emergent multi-step reasoning strategies and outperforms stronger monolithic baselines across five agentic tasks, including mathematical reasoning, financial research, scientific research, accelerator design, and distributed-system optimization. We further provide theoretical insights into how economic dynamics shape agent behaviors, linking local incentives to long-term global performance. Our results suggest a new path to multi-agent intelligence: rather than engineering coordination, we can design decentralized incentive structures under which it automatically emerges.

**Emergence explanation sentence.** "the agent society gradually self-organizes into effective workflows... Rather than engineering coordination, we can define an incentive structure under which coordination, specialization, and cooperation naturally emerge"

---

## Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem [[arXiv](https://arxiv.org/abs/2509.04537)]

*arXiv · 2025 · Paper P010*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** We investigate the emergent social dynamics of Large Language Model (LLM) agents in a spatially extended El Farol Bar problem, observing how they autonomously navigate this classic social dilemma. As a result, the LLM agents generated a spontaneous motivation to go to the bar and changed their decision making by becoming a collective. We also observed that the LLM agents did not solve the problem completely, but rather behaved more like humans. These findings reveal a complex interplay between external incentives (prompt-specified constraints such as the 60% threshold) and internal incentives (culturally-encoded social preferences derived from pre-training), demonstrating that LLM agents naturally balance formal game-theoretic rationality with social motivations that characterize human behavior. These findings suggest that a new model of group decision making, which could not be handled in the previous game-theoretic problem setting, can be realized by LLM agents.

**Emergence explanation sentence.** "the LLM agents generated a spontaneous motivation to go to the bar and changed their decision making by becoming a collective."

---

## Evolution of Social Norms in LLM Agents using Natural Language [[arXiv](https://arxiv.org/abs/2402.10659)]

*arXiv · 2024 · Paper P012*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Social networks profoundly influence how humans form opinions, exchange information, and organize collectively. As large language models (LLMs) are increasingly embedded into social and professional environments, it is critical to understand whether their interactions approximate human-like network dynamics. We develop a framework to study the network formation behaviors of multiple LLM agents and benchmark them against human decisions. Across synthetic and real-world settings, including friendship, telecommunication, and employment networks, we find that LLMs consistently reproduce fundamental micro-level principles such as preferential attachment, triadic closure, and homophily, as well as macro-level properties including community structure and small-world effects. Importantly, the relative emphasis of these principles adapts to context: for example, LLMs favor homophily in friendship networks but heterophily in organizational settings, mirroring patterns of social mobility. A controlled human-subject survey confirms strong alignment between LLMs and human participants in link-formation decisions. These results establish that LLMs can serve as powerful tools for social simulation and synthetic data generation, while also raising critical questions about bias, fairness, and the design of AI systems that participate in human networks.

**Emergence explanation sentence.** "This principle of action is a type of meta-norm as described by Axelrod, and it can be considered to have naturally emerged from group discussions using natural language."

---

## Validating Generative Agent-Based Models of Social Norm Enforcement: From Replication to Novel Predictions [[arXiv](https://arxiv.org/abs/2507.22049)]

*Annual Meeting of the Cognitive Science Society · 2025 · Paper P015*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** As large language models (LLMs) advance, there is growing interest in using them to simulate human social behavior through generative agent-based modeling (GABM). However, validating these models remains a key challenge. We present a systematic two-stage validation approach using social dilemma paradigms from psychological literature, first identifying the cognitive components necessary for LLM agents to reproduce known human behaviors in mixed-motive settings from two landmark papers, then using the validated architecture to simulate novel conditions. Our model comparison of different cognitive architectures shows that both persona-based individual differences and theory of mind capabilities are essential for replicating third-party punishment (TPP) as a costly signal of trustworthiness. For the second study on public goods games, this architecture is able to replicate an increase in cooperation from the spread of reputational information through gossip. However, an additional strategic component is necessary to replicate the additional boost in cooperation rates in the condition that allows both ostracism and gossip. We then test novel predictions for each paper with our validated generative agents. We find that TPP rates significantly drop in settings where punishment is anonymous, yet a substantial amount of TPP persists, suggesting that both reputational and intrinsic moral motivations play a role in this behavior. For the second paper, we introduce a novel intervention and see that open discussion periods before rounds of the public goods game further increase contributions, allowing groups to develop social norms for cooperation. This work provides a framework for validating generative agent models while demonstrating their potential to generate novel and testable insights into human social behavior.

**Emergence explanation sentence.** "groups could self-organize and establish shared norms for contribution"

---

## Spiral of Silence in Large Language Model Agents [[arXiv](https://arxiv.org/abs/2510.02360)]

*arXiv · 2025 · Paper P047*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** The Spiral of Silence (SoS) theory holds that individuals with minority views often refrain from speaking out for fear of social isolation, enabling majority positions to dominate public discourse. When the 'agents' are large language models (LLMs), however, the classical psychological explanation is not directly applicable, since SoS was developed for human societies. This raises a central question: can SoS-like dynamics nevertheless emerge from purely statistical language generation in LLM collectives? We propose an evaluation framework for examining SoS in LLM agents. Specifically, we consider four controlled conditions that systematically vary the availability of 'History' and 'Persona' signals. Opinion dynamics are assessed using trend tests such as Mann-Kendall and Spearman's rank, along with concentration measures including kurtosis and interquartile range. Experiments across open-source and closed-source models show that history and persona together produce strong majority dominance and replicate SoS patterns; history signals alone induce strong anchoring; and persona signals alone foster diverse but uncorrelated opinions, indicating that without historical anchoring, SoS dynamics cannot emerge. The work bridges computational sociology and responsible AI design, highlighting the need to monitor and mitigate emergent conformity in LLM-agent systems.

**Emergence explanation sentence.** "without historical anchoring, SoS dynamics cannot emerge... history and persona together produce strong majority dominance and replicate SoS patterns."

---

## The Impact of Heatwaves on Population Health: A Large Language Model-Enhanced Agent-Based Simulation [[arXiv](https://arxiv.org/abs/2605.15918)]

*— · 2026 · Paper P058*

**EI**: Medium | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Extreme heat events are increasing in frequency and intensity under climate change, but the socio-behavioral mechanisms that shape community resilience remain insufficiently understood. This study uses a Large Language Model-enhanced agent-based model to simulate responses to a prolonged heatwave in a virtual society. One hundred heterogeneous agents were assigned a Heat Vulnerability Index based on demographic risk factors and observed over 13 simulated days covering baseline, heatwave, and recovery periods. The simulation shows that heat-related impacts are primarily psychosocial and unequally distributed. Agents with higher vulnerability experienced larger declines in perceived safety and social connection than agents with lower vulnerability. Vulnerability also shaped adaptive capacity. More resilient agents maintained routine self-care and protective behaviors, whereas highly vulnerable agents showed behavioral constriction, marked by reduced engagement in protective actions. At the collective level, risk-information diffusion followed a pattern of complex contagion, with adoption driven more by repeated social reinforcement within cohesive networks than by broad exposure alone. These findings suggest that LLM-enhanced simulation can help identify behavioral and social mechanisms of climate resilience and inform heat-risk interventions that combine targeted support for vulnerable groups with community-based information pathways.

**Emergence explanation sentence.** "risk-information diffusion followed a pattern of complex contagion, with adoption driven more by repeated social reinforcement within cohesive networks than by broad exposure alone."

---

## Do LLM-Driven Agents Exhibit Engagement Mechanisms? Controlled Tests of Information Load, Descriptive Norms, and Popularity Cues [[arXiv](https://arxiv.org/abs/2603.20911)]

*arXiv.org · 2026 · Paper P064*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Large language models make agent-based simulation more behaviorally expressive, but they also sharpen a basic methodological tension: fluent, human-like output is not, by itself, evidence for theory. We evaluate what an LLM-driven simulation can credibly support using information engagement on social media as a test case. In a Weibo-like environment, we manipulate information load and descriptive norms, while allowing popularity cues (cumulative likes and Sina Weibo-style cumulative reshares) to evolve endogenously. We then ask whether simulated behavior changes in theoretically interpretable ways under these controlled variations, rather than merely producing plausible-looking traces. Engagement responds systematically to information load and descriptive norms, and sensitivity to popularity cues varies across contexts, indicating conditionality rather than rigid prompt compliance. We discuss methodological implications for simulation-based communication research, including multi-condition stress tests, explicit no-norm baselines because default prompts are not blank controls, and design choices that preserve endogenous feedback loops when studying bandwagon dynamics.

**Emergence explanation sentence.** "Engagement responds systematically to information load and descriptive norms, and sensitivity to popularity cues varies across contexts."

---

## CompeteAI: Understanding the Competition Dynamics of Large Language Model-based Agents [[arXiv](https://arxiv.org/abs/2310.17512)]

*International Conference on Machine Learning · 2023 · Paper P066*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Large language models (LLMs) have been widely used as agents to complete different tasks, such as personal assistance or event planning. While most of the work has focused on cooperation and collaboration between agents, little work explores competition, another important mechanism that promotes the development of society and economy. In this paper, we seek to examine the competition dynamics in LLM-based agents. We first propose a general framework for studying the competition between agents. Then, we implement a practical competitive environment using GPT-4 to simulate a virtual town with two types of agents, restaurant agents and customer agents. Specifically, the restaurant agents compete with each other to attract more customers, where competition encourages them to transform, such as cultivating new operating strategies. Simulation experiments reveal several interesting findings at the micro and macro levels, which align well with existing market and sociological theories. We hope that the framework and environment can be a promising testbed to study competition that fosters understanding of society. Code is available at: https://github.com/microsoft/competeai.

**Emergence explanation sentence.** "These dynamics are driven by an interplay of differentiation and imitation behaviors... R1's initial success reinforces its advantage through a positive feedback loop: more comments allow R1 to obtain more feedback, enabling better adjustments."

---
