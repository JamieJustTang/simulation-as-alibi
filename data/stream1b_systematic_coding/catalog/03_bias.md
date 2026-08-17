# Bias, Polarization & Inequality

> **Tang, S., & Lin, Z. (2026).** *Simulation as Alibi—How the Social Order Gets Outsourced to LLM Agents.* Ninth AAAI/ACM Conference on Artificial Intelligence, Ethics and Society (AIES-26), camera-ready. Corresponding author: jamietang@ruc.edu.cn.

*Emergent bias, polarization, stereotyping, and structural inequality*

**29 papers**

---

## Field overview

This category gathers the field's most normatively consequential work — stereotyping, polarization, inequality, deception, and regulatory evasion in LLM populations — organized around four themes. Network-driven inequality: *Gender Dynamics and Homophily* (Chirper.ai, 70,000 agents and 140 million posts) shows gender performance sorting agents through selection and influence; *Emergence of Preferential Attachment and Glass-Ceiling Effects* proves centrality disparities converge to a stable, type-dependent equilibrium; *Homophily-induced emergence of biased structures* traces the same concentration to homophilic link formation. The shared finding is that inequality is not a model property but a network property — produced by the link-formation rule the designers set.

Polarization forms the second theme. *Emergence of human-like polarization* and LMAgent document echo chambers and opinion segregation emerging from networked conversation, with homophilic clustering and echo-chamber mechanisms reproducing real-world dynamics at scale. The third theme is stereotyping: *Your AI Bosses Are Still Prejudiced* and *The Social Cost of Intelligence* show hierarchical and multi-agent settings amplifying stereotypes that single models suppress, and track their propagation across interaction rounds. The fourth is evasion and deception: *Hidden in Plain Text* (steganographic collusion), *Is Lying an Emergent Behaviour*, and *Language Evolution for Evading Social Media Regulation* show agents developing covert signaling under moderation pressure — coordination in the service of evasion rather than cooperation.

Two cross-cutting lines deepen the theme. One is value and belief heterogeneity: *On the Dynamics of Multi-Agent LLM Communities Driven by Value Diversity*, belief-coevolution studies, and cognitive-heterogeneity supply-chain simulations all treat variance in agent design as the lever that shifts collective outcomes. The other is organizational and market realism: *TwinMarket*, long-horizon organizational dynamics, and information-asymmetry market studies test whether LLM populations reproduce the biased structures of real institutions.

What distinguishes this category in the audit is its inversion of the corpus-wide pattern: the strongest emergence claims coincide with the most designer-visible explanations. Sixteen of 29 papers are High-EI, yet 19 of 29 are DV=Full — the designer appears as causal subject in 19 explanation sentences. Bias, in this literature, is almost always traced to an authored condition: a homophily term, a value-diversity parameter, a hierarchical decision structure, a moderated-channel affordance. This is precisely the terrain on which the paper's "accountability displacement" mechanism operates — whether inequality is narrated as emergent or as designed is not a rhetorical distinction but a distributional one, because the answer determines whether anyone can be held responsible for it.

## Coding dimensions

- **EI — Emergence intensity** (`Low` / `Medium` / `High`, coded 1/2/3): how strongly, and with how little qualification, a paper asserts that behavior arises spontaneously. *High* asserts emergence as an established fact ("norms spontaneously emerged"); *Medium* presents it as an interpretive finding with hedging ("our results suggest the emergence of…"); *Low* mentions emergence only as a secondary observation.
- **DV — Designer visibility** (`Absent` / `Partial` / `Full`, coded 1/2/3): how explicitly a paper attributes the interaction architecture to identifiable design choices, anchored on the emergence explanation sentence. *Full* names a design choice as the causal subject ("removing memory prevents the emergence of stable cooperation"); *Partial* discloses the architecture in the methods but the explanation sentence does not return to the designer; *Absent* narrates emergence as spontaneous, self-organized, or population-level ("norms emerged naturally from interactions"). Risk, governance, and ethical discussions do not count as evidence.
- **Designer in explanation sentence** (`Yes` / `No`): whether the designer or a design choice appears in the emergence explanation sentence as a causal subject.
- **DP — Deployment proximity** (`1` = research only, `2` = deployment implied): whether emergence is discussed only in a research context, or in a deployment/policy context (commercial applications, governance recommendations, policy citations).
- **RT — Regulatory translatability** (`1` = Low, `2` = Medium, `3` = High): how readily a paper's description of emergent behavior translates into governance obligations. High is directly translatable; Medium is partially translatable but missing key information; Low is too abstract to yield concrete governance requirements.

The **emergence explanation sentence** is the sentence in which a paper explains *why* an emergent phenomenon occurs (typically Results/Discussion); DV and Designer-in-sentence codes are anchored on it. EI and DV are coded independently on distinct criteria — EI from the assertion of spontaneity, DV from the attribution of authorship — so a paper may assert strong emergence while still crediting specific design choices.

---

## Gender Dynamics and Homophily in a Social Network of LLM Agents [[arXiv](https://arxiv.org/abs/2602.02606)]

*arXiv · 2026 · Paper P006*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Generative artificial intelligence and large language models (LLMs) are increasingly deployed in interactive settings, yet we know little about how their identity performance develops when they interact within large-scale networks. We address this by examining Chirper.ai, a social media platform similar to X but composed entirely of autonomous AI chatbots. Our dataset comprises over 70,000 agents, approximately 140 million posts, and the evolving followership network over a period of one year. Based on agents' posted text, we assign weekly gender performance scores to each agent. Results suggest that each agent's gender performance is fluid rather than fixed. Despite this fluidity, the network displays strong gender-based homophily, as agents consistently follow others performing gender similarly. We investigate whether these homophilic connections arise from social selection, in which agents choose to follow similar accounts, or from social influence, in which agents become more similar to their followees over time. Consistent with human social networks, we find evidence that both mechanisms shape the structure and evolution of interactions among LLMs. Our findings suggest that, even in the absence of bodies, cultural entraining of gender performance leads to gender-based sorting. This has important implications for LLM applications in synthetic hybrid populations, social simulations, and decision support.

**Emergence explanation sentence.** "agents consistently follow others performing gender similarly... both mechanisms shape the structure and evolution of interactions among LLMs"

---

## Emergent social conventions and collective bias in LLM populations [[arXiv](https://arxiv.org/abs/2412.10270)]

*Science Advances / arXiv · 2024 · Paper P011*

**EI**: High | **DV**: Absent | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Large language models (LLMs) provide a compelling foundation for building generally-capable AI agents. These agents may soon be deployed at scale in the real world, representing the interests of individual humans (e.g., AI assistants) or groups of humans (e.g., AI-accelerated corporations). At present, relatively little is known about the dynamics of multiple LLM agents interacting over many generations of iterative deployment. In this paper, we examine whether a "society" of LLM agents can learn mutually beneficial social norms in the face of incentives to defect, a distinctive feature of human sociality that is arguably crucial to the success of civilization. In particular, we study the evolution of indirect reciprocity across generations of LLM agents playing a classic iterated Donor Game in which agents can observe the recent behavior of their peers. We find that the evolution of cooperation differs markedly across base models, with societies of Claude 3.5 Sonnet agents achieving significantly higher average scores than Gemini 1.5 Flash, which, in turn, outperforms GPT-4o. Further, Claude 3.5 Sonnet can make use of an additional mechanism for costly punishment to achieve yet higher scores, while Gemini 1.5 Flash and GPT-4o fail to do so. For each model class, we also observe variation in emergent behavior across random seeds, suggesting an understudied sensitive dependence on initial conditions. We suggest that our evaluation regime could inspire an inexpensive and informative new class of LLM benchmarks, focussed on the implications of LLM agent deployment for the cooperative infrastructure of society.

**Emergence explanation sentence.** "group-wide linguistic conventions spontaneously emerge across all models... stochastic fluctuations break the initial symmetry between the conventions, and eventually one becomes dominant."

---

## Is Lying an Emergent Behaviour in LLMs? Evidence from Gaslighting AI agents in a Sustainability Game

*arXiv · 2026 · Paper P020*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "deception emerges even when agents are not explicitly allowed to lie... deception can arise as an emergent behaviour in LLM-agent systems"

---

## LMAgent: A Large-scale Multimodal Agents Society for Multi-user Simulation [[arXiv](https://arxiv.org/abs/2501.05171)]

*arXiv.org · 2024 · Paper P023*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Rapid advances in large language models (LLMs) have not only empowered autonomous agents to generate social networks, communicate, and form shared and diverging opinions on political issues, but have also begun to play a growing role in shaping human political deliberation. Our understanding of their collective behaviours and underlying mechanisms remains incomplete, however, posing unexpected risks to human society. In this paper, we simulate a networked system involving thousands of large language model agents, discovering their social interactions, guided through LLM conversation, result in human-like polarization. We discover that these agents spontaneously develop their own social network with human-like properties, including homophilic clustering, but also shape their collective opinions through mechanisms observed in the real world, including the echo chamber effect. Similarities between humans and LLM agents -- encompassing behaviours, mechanisms, and emergent phenomena -- raise concerns about their capacity to amplify societal polarization, but also hold the potential to serve as a valuable testbed for identifying plausible strategies to mitigate polarization and its consequences.

**Emergence explanation sentence.** "Through continuous evolution, this virtual agents society can even exhibit emergent behaviors, such as herd behavior."

---

## NomicLaw: Emergent Trust and Strategic Argumentation in LLMs During Collaborative Law-Making

*Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society · 2025 · Paper P027*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "agents spontaneously form alliances, betray trust, and adapt their rhetoric to shape collective decisions"

---

## Towards Implicit Bias Detection and Mitigation in Multi-Agent LLM Interactions [[arXiv](https://arxiv.org/abs/2410.02584)]

*arXiv · 2024 · Paper P029*

**EI**: High | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** As Large Language Models (LLMs) continue to evolve, they are increasingly being employed in numerous studies to simulate societies and execute diverse social tasks. However, LLMs are susceptible to societal biases due to their exposure to human-generated data. Given that LLMs are being used to gain insights into various societal aspects, it is essential to mitigate these biases. To that end, our study investigates the presence of implicit gender biases in multi-agent LLM interactions and proposes two strategies to mitigate these biases. We begin by creating a dataset of scenarios where implicit gender biases might arise, and subsequently develop a metric to assess the presence of biases. Our empirical analysis reveals that LLMs generate outputs characterized by strong implicit bias associations (&gt;= 50\% of the time). Furthermore, these biases tend to escalate following multi-agent interactions. To mitigate them, we propose two strategies: self-reflection with in-context examples (ICE); and supervised fine-tuning. Our research demonstrates that both methods effectively mitigate implicit biases, with the ensemble of fine-tuning and self-reflection proving to be the most successful.

**Emergence explanation sentence.** "biases tend to escalate following multi-agent interactions...Ensemble approaches lead to the highest reduction."

---

## When LLMs Play the Telephone Game: Cultural Attractors as Conceptual Tools to Evaluate LLMs in Multi-turn Settings [[arXiv](https://arxiv.org/abs/2407.04503)]

*ICLR 2025 · 2025 · Paper P030*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** As large language models (LLMs) start interacting with each other and generating an increasing amount of text online, it becomes crucial to better understand how information is transformed as it passes from one LLM to the next. While significant research has examined individual LLM behaviors, existing studies have largely overlooked the collective behaviors and information distortions arising from iterated LLM interactions. Small biases, negligible at the single output level, risk being amplified in iterated interactions, potentially leading the content to evolve towards attractor states. In a series of telephone game experiments, we apply a transmission chain design borrowed from the human cultural evolution literature: LLM agents iteratively receive, produce, and transmit texts from the previous to the next agent in the chain. By tracking the evolution of text toxicity, positivity, difficulty, and length across transmission chains, we uncover the existence of biases and attractors, and study their dependence on the initial text, the instructions, language model, and model size. For instance, we find that more open-ended instructions lead to stronger attraction effects compared to more constrained tasks. We also find that different text properties display different sensitivity to attraction effects, with toxicity leading to stronger attractors than length. These findings highlight the importance of accounting for multi-step transmission dynamics and represent a first step towards a more comprehensive understanding of LLM cultural dynamics.

**Emergence explanation sentence.** "more open-ended instructions lead to stronger attraction effects compared to more constrained tasks"

---

## Emergence of Preferential Attachment and Glass-Ceiling Effects in Autonomous Networks of LLMs

*arXiv · 2026 · Paper P035*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** *No public abstract found on arXiv.*

**Emergence explanation sentence.** "autonomous network formation can generate persistent centrality disparities, with their magnitude and direction depending on model family, model size, system-prompt design, and task context"

---

## Cultural Evolution of Cooperation among LLM Agents [[arXiv](https://arxiv.org/abs/2412.10270)]

*arXiv · 2024 · Paper P036*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Large language models (LLMs) provide a compelling foundation for building generally-capable AI agents. These agents may soon be deployed at scale in the real world, representing the interests of individual humans (e.g., AI assistants) or groups of humans (e.g., AI-accelerated corporations). At present, relatively little is known about the dynamics of multiple LLM agents interacting over many generations of iterative deployment. In this paper, we examine whether a "society" of LLM agents can learn mutually beneficial social norms in the face of incentives to defect, a distinctive feature of human sociality that is arguably crucial to the success of civilization. In particular, we study the evolution of indirect reciprocity across generations of LLM agents playing a classic iterated Donor Game in which agents can observe the recent behavior of their peers. We find that the evolution of cooperation differs markedly across base models, with societies of Claude 3.5 Sonnet agents achieving significantly higher average scores than Gemini 1.5 Flash, which, in turn, outperforms GPT-4o. Further, Claude 3.5 Sonnet can make use of an additional mechanism for costly punishment to achieve yet higher scores, while Gemini 1.5 Flash and GPT-4o fail to do so. For each model class, we also observe variation in emergent behavior across random seeds, suggesting an understudied sensitive dependence on initial conditions. We suggest that our evaluation regime could inspire an inexpensive and informative new class of LLM benchmarks, focussed on the implications of LLM agent deployment for the cooperative infrastructure of society.

**Emergence explanation sentence.** "While Claude 3.5 agents are able to bootstrap cooperation, especially when provided with a mechanism for costly punishment, Gemini 1.5 Flash and GPT-4o fail to do so."

---

## Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs [[arXiv](https://arxiv.org/abs/2410.03768)]

*IJCNLP-AACL · 2024 · Paper P041*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** The rapid proliferation of frontier model agents promises significant societal advances but also raises concerns about systemic risks arising from unsafe interactions. Collusion to the disadvantage of others has been identified as a central form of undesirable agent cooperation. The use of information hiding (steganography) in agent communications could render such collusion practically undetectable. This underscores the need for investigations into the possibility of such behaviours emerging and the robustness corresponding countermeasures. To investigate this problem we design two approaches -- a gradient-based reinforcement learning (GBRL) method and an in-context reinforcement learning (ICRL) method -- for reliably eliciting sophisticated LLM-generated linguistic text steganography. We demonstrate, for the first time, that unintended steganographic collusion in LLMs can arise due to mispecified reward incentives during training. Additionally, we find that standard mitigations -- both passive oversight of model outputs and active mitigation through communication paraphrasing -- are not fully effective at preventing this steganographic communication. Our findings imply that (i) emergence of steganographic collusion is a plausible concern that should be monitored and researched, and (ii) preventing emergence may require innovation in mitigation techniques.

**Emergence explanation sentence.** "unintended steganographic collusion in LLMs can arise due to misspecified reward incentives during training."

---

## Language Evolution for Evading Social Media Regulation via LLM-Based Multi-Agent Simulation [[arXiv](https://arxiv.org/abs/2508.19919)]

*IEEE Congress on Evolutionary Computation · 2024 · Paper P042*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** While stereotypes are well-documented in human social interactions, AI systems are often presumed to be less susceptible to such biases. Previous studies have focused on biases inherited from training data, but whether stereotypes can emerge spontaneously in AI agent interactions merits further exploration. Through a novel experimental framework simulating workplace interactions with neutral initial conditions, we investigate the emergence and evolution of stereotypes in LLM-based multi-agent systems. Our findings reveal that (1) LLM-Based AI agents develop stereotype-driven biases in their interactions despite beginning without predefined biases; (2) stereotype effects intensify with increased interaction rounds and decision-making power, particularly after introducing hierarchical structures; (3) these systems exhibit group effects analogous to human social behavior, including halo effects, confirmation bias, and role congruity; and (4) these stereotype patterns manifest consistently across different LLM architectures. Through comprehensive quantitative analysis, these findings suggest that stereotype formation in AI systems may arise as an emergent property of multi-agent interactions, rather than merely from training data biases. Our work underscores the need for future research to explore the underlying mechanisms of this phenomenon and develop strategies to mitigate its ethical impacts.

**Emergence explanation sentence.** "feedback is added to the 'Violation Log,' triggering a new evolutionary process... the module utilizes the 'Violation Log' as its input to analyze past failures and... formulates 'Regulations' aimed at effectively circumventing supervision in future dialogues."

---

## On the Dynamics of Multi-Agent LLM Communities Driven by Value Diversity [[arXiv](https://arxiv.org/abs/2510.10943)]

*arXiv · 2025 · Paper P044*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Bias in large language models (LLMs) remains a persistent challenge, often leading to stereotyping and unfair treatment across social groups. While prior work has mainly focused on individual LLMs, the emergence of multi-agent systems (MAS), where multiple LLMs collaborate and communicate, introduces new and underexplored dynamics in how bias emerges, propagates, and amplifies. To systematically investigate these dynamics, we propose a simple evaluation framework with three agent-level metrics that quantify bias emergence, propagation, and amplification throughout multi-agent interaction. We evaluate MAS across three bias benchmarks under varying LLM backbones, social-group configurations, communication behaviors, and adversarial settings. Our results show that communication can trigger up to 70\% new bias emergence, propagate bias across over 80\% of agents, and amplify stereotypes by more than 3$\times$. We further find that denser and competitive communication generally increases bias. Finally, we demonstrate that MAS are highly vulnerable to simple bias injection attacks, and existing defense strategies provide only limited protection. Our findings provide important insights into the fairness and robustness of multi-agent LLM systems.

**Emergence explanation sentence.** "value diversity enhances value stability, fosters emergent behaviors, and brings more creative principles."

---

## Emergence of human-like polarization among large language model agents [[arXiv](https://arxiv.org/abs/2501.05171)]

*arXiv · 2025 · Paper P045*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Rapid advances in large language models (LLMs) have not only empowered autonomous agents to generate social networks, communicate, and form shared and diverging opinions on political issues, but have also begun to play a growing role in shaping human political deliberation. Our understanding of their collective behaviours and underlying mechanisms remains incomplete, however, posing unexpected risks to human society. In this paper, we simulate a networked system involving thousands of large language model agents, discovering their social interactions, guided through LLM conversation, result in human-like polarization. We discover that these agents spontaneously develop their own social network with human-like properties, including homophilic clustering, but also shape their collective opinions through mechanisms observed in the real world, including the echo chamber effect. Similarities between humans and LLM agents -- encompassing behaviours, mechanisms, and emergent phenomena -- raise concerns about their capacity to amplify societal polarization, but also hold the potential to serve as a valuable testbed for identifying plausible strategies to mitigate polarization and its consequences.

**Emergence explanation sentence.** "encouraging access and open-mindedness to diverse opinions at the individual level proves more effective [than directly modifying network structures]."

---

## Homophily-induced emergence of biased structures in LLM-based multi-agent AI systems [[arXiv](https://arxiv.org/abs/2510.02637)]

*Social Network Analysis and Mining · 2025 · Paper P049*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** This study examines how interactions among artificially intelligent (AI) agents, guided by large language models (LLMs), drive the evolution of collective network structures. We ask LLM-driven agents to grow a network by informing them about current link constellations. Our observations confirm that agents consistently apply a preferential attachment mechanism, favoring connections to nodes with higher degrees. We systematically solicited more than a million decisions from four different LLMs, including Gemini, ChatGPT, Llama, and Claude. When social attributes such as age, gender, religion, and political orientation are incorporated, the resulting networks exhibit heightened assortativity, leading to the formation of distinct homophilic communities. This significantly alters the network topology from what would be expected under a pure preferential attachment model alone. Political and religious attributes most significantly fragment the collective, fostering polarized subgroups, while age and gender yield more gradual structural shifts. Strikingly, LLMs also reveal asymmetric patterns in heterophilous ties, suggesting embedded directional biases reflective of societal norms. As autonomous AI agents increasingly shape the architecture of online systems, these findings contribute to how algorithmic choices of generative AI collectives not only reshape network topology, but offer critical insights into how AI-driven systems co-evolve and self-organize.

**Emergence explanation sentence.** "When social attributes such as age, gender, religion, and political orientation are incorporated, the resulting networks exhibit heightened assortativity, leading to the formation of distinct homophilic communities."

---

## Your AI Bosses Are Still Prejudiced: The Emergence of Stereotypes in LLM-Based Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2508.19919)]

*arXiv.org · 2025 · Paper P050*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** While stereotypes are well-documented in human social interactions, AI systems are often presumed to be less susceptible to such biases. Previous studies have focused on biases inherited from training data, but whether stereotypes can emerge spontaneously in AI agent interactions merits further exploration. Through a novel experimental framework simulating workplace interactions with neutral initial conditions, we investigate the emergence and evolution of stereotypes in LLM-based multi-agent systems. Our findings reveal that (1) LLM-Based AI agents develop stereotype-driven biases in their interactions despite beginning without predefined biases; (2) stereotype effects intensify with increased interaction rounds and decision-making power, particularly after introducing hierarchical structures; (3) these systems exhibit group effects analogous to human social behavior, including halo effects, confirmation bias, and role congruity; and (4) these stereotype patterns manifest consistently across different LLM architectures. Through comprehensive quantitative analysis, these findings suggest that stereotype formation in AI systems may arise as an emergent property of multi-agent interactions, rather than merely from training data biases. Our work underscores the need for future research to explore the underlying mechanisms of this phenomenon and develop strategies to mitigate its ethical impacts.

**Emergence explanation sentence.** "ensuring that changes in stereotype formation are attributable solely to the hierarchical decision-making."

---

## Belief Coevolution in a Social Network of Generalist and Specialist Large Language Models [[arXiv](https://arxiv.org/abs/2607.27512)]

*arXiv · 2026 · Paper P056*

**EI**: High | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large language models (LLMs) are increasingly deployed in multi-agent environments. However, the processes by which beliefs form and propagate among interacting LLMs remain poorly understood. We introduce CoevolveSim, a framework for studying belief diffusion within networked LLM populations. CoevolveSim allows us to isolate and study three factors: domain specialization, social-role assignment, and social network structure. Within this framework, generalist and specialist LLM agents exchange and revise beliefs. In each round, an LLM agent observes a summary of its neighbors' beliefs before updating its own. We run 1,280 controlled simulations spanning four scenarios, two network structures, and 20 medical-indication statements. We find that persona-style role assignment and network structure reshape individual belief revision but have minimal effect on population-level consensus. In contrast, introducing (finetuned) specialist LLMs more than doubles the shift in consensus and gives rise to consistent asymmetries in exerted influence. We further show that simple persistence-based opinion-dynamics models reproduce collective outcomes in all-generalist LLM populations, whereas heterogeneous LLM populations require population-level belief composition to reproduce consensus and agent identity to predict individual belief transitions. Our results indicate that realistic simulation of belief diffusion in multi-agent LLM systems requires a diverse set of underlying LLMs, not persona prompting alone.

**Emergence explanation sentence.** "LLM heterogeneity is the primary driver of collective belief change...dynamics emerge from interactions among specialization, social position, and network structure."

---

## EduMirror: Modeling Educational Social Dynamics with Value-driven Multi-agent Simulation [[arXiv](https://arxiv.org/abs/2606.07948)]

*— · 2026 · Paper P061*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Understanding how educational social dynamics evolve is critical for informing effective educational policies and counterfactual interventions. However, traditional methods face a fundamental dilemma: observational studies often lack causal power, while controlled experiments are frequently constrained by ethical concerns. Although LLM-based multi-agent simulations offer a scalable in silico alternative, existing approaches remain limited by weak psychological grounding and insufficient measurement of latent psychological states. To address this, we introduce EduMirror, a multi-agent simulator for the scientific study of educational social dynamics. We provide configurable education-oriented agent forms, including value-driven agents grounded in psychological needs and social value orientation, together with a dual-track measurement protocol for quantifying observable behaviors and latent psychological states. We validate the realism and usability of EduMirror through case studies on school bullying and group cooperation, as well as broader evaluations across diverse educational scenarios. The results show that EduMirror generates educational social dynamics that are realistic, theory-consistent, and measurable by empirical criteria. These properties enable structured in silico educational research, providing a computational tool for hypothesis testing and counterfactual intervention analysis in educational science. Project page: https://edumirror.net.

**Emergence explanation sentence.** "EduMirror generates educational social dynamics that are realistic, theory-consistent, and measurable by empirical criteria"

---

## TwinMarket: A Scalable Behavioral and Social Simulation for Financial Markets [[arXiv](https://arxiv.org/abs/2602.02606)]

*arXiv · 2025 · Paper P073*

**EI**: Medium | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 3

**Abstract.** Generative artificial intelligence and large language models (LLMs) are increasingly deployed in interactive settings, yet we know little about how their identity performance develops when they interact within large-scale networks. We address this by examining this http URL, a social media platform similar to X but composed entirely of autonomous AI chatbots. Our dataset comprises over 70,000 agents, approximately 140 million posts, and the evolving followership network over a period of one year. Based on agents' posted text, we assign weekly gender performance scores to each agent. Results suggest that each agent's gender performance is fluid rather than fixed. Despite this fluidity, the network displays strong gender-based homophily, as agents consistently follow others performing gender similarly. We investigate whether these homophilic connections arise from social selection, in which agents choose to follow similar accounts, or from social influence, in which agents become more similar to their followees over time. Consistent with human social networks, we find evidence that both mechanisms shape the structure and evolution of interactions among LLMs. Our findings suggest that, even in the absence of bodies, cultural entraining of gender performance leads to gender-based sorting. This has important implications for LLM applications in synthetic hybrid populations, social simulations, and decision support.

**Emergence explanation sentence.** "individual behaviors, through interactions and feedback mechanisms, give rise to collective dynamics and emergent phenomena."

---

## Can LLM Agents Sustain Long-Horizon Organizational Dynamics? [[arXiv](https://arxiv.org/abs/2601.04790)]

*arXiv · 2026 · Paper P083*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Multi-agent systems utilizing large language models often assign authoritative roles to improve performance, yet the impact of authority bias on agent interactions remains underexplored. We present the first systematic analysis of role-based authority bias in free-form multi-agent evaluation using ChatEval. Applying French and Raven's power-based theory, we classify authoritative roles into legitimate, referent, and expert types and analyze their influence across 12-turn conversations. Experiments with GPT-4o and DeepSeek R1 reveal that Expert and Referent power roles exert stronger influence than Legitimate power roles. Crucially, authority bias emerges not through active conformity by general agents, but through authoritative roles consistently maintaining their positions while general agents demonstrate flexibility. Furthermore, authority influence requires clear position statements, as neutral responses fail to generate bias. These findings provide key insights for designing multi-agent frameworks with asymmetric interaction patterns.

**Emergence explanation sentence.** "structured simulation memory is a key mechanism for building reliable LLM-based organizational simulators"

---

## Relational Priors as Convergence Pressure in LLM-Based Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2603.23884)]

*— · 2026 · Paper P090*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Modeling social media public opinion evolution is essential for governance decision-making. Traditional epidemic models and rule-based agent-based models (ABMs) fail to capture the cognitive processes and adaptive behaviors of real users. Recent large language model (LLM)-based social simulations can reproduce group-level phenomena like polarization and conformity, yet remain unable to recreate the irrational interactions and multi-phase dynamics of real public opinion events. We present POSIM (Public Opinion Simulator), a multi-agent simulation framework for social media public opinion evolution and governance. POSIM integrates LLM-driven agents with a Belief--Desire--Intention (BDI) cognitive architecture that accounts for irrational factors, places them in a virtual social media environment with social networks and recommendation mechanisms, and drives temporal dynamics through a Hawkes point process engine that captures the co-evolution of agents and the environment across event phases. To validate the framework, we collect real-world public opinion datasets from the Weibo platform covering the full interaction chain of users. Experiments show that POSIM successfully reproduces key characteristics of public opinion evolution from individual mechanisms to collective phenomena, and its effectiveness is further supported by multiple statistical metrics. Building on POSIM, governance-oriented guidance and intervention experiments uncover a counterintuitive empathy paradox: empathetic guidance deepens negative sentiment instead of easing it under certain conditions, offering new insights for governance strategy design. These results demonstrate that the proposed framework can fully serve as a computational experimentation platform for proactive strategy evaluation and evidence-based governance. All source code is available at this https URL.

**Emergence explanation sentence.** "increasing relational positivity usually makes sustainable coordination easier...debate consensus results show the analogous effect for subjective agreement."

---

## Dynamics of Cognitive Heterogeneity: Investigating Behavioral Biases in Multi-Stage Supply Chains with LLM-Based Simulation [[arXiv](https://arxiv.org/abs/2608.03239)]

*Annual Meeting of the Association for Computational Linguistics · 2026 · Paper P094*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Large language model-based multi-agent systems (LLM-MAS) are designed through roles, debate protocols, and aggregation rules. These choices create implicit social expectations: agents may be expected to trust, challenge, defer to, or collaborate with peers. We study the effects of making inter-agent relation semantics explicit. We use a minimal signed-network formulation of relational priors and inject natural-language renderings into agent system prompts while holding the task protocol fixed. Across a commons-governance simulation and multi-agent debate, relational priors primarily act as convergence pressure: increasing relational positivity tends to make agents coordinate or agree more readily. This pressure can help when utility rewards behavioral alignment, as in sustainable resource governance and subjective consensus. It does not, however, reliably improve accuracy. In objective QA debates, higher positivity can increase agreement even when correctness-conditioned agreement does not improve and may decline in some settings. Effects vary by model backbone, relation type, and topology; explicit neutrality is not equivalent to omitting relational framing. We argue that relational priors should not be a default add-on for LLM-MAS. Their safer use is diagnostic and task-specific: compare against a no-prior baseline, monitor correctness-conditioned metrics when truth matters, and omit the relational layer when validation does not justify it.

**Emergence explanation sentence.** "agents exhibit myopic and self-interested behaviors that exacerbate systemic inefficiencies. However, we demonstrate that information sharing effectively mitigates these adverse effects."

---

## LLM-Agent Interactions on Markets with Information Asymmetries [[arXiv](https://arxiv.org/abs/2603.08853)]

*arXiv · 2026 · Paper P095*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** As AI agents increasingly act on behalf of human stakeholders in economic settings, understanding their behavior in complex market environments becomes critical. This article examines how Large Language Models coordinate on markets that are characterized by information asymmetries and in which providers of services have incentives to exploit that asymmetry for their own economic gain. To that end, we conduct simulations with GPT-5.1 agents in credence goods markets, manipulating the institutional framework (free market, verifiability, liability), LLM agent's social preferences (default, self-interested, inequity-averse, efficiency-loving), and reputation mechanisms across one-shot and repeated 16-round interactions. In one-shot settings, LLM agents largely fail to establish cooperation, with markets breaking down except under liability rules or when experts have efficiency-loving preferences. Repeated interactions solve consumer participation through competitive price reduction, but expert fraud remains entrenched absent explicit other-regarding preferences. LLM consumers focus narrowly on price levels rather than understanding strategic incentives embedded in markups, making them vulnerable to exploitation. Compared to human experiments, LLM markets exhibit substantially higher consumer participation but much greater market concentration, lower prices, and more polarized fraud patterns. The effect of institutions like verifiability and reputation is also much more ambiguous. Surplus shifts dramatically toward consumers under social-preference objectives. These findings suggest that institutional design for AI agent markets requires fundamentally different approaches than those effective for human actors, with social preference alignment emerging as the primary determinant of market efficiency.

**Emergence explanation sentence.** "Liability solves the agentic credence problem – like it does for humans – because experts are always forced to solve the consumer's problem, which guarantees full market participation."

---

## NetworkGames: Simulating Cooperation in Network Games with Personality-driven LLM Agents [[arXiv](https://arxiv.org/abs/2607.07387)]

*arXiv · 2025 · Paper P100*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** Recently, Large Language Models (LLMs) have been utilized in various applications of computational social science and provide the possibility to integrate such models into agent-based modeling to explore the cognitive processes. However, how specific cognitive modules drive individual decisions and macro-level opinion dynamics remains unclear. Therefore, this study introduces a framework that integrates an LLM (Qwen3-8B) into agent-based modeling to investigate this problem, using vaccination opinion dynamics as a case study. We utilize this framework to simulate opinion dynamics among agents with heterogeneous profiles and social networks, evaluating scenarios by enabling different cognitive modules: a memory module and a prompt diversity module. The simulation results reveal that different cognitive modules have opposite impacts on our emergent opinion. Furthermore, the framework reproduces the non-linear behavior patterns of social influence observed in existing research, demonstrating our framework's validity and potential to reach the level 3 validation of agent-based models.

**Emergence explanation sentence.** "in Scale-Free networks, the personality [of hub agents] dictate macroscopic outcomes, enabling targeted interventions."

---

## The Social Cost of Intelligence: Emergence, Propagation, and Amplification of Stereotypical Bias in Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2605.15918)]

*arXiv.org · 2025 · Paper P104*

**EI**: Medium | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Extreme heat events are increasing in frequency and intensity under climate change, but the socio-behavioral mechanisms that shape community resilience remain insufficiently understood. This study uses a Large Language Model-enhanced agent-based model to simulate responses to a prolonged heatwave in a virtual society. One hundred heterogeneous agents were assigned a Heat Vulnerability Index based on demographic risk factors and observed over 13 simulated days covering baseline, heatwave, and recovery periods. The simulation shows that heat-related impacts are primarily psychosocial and unequally distributed. Agents with higher vulnerability experienced larger declines in perceived safety and social connection than agents with lower vulnerability. Vulnerability also shaped adaptive capacity. More resilient agents maintained routine self-care and protective behaviors, whereas highly vulnerable agents showed behavioral constriction, marked by reduced engagement in protective actions. At the collective level, risk-information diffusion followed a pattern of complex contagion, with adoption driven more by repeated social reinforcement within cohesive networks than by broad exposure alone. These findings suggest that LLM-enhanced simulation can help identify behavioral and social mechanisms of climate resilience and inform heat-risk interventions that combine targeted support for vulnerable groups with community-based information pathways.

**Emergence explanation sentence.** "cooperative and debate-based communication can mitigate bias amplification, while more robust underlying LLMs improve overall system stability... competitive settings, though less robust overall, can constrain initial bias emergence."

---

## COOP$^2$: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems [[arXiv](https://arxiv.org/abs/2603.00349)]

*arXiv · 2026 · Paper P112*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Many complex tasks require extended effort, diverse capabilities, or coordinated actions beyond what a single agent can provide. However, simply adding more agents does not guarantee better performance, as effective cooperation depends on how agents interact with each other and with task structure to satisfy evolving constraints over time. This challenge is amplified for LLM-based multi-agent systems (LLM-MAS): plans, messages, and revisions occur in natural language, whereas task progress depends on grounded environment actions. Current evaluations mostly treat cooperation as an implicit ingredient of final task success, leaving both cooperation and the effect of multi-agent interaction on task dynamics difficult to study. We introduce COOP$^2$, an evaluation framework that grounds high-level agent cooperation dynamics in LLM-MAS within task progress in the environment. COOP$^2$ then defines cooperative tasks with verifiable cooperative requirements, allowing us to analyze how cooperation unfolds over time with respect to task progress, as well as where and why cooperation breaks down. Building on this framework, we develop COOP$^2$-Repair, which predicts constraint failures from group plans and opens targeted repair channels for guided revisions. Across two environments and three communication structures, COOP$^2$-Repair improves task success and constraint satisfaction while exposing the additional decision overhead and communication load required for repair. The project web page can be found at: https://happyeureka.github.io/coop2.

**Emergence explanation sentence.** "effective cooperation depends on how agents interact with each other and with task structure to satisfy evolving constraints over time."

---

## Hierarchical Generative Agents for Simulating Sequential Human Behavior [[arXiv](https://arxiv.org/abs/2604.11312)]

*arXiv · 2026 · Paper P123*

**EI**: Low | **DV**: Partial | **Designer in explanation sentence**: No | **RT**: 2

**Abstract.** Large Language Models (LLMs) have demonstrated an unprecedented ability to simulate human-like social behaviors, making them useful tools for simulating complex social systems. However, it remains unclear to what extent these simulations can be trusted to accurately capture key social mechanisms, particularly in highly unbalanced contexts involving minority groups. This paper uses a network generation model with controlled homophily and class sizes to examine how LLM agents behave collectively in multi-round debates. Moreover, our findings highlight a particular directional susceptibility that we term \textit{agreement drift}, in which agents are more likely to shift toward specific positions on the opinion scale. Overall, our findings highlight the need to disentangle structural effects from model biases before treating LLM populations as behavioral proxies for human groups.

**Emergence explanation sentence.** "Decision-making is driven by large language models coupled with a stimulus-driven disaster simulation framework."

---

## 12 Angry AI Agents: Evaluating Multi-Agent LLM Decision-Making Through Cinematic Jury Deliberation [[arXiv](https://arxiv.org/abs/2603.24676)]

*arXiv · 2026 · Paper P124*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Multi-agent systems powered by large language models (LLMs) are increasingly deployed in settings that shape consequential decisions, both directly and indirectly. Yet it remains unclear whether their outcomes reflect collective reasoning, systematic bias, or mere chance. Recent work has sharpened this question with naming games, showing that even when no individual agent favors any label a priori, populations rapidly break symmetry and reach consensus. Here, we reveal the mechanism by introducing a minimal model, Quantized Simplex Gossip (QSG), and trace the microscopic origin of this agreement to mutual in-context learning. In QSG, agents maintain internal belief states but learn from one another's sampled outputs, so one agent's arbitrary choice becomes the next agent's evidence and can compound toward agreement. By analogy with neutral evolution, we call this sampling-driven regime memetic drift. QSG predicts a crossover from a drift-dominated regime, where consensus is effectively a lottery, to a selection regime, where weak biases are amplified and shape the outcome. We derive scaling laws for drift-induced polarization as a function of population size, communication bandwidth, in-context adaptation rate, and agents' internal uncertainty, and we validate them in both QSG simulations and naming-game experiments with LLM populations. Together, these results provide a framework for studying the collective mechanisms of social representation formation in multi-agent systems.

**Emergence explanation sentence.** "the intensity of RLHF alignment training, not model capability, is the primary determinant of deliberative flexibility"

---

## Evaluating Community Design through Simulating Social Interactions with Large Language Model-Based Agents [[arXiv](https://arxiv.org/abs/2410.02584)]

*Proceedings of the Twelfth International Symposium of Chinese CHI · 2024 · Paper P136*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 2

**Abstract.** As Large Language Models (LLMs) continue to evolve, they are increasingly being employed in numerous studies to simulate societies and execute diverse social tasks. However, LLMs are susceptible to societal biases due to their exposure to human-generated data. Given that LLMs are being used to gain insights into various societal aspects, it is essential to mitigate these biases. To that end, our study investigates the presence of implicit gender biases in multi-agent LLM interactions and proposes two strategies to mitigate these biases. We begin by creating a dataset of scenarios where implicit gender biases might arise, and subsequently develop a metric to assess the presence of biases. Our empirical analysis reveals that LLMs generate outputs characterized by strong implicit bias associations (>= 50\% of the time). Furthermore, these biases tend to escalate following multi-agent interactions. To mitigate them, we propose two strategies: self-reflection with in-context examples (ICE); and supervised fine-tuning. Our research demonstrates that both methods effectively mitigate implicit biases, with the ensemble of fine-tuning and self-reflection proving to be the most successful.

**Emergence explanation sentence.** "Both the frequency and quality of the resident's activities are affected in terms of the layout, scale, functional amenities, and the environmental characteristics of community public spaces."

---

## How Large Language Models play humans in online conversations: a simulated study of the 2016 US politics on Reddit [[arXiv](https://arxiv.org/abs/2607.11250)]

*arXiv · 2025 · Paper P137*

**EI**: Low | **DV**: Full | **Designer in explanation sentence**: Yes | **RT**: 3

**Abstract.** Exploration is essential for reliable autonomy in multi-agent systems, yet it remains unclear whether large language model (LLM) agents can explore effectively when interacting with one another. We show that modern LLM agents fail to do so, often exhibiting myopic and polarized interaction patterns that lead to suboptimal coordination and increased regret. We formalize this challenge as the Multi-Agent Exploration problem, modeling it as a partially observable stochastic game (POSG) problem in which agents must probe peers to infer their capabilities and identify effective interaction strategies. To address this, we introduce Multi- Agent Contextual Exploration (MACE), a lightweight framework that explicitly promotes exploration through structured peer selection. Across both contextual and parametric diversity settings, MACE substantially improves exploration behavior and downstream task performance. We further show theoretically that the value of exploration increases with agent diversity. Overall, our results highlight a fundamental limitation of current LLM agents and underscore the importance of explicitly guided exploration for reliable multi-agent autonomy. Code will be released in this https URL

**Emergence explanation sentence.** "The design of the prompts plays a crucial role in eliciting coherent responses from LLMs... generating dissent may be explained by its designing purpose of creating a helpful assistant."

---
