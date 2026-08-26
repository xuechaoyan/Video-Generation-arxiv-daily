# Generation Research Daily Digest

> 生成时间：2026-08-26T12:21:47+00:00 · 筛选方式：规则评分（未配置模型 API Key）
> 建议先读“优先精读”，快速浏览只看摘要、方法图和主实验表。

## 优先精读

### 1. [ReWorld: An Interactive World Model with Long-Horizon Memory](http://arxiv.org/abs/2608.23565v1)

- **评分**：74/100
- **作者**：Zhifei Chen, Luozhou Wang, Guibao Shen et al.
- **方向**：World Models
- **摘要摘录**：An interactive world model must follow the user's actions, remember the places it has shown, and stream in real time.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, interactive, streaming, real-time, distillation, cache
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](http://arxiv.org/abs/2608.24199v1)

- **评分**：72/100
- **作者**：Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth et al.
- **方向**：World Models
- **摘要摘录**：Generative simulation for surgical robotics still lacks real-time interaction.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, video world model, action-conditioned, interactive, simulation, streaming
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [DreamMimic: Learning Visuomotor Whole-Body Loco-Manipulation via World Model](http://arxiv.org/abs/2608.22278v1)

- **评分**：71/100
- **作者**：Jie Yin, Xingyu Lai
- **方向**：World Models
- **摘要摘录**：Vision-based whole-body loco-manipulation on humanoid robots is challenging due to partial observability, contact-rich dynamics, and the difficulty of learning long-horizon behaviors from high-dimensional visual inputs.
- **核心贡献**：We present \href{https://github.com/DreamMimic/DreamMimic}{DreamMimic}, a framework that distills privileged teacher policies into vision-based humanoid controllers via world-model-assisted distillation.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, action-conditioned, simulation, distillation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [TrAct: Bridging Robot Control and Visual Prediction with Visual Tracks](http://arxiv.org/abs/2608.24101v1)

- **评分**：59/100
- **作者**：Zhi Cao, Howard Ji, Kevin Zhang et al.
- **方向**：World Models
- **摘要摘录**：Robot actions are inherently embodiment-specific and only weakly aligned with image-space visual changes, limiting their effectiveness as conditioning signals for robot world models.
- **核心贡献**：Building on this observation, we propose TrAct, a world-model-based robot decision-making framework that uses visual tracks as an intermediate interface between control and prediction.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, simulation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [LeFlow: Generative Latent Flow Planning for World Models](http://arxiv.org/abs/2608.24855v1)

- **评分**：58/100
- **作者**：Hsiang-Wei Huang, Jianxu Shangguan, Junbin Lu et al.
- **方向**：World Models
- **摘要摘录**：Latent world models are inherently strong encoders that transform image pixel to latent embedding, yet existing world models still rely on online trajectory optimization for action planning: for every state-goal pair, an iterative optimizer is run from scratch to search for optimal action sequences, treating the world model as a black-box simulator.
- **核心贡献**：We present LeFlow, which learns a reusable latent trajectory prior operating directly in the latent dynamics space from the world model.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, autoregressive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [Beyond Instance Slots: Semantically Rich World Models for Physical Interaction Planning](http://arxiv.org/abs/2608.22294v1)

- **评分**：57/100
- **作者**：Juntao Cheng, Jingkai Wang, Yijun Shen et al.
- **方向**：World Models
- **摘要摘录**：World models for physical interaction are typically trained to predict future observations or latent features; however, a planning-oriented model must answer a fundamentally different question: whether a candidate action produces a task-consistent future while preserving essential relations.Monolithic state representations obscure the underlying entities, while standard instance-level object slots merely identify \emph{what} is present without specifying \emph{what role} each entity plays in the task context.
- **核心贡献**：To bridge this gap, we present the Semantically Rich World Model (SR-WM), a task-conditioned world model structured around five functional roles: gripper, target, goal, relation, and phase.Within SR-WM, a visual entity encoder extracts soft entity hypotheses from pretrained patch features, allowing segmentation masks to serve as optional proposal priors without mandating them as required state representations or inference inputs.A role binder subsequently maps these hypotheses to task-specific roles, while an ac...
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, simulation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](http://arxiv.org/abs/2608.23486v2)

- **评分**：57/100
- **作者**：Yiren Lu, Xin Ye, Jiaming Liu et al.
- **方向**：World Models
- **摘要摘录**：World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving.
- **核心贡献**：Building on this insight, we introduce \textbf{GeoWAM}, a visual geometry world action model for autonomous driving.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, closed-loop, driving
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](http://arxiv.org/abs/2608.23383v2)

- **评分**：56/100
- **作者**：Nan Duan, Haoyang Huang, Weiyang Jin et al.
- **方向**：World Models
- **摘要摘录**：Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts.
- **核心贡献**：We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants.
- **与你课题的关系**：匹配研究线：efficient generation, video generation；关键词：interactive, few-step, efficient, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [Do Robotic World Models Really Follow Actions? Diagnosing and Aligning Action-Conditioned Generation for Policy Learning](http://arxiv.org/abs/2608.24885v1)

- **评分**：56/100
- **作者**：Sixiang Chen, Jiaming Liu, Jixian Wu et al.
- **方向**：World Models
- **摘要摘录**：Action-conditioned world models are increasingly used as learned simulators for policy evaluation and improvement, yet their effectiveness rests on an unverified assumption: generated futures faithfully reflect arbitrary valid actions.
- **核心贡献**：To address this gap, we introduce WorldEcho, which probes action following over a broader action distribution using visual integrity and SE(3) trajectory alignment.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 8. [From Generation to Simulation: How Far Are World Models from Being True Simulators?](http://arxiv.org/abs/2608.23070v1)

- **评分**：56/100
- **作者**：Tong Wang, Huan Deng, Mucheng Yang et al.
- **方向**：World Models
- **摘要摘录**：With the rapid progress of diffusion models and large-scale video generation, generative world models are increasingly expected to replace traditional simulators, including physics engines, game engines, and reinforcement-learning environments.
- **核心贡献**：We present a capability-based study using an external yardstick: eight capabilities of a traditional simulator, namely asset construction, physics engine, interaction, controllability, stability, state feedback, diversity, and evaluation metrics.
- **与你课题的关系**：匹配研究线：world model, video generation；关键词：world model, simulation, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
