# Generation Research Daily Digest

> 生成时间：2026-08-25T12:19:50+00:00 · 筛选方式：规则评分（未配置模型 API Key）
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

### 2. [SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](http://arxiv.org/abs/2608.10519v2)

- **评分**：73/100
- **作者**：Jongbeom Lee, Hyunwoo Yu, Jincheol Yang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **摘要摘录**：InfinityStar extends visual autoregressive generation to video through a sequence of image and clip pyramids.
- **核心贡献**：We introduce SparSTAR, a training-free block-sparse attention method tailored to this setting.
- **与你课题的关系**：匹配研究线：video generation, streaming video；关键词：autoregressive, sparse attention, video generation, text-to-video, image-to-video, video synthesis
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

### 2. [Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](http://arxiv.org/abs/2608.19556v1)

- **评分**：66/100
- **作者**：Yuanhao Ban, Jiaqi Feng, Hengguang Zhou et al.
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：Streaming autoregressive diffusion models enable real-time, long-horizon video generation, but their training objectives optimize local frame prediction rather than the geometry and dynamics of a coherent world: long rollouts accumulate geometric drift and degrade into static or unnatural motion.
- **核心贡献**：In this work, we propose Stream4D, which replaces the static critic with a feed-forward 4D reconstruction reward that explicitly models scene dynamics, allowing coherent motion to receive high consistency rewards.
- **与你课题的关系**：匹配研究线：streaming video, efficient generation；关键词：autoregressive, streaming, real-time, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](http://arxiv.org/abs/2608.18484v1)

- **评分**：63/100
- **作者**：Pardis Taghavi, Reza Langari, Gaurav Pandey
- **方向**：Video Generation, World Models
- **摘要摘录**：Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sparse operator.
- **核心贡献**：We introduce SparsePR, which combines Response-Coupled Partitioning with Probe-Fitted Residual Reconstruction.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, sparse attention, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [DA-WAM: Decision-Aligned Future Latents for Driving World Models](http://arxiv.org/abs/2608.19085v2)

- **评分**：63/100
- **作者**：Ruiguo Zhong, Benshan Ma, Xiaolong Chen et al.
- **方向**：World Models
- **摘要摘录**：Anticipating how scenes evolve under ego actions is fundamental to safe autonomous driving, yet the full potential of world models for decision-making remains unrealized.
- **核心贡献**：To bridge this gap, we propose DA-WAM, a framework that unifies predictive representation learning, action-conditioned future modeling, and trajectory scoring under a single decision-making objective.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, driving
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [GeoWAM: Visual Geometry World Action Models for Autonomous Driving](http://arxiv.org/abs/2608.23486v1)

- **评分**：57/100
- **作者**：Yiren Lu, Xin Ye, Jiaming Liu et al.
- **方向**：World Models
- **摘要摘录**：World action models (WAMs) have recently gained increasing attention as a framework for jointly modeling scene evolution and ego actions in autonomous driving.
- **核心贡献**：Building on this insight, we introduce \textbf{GeoWAM}, a visual geometry world action model for autonomous driving.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, closed-loop, driving
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [Beyond Instance Slots: Semantically Rich World Models for Physical Interaction Planning](http://arxiv.org/abs/2608.22294v1)

- **评分**：57/100
- **作者**：Juntao Cheng, Jingkai Wang, Yijun Shen et al.
- **方向**：World Models
- **摘要摘录**：World models for physical interaction are typically trained to predict future observations or latent features; however, a planning-oriented model must answer a fundamentally different question: whether a candidate action produces a task-consistent future while preserving essential relations.Monolithic state representations obscure the underlying entities, while standard instance-level object slots merely identify \emph{what} is present without specifying \emph{what role} each entity plays in the task context.
- **核心贡献**：To bridge this gap, we present the Semantically Rich World Model (SR-WM), a task-conditioned world model structured around five functional roles: gripper, target, goal, relation, and phase.Within SR-WM, a visual entity encoder extracts soft entity hypotheses from pretrained patch features, allowing segmentation masks to serve as optional proposal priors without mandating them as required state representations or inference inputs.A role binder subsequently maps these hypotheses to task-specific roles, while an ac...
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, simulation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms](http://arxiv.org/abs/2608.19661v1)

- **评分**：57/100
- **作者**：Markus Buchholz, Ignacio Carlucho, Yvan R. Petillot
- **方向**：World Models
- **摘要摘录**：Large language models can turn a natural-language mission into a sequence of robot actions, but they do not have a sense of physics: they cannot judge how long a command should run, or whether it will make the robot drift into an obstacle.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model；关键词：world model, closed-loop, driving
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 8. [Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](http://arxiv.org/abs/2608.23383v1)

- **评分**：56/100
- **作者**：Nan Duan, Haoyang Huang, Weiyang Jin et al.
- **方向**：World Models
- **摘要摘录**：Video generation is progressing beyond isolated clips toward long-form narratives and interactive worlds, requiring models to preserve identities, follow user controls, and remain stable over extended rollouts.
- **核心贡献**：We present JoyAI-Echo-1.5, a unified audio-visual generation system with two purpose-built variants.
- **与你课题的关系**：匹配研究线：efficient generation, video generation；关键词：interactive, few-step, efficient, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
