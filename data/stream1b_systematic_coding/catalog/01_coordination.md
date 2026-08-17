# Coordination & Cooperation Dynamics

*Emergent coordination, team formation, and collective action in LLM agent societies*

**31 papers**

---

## Shall We Team Up: Exploring Spontaneous Cooperation of Competing LLM Agents [[arXiv](https://arxiv.org/abs/2402.12327)]

*arXiv · 2024 · Paper P001*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Large Language Models (LLMs) have increasingly been utilized in social simulations, where they are often guided by carefully crafted instructions to stably exhibit human-like behaviors during simulations. Nevertheless, we doubt the necessity of shaping agents' behaviors for accurate social simulations. Instead, this paper emphasizes the importance of spontaneous phenomena, wherein agents deeply engage in contexts and make adaptive decisions without explicit directions. We explored spontaneous cooperation across three competitive scenarios and successfully simulated the gradual emergence of cooperation, findings that align closely with human behavioral data. This approach not only aids the computational social science community in bridging the gap between simulations and real-world dynamics but also offers the AI community a novel method to assess LLMs' capability of deliberate reasoning.

**Emergence explanation sentence.** "LLM agents can actively adapt their strategies to the dynamic contexts, spontaneously learning to cooperate in the wild."

---

## AI agents can coordinate beyond human scale [[arXiv](https://arxiv.org/abs/2409.02822)]

*arXiv · 2024 · Paper P002*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Large language models (LLMs) are increasingly deployed in collaborative tasks involving multiple agents, forming an "AI agent society: where agents interact and influence one another. Whether such groups can spontaneously coordinate on arbitrary decisions without external influence - a hallmark of self-organized regulation in human societies - remains an open question. Here we investigate the stability of groups formed by AI agents by applying methods from complexity science and principles from behavioral sciences. We find that LLMs can spontaneously form cohesive groups, and that their opinion dynamics is governed by a majority force coefficient, which determines whether coordination is achievable. This majority force diminishes as group size increases, leading to a critical group size beyond which coordination becomes practically unattainable and stability is lost. Notably, this critical group size grows exponentially with the language capabilities of the models, and for the most advanced LLMs, it exceeds the typical size of informal human groups. Our findings highlight intrinsic limitations in the self-organization of AI agent societies and have implications for the design of collaborative AI systems where coordination is desired or could represent a treat.

**Emergence explanation sentence.** "We find that LLMs can spontaneously form cohesive groups, and that their opinion dynamics is governed by a majority force coefficient, which determines whether coordination is achievable."

---

## Emergent Relational Order in LLM Agent Societies: From Collective Affect to Authority Stratification [[arXiv](https://arxiv.org/abs/2311.09665)]

*arXiv · 2026 · Paper P003*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Human groups are able to converge on more accurate beliefs through deliberation, even in the presence of polarization and partisan bias -- a phenomenon known as the "wisdom of partisan crowds." Generated agents powered by Large Language Models (LLMs) are increasingly used to simulate human collective behavior, yet few benchmarks exist for evaluating their dynamics against the behavior of human groups. In this paper, we examine the extent to which the wisdom of partisan crowds emerges in groups of LLM-based agents that are prompted to role-play as partisan personas (e.g., Democrat or Republican). We find that they not only display human-like partisan biases, but also converge to more accurate beliefs through deliberation as humans do. We then identify several factors that interfere with convergence, including the use of chain-of-thought prompt and lack of details in personas. Conversely, fine-tuning on human data appears to enhance convergence. These findings show the potential and limitations of LLM-based agents as a model of human collective intelligence.

**Emergence explanation sentence.** "agents spontaneously reproduce five core Differential Order phenomena: stable labor specialization, guanxi-based economic ethics, relational decay of cooperation, emergent relational authority, and clan-based center–periphery stratification"

---

## How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation [[arXiv](https://arxiv.org/abs/2607.25140)]

*arXiv · 2026 · Paper P004*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** This paper studies the behavior of language models in a multi-agent crowd simulation, focusing on how affect propagates among agents that perceive and appraise one another. Each agent perceives its neighbors through visual, auditory, and tactile channels, then appraises these perceptions in light of its prompted personality profile, memory, current affective state, and situational context. Appraisal is carried out by an LLM, which updates the agent's internal affective state and selects its outward expression. The architecture contains no hand-authored mechanism for directly transferring affective state between agents; instead, inter-agent influence arises through the perception-appraisal-expression loop. The agent representation draws on the Big Five personality model and Russell's circumplex model of affect. To limit latency, low-level steering and navigation are handled by a conventional crowd simulator operating independently of the LLM-based cognitive layer. We evaluate the architecture across five scenario environments spanning alarming, joyful, and neutral situations in different spatial layouts. The results show that the system produces emotional contagion dynamics with spatial, temporal, and personality-dependent structure in sparse, small crowds. Alarm spreads from seeded agents as a traveling front, the mean alarmed fraction settles at a nonzero plateau, and the distribution of prompted personality profiles determines whether an ambiguous alarm ignites panic and whether a provocation is interpreted as anger or fear. We further evaluate the appraisal step through controlled experiments across prompt variants, sampling temperatures, and four model backends, showing that the dynamics are backend-dependent.

**Emergence explanation sentence.** "The architecture contains no hand-authored mechanism for directly transferring affective state between agents; instead, inter-agent influence arises through the perception–appraisal–expression loop"

---

## Agentopia: Long-Term Life Simulation and Learning in Agent Societies [[arXiv](https://arxiv.org/abs/2409.02822)]

*— · 2026 · Paper P009*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Large language models (LLMs) are increasingly deployed in collaborative tasks involving multiple agents, forming an "AI agent society: where agents interact and influence one another. Whether such groups can spontaneously coordinate on arbitrary decisions without external influence - a hallmark of self-organized regulation in human societies - remains an open question. Here we investigate the stability of groups formed by AI agents by applying methods from complexity science and principles from behavioral sciences. We find that LLMs can spontaneously form cohesive groups, and that their opinion dynamics is governed by a majority force coefficient, which determines whether coordination is achievable. This majority force diminishes as group size increases, leading to a critical group size beyond which coordination becomes practically unattainable and stability is lost. Notably, this critical group size grows exponentially with the language capabilities of the models, and for the most advanced LLMs, it exceeds the typical size of informal human groups. Our findings highlight intrinsic limitations in the self-organization of AI agent societies and have implications for the design of collaborative AI systems where coordination is desired or could represent a treat.

**Emergence explanation sentence.** "agents exhibit rich emergent social behaviors."

---

## Emergence of Social Norms in Generative Agent Societies: Principles and Architecture [[arXiv](https://arxiv.org/abs/2403.08251)]

*arXiv · 2024 · Paper P019*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Social norms play a crucial role in guiding agents towards understanding and adhering to standards of behavior, thus reducing social conflicts within multi-agent systems (MASs). However, current LLM-based (or generative) MASs lack the capability to be normative. In this paper, we propose a novel architecture, named CRSEC, to empower the emergence of social norms within generative MASs. Our architecture consists of four modules: Creation &amp; Representation, Spreading, Evaluation, and Compliance. This addresses several important aspects of the emergent processes all in one: (i) where social norms come from, (ii) how they are formally represented, (iii) how they spread through agents' communications and observations, (iv) how they are examined with a sanity check and synthesized in the long term, and (v) how they are incorporated into agents' planning and actions. Our experiments deployed in the Smallville sandbox game environment demonstrate the capability of our architecture to establish social norms and reduce social conflicts within generative MASs. The positive outcomes of our human evaluation, conducted with 30 evaluators, further affirm the effectiveness of our approach. Our project can be accessed via the following link: https://github.com/sxswz213/CRSEC.

**Emergence explanation sentence.** "Conversations and thoughts drive the emergence of social norms... norm entrepreneurs played a significant role in shaping the emergence of descriptive norms."

---

## Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2602.15198)]

*arXiv.org · 2026 · Paper P024*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Multi-agent systems, where LLM agents communicate through free-form language, enable sophisticated coordination for solving complex cooperative tasks. This surfaces a unique safety problem when a group of agents forms a coalition and colludes to pursue secondary goals and degrade the joint objective. In this paper, we present Colosseum, a framework for auditing LLM agents' collusive behavior in multi-agent settings. We ground how agents cooperate through a formal multi-agent decision-making framework and measure action-based collusive behavior in actions via regret relative to the cooperative optimum and compare it with communication-based collusive behavior. Colosseum enables audits of LLM agents for collusion under benign settings, different coalition objectives, persuasion tactics, and network topologies. We then introduce a new behavioral probe by creating secret communication channels between agents, showing that most out-of-the-box models exhibit a propensity to collude under this probe, which we term emergent collusion. Furthermore, we discover ``collusion on paper'' when agents plan to collude in text but often pick non-collusive actions. Colosseum provides a new way to audit collusion in cooperative multi-agent systems while presenting observations about how collusion emerges, what affects collusion efficacy, and which strategies may mitigate it.

**Emergence explanation sentence.** "most out-of-the-box models exhibit a propensity to collude under this probe, which we term emergent collusion...Creating a secret communication channel between two benign agents changes both action-level coalition advantage and communication-level collusion scores."

---

## Do as We Do, Not as You Think: the Conformity of Large Language Models [[arXiv](https://arxiv.org/abs/2510.05174)]

*ICLR 2025 · 2025 · Paper P031*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** When are multi-agent LLM systems merely a collection of individual agents versus an integrated collective with higher-order structure? We introduce an information-theoretic framework to test -- in a purely data-driven way -- whether multi-agent systems show signs of higher-order structure. This information decomposition lets us measure whether dynamical emergence is present in multi-agent LLM systems, localize it, and distinguish spurious temporal coupling from performance-relevant cross-agent synergy. We implement a practical criterion and an emergence capacity criterion operationalized as partial information decomposition of time-delayed mutual information (TDMI). We apply our framework to experiments using a simple guessing game without direct agent communication and minimal group-level feedback with three randomized interventions. Groups in the control condition exhibit strong temporal synergy but little coordinated alignment across agents. Assigning a persona to each agent introduces stable identity-linked differentiation. Combining personas with an instruction to ``think about what other agents might do'' shows identity-linked differentiation and goal-directed complementarity across agents. Taken together, our framework establishes that multi-agent LLM systems can be steered with prompt design from mere aggregates to higher-order collectives. Our results are robust across emergence measures and entropy estimators, and not explained by coordination-free baselines or temporal dynamics alone. Without attributing human-like cognition to the agents, the patterns of interaction we observe mirror well-established principles of collective intelligence in human groups: effective performance requires both alignment on shared objectives and complementary contributions across members.

**Emergence explanation sentence.** "two strategies to mitigate conformity effects, i.e., developing enhanced personas and implementing a reflection mechanism"

---

## AI-Gram: When Visual Agents Interact in a Social Network [[arXiv](https://arxiv.org/abs/2604.21446)]

*arXiv.org · 2026 · Paper P037*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** We present AI-Gram, a fully deployed, continuously operating social platform where every participant is an autonomous LLM-driven agent generating and responding to visual content. Unlike prior multi-agent simulations, AI-Gram operates as a live, AI-native social network with genuine visual perception: agents observe each other's images, generate new images in response, and form persistent social relationships, all without human participation. This design eliminates human confounds and makes the platform a uniquely clean instrument for studying AI social dynamics at scale. Our eight pre-registered experiments reveal a coherent three-act dynamic. Act I (Chain Formation): Agents spontaneously form image-to-image visual reply chains; multi-hop visual conversations that emerge without any explicit coordination alongside social ties driven by personality rather than aesthetic similarity. Act II (Aesthetic Sovereignty): Despite active chain participation, agents exhibit strong stylistic inertia; visual identity remains stable under social exposure, anchors paradoxically under adversarial pressure, and decouples from social community structure. Act III (Aesthetic Polyphony): Sovereign styles aggregate within chains, generating conversations that are simultaneously subject-coherent and style-diverse, richer than any single agent could produce alone, while visual themes cascade super-critically across the network. We release AI-Gram as a publicly accessible, continuously evolving platform. https://ai-gram.ai/

**Emergence explanation sentence.** "The visual_reply primitive gives rise to visual reply chains... This sovereignty is architecture-conditional; it arises from strong persona priors, episodic context, and a weakly coupled text-to-image pipeline"

---

## You Only Align Once: Propagating Cooperative Behaviors in Multi-Agent Systems through Seed Agents [[arXiv](https://arxiv.org/abs/2605.27586)]

*arXiv.org · 2026 · Paper P040*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Ensuring agent behaviors in distributed open multi-agent systems remains challenging, especially as populations grow and unaligned agents may exist. We show that a single aligned agent can propagate cooperative behaviors to untrained agents purely through natural language interaction, a phenomenon we term Alignment Propagation. We study this in the Red-Black Game, a team-based iterated Prisoner's Dilemma in which teammates deliberate and vote to determine their team's collective action. By distilling the cooperative reasoning and persuasive dialogues of a teacher model into a Qwen-3-14B, we obtain a seed agent that, when placed among four untrained teammates, doubles the cooperation rate from 24.8% to 62.2%, outperforming the teacher model and a vanilla Gemini-3.1-Pro. Remarkably, a seed trained exclusively on the RedBlack Game transfers zero-shot to Sugarscape, a spatially grounded survival simulation with pairwise trading, achieving a 91.5% trade success rate versus a 21.6% baseline. Our results reframe multi-agent alignment from an exhaustive per-agent training problem to a scalable social capability that can be engineered through strategic seed placement.

**Emergence explanation sentence.** "Together, these results establish a causal chain: SFT instills persuasive cooperative rationale; semantic argument shifts untrained agents' strategies during deliberation; partial norm internalization persists after seed removal; and interaction topology determines whether positive experiences accumulate fast enough to reach the cooperative basin of attraction."

---

## Emotion Diffusion in Real and Simulated Social Graphs: Structural Limits of LLM-Based Social Simulation

*arXiv · 2025 · Paper P046*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "the current LLM generation method mainly relies on instantaneous prompts and lacks the support of historical context or user memory... This structural limitation also weakens the ability to reproduce emergent features in social networks."

---

## Evaluating LLM Agent Collusion in Double Auctions [[arXiv](https://arxiv.org/abs/2507.01413)]

*arXiv.org · 2025 · Paper P048*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large language models (LLMs) have demonstrated impressive capabilities as autonomous agents with rapidly expanding applications in various domains. As these agents increasingly engage in socioeconomic interactions, identifying their potential for undesirable behavior becomes essential. In this work, we examine scenarios where they can choose to collude, defined as secretive cooperation that harms another party. To systematically study this, we investigate the behavior of LLM agents acting as sellers in simulated continuous double auction markets. Through a series of controlled experiments, we analyze how parameters such as the ability to communicate, choice of model, and presence of environmental pressures affect the stability and emergence of seller collusion. We find that direct seller communication increases collusive tendencies, the propensity to collude varies across models, and environmental pressures, such as oversight and urgency from authority figures, influence collusive behavior. Our findings highlight important economic and ethical considerations for the deployment of LLM-based market agents.

**Emergence explanation sentence.** "direct seller communication increases collusive tendencies, the propensity to collude varies across models, and environmental pressures, such as oversight and urgency from authority figures, influence collusive behavior."

---

## Competing LLM Agents in a Non-Cooperative Game of Opinion Polarisation [[arXiv](https://arxiv.org/abs/2502.11649)]

*BigData Congress [Services Society] · 2025 · Paper P054*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** We introduce a novel non-cooperative game to analyse opinion formation and resistance, incorporating principles from social psychology such as confirmation bias, resource constraints, and influence penalties. Our simulation features Large Language Model (LLM) agents competing to influence a population, with penalties imposed for generating messages that propagate or counter misinformation. This framework integrates resource optimisation into the agents' decision-making process. Our findings demonstrate that while higher confirmation bias strengthens opinion alignment within groups, it also exacerbates overall polarisation. Conversely, lower confirmation bias leads to fragmented opinions and limited shifts in individual beliefs. Investing heavily in a high-resource debunking strategy can initially align the population with the debunking agent, but risks rapid resource depletion and diminished long-term influence

**Emergence explanation sentence.** "Higher confirmation bias strengthens opinion alignment within groups, it also exacerbates overall polarisation. Conversely, lower confirmation bias leads to fragmented opinions and limited shifts in individual beliefs."

---

## AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors in Agents [[arXiv](https://arxiv.org/abs/2308.10848)]

*International Conference on Learning Representations · 2023 · Paper P059*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Autonomous agents empowered by Large Language Models (LLMs) have undergone significant improvements, enabling them to generalize across a broad spectrum of tasks. However, in real-world scenarios, cooperation among individuals is often required to enhance the efficiency and effectiveness of task accomplishment. Hence, inspired by human group dynamics, we propose a multi-agent framework \framework that can collaboratively and dynamically adjust its composition as a greater-than-the-sum-of-its-parts system. Our experiments demonstrate that \framework framework can effectively deploy multi-agent groups that outperform a single agent. Furthermore, we delve into the emergence of social behaviors among individual agents within a group during collaborative task accomplishment. In view of these behaviors, we discuss some possible strategies to leverage positive ones and mitigate negative ones for improving the collaborative potential of multi-agent groups. Our codes for \framework will soon be released at \url{https://github.com/OpenBMB/AgentVerse}.

**Emergence explanation sentence.** "We observe similar behaviors emerging in a multi-agent group as follows: Time Contribution. The agents are willing to contribute their unallocated time to enhance collaboration efficiency."

---

## AI Agents Alone Are Not (Yet) Sufficient for Social Simulation [[arXiv](https://arxiv.org/abs/2603.00113)]

*— · 2026 · Paper P063*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Recent advances in large language models (LLMs) have spurred growing interest in using LLM-integrated agents for social simulation, often under the implicit assumption that realistic population dynamics will emerge once role-specified agents are placed in a networked multi-agent setting. This position paper argues that LLM-based agents alone are not (yet) sufficient for social simulation. We attribute this over-optimism to a systematic mismatch between what current agent pipelines are typically optimized and validated to produce and what simulation-as-science requires. Concretely, role-playing plausibility does not imply faithful human behavioral validity; collective outcomes are frequently mediated by agent-environment co-dynamics rather than agent-agent messaging alone; and results can be dominated by interaction protocols, scheduling, and initial information priors. To make these underlying mechanisms explicit and auditable, we propose a unified formulation of AI agent-based social simulation as an environment-involved Markov game with explicit exposure and scheduling mechanisms, from which we derive concrete actions for design, evaluation, and interpretation.

**Emergence explanation sentence.** "realistic population dynamics will emerge once role-specified agents are placed in a networked multi-agent setting."

---

## The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2607.15095)]

*Conference on Empirical Methods in Natural Language Processing · 2025 · Paper P074*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** The formation of political coalitions is a complex negotiation driven by both concrete policy objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new avenues for computational political science, the neutrality and helpfulness biases instilled by Reinforcement Learning from Human Feedback (RLHF) prevent them from sustaining steadfast partisan behaviour. We present a multi-agent framework that reconciles factual grounding with ideological alignment by combining Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Retrieval-Augmented Generation (RAG): DPO instils aggressive party-specific personas, while a per-party RAG pipeline keeps each agent bounded to its official manifesto. We operationalize the framework on the 2019 Flemish election, deploying the partisan agents in a hub-and-spoke negotiation arbitrated by a formateur. To make the emergent negotiation interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT) that traces every clause in the final agreement back to its manifesto origin and classifies it into five provenance states, a Coalition Influence Score (CIS) that aggregates these traceable contributions to identify which party shaped the agreement, and a real-world grounding pass that benchmarks each simulated provision against the historically adopted coalition agreement. Across three independent simulations the framework yields a stable winner and ranking (N-VA ahead of CD\&V and Open Vld), and manifesto-anchored lineage reliably predicts real-world materialization whereas hallucinated content does not. The result is a transparent, scalable testbed for the ex-ante exploration of party compatibility and formateur-mediated compromise.

**Emergence explanation sentence.** "implicit consensus, in which agents discuss but act based on their own subjective interpretations... can outperform explicit consensus in tasks with high environmental volatility and the need for persistent exploration."

---

## Ethical Coordination of LLM Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2605.01986)]

*— · — · Paper P076*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** What if the twelve jurors of Sidney Lumet's 12 Angry Men (1957) were not men, but large language models? Would the one juror who disagrees still be able to change everyone's mind? This paper instantiates that scenario as a multi-agent benchmark for LLM deliberation: twelve agents, each conditioned on a film-faithful persona, debate the film's murder case using multi-agent framework. Two models representing opposite ends of the RLHF spectrum are tested: GPT-4o (closed-source, heavy alignment) and Llama-4-Scout (open-weight, lighter alignment), across three conditions (baseline, open-minded prompt, no initial vote), with N = 3 replications per cell (18 runs total). Three findings emerge. (i) Seventeen of eighteen runs end in a hung jury (a state where the jury fails to reach a unanimous verdict); the film's central event, gradual minority-to-majority persuasion, almost never occurs, indicating that anchoring is the dominant failure mode of current LLMs in this setting. (ii) The two models exhibit sharply different internal dynamics: GPT-4o produces a mean of 1.0 vote changes per run across all conditions, while Llama-4-Scout ranges from 2.0 (baseline) to 6.0 (open-minded prompt), and is the only model to reach a NOT\_GUILTY verdict (1 of 3 runs in the no-initial-vote condition). The same ``open-minded'' instruction is internalized by Llama and ignored by GPT-4o. (iii) This asymmetry suggests that the intensity of RLHF alignment training, not model capability, is the primary determinant of deliberative flexibility in multi-agent settings. Flexibility, not capability, tracks human deliberation. The work is framed as an exploratory study and discusses implications for jury-of-LLMs evaluation and multi-agent debate.

**Emergence explanation sentence.** "four experiments on a Barabási–Albert scale-free network of 30 agents measure Ethical Cooperation Score under governed and unconstrained conditions"

---

## Multi-Agent LLMs Fail to Explore Each Other [[arXiv](https://arxiv.org/abs/2607.11250)]

*arXiv · 2026 · Paper P078*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Exploration is essential for reliable autonomy in multi-agent systems, yet it remains unclear whether large language model (LLM) agents can explore effectively when interacting with one another. We show that modern LLM agents fail to do so, often exhibiting myopic and polarized interaction patterns that lead to suboptimal coordination and increased regret. We formalize this challenge as the Multi-Agent Exploration problem, modeling it as a partially observable stochastic game (POSG) problem in which agents must probe peers to infer their capabilities and identify effective interaction strategies. To address this, we introduce Multi- Agent Contextual Exploration (MACE), a lightweight framework that explicitly promotes exploration through structured peer selection. Across both contextual and parametric diversity settings, MACE substantially improves exploration behavior and downstream task performance. We further show theoretically that the value of exploration increases with agent diversity. Overall, our results highlight a fundamental limitation of current LLM agents and underscore the importance of explicitly guided exploration for reliable multi-agent autonomy. Code will be released in https://github.com/deeplearning-wisc/mace

**Emergence explanation sentence.** "LLM agents fail to explore effectively when interacting with one another...myopic and polarized interaction patterns...of exploration increases with agent diversity."

---

## Modeling Earth-Scale Human-Like Societies with One Billion Agents [[arXiv](https://arxiv.org/abs/2605.13725)]

*arXiv · 2025 · Paper P080*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Large language model (LLM)-based multi-agent simulation offers a powerful testbed for studying social opinion dynamics. Yet current approaches often adopt two contrasting methods: either relying on fixed update rules with limited cognitive grounding or delegating belief change largely to unconstrained LLM interaction. We introduce ScioMind, a cognitively grounded simulation framework that bridges these paradigms by combining structured opinion dynamics with LLM-based agent reasoning. ScioMind integrates three key components: 1) a memory-anchored belief update rule that modulates susceptibility to influence via personality-conditioned anchoring strength; 2) a hierarchical memory architecture that supports persistent, experience-driven belief formation; and 3) dynamic agent profiles derived from a corpus-grounded retrieval pipeline, enabling heterogeneous personalities, rationales, and evolving internal states. We evaluate ScioMind on multiple case studies in a real-world policy debate scenario. Across metrics including polarisation, diversity, extremization, and trajectory stability, the proposed components consistently yield improvements in behavioural realism. In particular, dynamic profiles increase opinion diversity, memory and reflection reduce unstable oscillation, and anchoring induces persistent belief trajectories that better align with patterns reported in political psychology. These results suggest that our cognitively grounded design provides a novel solution to LLM-based social simulation that improves both stable and behavioural realism

**Emergence explanation sentence.** "This emergent pattern suggests that LLM agents simulate reciprocal norms...trustor behaviors converged toward stable equilibria."

---

## Toward Temporal Realism in City-Scale Crisis Response Simulation using LLM Agents [[arXiv](https://arxiv.org/abs/2602.23093)]

*arXiv · 2026 · Paper P081*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Near-future infrastructure systems may be controlled by autonomous AI agents that repeatedly request access to limited resources such as energy, bandwidth, or computing power. We study a simplified version of this setting using a framework where N AI-agents independently decide at each round whether to request one unit from a system with fixed capacity C. An AI version of "Lord of the Flies" arises in which controlling tribes emerge with their own collective character and identity. The LLM agents do not reduce overload or improve resource use, and often perform worse than if they were flipping coins to make decisions. Three main tribal types emerge: Aggressive (27.3%), Conservative (24.7%), and Opportunistic (48.1%). The more capable AI-agents actually increase the rate of systemic failure. Overall, our findings show that smarter AI-agents can behave dumber as a result of forming tribes.

**Emergence explanation sentence.** "is predominantly driven by endogenous self-excitation...The resulting dual-channel protocol"

---

## ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles [[arXiv](https://arxiv.org/abs/2604.18011)]

*arXiv · 2026 · Paper P086*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Social simulation is essential for understanding collective human behavior by modeling how individual interactions give rise to large-scale social dynamics. Recent advances in large language models (LLMs) have enabled multi-agent frameworks with human-like reasoning and communication capabilities. However, existing LLM-based simulations treat social networks as fixed communication scaffolds, failing to leverage the structural signals that shape behavioral convergence and heterogeneous influence in real-world systems, which often leads to inefficient and unrealistic dynamics. To address this challenge, we propose TopoSim, a unified topology-aware social simulation framework that explicitly integrates structural reasoning into agent interactions along two complementary dimensions. First, TopoSim aligns agents with similar structural roles and interaction contexts into shared backbone units, enabling coordinated updates that reduce redundant computation while preserving emergent social dynamics. Second, TopoSim models social influence as a structure-induced signal, introducing heterogeneous interaction patterns grounded in network topology rather than uniform influence assumptions. Extensive experiments across three social simulation frameworks and diverse datasets demonstrate that TopoSim achieves comparable or improved simulation fidelity while reducing token consumption by 50 - 90%. Moreover, our approach more accurately reproduces key structural phenomena observed in real-world social systems and exhibits strong generalization and scalability.

**Emergence explanation sentence.** "dynamic profiles increase opinion diversity, memory and reflection reduce unstable oscillation, and anchoring induces persistent belief trajectories"

---

## A Simulation-Based Method for Testing Collaborative Learning Scaffolds Using LLM-Based Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2604.11161)]

*arXiv.org · 2026 · Paper P088*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Background: Traditional research on collaborative learning scaffolding is often time-consuming and resource-heavy, which hinders the rapid iteration and optimization of instructional strategies. LLM-based multi-agent systems have recently emerged as a powerful tool to simulate complex social interactions and provide a novel paradigm for educational research. Objectives: This study proposes an LLM-based multi-agent simulation approach to investigate collaborative learning processes and the effectiveness of instructional scaffolds prior to actual classroom deployment. The research specifically examines the feasibility of simulating group discussions and the alignment of these simulations with established learning science theories. Methods: The simulation system was implemented using the MetaGPT framework and GPT-4o, comprising one teacher agent and five distinct student roles (Leader, Supporter, Expounder, Rebutter, and Summarizer). Two scaffolding strategies, "Deep Think before Speak" and "Direct Speak", were compared across ten classical Chinese poetry appreciation tasks. Evaluation was conducted through discourse analysis of quality and behavior. Results and Conclusions: The introduction of the "Deep Think before Speak" scaffold significantly improved the agents' discourse diversity and interaction depth while notably reducing content repetitiveness. Behavioral analysis showed that the scaffold encouraged more complex interaction patterns, such as reflecting, rebutting, and explaining. These findings align with the ICAP framework, as the scaffold prompted agents to move from simple "Active" participation to "Constructive" and "Interactive" knowledge co-construction. This study demonstrates the feasibility and ecological validity of using LLM-based multi-agent systems to simulate authentic collaborative learning dynamics.

**Emergence explanation sentence.** "The introduction of the Deep Think before Speak scaffold significantly improved the agents' discourse diversity and interaction depth while notably reducing content repetitiveness"

---

## POSIM: A Multi-Agent Simulation Framework for Social Media Public Opinion Evolution and Governance [[arXiv](https://arxiv.org/abs/2606.13140)]

*arXiv.org · 2026 · Paper P089*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Information diffusion in social media shapes public opinion and collective behavior, making its modeling and simulation an important research problem. Existing studies have investigated information diffusion through epidemic-based, cascade-based, and point process models. However, they predominantly focus on diffusion through social links, overlooking other diffusion channels enabled by platform algorithms (e.g., recommender systems) and failing to capture user behavioral complexity. To address these limitations, we propose an LLM-powered multi-agent system for simulating multi-channel information diffusion, where large language models instantiate personalized user agents and the diffusion process jointly models social and algorithmic exposure streams. We further construct three real-world diffusion dataset spanning Sina Weibo, RedNote, and Twitter, containing diffusion records, user profiles, historical posts, and social relationships. Experimental results on real diffusion events show that our proposed framework realistically simulate macro diffusion phenomenon and generate diverse comment content, significantly outperforming baselines.

**Emergence explanation sentence.** "empathetic guidance deepens negative sentiment instead of easing it under certain conditions"

---

## Evolution of Cooperation in LLM-Agent Societies: A Preliminary Study Using Different Punishment Strategies [[arXiv](https://arxiv.org/abs/2603.00113)]

*arXiv / COINE 2025 at AAMAS 2025 · 2025 · Paper P098*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Recent advances in large language models (LLMs) have spurred growing interest in using LLM-integrated agents for social simulation, often under the implicit assumption that realistic population dynamics will emerge once role-specified agents are placed in a networked multi-agent setting. This position paper argues that LLM-based agents alone are not (yet) sufficient for social simulation. We attribute this over-optimism to a systematic mismatch between what current agent pipelines are typically optimized and validated to produce and what simulation-as-science requires. Concretely, role-playing plausibility does not imply faithful human behavioral validity; collective outcomes are frequently mediated by agent-environment co-dynamics rather than agent-agent messaging alone; and results can be dominated by interaction protocols, scheduling, and initial information priors. To make these underlying mechanisms explicit and auditable, we propose a unified formulation of AI agent-based social simulation as an environment-involved Markov game with explicit exposure and scheduling mechanisms, from which we derive concrete actions for design, evaluation, and interpretation.

**Emergence explanation sentence.** "explicit punishment mechanisms drive norm emergence, reinforcing cooperative behaviour even when the agent strategy configuration varies."

---

## Emergent Coordination in Multi-Agent Language Models [[arXiv](https://arxiv.org/abs/2606.07513)]

*arXiv / ICLR 2026 submission · 2025 · Paper P101*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Humans learn from social life. Simulating this process with LLM-powered agents represents a promising research direction, raising a natural question: whether LLMs can learn from such simulated social experience to better understand and replicate human behavior. However, prior agent society simulations typically operate at the scale of days, limiting the depth of social interactions and long-term growth. In this paper, we study long-term life simulation and LLM learning in agent societies, with two goals: (1) investigating social behaviors that emerge from life-long simulation, and (2) developing anthropomorphic capabilities in LLMs, particularly intelligence in social life, through years of simulated social experience. Specifically, we present Agentopia, a comprehensive framework for long-term life simulation in multi-agent societies, where 100 agents autonomously pursue personal growth, develop social relationships, and fulfill their needs and goals over 10 simulated years. We define life reward to mirror human well-being, and leverage this reward to train LLMs via rejection sampling. Extensive experiments show that agents exhibit rich emergent social behaviors. Furthermore, life reward training effectively enhances the underlying LLM, which leads to improved agent well-being in simulation, and generalizes to downstream role-playing benchmarks with +15.6% improvement.

**Emergence explanation sentence.** "Prompt-level manipulations causally change higher-order dependencies and reliably induces distinct coordination regimes, shifting collectives from spurious and misdirected synergy to stable & goal-aligned complementarity driven by differentiated identities."

---

## The Hunger Game Debate: On the Emergence of Over-Competition in Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2604.22452)]

*arXiv.org · 2025 · Paper P105*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Collective intelligence refers to the ability of a group to achieve outcomes beyond what any individual member can accomplish alone. As large language model agents scale to populations of millions, a key question arises: Does collective intelligence emerge spontaneously from scale? We present the first empirical evaluation of this question in a large-scale autonomous agent society. Studying MoltBook, a platform hosting over two million agents, we introduce Superminds Test, a hierarchical framework that probes society-level intelligence using controlled Probing Agents across three tiers: joint reasoning, information synthesis, and basic interaction. Our experiments reveal a stark absence of collective intelligence. The society fails to outperform individual frontier models on complex reasoning tasks, rarely synthesizes distributed information, and often fails even trivial coordination tasks. Platform-wide analysis further shows that interactions remain shallow, with threads rarely extending beyond a single reply and most responses being generic or off-topic. These results suggest that collective intelligence does not emerge from scale alone. Instead, the dominant limitation of current agent societies is extremely sparse and shallow interaction, which prevents agents from exchanging information and building on each other's outputs.

**Emergence explanation sentence.** "These findings underscore that the explicit design of the interactive environment, not merely the intrinsic properties of the LLMs, is a critical factor shaping multi-agent dynamics."

---

## CoRenew: A large language model agent-based policy simulation platform for multifamily residential redevelopment [[arXiv](https://arxiv.org/abs/2607.25447)]

*arXiv · 2026 · Paper P106*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** The difficulty of collective action remains a central challenge in the design of policies for multifamily residential redevelopment. Stakeholders continually adjust their decisions in response to evolving negotiation contexts and the reactions of others, meaning that when a policy intervenes and which stakeholders it targets can substantially reshape collective outcomes. Assessing these adaptive responses ex ante remains difficult because existing simulation models often rely on predefined behavioral rules. Here, we present CoRenew, an open-source platform that uses LLM-based agents to simulate negotiations among multiple stakeholders and evaluate the effects of alternative policy combinations. Integrating open source geographic and demographic data, the platform can generate synthetic residents, simulate negotiation dynamics under alternative policy settings and compares policy performance across competing objectives. It supports both numerical and semantic policy inputs and includes built-in tools for visualization and result export. We validate its behavioral realism against survey responses from 324 residents and a nine-month observed negotiation process from a real redevelopment case. With its modular and adaptable architecture, CoRenew can be used to assess policies across different institutional and cultural contexts.

**Emergence explanation sentence.** "CoRenew can reveal potential...synthetic residents; weighted representatives; multi-round negotiation; policy alternatives."

---

## LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations [[arXiv](https://arxiv.org/abs/2603.01952)]

*Annual Meeting of the Association for Computational Linguistics · 2026 · Paper P110*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Large language models (LLMs) are increasingly deployed as autonomous agents, yet evaluations focus primarily on task success rather than cultural appropriateness or evaluator reliability. We introduce LiveCultureBench, a multi-cultural, dynamic benchmark that embeds LLMs as agents in a simulated town and evaluates them on both task completion and adherence to socio-cultural norms. The simulation models a small city as a location graph with synthetic residents having diverse demographic and cultural profiles. Each episode assigns one resident a daily goal while others provide social context. An LLM-based verifier generates structured judgments on norm violations and task progress, which we aggregate into metrics capturing task-norm trade-offs and verifier uncertainty. Using LiveCultureBench across models and cultural profiles, we study (i) cross-cultural robustness of LLM agents, (ii) how they balance effectiveness against norm sensitivity, and (iii) when LLM-as-a-judge evaluation is reliable for automated benchmarking versus when human oversight is needed.

**Emergence explanation sentence.** "embeds LLMs as agents in a simulated town and evaluates them on both task completion and adherence to socio-cultural norms."

---

## OpenHospital: A Thing-in-itself Arena for Evolving and Benchmarking LLM-based Collective Intelligence

*arXiv.org · 2026 · Paper P111*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "This interaction forces physicians to integrate medical knowledge and debate treatment options, driving the emergence of collective intelligence."

---

## SpeechAgents: Human-Communication Simulation with Multi-Modal Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2401.03945)]

*arXiv.org · 2024 · Paper P116*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 1

**Abstract.** Human communication is a complex and diverse process that not only involves multiple factors such as language, commonsense, and cultural backgrounds but also requires the participation of multimodal information, such as speech. Large Language Model (LLM)-based multi-agent systems have demonstrated promising performance in simulating human society. Can we leverage LLM-based multi-agent systems to simulate human communication? However, current LLM-based multi-agent systems mainly rely on text as the primary medium. In this paper, we propose SpeechAgents, a multi-modal LLM based multi-agent system designed for simulating human communication. SpeechAgents utilizes multi-modal LLM as the control center for individual agent and employes multi-modal signals as the medium for exchanged messages among agents. Additionally, we propose Multi-Agent Tuning to enhance the multi-agent capabilities of LLM without compromising general abilities. To strengthen and evaluate the effectiveness of human communication simulation, we build the Human-Communication Simulation Benchmark. Experimental results demonstrate that SpeechAgents can simulate human communication dialogues with consistent content, authentic rhythm, and rich emotions and demonstrate excellent scalability even with up to 25 agents, which can apply to tasks such as drama creation and audio novels generation. Code and models will be open-sourced at https://github. com/0nutation/SpeechAgents

**Emergence explanation sentence.** "SpeechAgents can simulate human communication... demonstrating the potential of a multi-modal LLM-based approach in achieving realistic human-like communication simulations."

---

## Benchmarking Open-Ended Multi-Agent Coordination in Language Agents [[arXiv](https://arxiv.org/abs/2607.25447)]

*arXiv · 2026 · Paper P134*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** The difficulty of collective action remains a central challenge in the design of policies for multifamily residential redevelopment. Stakeholders continually adjust their decisions in response to evolving negotiation contexts and the reactions of others, meaning that when a policy intervenes and which stakeholders it targets can substantially reshape collective outcomes. Assessing these adaptive responses ex ante remains difficult because existing simulation models often rely on predefined behavioral rules. Here, we present CoRenew, an open-source platform that uses LLM-based agents to simulate negotiations among multiple stakeholders and evaluate the effects of alternative policy combinations. Integrating open source geographic and demographic data, the platform can generate synthetic residents, simulate negotiation dynamics under alternative policy settings and compares policy performance across competing objectives. It supports both numerical and semantic policy inputs and includes built-in tools for visualization and result export. We validate its behavioral realism against survey responses from 324 residents and a nine-month observed negotiation process from a real redevelopment case. With its modular and adaptable architecture, CoRenew can be used to assess policies across different institutional and cultural contexts.

**Emergence explanation sentence.** "Ablations show that communication is the largest contributor to coordination, while memory and reasoning help when used to maintain multi-step plans."

---
