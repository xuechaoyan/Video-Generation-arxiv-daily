# Generation Research Daily Digest

> 生成时间：2026-08-29T15:46:44+00:00 · 筛选方式：规则评分（未配置模型 API Key）
> 建议先读“优先精读”，快速浏览只看摘要、方法图和主实验表。

## 优先精读

### 1. [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](http://arxiv.org/abs/2608.27406v1)

- **评分**：77/100
- **作者**：Kechen Liu, Ola Shorinwa
- **方向**：World Models
- **摘要摘录**：State-of-the-art action-conditioned video models are typically restricted to a single robot embodiment, preventing them from leveraging the vast corpus of heterogeneous video data that contains rich signals for learning generalizable physics.
- **核心贡献**：To bridge this gap, we introduce CLAP, a framework for cross-embodiment action-conditioned video generation capable of being trained on diverse, internet-scale videos across human and robotic agents.
- **与你课题的关系**：匹配研究线：world model, video generation；关键词：world model, video world model, action-conditioned, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [ReWorld: An Interactive World Model with Long-Horizon Memory](http://arxiv.org/abs/2608.23565v1)

- **评分**：74/100
- **作者**：Zhifei Chen, Luozhou Wang, Guibao Shen et al.
- **方向**：World Models
- **摘要摘录**：An interactive world model must follow the user's actions, remember the places it has shown, and stream in real time.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, interactive, streaming, real-time, distillation, cache
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [WALL-SS: Scaling Long-horizon World Models via Next-Scale Autoregression](http://arxiv.org/abs/2608.26239v1)

- **评分**：74/100
- **作者**：Maeve Zhang, Rain Sun, Xiang Wang et al.
- **方向**：World Models
- **摘要摘录**：Generative world models provide robots with predictive models of how the world evolves under interaction, with growing potential for simulation, planning, policy evaluation, and robot learning.
- **核心贡献**：We introduce WALL-SS, a world model that generates visual futures through Scale-wise autoregressive Scaling, enabling action-controllable and long-horizon robotic simulation.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, action-conditioned, simulation, embodied, autoregressive, streaming
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [4DStreamCtrl: Interactive Video Generation with Online 4D Control](http://arxiv.org/abs/2608.25479v2)

- **评分**：73/100
- **作者**：Shiqian Li, Chenguo Lin, Zhiguang Liu et al.
- **方向**：Video Generation, World Models
- **摘要摘录**：Generative video models now synthesize footage nearly indistinguishable from reality.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, interactive, closed-loop, embodied, streaming, long video
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](http://arxiv.org/abs/2608.24199v2)

- **评分**：72/100
- **作者**：Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth et al.
- **方向**：World Models
- **摘要摘录**：Generative simulation for surgical robotics still lacks real-time interaction.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, video world model, action-conditioned, interactive, simulation, streaming
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models](http://arxiv.org/abs/2608.27328v1)

- **评分**：70/100
- **作者**：Qiwen Gu, Bingjie Gao, Rui Chen et al.
- **方向**：World Models
- **摘要摘录**：High similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene; the intervening rollout may simply have changed very little.
- **核心贡献**：We introduce \emph{R2M-Bench} (\textbf{R}elative \textbf{R}evisit \textbf{M}emory Benchmark), a benchmark of observable revisit-selective consistency.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, video world model, action-conditioned, interactive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [RECAP-Forcing: Retaining Content Appearances for Long Video Generation](http://arxiv.org/abs/2608.26671v1)

- **评分**：68/100
- **作者**：Haiyang Xu, Zheng Ding, Zhuowen Tu
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：Long autoregressive video generation faces a fundamental memory challenge: with a finite attention window, a model must decide which information from an ever-expanding history to retain.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：streaming video, efficient generation；关键词：autoregressive, long video, cache, kv cache, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [PRISM: Projection-Integrated Sampling-Based MPC with Bayesian Cost Tuning for Bimanual Manipulation](http://arxiv.org/abs/2608.25666v1)

- **评分**：67/100
- **作者**：Alinjar Dan, Iryna Hurova, Karl Kruusamäe et al.
- **方向**：World Models
- **摘要摘录**：Bimanual manipulation in cluttered, contact-rich environments remains challenging because it requires coordinated motion generation, interaction-aware planning, and reliable execution under tight kinematic constraints.
- **核心贡献**：We present PRISM, a projection-integrated sampling-based Model Predictive Control (MPC) framework that uses a GPU-accelerated physics simulator as an online world model for complex dual-arm manipulation.
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：world model, real-time, acceleration, efficient
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [ConfAL-WM: Confidence-Guided Active Learning for Action-Conditioned World Models](http://arxiv.org/abs/2608.25572v1)

- **评分**：66/100
- **作者**：Xiang Liu, Sen Cui, Changshui Zhang
- **方向**：World Models
- **摘要摘录**：Action-conditioned world models have become an important foundation for embodied prediction, planning, and synthetic data generation, but their errors under new task and scene distributions are often concentrated in localized spatiotemporal regions such as robot arms, manipulated objects, contact areas, and occluded objects.
- **核心贡献**：This paper presents ConfAL-WM, a confidence-guided active learning framework for post-training embodied world models.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, action-conditioned, embodied, efficient
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [Riemann-1.0: An Embodied World Action Model for Physical AI](http://arxiv.org/abs/2608.27033v1)

- **评分**：64/100
- **作者**：Haofeng Sun, Jiangbo Pei, Fei Kang et al.
- **方向**：World Models
- **摘要摘录**：We introduce Riemann-1.0, a fully causal autoregressive World Action Model for embodied intelligence.
- **核心贡献**：We introduce Riemann-1.0, a fully causal autoregressive World Action Model for embodied intelligence.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：action-conditioned, simulation, embodied, autoregressive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
