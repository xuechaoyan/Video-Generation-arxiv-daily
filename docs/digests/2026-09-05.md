# Generation Research Daily Digest

> 生成时间：2026-09-05T14:01:58+00:00 · 筛选方式：规则评分（未配置模型 API Key）
> 建议先读“优先精读”，快速浏览只看摘要、方法图和主实验表。

## 优先精读

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

### 3. [SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](http://arxiv.org/abs/2609.02886v1)

- **评分**：74/100
- **作者**：Junchao Huang, Guian Fang, Shengju Qian et al.
- **方向**：World Models
- **摘要摘录**：We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference.
- **核心贡献**：We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, video world model, interactive, autoregressive, real-time, distillation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [Long-Horizon Consistent and Interaction-Aware World Models for Multi-Style End-to-End Driving](http://arxiv.org/abs/2609.03225v1)

- **评分**：72/100
- **作者**：Yuxuan Han, Kunyuan Wu, Liyunong Yang et al.
- **方向**：World Models
- **摘要摘录**：End-to-end autonomous driving has increasingly adopted world model-based reinforcement learning frameworks to improve learning efficiency through \textit{imagined rollouts}.
- **核心贡献**：To address these challenges, we propose \textit{StyleDrive}, a world-model-based learning framework that jointly enforces long-horizon consistency, explicitly disentangles interactive traffic states, and supports multi-style policy optimization within a unified learning paradigm.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, interactive, closed-loop, driving, temporal consistency, efficient
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [Solaris: Towards Interfaces That Are Generated, Not Coded](http://arxiv.org/abs/2609.00776v1)

- **评分**：70/100
- **作者**：Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem et al.
- **方向**：World Models
- **摘要摘录**：Digital interfaces are traditionally implemented through intermediate representations such as code, requiring their appearance and behavior to be specified in advance.
- **核心贡献**：We introduce Solaris, an interface world model that instead generates an interactive UI directly, frame by frame, in response to user actions.
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, interactive, autoregressive, real-time, few-step, distillation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Motus2: A Self-Evolving General World Model for Dexterous Manipulation](http://arxiv.org/abs/2608.30237v1)

- **评分**：70/100
- **作者**：Hongzhe Bi, Zihao Zhou, Yihang Tang et al.
- **方向**：World Models
- **摘要摘录**：General embodied agents should perceive, predict, act, evaluate, and improve within a unified system.
- **核心贡献**：We present Motus2, a self-evolving general world model for dexterous manipulation.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, action-conditioned, closed-loop, embodied, autoregressive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation](http://arxiv.org/abs/2609.03557v1)

- **评分**：70/100
- **作者**：Haoyu Wang, Songchun Zhang, Haoran Li et al.
- **方向**：World Models
- **摘要摘录**：Action-conditioned video models require large-scale visual data paired with control signals that are temporally aligned with the resulting scene transitions.
- **核心贡献**：We present a large-scale synthetic data production pipeline built on Unreal Engine for generating action-conditioned, multi-view video.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, action-conditioned, real-time, cache, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [Can Video World Models Track Unobserved World States?](http://arxiv.org/abs/2608.30692v1)

- **评分**：70/100
- **作者**：Joonghyuk Shin, Yicong Hong, Jaesik Park et al.
- **方向**：World Models
- **摘要摘录**：Video world models are increasingly used as simulators, yet visual fidelity alone does not show that a model maintains the hidden state of the world.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, video world model, action-conditioned, autoregressive, cache, kv cache
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](http://arxiv.org/abs/2609.03602v1)

- **评分**：66/100
- **作者**：Jinyang Wang, Shiwei Li, Junjian Wang et al.
- **方向**：World Models
- **摘要摘录**：World models (WMs) have demonstrated strong potential for end-to-end autonomous driving by learning predictive representations of future scene dynamics.
- **核心贡献**：To address this limitation, we propose SV-WAM, a surround-view world-action model (WAM) that preserves full six-camera observations while maintaining efficient inference.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, closed-loop, driving, efficient
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation](http://arxiv.org/abs/2609.04031v1)

- **评分**：60/100
- **作者**：Shuaiting Li, Zelin Gao, Haibin Shen et al.
- **方向**：Video Generation
- **摘要摘录**：Video diffusion models (VDMs) have achieved impressive progress in text-to-video generation, but their high memory and computational costs hinder practical deployment.
- **核心贡献**：Based on this insight, we propose DSAQuant, a Denoising-Stage-Aligned Quantization-aware training framework for VDMs.
- **与你课题的关系**：匹配研究线：video generation, efficient generation；关键词：distillation, video generation, text-to-video, video diffusion
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
