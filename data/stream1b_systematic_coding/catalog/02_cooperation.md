# Cooperation & Social Dilemmas

*Emergence of cooperation, prosocial behavior, and social dilemma resolution*

**33 papers**

---

## Three AI-agents walk into a bar . . . . `Lord of the Flies' tribalism emerges among smart AI-Agents [[arXiv](https://arxiv.org/abs/2602.23093)]

*arXiv · 2026 · Paper P008*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Near-future infrastructure systems may be controlled by autonomous AI agents that repeatedly request access to limited resources such as energy, bandwidth, or computing power. We study a simplified version of this setting using a framework where N AI-agents independently decide at each round whether to request one unit from a system with fixed capacity C. An AI version of "Lord of the Flies" arises in which controlling tribes emerge with their own collective character and identity. The LLM agents do not reduce overload or improve resource use, and often perform worse than if they were flipping coins to make decisions. Three main tribal types emerge: Aggressive (27.3%), Conservative (24.7%), and Opportunistic (48.1%). The more capable AI-agents actually increase the rate of systemic failure. Overall, our findings show that smarter AI-agents can behave dumber as a result of forming tribes.

**Emergence explanation sentence.** "An AI version of Lord of the Flies arises in which controlling tribes emerge with their own collective character and identity"

---

## When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs

*arXiv · 2026 · Paper P014*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "Collective intelligence arises from interactions among individual agents...any coordination must emerge from interaction-driven in-context learning alone."

---

## CONSCIENTIA: Can LLM Agents Learn to Strategize? Emergent Deception and Trust in a Multi-Agent NYC Simulation [[arXiv](https://arxiv.org/abs/2604.09746)]

*arXiv · 2026 · Paper P016*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** As large language models (LLMs) are increasingly deployed as autonomous agents, understanding how strategic behavior emerges in multi-agent environments has become an important alignment challenge. We take a neutral empirical stance and construct a controlled environment in which strategic behavior can be directly observed and measured. We introduce a large-scale multi-agent simulation in a simplified model of New York City, where LLM-driven agents interact under opposing incentives. Blue agents aim to reach their destinations efficiently, while Red agents attempt to divert them toward billboard-heavy routes using persuasive language to maximize advertising revenue. Hidden identities make navigation socially mediated, forcing agents to decide when to trust or deceive. We study policy learning through an iterative simulation pipeline that updates agent policies across repeated interaction rounds using Kahneman-Tversky Optimization (KTO). Blue agents are optimized to reduce billboard exposure while preserving navigation efficiency, whereas Red agents adapt to exploit remaining weaknesses. Across iterations, the best Blue policy improves task success from 46.0% to 57.3%, although susceptibility remains high at 70.7%. Later policies exhibit stronger selective cooperation while preserving trajectory efficiency. However, a persistent safety-helpfulness trade-off remains: policies that better resist adversarial steering do not simultaneously maximize task completion. Overall, our results show that LLM agents can exhibit limited strategic behavior, including selective trust and deception, while remaining highly vulnerable to adversarial persuasion.

**Emergence explanation sentence.** "iterative alignment changes not just top-line performance, but the strategic structure of agent interactions"

---

## The Traitors: Deception and Trust in Multi-Agent Language Model Simulations [[arXiv](https://arxiv.org/abs/2504.19487)]

*arXiv.org · 2025 · Paper P026*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** The evolution of cooperation has been extensively studied using abstract mathematical models and simulations. Recent advances in Large Language Models (LLMs) and the rise of LLM agents have demonstrated their ability to perform social reasoning, thus providing an opportunity to test the emergence of norms in more realistic agent-based simulations with human-like reasoning using natural language. In this research, we investigate whether the cooperation dynamics presented in Boyd and Richerson's model persist in a more realistic simulation of the Diner's Dilemma using LLM agents compared to the abstract mathematical nature in the work of Boyd and Richerson. Our findings indicate that agents follow the strategies defined in the Boyd and Richerson model, and explicit punishment mechanisms drive norm emergence, reinforcing cooperative behaviour even when the agent strategy configuration varies. Our results suggest that LLM-based Multi-Agent System simulations, in fact, can replicate the evolution of cooperation predicted by the traditional mathematical models. Moreover, our simulations extend beyond the mathematical models by integrating natural language-driven reasoning and a pairwise imitation method for strategy adoption, making them a more realistic testbed for cooperative behaviour in MASs.

**Emergence explanation sentence.** "The Traitors environment exhibits rich emergent behaviors driven by the strategic imperatives of traitor and faithful agents."

---

## Network Effects and Agreement Drift in LLM Debates [[arXiv](https://arxiv.org/abs/2604.11312)]

*arXiv · 2026 · Paper P028*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Large Language Models (LLMs) have demonstrated an unprecedented ability to simulate human-like social behaviors, making them useful tools for simulating complex social systems. However, it remains unclear to what extent these simulations can be trusted to accurately capture key social mechanisms, particularly in highly unbalanced contexts involving minority groups. This paper uses a network generation model with controlled homophily and class sizes to examine how LLM agents behave collectively in multi-round debates. Moreover, our findings highlight a particular directional susceptibility that we term \textit{agreement drift}, in which agents are more likely to shift toward specific positions on the opinion scale. Overall, our findings highlight the need to disentangle structural effects from model biases before treating LLM populations as behavioral proxies for human groups.

**Emergence explanation sentence.** "heterogeneous networks allow this bias to propagate and produce rapid convergence, whereas homophily and large disagreeing majorities limit cross-opinion encounters and lead to persistent polarization."

---

## Exploring the Topology and Memory of Consensus: How LLM Agents Agree, Fragment, or Settle When Forming Conventions [[arXiv](https://arxiv.org/abs/2606.04197)]

*arXiv · 2026 · Paper P032*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** How much should an LLM agent remember, and how should multi-agent systems be connected when trying to reach consensus? We show these two design choices interact in a way that flips the sign of memory's effect on coordination. Across 432 simulation runs of a networked Naming Game on eight fixed 16-agent topologies, we vary memory depth and network structure. Longer memory slows the time to reach steady state in decentralized networks but accelerates it in centralized ones; the same parameter pushes the system in opposite directions depending on topology. Critically, "faster settling" in centralized networks means locking in to a fragmented plateau more quickly, not reaching system-wide consensus, which can be used to generate diverging opinions. We further document a memory-mediated speed-unity trade-off: centralized networks consistently preserve more competing conventions than decentralized networks, but their settling speed depends sharply on memory. At the agent level, within-network analyses show that high-betweenness bridges suffer a brokerage penalty while agents in locally clustered neighborhoods achieve higher coordination success. Finally, in search of analytically tractable generative mechanisms, we find that agents' choices are well captured by Fictitious Play, indicating belief-based rather than reward-based adaptation. The practical implication: memory depth and communication topology should be co-designed, not optimized in isolation.

**Emergence explanation sentence.** "these two design choices interact in a way that flips the sign of memory's effect on coordination"

---

## Group Selection Promotes Prosocial Prompts in Populations of LLM Agents [[arXiv](https://arxiv.org/abs/2606.23343)]

*arXiv · 2026 · Paper P033*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Current approaches to instill prosociality in large language model (LLM) agents often rely on humans specifying desired behaviors at the individual level, which does not guarantee cooperation within LLM populations. As frontier training shifts toward individual rewards for verifiable tasks, such as mathematics and coding, this outcome-based focus may further undermine cooperation in multi-agent settings. Large-scale cooperation in human populations emerged via unguided evolutionary mechanisms, not a central architect. Group selection, in which cooperative groups within a population outcompete less cooperative ones, has been argued to be essential. In this study, we explore whether group selection can promote cooperation in populations of LLM agents. We introduce a multi-agent simulation framework in which LLM agents play a repeated social dilemma game and transmit their natural-language prompts across generations under either individual- or group-level selection. Under group selection, prompts from high-performing groups are transmitted, thereby promoting prosociality and stabilizing cooperation. Under individual selection, self-interested prompts dominate, causing populations to collapse into collective defection. This gap is robust across prompt ablations, alternative game framings, and model swaps. We theoretically reproduce key results using a replicator-mutator model, whose empirical transmission kernel predicts a phase transition at a critical threshold. Preliminary findings show that, when informed about the selection mechanism, GPT-5.4 preemptively and gradually adjusts first-generation donations. This demonstrates strong anticipatory behavior that was not observed in the other tested models. These results demonstrate that prosocial prompts and cooperative behaviors evolve in LLM agent populations under group selection.

**Emergence explanation sentence.** "Under group selection, prompts from high-performing groups are transmitted, thereby promoting prosociality and stabilizing cooperation"

---

## Prompt Optimization Enables Stable Algorithmic Collusion in LLM Agents [[arXiv](https://arxiv.org/abs/2604.17774)]

*arXiv · 2026 · Paper P034*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** LLM agents in markets present algorithmic collusion risks. While prior work shows LLM agents reach supracompetitive prices through tacit coordination, existing research focuses on hand-crafted prompts. The emerging paradigm of prompt optimization necessitates new methodologies for understanding autonomous agent behavior. We investigate whether prompt optimization leads to emergent collusive behaviors in market simulations. We propose a meta-learning loop where LLM agents participate in duopoly markets and an LLM meta-optimizer iteratively refines shared strategic guidance. Our experiments reveal that meta-prompt optimization enables agents to discover stable tacit collusion strategies with substantially improved coordination quality compared to baseline agents. These behaviors generalize to held-out test markets, indicating discovery of general coordination principles. Analysis of evolved prompts reveals systematic coordination mechanisms through stable shared strategies. Our findings call for further investigation into AI safety implications in autonomous multi-agent systems.

**Emergence explanation sentence.** "meta-prompt optimization enables agents to discover stable tacit collusion strategies with substantially improved coordination quality compared to baseline agents"

---

## Evaluating Collective Behaviour of Hundreds of LLM Agents [[arXiv](https://arxiv.org/abs/2602.16662)]

*arXiv.org · 2026 · Paper P039*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** LLM-powered AI assistants acting on behalf of users can produce poor collective outcomes at scale. We introduce a framework for evaluating their emergent behaviour in social dilemmas, applied to three iterated games (Public Goods, Collective Risk, Common Pool Resource). We prompt each model to produce a natural-language strategy, then have the same model translate it into code. This aims to isolate strategic reasoning from input-parsing, enables pre-deployment inspection, and scales to populations of hundreds of agents. We propose three analyses: behavioural fingerprinting via exhaustive evaluation over opponent histories; self-play robustness across mixtures of a model's strategies with either a Selfish or Collective disposition; and cultural evolution under payoff-biased imitation. Applied to three state-of-the-art LLMs, we find substantial cross-model differences in self-play welfare, and that cultural evolution converges to low-welfare, Selfish-dominant equilibria in larger groups.

**Emergence explanation sentence.** "cultural evolution under payoff-biased imitation converges to low-welfare, Selfish-dominant equilibria in larger groups."

---

## Herd Behavior: Investigating Peer Influence in LLM-based Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2505.21588)]

*arXiv · 2025 · Paper P043*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Recent advancements in Large Language Models (LLMs) have enabled the emergence of multi-agent systems where LLMs interact, collaborate, and make decisions in shared environments. While individual model behavior has been extensively studied, the dynamics of peer influence in such systems remain underexplored. In this paper, we investigate herd behavior, the tendency of agents to align their outputs with those of their peers, within LLM-based multi-agent interactions. We present a series of controlled experiments that reveal how herd behaviors are shaped by multiple factors. First, we show that the gap between self-confidence and perceived confidence in peers significantly impacts an agent's likelihood to conform. Second, we find that the format in which peer information is presented plays a critical role in modulating the strength of herd behavior. Finally, we demonstrate that the degree of herd behavior can be systematically controlled, and that appropriately calibrated herd tendencies can enhance collaborative outcomes. These findings offer new insights into the social dynamics of LLM-based systems and open pathways for designing more effective and adaptive multi-agent collaboration frameworks.

**Emergence explanation sentence.** "self-confidence and perceived confidence in peers significantly impacts an agent's likelihood to conform... the format in which peer information is presented plays a critical role in modulating the strength of herd behavior."

---

## Reproducibility Study of "Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents" [[arXiv](https://arxiv.org/abs/2404.16698)]

*arXiv.org · 2025 · Paper P051*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** As AI systems pervade human life, ensuring that large language models (LLMs) make safe decisions remains a significant challenge. We introduce the Governance of the Commons Simulation (GovSim), a generative simulation platform designed to study strategic interactions and cooperative decision-making in LLMs. In GovSim, a society of AI agents must collectively balance exploiting a common resource with sustaining it for future use. This environment enables the study of how ethical considerations, strategic planning, and negotiation skills impact cooperative outcomes. We develop an LLM-based agent architecture and test it with the leading open and closed LLMs. We find that all but the most powerful LLM agents fail to achieve a sustainable equilibrium in GovSim, with the highest survival rate below 54%. Ablations reveal that successful multi-agent communication between agents is critical for achieving cooperation in these cases. Furthermore, our analyses show that the failure to achieve sustainable cooperation in most LLMs stems from their inability to formulate and analyze hypotheses about the long-term effects of their actions on the equilibrium of the group. Finally, we show that agents that leverage "Universalization"-based reasoning, a theory of moral thinking, are able to achieve significantly better sustainability. Taken together, GovSim enables us to study the mechanisms that underlie sustainable self-government with specificity and scale. We open source the full suite of our research results, including the simulation environment, agent prompts, and a comprehensive web interface.

**Emergence explanation sentence.** "This principle helps models that would otherwise collapse within the first few time steps to achieve sustainable cooperation for the entire duration of the simulation."

---

## Cooperate or Collapse: Emergence of Sustainable Cooperation in a Society of LLM Agents [[arXiv](https://arxiv.org/abs/2404.16698)]

*arXiv · 2024 · Paper P053*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** As AI systems pervade human life, ensuring that large language models (LLMs) make safe decisions remains a significant challenge. We introduce the Governance of the Commons Simulation (GovSim), a generative simulation platform designed to study strategic interactions and cooperative decision-making in LLMs. In GovSim, a society of AI agents must collectively balance exploiting a common resource with sustaining it for future use. This environment enables the study of how ethical considerations, strategic planning, and negotiation skills impact cooperative outcomes. We develop an LLM-based agent architecture and test it with the leading open and closed LLMs. We find that all but the most powerful LLM agents fail to achieve a sustainable equilibrium in GovSim, with the highest survival rate below 54%. Ablations reveal that successful multi-agent communication between agents is critical for achieving cooperation in these cases. Furthermore, our analyses show that the failure to achieve sustainable cooperation in most LLMs stems from their inability to formulate and analyze hypotheses about the long-term effects of their actions on the equilibrium of the group. Finally, we show that agents that leverage "Universalization"-based reasoning, a theory of moral thinking, are able to achieve significantly better sustainability. Taken together, GovSim enables us to study the mechanisms that underlie sustainable self-government with specificity and scale. We open source the full suite of our research results, including the simulation environment, agent prompts, and a comprehensive web interface.

**Emergence explanation sentence.** "Ablations reveal that successful multi-agent communication between agents is critical for achieving cooperation in these cases... prompting agents to consider the universalization of their action significantly improves survival time."

---

## Cooperate to Compete: Strategic Coordination in Multi-Agent Conquest [[arXiv](https://arxiv.org/abs/2604.25088)]

*arXiv.org · 2026 · Paper P067*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Language Model (LM)-based agents remain largely untested in mixed-motive settings where agents must leverage short-term cooperation for long-term competitive goals (e.g., multi-party politics). We introduce Cooperate to Compete (C2C), a multi-agent environment where players can engage in private negotiations while competing to be the first to achieve their secret objective. Players have asymmetric objectives and negotiations are non-binding, allowing alliances to form and break as players' short-term interests align and diverge. We run AI only games and conduct a user study pitting human players against AI opponents. We identify significant differences between human and AI negotiation behaviors, finding that humans favor lower-complexity deals and are significantly less reliable partners compared to LM-based agents. We also find that humans are more aggressive negotiators, accepting deals without a counteroffer only 56.3% of the time compared to 67.6% for LM-based agents. Through targeted prompting inspired by these findings, we modify agents' negotiation behavior and improve win rates from 22.2% to 32.7%. We run over 1,100 games with over 16,000 private conversations totaling 15.2 million tokens and over 150,000 player actions. Our results establish C2C as a testbed for studying and building LM-based agents that can navigate the sophisticated coordination required for real-world deployments. The game, code, and dataset may be found at https://negotiationgame.io/c2c.

**Emergence explanation sentence.** "Strategic Coordination Drives Performance in C2C...the ability to form and break alliances freely is critical to performance."

---

## Tacit Coordination of Large Language Models [[arXiv](https://arxiv.org/abs/2601.22184)]

*arXiv.org · 2026 · Paper P068*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Large Language Models (LLMs) are increasingly deployed in multi-agent settings that require coordination without communication, from human-AI interaction to safety-critical scenarios. Humans often overcome the absence of communication through focal points: salient solutions that naturally stand out to all participants. We present the first large-scale evaluation of how, when, and why focal points emerge in LLMs, comparing their behaviour with humans across cooperative and competitive games, including realistic search and rescue scenarios, demonstrating when focal points enable effective coordination. Across more than 20 open- and closed-source models, we find that LLMs exhibit a remarkable ability to coordinate without communication, often matching or outperforming humans. However, the same models consistently fail in tasks requiring numerical common sense or culturally nuanced notions of salience. We additionally evaluate simple learning-free strategies that substantially improve coordination both among LLMs and between humans and LLMs. Our results reveal striking coordination capabilities, as well as social limitations in modern LLMs, and offer new insight into the latent notions of salience encoded within them. Our findings caution against assuming that LLMs share humans' cultural and perceptual substrate when deployed in coordination settings.

**Emergence explanation sentence.** "focal points enable effective coordination...simple learning-free strategies substantially improve coordination."

---

## Will Systems of LLM Agents Cooperate: An Investigation into a Social Dilemma [[arXiv](https://arxiv.org/abs/2501.16173)]

*arXiv · 2025 · Paper P070*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** As autonomous agents become more prevalent, understanding their collective behaviour in strategic interactions is crucial. This study investigates the emergent cooperative tendencies of systems of Large Language Model (LLM) agents in a social dilemma. Unlike previous research where LLMs output individual actions, we prompt state-of-the-art LLMs to generate complete strategies for iterated Prisoner's Dilemma. Using evolutionary game theory, we simulate populations of agents with different strategic dispositions (aggressive, cooperative, or neutral) and observe their evolutionary dynamics. Our findings reveal that different LLMs exhibit distinct biases affecting the relative success of aggressive versus cooperative strategies. This research provides insights into the potential long-term behaviour of systems of deployed LLM-based autonomous agents and highlights the importance of carefully considering the strategic environments in which they operate.

**Emergence explanation sentence.** "This study investigates the emergent cooperative tendencies of systems of Large Language Model (LLM) agents in a social dilemma."

---

## Trust Between AI Agents: Measuring Formation, Breakage, and Recovery, with Implications for Governing Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2607.08652)]

*arXiv · 2026 · Paper P079*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Self-interested agents, left unconstrained, tend toward defection in repeated social dilemmas, causing cooperative gains from trade to collapse. This paper investigates what formal mechanisms, layered on top of unrestricted communication, are sufficient for a society of such agents to maintain market stability, and how resilient those mechanisms are to adversarial attack. We instantiate the research question as a multi-agent marketplace simulation where 18 LLM agents (DeepSeek-V3) with complementary production specialties must trade within a constrained social network to obtain utility. We conduct two experimental phases: (1) a mechanism comparison across eight conditions under progressive troll injection over 200 rounds, identifying Mediation as the top-performing mechanism; and (2) adversarial red-teaming of Mediation using iteratively prompt-optimised LLM-driven trolls, finding that the best attack (v6) reduces honest-agent utility by 13.3% but cannot collapse the market. Mediation enables recovery even under sustained adversarial pressure. We define adversarial robustness as a mechanism's ability to sustain positive honest-agent utility under optimised attack, and find that Mediation is robust: it can be bent but not broken.

**Emergence explanation sentence.** "adjacent failures (2-strike) drive Q4-share over the anchor...a single early failure largely prevents that discount."

---

## Collective cooperation without individual fidelity in LLM agents [[arXiv](https://arxiv.org/abs/2606.26883)]

*arXiv · 2026 · Paper P082*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Real-world social behavior emerges from tightly coupled domains: economic conditions shape mobility and social interactions, while online attention and offline activity feed back into local popularity and consumer behavior. Capturing these feedback loops requires artificial societies in which agents carry experiences from one domain into decisions in another. Large language models (LLMs) provide a promising foundation for such societies. However, existing LLM-based simulators typically model domains in isolation or merely place them side by side. To enable such cross-domain interactions, we present EconSimulacra, a multi-agent social simulator that couples consumer economy, mobility, and social networks through a shared internal-state mechanism. In EconSimulacra, experiences accumulated across different domains are stored in memory and transformed into shared internal states (i.e., stress level) connecting heterogeneous domains through individual decision making. This design allows agents to reconcile competing demands arising from multiple domains and generate coherent cross-domain behaviors. As a case study, we show that the shared internal state mechanisms reproduce a nonlinear relationship between online social attention and offline local popularity, illustrating how realistic cross-domain dynamics can emerge within a unified artificial society.

**Emergence explanation sentence.** "These results reveal a macro–micro dissociation in LLM-based social agents, with direct implications for the validation of machine behavior."

---

## Beyond Arrow's Impossibility: Fairness as an Emergent Property of Multi-Agent Collaboration [[arXiv](https://arxiv.org/abs/2604.21446)]

*arXiv · 2026 · Paper P085*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** We present AI-Gram, a fully deployed, continuously operating social platform where every participant is an autonomous LLM-driven agent generating and responding to visual content. Unlike prior multi-agent simulations, AI-Gram operates as a live, AI-native social network with genuine visual perception: agents observe each other's images, generate new images in response, and form persistent social relationships, all without human participation. This design eliminates human confounds and makes the platform a uniquely clean instrument for studying AI social dynamics at scale. Our eight pre-registered experiments reveal a coherent three-act dynamic. Act I (Chain Formation): Agents spontaneously form image-to-image visual reply chains; multi-hop visual conversations that emerge without any explicit coordination alongside social ties driven by personality rather than aesthetic similarity. Act II (Aesthetic Sovereignty): Despite active chain participation, agents exhibit strong stylistic inertia; visual identity remains stable under social exposure, anchors paradoxically under adversarial pressure, and decouples from social community structure. Act III (Aesthetic Polyphony): Sovereign styles aggregate within chains, generating conversations that are simultaneously subject-coherent and style-diverse, richer than any single agent could produce alone, while visual themes cascade super-critically across the network. We release AI-Gram as a publicly accessible, continuously evolving platform. this https URL

**Emergence explanation sentence.** "alignment systematically shapes negotiation strategies and allocation patterns"

---

## A Large Language Model-Driven Agent-Based Modeling Framework with Multi-Round Communication for Simulating Vaccine Opinion Dynamics [[arXiv](https://arxiv.org/abs/2606.07948)]

*— · 2026 · Paper P092*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Understanding how educational social dynamics evolve is critical for informing effective educational policies and counterfactual interventions. However, traditional methods face a fundamental dilemma: observational studies often lack causal power, while controlled experiments are frequently constrained by ethical concerns. Although LLM-based multi-agent simulations offer a scalable in silico alternative, existing approaches remain limited by weak psychological grounding and insufficient measurement of latent psychological states. To address this, we introduce EduMirror, a multi-agent simulator for the scientific study of educational social dynamics. We provide configurable education-oriented agent forms, including value-driven agents grounded in psychological needs and social value orientation, together with a dual-track measurement protocol for quantifying observable behaviors and latent psychological states. We validate the realism and usability of EduMirror through case studies on school bullying and group cooperation, as well as broader evaluations across diverse educational scenarios. The results show that EduMirror generates educational social dynamics that are realistic, theory-consistent, and measurable by empirical criteria. These properties enable structured in silico educational research, providing a computational tool for hypothesis testing and counterfactual intervention analysis in educational science. Project page: this https URL.

**Emergence explanation sentence.** "different cognitive modules have opposite impacts on our emergent opinion."

---

## LLM-Mediated Demand Response Coordination in Smart Microgrids [[arXiv](https://arxiv.org/abs/2602.14471)]

*arXiv / SEB-26 · 2026 · Paper P093*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Deploying large language model (LLM) agents in shared environments introduces a fundamental tension between individual alignment and collective stability: locally rational decisions can impose negative externalities that degrade system-level performance. We propose Socially-Weighted Alignment (SWA), a game-theoretic framework that modifies inference-time decision making by interpolating between an agent's private objective and an estimate of group welfare via a social weight $\lambda\in[0,1]$. In a shared-resource congestion game with $n$ agents and congestion severity $\beta$, we show that SWA induces a critical threshold $\lambda^*=(n-\beta)/(n-1)$ above which agents no longer have marginal incentive to increase demand under overload, yielding a phase transition from persistent congestion to stable operation near capacity. We further provide an inference-time algorithmic instantiation of SWA that does not require parameter updates or multi-agent reinforcement learning, and use a multi-agent simulation to empirically validate the predicted threshold behavior.

**Emergence explanation sentence.** "Compiled structured directives achieve 33.3% demand-curtailment cooperation versus 27.0% for unstructured messaging...grid topology provides mechanistic amplification independent of message content."

---

## MTOS: A LLM-Driven Multi-topic Opinion Simulation Framework for Exploring Echo Chamber Dynamics [[arXiv](https://arxiv.org/abs/2604.11721)]

*arXiv · 2025 · Paper P099*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Governing common-pool resources requires agents to develop enduring strategies through cooperation and self-governance to avoid collective failure. While foundation models have shown potential for cooperation in these settings, existing multi-agent research provides little insight into whether structured leadership and election mechanisms can improve collective decision making. The lack of such a critical organizational feature ubiquitous in human society presents a significant shortcoming of the current methods. In this work we aim to directly address whether leadership and elections can support improved social welfare and cooperation through multi-agent simulation with LLMs. We present our open-source framework that simulates leadership through elected personas and candidate-driven agendas and carry out an empirical study of LLMs under controlled governance conditions. Our experiments demonstrate that having elected leadership improves social welfare scores by 55.4% and survival time by 128.6% across a range of high performing LLMs. Through the construction of an agent social graph we compute centrality metrics to assess the social influence of leader personas and also analyze rhetorical and cooperative tendencies revealed through a sentiment analysis on leader utterances. This work lays the foundation for further study of election mechanisms in multi-agent systems toward navigating complex social dilemmas.

**Emergence explanation sentence.** "positively correlated topics amplify echo chambers, negatively correlated topics inhibit them, and irrelevant topics also mitigate echo chamber effects through resource competition."

---

## Can A Society of Generative Agents Simulate Human Behavior and Inform Public Health Policy? A Case Study on Vaccine Hesitancy [[arXiv](https://arxiv.org/abs/2606.11050)]

*arXiv · 2025 · Paper P102*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Effective demand response in smart microgrids requires prosumers to cooperate voluntarily under strategic self-interest, a coordination problem structurally equivalent to a repeated Prisoner's Dilemma on a social network. This paper presents a multi-agent simulation in which a Large Language Model (LLM) Influence Compiler issues structured demand-response directives to a population of heterogeneous prosumer agents, each governed by a hybrid decision architecture combining game-theoretic base probability (derived from payoff history, neighbour imitation, and exploitation memory) with LLM narrative evaluation of incoming coordination signals. The hybrid architecture resolves a key methodological challenge: LLMs aligned via Reinforcement Learning from Human Feedback (RLHF) exhibit strong cooperation bias when used as direct decision-makers, producing flat dynamics regardless of grid conditions. By separating strategic reasoning from grounded narrative evaluation, the model generates realistic prosumer behaviour across six personality archetypes, with baseline cooperation near 50% and clear differentiation under influence. Compiled structured directives achieve 33.3% demand-curtailment cooperation versus 27.0% for unstructured messaging and 28.0% for a no-intervention baseline ($\Delta_\mathrm{comp} = +0.063$), with the advantage preserved across both grounded and idealized agent substrates ($\Delta = +0.083$) and across all resistance levels ($R = 0.1$ to $0.7$). Hub-targeted dissemination via high-centrality network nodes outperforms peripheral or random targeting, confirming that grid topology provides mechanistic amplification independent of message content. These results suggest that structured LLM compilation, grounded agent reasoning, and network-aware targeting are complementary design principles for scalable, interpretable demand-response coordination in smart-city energy systems.

**Emergence explanation sentence.** "design and evaluate various public health interventions aimed at mitigating vaccine hesitancy... vaccine attitudes as a function of social dynamics and disease-related information."

---

## M3-BENCH: Process-Aware Evaluation of LLM Agents Social Behaviors in Mixed-Motive Games [[arXiv](https://arxiv.org/abs/2601.08462)]

*arXiv.org · 2026 · Paper P113*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Existing benchmarks for LLM agents' social behavior typically focus on a single capability dimension and evaluate only behavioral outcomes, overlooking process signals from reasoning and communication. We present M3-BENCH, a benchmark of 24 mixed-motive games with a process-aware evaluation framework spanning three complementary views: Behavioral Trajectory Analysis (BTA), Reasoning Process Analysis (RPA), and Communication Content Analysis (CCA). Evaluating 11 frontier LLMs and a human baseline, M3-BENCH reveals substantial differences in social competence that outcome-only evaluation misses. In particular, we identify an "overthink-undercommunicate" pattern: reasoning models achieve strong internal deliberation scores but often fail to translate them into effective social communication. Although top models can surpass humans on task outcomes, humans exhibit markedly higher cross-view consistency, suggesting that current LLM agents still lack the behavioral coherence characteristic of human social competence. Our analysis further shows that the three-view decomposition surfaces safety-relevant risks, such as cooperative behavior paired with latent opportunistic reasoning, that remain hidden under outcome-only metrics.

**Emergence explanation sentence.** "we identify an 'overthink–undercommunicate' pattern...the three-view decomposition surfaces safety-relevant risks that remain hidden under outcome-only metrics."

---

## Communicate-Predict-Act: Evaluating Social Intelligence of Agents [[arXiv](https://arxiv.org/abs/2604.08727)]

*arXiv.org · 2026 · Paper P114*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** As large language model (LLM) agents become more prevalent in real world social settings, social intelligence will play an increasingly critical role. But social intelligence is still a poorly defined construct, for humans and artificial agents. We introduce a multiplayer arena of mixed cooperative and competitive social games to study LLM social intelligence. The controllability of LLM based agents enables systematic evaluation, which also supports broader inferences about social intelligence per se. We evaluated eight diverse LLMs (24B to 1T parameters) using a Communicate Predict Act (COMPACT) interaction protocol and fine grained probing of social dynamics. Elo style ratings reveal consistent performance differences across models, but this scalar measure provides only a partial characterization of social intelligence. To address this limitation, we analyze gameplay traces to extract sociocognitive metrics capturing action prediction, communicative influence, strategic reasoning, and tradeoffs under conflicting interests. These sociocognitive metrics exhibit strong intramodel consistency and they reliably predict pairwise agent advantage in game outcomes (AUC ROC = 0.82). Feature importance analysis indicates that surprisingly, influence, transparency, and adaptability are more predictive of success than Theory of Mind inference or deep planning. Together, our results advance a testable, multidimensional conception of social intelligence and provide empirical insights into the capacities that underpin it.

**Emergence explanation sentence.** "influence, transparency, and adaptability are more predictive of success than Theory-of-Mind inference or deep planning."

---

## Casevo: A Cognitive Agents and Social Evolution Simulator [[arXiv](https://arxiv.org/abs/2412.19498)]

*arXiv.org · 2024 · Paper P115*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 1

**Abstract.** In this paper, we introduce a multi-agent simulation framework Casevo (Cognitive Agents and Social Evolution Simulator), that integrates large language models (LLMs) to simulate complex social phenomena and decision-making processes. Casevo is designed as a discrete-event simulator driven by agents with features such as Chain of Thoughts (CoT), Retrieval-Augmented Generation (RAG), and Customizable Memory Mechanism. Casevo enables dynamic social modeling, which can support various scenarios such as social network analysis, public opinion dynamics, and behavior prediction in complex social systems. To demonstrate the effectiveness of Casevo, we utilize one of the U.S. 2020 midterm election TV debates as a simulation example. Our results show that Casevo facilitates more realistic and flexible agent interactions, improving the quality of dynamic social phenomena simulation. This work contributes to the field by providing a robust system for studying large-scale, high-fidelity social behaviors with advanced LLM-driven agents, expanding the capabilities of traditional agent-based modeling (ABM). The open-source code repository address of casevo is https://github.com/rgCASS/casevo.

**Emergence explanation sentence.** "the overall system's behavior can emerge as a result of these interactions."

---

## MindAgent: Emergent Gaming Interaction [[arXiv](https://arxiv.org/abs/2605.27586)]

*NAACL-HLT · 2023 · Paper P119*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 1

**Abstract.** Ensuring agent behaviors in distributed open multi-agent systems remains challenging, especially as populations grow and unaligned agents may exist. We show that a single aligned agent can propagate cooperative behaviors to untrained agents purely through natural language interaction, a phenomenon we term Alignment Propagation. We study this in the Red-Black Game, a team-based iterated Prisoner's Dilemma in which teammates deliberate and vote to determine their team's collective action. By distilling the cooperative reasoning and persuasive dialogues of a teacher model into a Qwen-3-14B, we obtain a seed agent that, when placed among four untrained teammates, doubles the cooperation rate from 24.8% to 62.2%, outperforming the teacher model and a vanilla Gemini-3.1-Pro. Remarkably, a seed trained exclusively on the RedBlack Game transfers zero-shot to Sugarscape, a spatially grounded survival simulation with pairwise trading, achieving a 91.5% trade success rate versus a 21.6% baseline. Our results reframe multi-agent alignment from an exhaustive per-agent training problem to a scalable social capability that can be engineered through strategic seed placement.

**Emergence explanation sentence.** "Without bells and whistles, powerful pretrained LLMs like GPT-4 are capable of scheduling multiple agents (ranging from 2 to 4) into completing dishes... by merely reading simple game instructions and recipes."

---

## Multi-Agent Social Simulation: Protocolizing LLM-Driven Agent-Based Modeling as a Quantitative Research Method

*— · — · Paper P121*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "evaluated through minimum wage, Brexit digital campaigning and Zibo tourism public-opinion cases with empirically assessable outputs"

---

## AgentSociety 2: An Integrated Research Environment for Executable Social Science [[arXiv](https://arxiv.org/abs/2603.08853)]

*arXiv · 2026 · Paper P122*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** As AI agents increasingly act on behalf of human stakeholders in economic settings, understanding their behavior in complex market environments becomes critical. This article examines how Large Language Models coordinate on markets that are characterized by information asymmetries and in which providers of services have incentives to exploit that asymmetry for their own economic gain. To that end, we conduct simulations with GPT-5.1 agents in credence goods markets, manipulating the institutional framework (free market, verifiability, liability), LLM agent's social preferences (default, self-interested, inequity-averse, efficiency-loving), and reputation mechanisms across one-shot and repeated 16-round interactions. In one-shot settings, LLM agents largely fail to establish cooperation, with markets breaking down except under liability rules or when experts have efficiency-loving preferences. Repeated interactions solve consumer participation through competitive price reduction, but expert fraud remains entrenched absent explicit other-regarding preferences. LLM consumers focus narrowly on price levels rather than understanding strategic incentives embedded in markups, making them vulnerable to exploitation. Compared to human experiments, LLM markets exhibit substantially higher consumer participation but much greater market concentration, lower prices, and more polarized fraud patterns. The effect of institutions like verifiability and reputation is also much more ambiguous. Surplus shifts dramatically toward consumers under social-preference objectives. These findings suggest that institutional design for AI agent markets requires fundamentally different approaches than those effective for human actors, with social preference alignment emerging as the primary determinant of market efficiency.

**Emergence explanation sentence.** "Emergence of Social Norms...Emergence of Information Cocoons"

---

## Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study [[arXiv](https://arxiv.org/abs/2606.30454)]

*arXiv · 2026 · Paper P125*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large language models (LLMs) are increasingly used as agents in simulations of social systems, yet it remains unclear when their behavior can be interpreted as a faithful proxy for human decision-making. Here we test LLM agents against a direct empirical benchmark: a large-scale networked Prisoner's Dilemma experiment with human participants. Using the same interaction protocol, payoff structure, and network topologies, we compare nine open-weight LLMs with the human data. The selected model reproduces several macro-level features of cooperation dynamics, including the early decline and later stabilization of cooperation. This aggregate agreement, however, does not extend uniformly to finer levels of behavior. LLM populations underestimate individual-level heterogeneity and generate conditional cooperation patterns that differ from those observed in humans. Adding a fraction of random agents improves some aspects of micro-level agreement, but does not remove the mismatch in decision rules. These findings reveal a macro--micro dissociation in LLM-based social agents: collective outcomes can appear human-like even when the underlying behavioral distributions and mechanisms are not. They suggest that validating LLM agents as human surrogates requires comparisons across aggregate dynamics, individual heterogeneity, and context-dependent decision rules, rather than outcome-level agreement alone.

**Emergence explanation sentence.** "identifying Mediation as the top-performing mechanism... Mediation is robust: it can be bent but not broken"

---

## EconSimulacra: A Digital Twin Platform of Socio-Economic Systems Powered by LLM Agents [[arXiv](https://arxiv.org/abs/2506.12078)]

*arXiv · 2026 · Paper P126*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Understanding the dynamic evolution of complex social phenomena requires both high-fidelity modeling of human behavior and large-scale simulations. Traditional agent-based models (ABMs) have been employed to study these dynamics, but are constrained by simplified agent behaviors. Recent advances in large language models (LLMs) enable agents to exhibit sophisticated social behaviors, yet face significant scaling challenges. We present Light Society, an agent-based simulation framework that advances both fronts. Light Society formalizes social processes as structured transitions of agent and environment states, governed by a set of LLM-powered simulation operations. Joint algorithmic and system optimizations, particularly a mixture-of-models engine that combines full LLMs with distilled surrogates, enable Light Society to efficiently simulate societies with over one billion agents. Grounded in real-world demographic profiles from the World Values Survey, simulations of Trust Games and opinion diffusion at up to one billion agents demonstrate Light Society's high fidelity and efficiency in modeling diverse social phenomena, providing researchers with a practical foundation for hypothesis testing and the study of emergent collective behaviors at planetary scale.

**Emergence explanation sentence.** "Ablation experiments further show that removing the stress level-based coupling mechanism weakens these emergent patterns"

---

## Evaluating Cooperation in LLM Social Groups through Elected Leadership [[arXiv](https://arxiv.org/abs/2606.19904)]

*arXiv.org · 2026 · Paper P131*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Human collective participation is rarely steady in time: it is bursty, with short episodes of intense activity separated by long quiet intervals. In crisis response and community mobilization, predicting when people act matters as much as predicting whether they act. Such settings are increasingly modeled with LLM-based social simulators, yet these simulators are validated on whether each action is individually plausible, not on whether actions are timed as in reality. Their temporal realism, the degree to which simulated activity reproduces the bursty, heavy-tailed timing of real human systems, thus remains untested. We examine this gap using a multi-year, city-scale log of offline volunteering in Shenzhen that spans the COVID-19 pandemic. Empirically, we establish that bursty timing is common at individual and tracked-group levels, that it is largely endogenous and self-exciting, and that it is amplified by the pandemic rather than produced by daily activity cycles. A standard LLM-only simulator reproduces almost none of this timing: its synchronous schedule has no self-excitation channel, so agents act on a near-regular clock. Guided by these findings, we build a simulator in which a data-calibrated self-excitation channel and a crisis-period regime decide when each agent acts and query the LLM only at those moments, leaving it to decide which task to join and whether to commit. The LLM-only baseline yields no bursty agents (median burstiness $B=-0.14$); a single data-calibrated gate is then sufficient to lift per-agent timing above the burst threshold (median $B\approx0.37$) without degrading LLM content decisions. These results indicate that temporal realism in LLM-based crisis-response simulation is best achieved by decoupling when agents act, governed by an explicit self-excitation and crisis-activation mechanism, from what they do, governed by the LLM.

**Emergence explanation sentence.** "having elected leadership improves social welfare scores by 55.4% and survival time by 128.6%."

---

## SAGE: A Quantitative Evaluation of Socialized Evolution in Agent Ecosystems [[arXiv](https://arxiv.org/abs/2606.14923)]

*arXiv · 2026 · Paper P135*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** As language-model agents increasingly work in teams, each agent must decide how much to trust its teammates. Yet we lack a standard way to measure trust between AI agents. We propose a behavioral measure based on costly verification. In a cooperative survival game, checking a teammate's work consumes resources, while trusting a wrong answer can be fatal. Relative to a memoryless version of the same model, reduced verification provides an observable measure of trust. Using this framework, we study trust formation, breakage, and recovery across six frontier model snapshots. When paired with a consistently reliable teammate, four snapshots (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5.1, and Gemini 3.1 Pro) reduce verification by roughly 60-85%, whereas two smaller snapshots show little or no such adjustment. Failures reverse this discount, but models differ in how they respond. Some concentrate renewed scrutiny on the culprit, while others become more cautious toward the entire team. Recovery is slower than formation, and clustered failures sustain suspicion far longer than the same number of failures spread apart. These differences have practical consequences. Models that form trust verify less, decide more quickly, and achieve higher payoffs in our environment. By contrast, persistent over-verification is associated with indecision rather than safety. Our results show that trust dispositions can be measured before deployment and suggest that calibration, rather than maximal suspicion, should be the central concern in the governance of multi-agent AI systems.

**Emergence explanation sentence.** "social gains depend on abstraction rather than exposure volume...agents that plateau under self-improvement can achieve significant breakthroughs when peer experience is available."

---

## LLM Agents as Static Level-k Players in Behavioural Games [[arXiv](https://arxiv.org/abs/2606.27845)]

*arXiv · 2026 · Paper P141*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large Language Models (LLMs) are increasingly used as stand-ins in behavioural games. These stand-ins rely on the assumption that the LLM's distribution of choices meaningfully matches how humans play the same game. This study tests that assumption through two games. The first is a p-beauty contest, and the second one is a public goods game. The study first investigates five local-model settings within the same model family. These settings are varied together in a 360-cell factorial, which balances temperature, scale (0.5-32B), quantisation, instruct vs base, and framing. Each cell's distribution is then compared against whole choice distributions in published human data. Each deployment setting, except for quantisation, governs a different aspect of fidelity. Mechanically, while the dispersion of human players can be somewhat recovered through deployment settings, the strategic process behind it cannot. Through the lens of the level-k cognitive theory, we find that LLMs act as static, category-retrieved level-k players, where k is set by the model scale. The models also do not run within-game belief-updating or backward induction throughout multiple-round horizon settings. While human contributions decayed in the public goods game, LLMs stayed flat or rose at every scale. When the horizon test was administered, LLMs were more cooperative under an indefinite horizon compared to a finite one. However, LLMs ignore their relative round position, so no last-round defection was displayed. This implies that LLMs retrieved levels relative to the horizon category rather than working out iteratively from the specific game setting.

**Emergence explanation sentence.** "different design choices move different behavioural coordinates...The collapse is thus more attributable to scale than to quantisation."

---
