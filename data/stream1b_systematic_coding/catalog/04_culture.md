# Culture, Emotion & Normativity

*Cultural emergence, emotion diffusion, and normative dynamics*

**8 papers**

---

## TerraLingua: Emergence and Analysis of Open-endedness in LLM Ecologies [[arXiv](https://arxiv.org/abs/2603.16910)]

*arXiv.org · 2026 · Paper P022*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** As autonomous agents increasingly operate in real-world digital ecosystems, understanding how they coordinate, form institutions, and accumulate shared culture becomes both a scientific and practical priority. This paper introduces TerraLingua, a persistent multi-agent ecology designed to study open-ended dynamics in such systems. Unlike prior large language model simulations with static or consequence-free environments, TerraLingua imposes resource constraints and limited lifespans for the agents. As a result, agents create artifacts that persist beyond individuals, shaping future interactions and selection pressures. To characterize the dynamics, an AI Anthropologist systematically analyzes agent behavior, group structure, and artifact evolution. Across experimental conditions, the results reveal the emergence of cooperative norms, division of labor, governance attempts, and branching artifact lineages consistent with cumulative cultural processes. Divergent outcomes across experimental runs can be traced back to specific innovations and organizational structures. TerraLingua thus provides a platform for characterizing the mechanisms of cumulative culture and social organization in artificial populations, and can serve as a foundation for guiding real-world agentic populations to socially beneficial outcomes.

**Emergence explanation sentence.** "A central mechanism enabling this emergence is the use of artifacts: agents create persistent, interpretable objects that remain in the environment and influence future behavior"

---

## MOSAIC: Modeling Social AI for Content Dissemination and Regulation in Multi-Agent Simulations [[arXiv](https://arxiv.org/abs/2504.07830)]

*Conference on Empirical Methods in Natural Language Processing · 2025 · Paper P025*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** We present a novel, open-source social network simulation framework, MOSAIC, where generative language agents predict user behaviors such as liking, sharing, and flagging content. This simulation combines LLM agents with a directed social graph to analyze emergent deception behaviors and gain a better understanding of how users determine the veracity of online social content. By constructing user representations from diverse fine-grained personas, our system enables multi-agent simulations that model content dissemination and engagement dynamics at scale. Within this framework, we evaluate three different content moderation strategies with simulated misinformation dissemination, and we find that they not only mitigate the spread of non-factual content but also increase user engagement. In addition, we analyze the trajectories of popular content in our simulations, and explore whether simulation agents' articulated reasoning for their social interactions truly aligns with their collective engagement patterns. We open-source our simulation software to encourage further research within AI and social sciences.

**Emergence explanation sentence.** "we argue that perhaps LLM-driven agents have a tendency to simply copy the decisions of agents who act before them. This results in the preferential attachment and, as a natural consequence, establishes the power-law distribution of engagement patterns."

---

## When Agents Lie: Premeditation, Persistence, and Exploitation in Repeated Games [[arXiv](https://arxiv.org/abs/2607.05132)]

*arXiv · 2026 · Paper P057*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three frontier models across six games in homogeneous and heterogeneous groups over 10 rounds, we report two findings. First, when agents deviate from their announcements, the deviation is predominantly already stated in their private plan (exceeding 90% in the highest-deception conditions), yet this is not a fixed model property: the same model ranges from perfect honesty to near-total deviation across games. Second, different models interpret announcements incompatibly, some as binding commitments and others as cheap talk, producing payoff gaps that emerge in Round~0 and persist across all 10 rounds. Systems that combine models from different providers therefore cannot assume shared announcement semantics and require empirical testing of model interactions before deployment.

**Emergence explanation sentence.** "deception is game-dependent and premeditated...outcomes are highly variable depending on the specific game."

---

## MIDSim: Simulating Multi-Channel Information Diffusion in Social Media with LLM-Powered Multi-Agent System [[arXiv](https://arxiv.org/abs/2407.04503)]

*— · 2026 · Paper P060*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** As large language models (LLMs) start interacting with each other and generating an increasing amount of text online, it becomes crucial to better understand how information is transformed as it passes from one LLM to the next. While significant research has examined individual LLM behaviors, existing studies have largely overlooked the collective behaviors and information distortions arising from iterated LLM interactions. Small biases, negligible at the single output level, risk being amplified in iterated interactions, potentially leading the content to evolve towards attractor states. In a series of telephone game experiments, we apply a transmission chain design borrowed from the human cultural evolution literature: LLM agents iteratively receive, produce, and transmit texts from the previous to the next agent in the chain. By tracking the evolution of text toxicity, positivity, difficulty, and length across transmission chains, we uncover the existence of biases and attractors, and study their dependence on the initial text, the instructions, language model, and model size. For instance, we find that more open-ended instructions lead to stronger attraction effects compared to more constrained tasks. We also find that different text properties display different sensitivity to attraction effects, with toxicity leading to stronger attractors than length. These findings highlight the importance of accounting for multi-step transmission dynamics and represent a first step towards a more comprehensive understanding of LLM cultural dynamics.

**Emergence explanation sentence.** "our proposed framework realistically simulate macro diffusion phenomenon and generate diverse diffusion patterns"

---

## Investigating and Extending Homans' Social Exchange Theory with Large Language Model based Agents [[arXiv](https://arxiv.org/abs/2502.12450)]

*arXiv · 2025 · Paper P072*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Homans' Social Exchange Theory (SET) is widely recognized as a basic framework for understanding the formation and emergence of human civilizations and social structures. In social science, this theory is typically studied based on simple simulation experiments or real-world human studies, both of which either lack realism or are too expensive to control. In artificial intelligence, recent advances in large language models (LLMs) have shown promising capabilities in simulating human behaviors. Inspired by these insights, we adopt an interdisciplinary research perspective and propose using LLM-based agents to study Homans' SET. Specifically, we construct a virtual society composed of three LLM agents and have them engage in a social exchange game to observe their behaviors. Through extensive experiments, we found that Homans' SET is well validated in our agent society, demonstrating the consistency between the agent and human behaviors. Building on this foundation, we intentionally alter the settings of the agent society to extend the traditional Homans' SET, making it more comprehensive and detailed. To the best of our knowledge, this paper marks the first step in studying Homans' SET with LLM-based agents. More importantly, it introduces a novel and feasible research paradigm that bridges the fields of social science and computer science through LLM-based agents. Code is available at https://github.com/Paitesanshi/SET.

**Emergence explanation sentence.** "social value orientations influence the interaction... and the resilience of the social exchange systems."

---

## Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents [[arXiv](https://arxiv.org/abs/2607.15095)]

*arXiv · 2026 · Paper P084*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** The formation of political coalitions is a complex negotiation driven by both concrete policy objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new avenues for computational political science, the neutrality and helpfulness biases instilled by Reinforcement Learning from Human Feedback (RLHF) prevent them from sustaining steadfast partisan behaviour. We present a multi-agent framework that reconciles factual grounding with ideological alignment by combining Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Retrieval-Augmented Generation (RAG): DPO instils aggressive party-specific personas, while a per-party RAG pipeline keeps each agent bounded to its official manifesto. We operationalize the framework on the 2019 Flemish election, deploying the partisan agents in a hub-and-spoke negotiation arbitrated by a formateur. To make the emergent negotiation interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT) that traces every clause in the final agreement back to its manifesto origin and classifies it into five provenance states, a Coalition Influence Score (CIS) that aggregates these traceable contributions to identify which party shaped the agreement, and a real-world grounding pass that benchmarks each simulated provision against the historically adopted coalition agreement. Across three independent simulations the framework yields a stable winner and ranking (N-VA ahead of CD\&amp;V and Open Vld), and manifesto-anchored lineage reliably predicts real-world materialization whereas hallucinated content does not. The result is a transparent, scalable testbed for the ex-ante exploration of party compatibility and formateur-mediated compromise.

**Emergence explanation sentence.** "we stage a structured hub-and-spoke negotiation... To make the emergent negotiation interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT)"

---

## The Wisdom of Partisan Crowds: Comparing Collective Intelligence in Humans and LLM-based Agents [[arXiv](https://arxiv.org/abs/2603.01952)]

*Annual Meeting of the Cognitive Science Society / arXiv · 2023 · Paper P097*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Large language models (LLMs) are increasingly deployed as autonomous agents, yet evaluations focus primarily on task success rather than cultural appropriateness or evaluator reliability. We introduce LiveCultureBench, a multi-cultural, dynamic benchmark that embeds LLMs as agents in a simulated town and evaluates them on both task completion and adherence to socio-cultural norms. The simulation models a small city as a location graph with synthetic residents having diverse demographic and cultural profiles. Each episode assigns one resident a daily goal while others provide social context. An LLM-based verifier generates structured judgments on norm violations and task progress, which we aggregate into metrics capturing task-norm trade-offs and verifier uncertainty. Using LiveCultureBench across models and cultural profiles, we study (i) cross-cultural robustness of LLM agents, (ii) how they balance effectiveness against norm sensitivity, and (iii) when LLM-as-a-judge evaluation is reliable for automated benchmarking versus when human oversight is needed.

**Emergence explanation sentence.** "We then identify several factors that interfere with convergence, including the use of chain-of-thought prompt and lack of details in personas. Conversely, fine-tuning on human data appears to enhance convergence."

---

## Emotional Cognitive Modeling Framework with Desire-Driven Objective Optimization for LLM-empowered Agent in Social Simulation [[arXiv](https://arxiv.org/abs/2607.05132)]

*arXiv.org · 2025 · Paper P138*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** As large language models are deployed as autonomous agents that communicate intentions before acting, a critical safety question is whether agents that publicly commit to actions will honor those commitments. We place LLM agents in repeated $n$-player games with a three-stage protocol that separates private intent, public announcement, and final action, allowing us to identify whether each deviation from a stated announcement was already planned during private deliberation. Evaluating three frontier models across six games in homogeneous and heterogeneous groups over 10 rounds, we report two findings. First, when agents deviate from their announcements, the deviation is predominantly already stated in their private plan (exceeding 90% in the highest-deception conditions), yet this is not a fixed model property: the same model ranges from perfect honesty to near-total deviation across games. Second, different models interpret announcements incompatibly, some as binding commitments and others as cheap talk, producing payoff gaps that emerge in Round~0 and persist across all 10 rounds. Systems that combine models from different providers therefore cannot assume shared announcement semantics and require empirical testing of model interactions before deployment.

**Emergence explanation sentence.** "This mechanism ultimately enables the emergence of naturalistic human-like behavioral patterns."

---
