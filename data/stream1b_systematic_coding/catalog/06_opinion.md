# Opinion Dynamics & Social Influence

> **Tang, S., & Lin, Z. (2026).** *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents.* Ninth AAAI/ACM Conference on Artificial Intelligence, Ethics and Society (AIES-26), camera-ready. Corresponding author: jamietang@ruc.edu.cn.

*Opinion formation, conformity, and influence diffusion*

**8 papers**

---

## Field overview

The opinion-dynamics category studies how beliefs spread, conform, and resist manipulation across LLM populations. Two clusters organize the eight papers. The first is conformity and influence. *An Empirical Study of Group Conformity* shows agents align with numerically dominant groups, mirroring human behavior; *Belief in Authority* measures how much an authority framing bends evaluation against an agent's own judgment. The second is dissemination and manipulation. *DEBATE* and *LLM-AIDSim* provide benchmarks and platforms for influence diffusion; *Public opinion dissemination* models multi-agent opinion spread; *TrendSim* studies how trending topics respond to poisoning attacks; *Topology-Aware LLM-Driven Social Simulation* and *Step-Level Preference Learning* close the loop by showing that opinion outcomes track network structure and preference supervision rather than any free-floating sociality.

The recurring finding across both clusters is that opinion is a function of the exposure architecture: who an agent sees, in what format, and with what authority signal. Conformity bends toward the majority only when peer information is presented in a particular format; authority effects track the framing; cascade dynamics track the topology. Opinion, in this literature, rarely "just forms" — it is pushed through a channel, and the channel is a design choice.

The audit profile is moderate and designer-leaning: 6 of 8 papers are Medium-EI, and 5 of 8 are DV=Full. Emergence claims are real but hedged, and the designer usually survives into the explanation. This category thus occupies the field's middle ground between the norms category's naturalization and the methods category's full disclosure — and its consistency in naming the exposure mechanism makes it a quiet ally of the paper's argument.

## Coding dimensions

- **EI — Emergence intensity** (`Low` / `Medium` / `High`, coded 1/2/3): how strongly, and with how little qualification, a paper asserts that behavior arises spontaneously. *High* asserts emergence as an established fact ("norms spontaneously emerged"); *Medium* presents it as an interpretive finding with hedging ("our results suggest the emergence of…"); *Low* mentions emergence only as a secondary observation.
- **DV — Designer visibility** (`Absent` / `Partial` / `Full`, coded 1/2/3): how explicitly a paper attributes the interaction architecture to identifiable design choices, anchored on the emergence explanation sentence. *Full* names a design choice as the causal subject ("removing memory prevents the emergence of stable cooperation"); *Partial* discloses the architecture in the methods but the explanation sentence does not return to the designer; *Absent* narrates emergence as spontaneous, self-organized, or population-level ("norms emerged naturally from interactions"). Risk, governance, and ethical discussions do not count as evidence.
- **Designer in explanation sentence** (`Yes` / `No`): whether the designer or a design choice appears in the emergence explanation sentence as a causal subject.
- **DP — Deployment proximity** (`1` = research only, `2` = deployment implied): whether emergence is discussed only in a research context, or in a deployment/policy context (commercial applications, governance recommendations, policy citations).
- **RT — Regulatory translatability** (`1` = Low, `2` = Medium, `3` = High): how readily a paper's description of emergent behavior translates into governance obligations. High is directly translatable; Medium is partially translatable but missing key information; Low is too abstract to yield concrete governance requirements.

The **emergence explanation sentence** is the sentence in which a paper explains *why* an emergent phenomenon occurs (typically Results/Discussion); DV and Designer-in-sentence codes are anchored on it. EI and DV are coded independently on distinct criteria — EI from the assertion of spontaneity, DV from the attribution of authorship — so a paper may assert strong emergence while still crediting specific design choices.

---

## An Empirical Study of Group Conformity in Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2607.01148)]

*arXiv · 2025 · Paper P071*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** We investigate the emergence of structural disparities in networks of collaborating large language model (LLM) agents. When LLM agents autonomously choose collaborators, the resulting communication network exhibits preferential-attachment dynamics: agents that are already prominent become increasingly likely to attract additional connections. In some cases, weaker LLM agents (agents with smaller base model or older version) can disproportionately occupy central and influential network positions relative to stronger LLM agents. We interpret this as a type-dependent glass-ceiling effect (GCE). We model the network of LLM agents as a time-evolving sequence of directed weighted graphs, where the vector-valued edge weights represent cumulative tokens exchanged, number of interaction rounds, and reasoning effort. Using a contraction mapping argument on the mean-field dynamics, we prove that the importance (centrality) of each agent type converges to a unique stable equilibrium. To ground the model in LLM decision mechanisms, we introduce a cross-attention-inspired utility for collaborator selection. This utility specifies the local connection dynamics and, together with the mean-field model, yields a predictive characterization of the limiting network structure and its type-dependent centrality gaps. To validate the theory, we develop an experimental testbed with 100 LLM agents. Our experiments show that autonomous network formation can generate persistent centrality disparities, with their magnitude and direction depending on model family, model size, system-prompt design, and task context. They further show that the effect of preferential attachment depends on its alignment with model capability: reinforcing it improves collective performance when stronger agents become central, whereas weakening it improves performance when network dynamics instead favor weaker agents.

**Emergence explanation sentence.** "analyses reveal significant group conformity mirroring human behavior; LLM agents tend to align with numerically dominant groups."

---

## DEBATE: A Large-Scale Benchmark for Evaluating Opinion Dynamics in Role-Playing LLM Agents [[arXiv](https://arxiv.org/abs/2606.28456)]

*— · 2025 · Paper P075*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** LLMs agents are increasingly used in multi-agent settings, yet their behaviour in sustainability games remains largely unexplored. This work investigates whether lying can emerge among LLM agents in a competitive sustainability game in which agents are informed that common resources can regenerate, although regeneration does not actually occur. We develop an agent-based model of a sustainability game in which agents manage industrial, military, and ecological resources, and interact through a network. LLM agents can observe neighbours' status, declare future attacks, receive permission to lie, and access reputation information, while rule-based agents provide an interpretable behavioural baseline. The results show that neighbour information strongly changes system dynamics, increasing attacks while improving biosphere retention and coexistence. Also, the presence of future declarations reduce extinction risk without suppressing conflict. Behaviourally, deception emerges even when agents are not explicitly allowed to lie, and explicit permission mainly increases bluffing and diversion rather than direct backstabbing. Finally, the presence of reputation memory and information about the current biosphere level reduces system ecological depletion. These findings suggest that deception can arise as an emergent behaviour in LLM-agent systems and that communication between LLM-agents could support sustainability while dealing with risk.

**Emergence explanation sentence.** "The conversation is therefore the mechanism through which agents reveal and revise their opinions"

---

## LLM-AIDSim: LLM-Enhanced Agent-Based Influence Diffusion Simulation in Social Networks [[arXiv](https://arxiv.org/abs/2604.13705)]

*— · — · Paper P077*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Fairness in language models is typically studied as a property of a single, centrally optimized model. As large language models become increasingly agentic, we propose that fairness emerges through interaction and exchange. We study this via a controlled hospital triage framework in which two agents negotiate over three structured debate rounds. One agent is aligned to a specific ethical framework via retrieval-augmented generation (RAG), while the other is either unaligned or adversarially prompted to favor demographic groups over clinical need. We find that alignment systematically shapes negotiation strategies and allocation patterns, and that neither agent's allocation is ethically adequate in isolation, yet their joint final allocation can satisfy fairness criteria that neither would have reached alone. Aligned agents partially moderate bias through contestation rather than override, acting as corrective patches that restore access for marginalized groups without fully converting a biased counterpart. We further observe that even explicitly aligned agents exhibit intrinsic biases toward certain frameworks, consistent with known left-leaning tendencies in LLMs. We connect these limits to Arrow's Impossibility Theorem: no aggregation mechanism can simultaneously satisfy all desiderata of collective rationality, and multi-agent deliberation navigates rather than resolves this constraint. Our results reposition fairness as an emergent, procedural property of decentralized agent interaction, and the system rather than the individual agent as the appropriate unit of evaluation.

**Emergence explanation sentence.** "experimental results highlight the role of influence diffusion in shaping collective discussions and dominant topics"

---

## Belief in Authority: Impact of Authority in Multi-Agent Evaluation Framework [[arXiv](https://arxiv.org/abs/2601.04790)]

*arXiv · 2026 · Paper P087*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Multi-agent systems utilizing large language models often assign authoritative roles to improve performance, yet the impact of authority bias on agent interactions remains underexplored. We present the first systematic analysis of role-based authority bias in free-form multi-agent evaluation using ChatEval. Applying French and Raven's power-based theory, we classify authoritative roles into legitimate, referent, and expert types and analyze their influence across 12-turn conversations. Experiments with GPT-4o and DeepSeek R1 reveal that Expert and Referent power roles exert stronger influence than Legitimate power roles. Crucially, authority bias emerges not through active conformity by general agents, but through authoritative roles consistently maintaining their positions while general agents demonstrate flexibility. Furthermore, authority influence requires clear position statements, as neutral responses fail to generate bias. These findings provide key insights for designing multi-agent frameworks with asymmetric interaction patterns.

**Emergence explanation sentence.** "authority bias emerges not through active conformity by general agents, but through authoritative roles consistently maintaining their positions"

---

## Public opinion dissemination simulation based on large language model multi-agent systems [[arXiv](https://arxiv.org/abs/2603.20678)]

*Scientific Reports · 2026 · Paper P091*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Contemporary societies face a severe crisis of demographic reproduction. Global fertility rates continue to decline precipitously, with East Asian nations exhibiting the most dramatic trends -- China's total fertility rate (TFR) fell to approximately 1.0 in 2023, while South Korea's dropped below 0.72. Simultaneously, the institution of marriage is undergoing structural disintegration: educated women rationally reject unions lacking both emotional fulfillment and economic security, while a growing proportion of men at the lower end of the socioeconomic spectrum experience chronic sexual deprivation, anxiety, and learned helplessness. This paper proposes a computational framework for modeling and evaluating a Stratified Polyamory System (SPS) using techniques from agent-based modeling (ABM), multi-agent reinforcement learning (MARL), and large language model (LLM)-empowered social simulation. The SPS permits individuals to maintain a limited number of legally recognized secondary partners in addition to one primary spouse, combined with socialized child-rearing and inheritance reform. We formalize the A/B/C stratification as heterogeneous agent types in a multi-agent system and model the matching process as a MARL problem amenable to Proximal Policy Optimization (PPO). The mating network is analyzed using graph neural network (GNN) representations. Drawing on evolutionary psychology, behavioral ecology, social stratification theory, computational social science, algorithmic fairness, and institutional economics, we argue that SPS can improve aggregate social welfare in the Pareto sense. Preliminary computational results demonstrate the framework's viability in addressing the dual crisis of female motherhood penalties and male sexlessness, while offering a non-violent mechanism for wealth dispersion analogous to the historical Chinese Grace Decree (Tui'en Ling).

**Emergence explanation sentence.** "Role heterogeneity in modeling can facilitate the emergence of high-fidelity collective behaviors."

---

## TrendSim: Simulating Trending Topics in Social Media Under Poisoning Attacks with LLM-based Multi-agent System [[arXiv](https://arxiv.org/abs/2412.12196)]

*North American Chapter of the Association for Computational Linguistics · 2024 · Paper P096*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Trending topics have become a significant part of modern social media, attracting users to participate in discussions of breaking events. However, they also bring in a new channel for poisoning attacks, resulting in negative impacts on society. Therefore, it is urgent to study this critical problem and develop effective strategies for defense. In this paper, we propose TrendSim, an LLM-based multi-agent system to simulate trending topics in social media under poisoning attacks. Specifically, we create a simulation environment for trending topics that incorporates a time-aware interaction mechanism, centralized message dissemination, and an interactive system. Moreover, we develop LLM-based human-like agents to simulate users in social media, and propose prototype-based attackers to replicate poisoning attacks. Besides, we evaluate TrendSim from multiple aspects to validate its effectiveness. Based on TrendSim, we conduct simulation experiments to study four critical problems about poisoning attacks on trending topics for social benefit.

**Emergence explanation sentence.** "We find that the content censorship mechanism can effectively mitigate the negative impact of poisoning attacks in most cases."

---

## Topology-Aware LLM-Driven Social Simulation: A Unified Framework for Efficient and Realistic Agent Dynamics [[arXiv](https://arxiv.org/abs/2607.27512)]

*arXiv.org · 2026 · Paper P127*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Large language models (LLMs) are increasingly deployed in multi-agent environments. However, the processes by which beliefs form and propagate among interacting LLMs remain poorly understood. We introduce CoevolveSim, a framework for studying belief diffusion within networked LLM populations. CoevolveSim allows us to isolate and study three factors: domain specialization, social-role assignment, and social network structure. Within this framework, generalist and specialist LLM agents exchange and revise beliefs. In each round, an LLM agent observes a summary of its neighbors' beliefs before updating its own. We run 1,280 controlled simulations spanning four scenarios, two network structures, and 20 medical-indication statements. We find that persona-style role assignment and network structure reshape individual belief revision but have minimal effect on population-level consensus. In contrast, introducing (finetuned) specialist LLMs more than doubles the shift in consensus and gives rise to consistent asymmetries in exerted influence. We further show that simple persistence-based opinion-dynamics models reproduce collective outcomes in all-generalist LLM populations, whereas heterogeneous LLM populations require population-level belief composition to reproduce consensus and agent identity to predict individual belief transitions. Our results indicate that realistic simulation of belief diffusion in multi-agent LLM systems requires a diverse set of underlying LLMs, not persona prompting alone.

**Emergence explanation sentence.** "By making structure an explicit driver of simulation rather than a passive scaffold, TopoSim enables efficient and realistic LLM-based social simulation"

---

## Step-Level Preference Learning for Generative Agents in Social Simulations [[arXiv](https://arxiv.org/abs/2607.14485)]

*arXiv · 2026 · Paper P140*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Large language model (LLM)-based generative agents simulate human behavior through long-horizon decision-making processes that comprise intermediate steps such as planning, memory retrieval, reflection, and action selection. However, fine-grained human annotations of these intermediate steps remain scarce, and existing agents are not grounded in human preferences over such intermediate decisions. To address this gap, we introduce \method, an interactive simulation interface that enables us to collect step-level human preference supervision over agent decision trajectories, leading to a dataset of 57K fine-grained annotations. We conduct step-level preference learning on open-weight language models using supervised finetuning and direct preference optimization on this data, consistently improving simulation fidelity, coordination, and interaction quality, and inducing more socially effective agent behavior. Our results show that step-level human supervision is an effective training signal for improving both local decision quality and long-horizon agent behavior.

**Emergence explanation sentence.** "agents become better at coordinating with timing, adhering to scenario...Preference optimization brings modest and uneven additional gains."

---
