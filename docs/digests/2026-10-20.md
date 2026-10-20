# Generation Research Daily Digest

> 生成时间：2026-10-20T02:13:22+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base](http://arxiv.org/abs/2610.25634v1)

- **评分**：81/100
- **作者**：Wenqing Wang, Joonghyuk Shin, Jonathan Tremblay et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video diffusion models generate streaming video of arbitrary length by conditioning each new chunk of frames on those already generated.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 2. [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](http://arxiv.org/abs/2610.23156v1)

- **评分**：72/100
- **作者**：Yueyang Weng, Xiaopeng Zhang, Yuxi Ou et al.
- **方向**：World Models
- **一句话**：本文提出 ORD-WM，用于机器人操作中的三维物体中心世界建模。方法通过 SDF 监督的旋转等变向量神经元变分自编码器，将物体点云编码为可进行刚体变换的几何潜变量；随后根据当前场景状态和机器人动作预测各物体的 SE(3) 运动增量，并直接在潜空间中更新物体状态。该结构避免了自由预测潜变量造成的形状漂移，并支持无需重复分割、点云重建和编码的多步 rollou…
- **精读笔记**：[打开笔记](../notes/2026-10-20/2610.23156-ord-wm-learning-object-centric-rigid-dynamics-fo.md)

## 快速浏览

### 1. [Structured Latent Dynamics for Long-Horizon Embodied World Models](http://arxiv.org/abs/2610.24534v1)

- **评分**：71/100
- **作者**：Kevin Chen, Yu-Wei Zhan, Haoran Liang et al.
- **方向**：World Models
- **一句话**：本文提出哈密顿世界模型 HWM，用学习到的广义坐标—动量相空间替代普通的黑箱潜在转移，并通过带耗散、控制输入和残差项的哈密顿动力学及半隐式辛 Euler 积分进行长时域滚动。多步潜在一致性损失将滚动轨迹约束在真实观测诱导的潜在流形附近。仿真和三类具身视频世界模型实验表明，HWM 可减少能量漂移、改善物理状态预测、视觉与逻辑一致性，并提升下游任务成功率。

### 2. [Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips](http://arxiv.org/abs/2610.25666v1)

- **评分**：70/100
- **作者**：Yian Zhao, Yu Yan, Hongcan Guo et al.
- **方向**：World Models
- **一句话**：Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions.

### 3. [Persistent Planar Memory for Video World Models](http://arxiv.org/abs/2610.23795v1)

- **评分**：69/100
- **作者**：Yuze He, Bin Tan, Zelin Gao et al.
- **方向**：World Models
- **一句话**：Video world models that generate and explore environments at scale need a persistent 3D memory of what they have produced.

### 4. [Momentum: Persistent Dynamics for Video World Models](http://arxiv.org/abs/2610.23423v1)

- **评分**：65/100
- **作者**：Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel et al.
- **方向**：World Models
- **一句话**：Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears.

### 5. [EmbodiedWorld-200K: Toward Embodied World Agents via Embodied-Planning Dataset and Interactive World Models](http://arxiv.org/abs/2610.25959v1)

- **评分**：61/100
- **作者**：X. Feng, J. Tang, Z. Lin et al.
- **方向**：World Models
- **一句话**：Building embodied agents that can perceive, reason, and act across diverse 3D worlds is a central research direction toward artificial general intelligence.

### 6. [LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence](http://arxiv.org/abs/2610.23334v1)

- **评分**：61/100
- **作者**：Jiajun Cao, Kai Tang, Bohua Zhang et al.
- **方向**：World Models
- **一句话**：World-action models jointly predict actions and future world states, but long-horizon manipulation further requires language reasoning to plan subtask objectives, assess execution…

### 7. [T2-z: Test-Time Optimization of Environment Latents for Robotic World Models](http://arxiv.org/abs/2610.22364v1)

- **评分**：57/100
- **作者**：Chenyuan Zhou, Yining Hong, Huang Huang et al.
- **方向**：World Models
- **一句话**：Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicit…

### 8. [BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL](http://arxiv.org/abs/2610.23127v1)

- **评分**：56/100
- **作者**：Liyun Yan, Haoyang Li, Yang Zhang et al.
- **方向**：World Models
- **一句话**：Humanoid control requires coordinating whole-body posture with position and heading in the world frame.
