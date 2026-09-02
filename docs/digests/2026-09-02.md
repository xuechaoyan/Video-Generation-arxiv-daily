# Generation Research Daily Digest

> 生成时间：2026-09-02T15:23:45+00:00 · 筛选方式：规则评分（未配置模型 API Key）
> 建议先读“优先精读”，快速浏览只看摘要、方法图和主实验表。

## 优先精读

### 1. [DensityKV: Density-Guided KV Cache Compression for Long Video Generation](http://arxiv.org/abs/2608.27922v1)

- **评分**：79/100
- **作者**：Wenqu Zhao, Xuemin Chi, Xin Zhang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **摘要摘录**：Autoregressive video diffusion models enable streaming generation through sliding-window attention, but each generated block is conditioned on previously generated content, causing appearance and motion errors to propagate recursively over time.
- **核心贡献**：To address this problem, we propose DensityKV, a training-free historical KV bank management strategy.
- **与你课题的关系**：匹配研究线：streaming video, efficient generation；关键词：autoregressive, streaming, long video, cache, kv cache, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](http://arxiv.org/abs/2608.27406v1)

- **评分**：77/100
- **作者**：Kechen Liu, Ola Shorinwa
- **方向**：World Models
- **摘要摘录**：State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics.
- **核心贡献**：To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents.
- **与你课题的关系**：匹配研究线：world model, video generation；关键词：world model, video world model, action-conditioned, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](http://arxiv.org/abs/2608.29910v1)

- **评分**：76/100
- **作者**：Runjia Qian, Zile Wang, Jihai Zhang et al.
- **方向**：World Models
- **摘要摘录**：Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR.
- **核心贡献**：Building upon Matrix-Game 3.0, we present Matrix-Game 3.5, as shown in Figure 1, which advances real-time interactive world generation toward geometry-aware and long-horizon consistent simulation through three key improvements.
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, interactive, simulation, embodied, autoregressive, streaming
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](http://arxiv.org/abs/2609.00610v1)

- **评分**：75/100
- **作者**：Xiaoyan Liu, Jiaxin Liu, Kangrui Li et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **摘要摘录**：Current 4D generation paradigms are often bottlenecked by a sequential decoupling design: video is generated first, followed by 3D reconstruction, leading to high interaction latency.
- **核心贡献**：To this end, we propose \textbf{Streaming4D}, a tightly coupled synchronous pipeline that integrates block-wise autoregressive video generation with incremental 3D reconstruction.
- **与你课题的关系**：匹配研究线：streaming video, world model；关键词：world model, interactive, autoregressive, streaming, self-forcing, real-time
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [CAER: Causal Action Effect Reweighting for World Model Training](http://arxiv.org/abs/2608.30897v1)

- **评分**：75/100
- **作者**：Jianjie Fang, Xvyuan Liu, Ziyou Wang et al.
- **方向**：World Models
- **摘要摘录**：World models are becoming core infrastructure for embodied intelligence, with action-conditioned video generation providing controllable predictions of how scenes evolve after agent interventions.
- **核心贡献**：We introduce Causal Action Effect Reweighting (CAER), a general training paradigm that redistributes supervision toward the tokens whose predicted future is causally affected by the action.
- **与你课题的关系**：匹配研究线：world model, video generation；关键词：world model, action-conditioned, embodied, efficient, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [4DStreamCtrl: Interactive Video Generation with Online 4D Control](http://arxiv.org/abs/2608.25479v2)

- **评分**：73/100
- **作者**：Shiqian Li, Chenguo Lin, Zhiguang Liu et al.
- **方向**：Video Generation, World Models
- **摘要摘录**：Generative video models now synthesize footage nearly indistinguishable from reality.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, interactive, closed-loop, embodied, streaming, long video
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [Hydra: A Navigation World Action Model with Discrete Latent Planning and Continuous Flow-Matching Execution](http://arxiv.org/abs/2608.28995v1)

- **评分**：71/100
- **作者**：Mohammad Nazeri, Alexandyr Card, Samira Huber et al.
- **方向**：World Models
- **摘要摘录**：World models let robots imagine possible futures, but exploiting this capability for real-time control is bottlenecked by a representation misalignment: the generative model and the planner operate on decoupled manifolds, so the planner has no shared structure to search over and must instead decode every candidate back into high-dimensional pixel space to evaluate it.
- **核心贡献**：In this paper, we present Hydra, a discrete World Action Model that closes this gap by moving the planner, both the sampler and the evaluator, inside the model.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, closed-loop, real-time
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [Solaris: Towards Interfaces That Are Generated, Not Coded](http://arxiv.org/abs/2609.00776v1)

- **评分**：70/100
- **作者**：Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem et al.
- **方向**：World Models
- **摘要摘录**：Digital interfaces are traditionally implemented through intermediate representations such as code, requiring their appearance and behavior to be specified in advance.
- **核心贡献**：We introduce Solaris, an interface world model that instead generates an interactive UI directly, frame by frame, in response to user actions.
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, interactive, autoregressive, real-time, few-step, distillation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models](http://arxiv.org/abs/2608.27328v1)

- **评分**：70/100
- **作者**：Qiwen Gu, Bingjie Gao, Rui Chen et al.
- **方向**：World Models
- **摘要摘录**：High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little.
- **核心贡献**：We introduce \emph{R2M-Bench} (\textbf{R}elative \textbf{R}evisit \textbf{M}emory Benchmark), a benchmark of observable revisit-selective consistency.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, video world model, action-conditioned, interactive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [Motus2: A Self-Evolving General World Model for Dexterous Manipulation](http://arxiv.org/abs/2608.30237v1)

- **评分**：70/100
- **作者**：Hongzhe Bi, Zihao Zhou, Yihang Tang et al.
- **方向**：World Models
- **摘要摘录**：General embodied agents should perceive, predict, act, evaluate, and improve within a unified system.
- **核心贡献**：We present Motus2, a self-evolving general world model for dexterous manipulation.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, action-conditioned, closed-loop, embodied, autoregressive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
