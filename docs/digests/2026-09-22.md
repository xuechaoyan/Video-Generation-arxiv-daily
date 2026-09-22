# Generation Research Daily Digest

> 生成时间：2026-09-22T15:46:52+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](http://arxiv.org/abs/2609.24984v1)

- **评分**：76/100
- **作者**：Wangbo Yu, Kunhao Liu, Wenbo Hu et al.
- **方向**：World Models
- **一句话**：本文提出 WorldCrafter，用于长时间、可交互视频生成的相机可控自回归视频世界模型。方法将历史潜在帧及其相机参数输入由预训练多视角三维表示初始化的记忆编码器，形成隐式三维感知表示；随后，姿态引导的读出模块根据即将执行的相机轨迹，从该表示中提取固定数量的记忆令牌，与近期时间上下文共同条件化视频 DiT。为控制计算量，系统保留最新帧并通过最大化目标区域…
- **精读笔记**：[打开笔记](../notes/2026-09-22/2609.24984-worldcrafter-consistent-video-world-model-with-i.md)

### 2. [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](http://arxiv.org/abs/2609.21712v1)

- **评分**：74/100
- **作者**：Boni Hu, Xiong Wei, Haoming Huang et al.
- **方向**：World Models
- **一句话**：ZYT-World 面向自动驾驶闭环仿真，构建了一个可控的七视图世界模型，原生支持四个超广角鱼眼视图和三个针孔视图，并保持各自的投影、分辨率和几何关系。模型结合 Plücker 射线、基于自车运动的 AdaLN、像素对齐布局条件和跨视图注意力，实现逐时间步的运动、交通参与者及信号灯控制。通过教师强制、因果一致性蒸馏、自回滚分布匹配蒸馏和 RigCritic…
- **精读笔记**：[打开笔记](../notes/2026-09-22/2609.21712-zyt-world-a-real-time-controllable-world-model-f.md)

### 3. [CausalWM: Causal Chain-of-Thought Reasoning for Embodied World Model](http://arxiv.org/abs/2609.23184v1)

- **评分**：74/100
- **作者**：Ziming Xu, Shuang Liang, Ruobing Han et al.
- **方向**：World Models
- **一句话**：Embodied world models learn to predict future physical dynamics from visual observations and control signals, where physical knowledge is implicitly entangled within latent repres…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [Streaming Video Editing with Easy Adaptation](http://arxiv.org/abs/2609.24788v1)

- **评分**：72/100
- **作者**：Yujia Hu, Jiajun Li, Zihao He et al.
- **方向**：Video Generation
- **一句话**：In this paper, we propose SVEET, a framework that requires merely training on a pretrained bidirectional video diffusion model but supports high-quality streaming video editing in…

### 2. [ConsistWorld: Evidence Routing for Consistent Multi-Agent World Models](http://arxiv.org/abs/2609.22641v1)

- **评分**：71/100
- **作者**：Qianxun Xu, Xianfang Zeng, Xinyao Liao et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Autoregressive video world models enable temporally coherent generation for a single observer.

### 3. [Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning](http://arxiv.org/abs/2609.24033v1)

- **评分**：69/100
- **作者**：Kejia Hu, Wentong Zhai, Bo Zhao et al.
- **方向**：World Models
- **一句话**：Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences.

### 4. [CrossDistill: Balancing Quality and Diversity via Trajectory-Level Hybrid Few-Step Distillation](http://arxiv.org/abs/2609.14725v2)

- **评分**：65/100
- **作者**：Yuxi Liu, Haoyu Li, Yixiang Cai et al.
- **方向**：Video Generation
- **一句话**：Few-step distillation accelerates diffusion models but must balance diversity and fidelity: trajectory-based distillation preserves mode coverage, while distribution matching shar…

### 5. [DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](http://arxiv.org/abs/2609.24976v1)

- **评分**：62/100
- **作者**：Haoran Yuan, Zekai Wang, Boning Shao et al.
- **方向**：World Models
- **一句话**：Dexterous manipulation depends on contact dynamics that are often only partially observable from vision.

### 6. [OnlineWM: Causality-Aware Active Online Learning for Effective World Modeling](http://arxiv.org/abs/2609.23753v1)

- **评分**：54/100
- **作者**：Yikun Miao, Fangqi Zhu, Quanxin Shou et al.
- **方向**：World Models
- **一句话**：Generative world models aim to predict future states conditioned on actions, where action controllability is fundamental for reliable dynamics modeling.

### 7. [HappyWorld-Bench](http://arxiv.org/abs/2609.24308v1)

- **评分**：53/100
- **作者**：Zhiqi Bai, Junai Cai, Yixin Chen et al.
- **方向**：World Models
- **一句话**：Evaluating world models requires assessing both the quality of the worlds they generate and their consistency and responsiveness under exploration, interaction, and modification.
