# Generation Research Daily Digest

> 生成时间：2026-09-03T15:16:33+00:00 · 筛选方式：规则评分（未配置模型 API Key）
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

### 2. [Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](http://arxiv.org/abs/2608.29910v1)

- **评分**：76/100
- **作者**：Runjia Qian, Zile Wang, Jihai Zhang et al.
- **方向**：World Models
- **摘要摘录**：Interactive world models extend video generation from offline clip synthesis toward persistent simulation of interactive virtual worlds, enabling applications in games, robotics, embodied agents, and XR.
- **核心贡献**：Building upon Matrix-Game 3.0, we present Matrix-Game 3.5, as shown in Figure 1, which advances real-time interactive world generation toward geometry-aware and long-horizon consistent simulation through three key improvements.
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, interactive, simulation, embodied, autoregressive, streaming
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](http://arxiv.org/abs/2609.00610v1)

- **评分**：75/100
- **作者**：Xiaoyan Liu, Jiaxin Liu, Kangrui Li et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **摘要摘录**：Current 4D generation paradigms are often bottlenecked by a sequential decoupling design: video is generated first, followed by 3D reconstruction, leading to high interaction latency.
- **核心贡献**：To this end, we propose \textbf{Streaming4D}, a tightly coupled synchronous pipeline that integrates block-wise autoregressive video generation with incremental 3D reconstruction.
- **与你课题的关系**：匹配研究线：streaming video, world model；关键词：world model, interactive, autoregressive, streaming, self-forcing, real-time
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [CAER: Causal Action Effect Reweighting for World Model Training](http://arxiv.org/abs/2608.30897v1)

- **评分**：75/100
- **作者**：Jianjie Fang, Xvyuan Liu, Ziyou Wang et al.
- **方向**：World Models
- **摘要摘录**：World models are becoming core infrastructure for embodied intelligence, with action-conditioned video generation providing controllable predictions of how scenes evolve after agent interventions.
- **核心贡献**：We introduce Causal Action Effect Reweighting (CAER), a general training paradigm that redistributes supervision toward the tokens whose predicted future is causally affected by the action.
- **与你课题的关系**：匹配研究线：world model, video generation；关键词：world model, action-conditioned, embodied, efficient, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](http://arxiv.org/abs/2609.02886v1)

- **评分**：74/100
- **作者**：Junchao Huang, Guian Fang, Shengju Qian et al.
- **方向**：World Models
- **摘要摘录**：We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference.
- **核心贡献**：We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, video world model, interactive, autoregressive, real-time, distillation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Hydra: A Navigation World Action Model with Discrete Latent Planning and Continuous Flow-Matching Execution](http://arxiv.org/abs/2608.28995v1)

- **评分**：71/100
- **作者**：Mohammad Nazeri, Alexandyr Card, Samira Huber et al.
- **方向**：World Models
- **摘要摘录**：World models let robots imagine possible futures, but exploiting this capability for real-time control is bottlenecked by a representation misalignment: the generative model and the planner operate on decoupled manifolds, so the planner has no shared structure to search over and must instead decode every candidate back into high-dimensional pixel space to evaluate it.
- **核心贡献**：In this paper, we present Hydra, a discrete World Action Model that closes this gap by moving the planner, both the sampler and the evaluator, inside the model.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, closed-loop, real-time
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [Solaris: Towards Interfaces That Are Generated, Not Coded](http://arxiv.org/abs/2609.00776v1)

- **评分**：70/100
- **作者**：Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem et al.
- **方向**：World Models
- **摘要摘录**：Digital interfaces are traditionally implemented through intermediate representations such as code, requiring their appearance and behavior to be specified in advance.
- **核心贡献**：We introduce Solaris, an interface world model that instead generates an interactive UI directly, frame by frame, in response to user actions.
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, interactive, autoregressive, real-time, few-step, distillation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [Motus2: A Self-Evolving General World Model for Dexterous Manipulation](http://arxiv.org/abs/2608.30237v1)

- **评分**：70/100
- **作者**：Hongzhe Bi, Zihao Zhou, Yihang Tang et al.
- **方向**：World Models
- **摘要摘录**：General embodied agents should perceive, predict, act, evaluate, and improve within a unified system.
- **核心贡献**：We present Motus2, a self-evolving general world model for dexterous manipulation.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, action-conditioned, closed-loop, embodied, autoregressive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [Can Video World Models Track Unobserved World States?](http://arxiv.org/abs/2608.30692v1)

- **评分**：70/100
- **作者**：Joonghyuk Shin, Yicong Hong, Jaesik Park et al.
- **方向**：World Models
- **摘要摘录**：Video world models are increasingly used as simulators, yet visual fidelity alone does not show that a model maintains the hidden state of the world.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, video world model, action-conditioned, autoregressive, cache, kv cache
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [IMPACT: Attention Is the Interaction Map for Scalable Interaction-Aware World Model Training](http://arxiv.org/abs/2609.00161v1)

- **评分**：59/100
- **作者**：Rongze Tang, Jianjie Fang, Zhaolu Wang et al.
- **方向**：World Models
- **摘要摘录**：World models have made remarkable progress in action-conditioned future prediction for embodied agents, yet still struggle to model physically plausible interactions.
- **核心贡献**：Motivated by this observation, we introduce IMPACT, a scalable Interaction-aware Model training framework with Prior-guided Attention Calibration and Targeting.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, embodied
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
