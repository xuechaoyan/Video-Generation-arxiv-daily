# Generation Research Daily Digest

> 生成时间：2026-11-19T04:37:46+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [FastFrames: Video Generation at Interactive Latency](http://arxiv.org/abs/2611.23226v1)

- **评分**：79/100
- **作者**：Gene Chou, Guandao Yang, Fujun Luan et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文研究如何将自回归视频扩散模型的端到端单帧响应延迟降至交互式范围。作者分析发现，VAE 解码和 KV 缓存更新等非去噪操作是主要瓶颈，并提出轻量级像素解码器、KV 缓存修复网络以及面向硬件的系统优化。FastFrames 在 480p 下使用两步扩散生成单个潜在帧：1.3B 版本在单张 B200 GPU 上达到 36 毫秒延迟，14B 版本在 8 张 B…
- **精读笔记**：[打开笔记](../notes/2026-11-19/2611.23226-fastframes-video-generation-at-interactive-laten.md)

### 2. [Code World Model 2.0: Towards Infinite Controllable Video Generation](http://arxiv.org/abs/2611.22925v2)

- **评分**：75/100
- **作者**：Ruoyu Wang, Hao Zhong, Yanming Yang et al.
- **方向**：Video Generation, World Models
- **一句话**：论文提出 Invoker-Render，一种由视觉代理驱动的视频渲染框架，将双向离线视频创作与四步因果实时流式生成统一在同一条件接口下。模型可处理语义布局、几何结构等不同代理及粗细不同的控制粒度：粗代理约束场景布局、相机和主体根轨迹，细代理进一步约束关节和表面几何。作者提出 ProForcing 训练流程，依次进行因果教师强制与重采样强制、基于数据历史的四…
- **精读笔记**：[打开笔记](../notes/2026-11-19/2611.22925-code-world-model-2-0-towards-infinite-controllab.md)

### 3. [Towards Data-Efficient, Real-Time World Models](http://arxiv.org/abs/2611.22497v1)

- **评分**：72/100
- **作者**：Raluca Stevenson, David Bignell, Jennifer C. White et al.
- **方向**：World Models
- **一句话**：本文针对动作条件世界模型的两个关键问题展开研究：高质量长时游戏生成速度慢，以及训练所需数据量过大。作者提出WHAM-RT，将大规模双向骨干Transformer的一次性下一帧预测与轻量级离散扩散细化Transformer结合，并通过可学习寄存器式上下文压缩保留长时序信息。在Bleeding Edge游戏环境中，WHAM-RT在单个H100上最高达到17 F…
- **精读笔记**：[打开笔记](../notes/2026-11-19/2611.22497-towards-data-efficient-real-time-world-models.md)

## 快速浏览

### 1. [Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving](http://arxiv.org/abs/2611.22691v1)

- **评分**：65/100
- **作者**：Jia Hu, Yang Chang, Panqu Wang et al.
- **方向**：World Models
- **一句话**：World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions.

### 2. [Risk-Triggered Search: Behavior-Preserving Safe Control](http://arxiv.org/abs/2611.24409v1)

- **评分**：64/100
- **作者**：Xinyu Deng, Bohao Lan, Kunpeng Li et al.
- **方向**：World Models
- **一句话**：Pre-trained visual world models generate multi-step action plans from current and goal observations, yet terminal-proximity objectives fail to prevent forbidden-zone traversal or…

### 3. [Distilling World Action Models for Efficient Bimanual Manipulation via Anchored Path Matching](http://arxiv.org/abs/2611.22592v1)

- **评分**：63/100
- **作者**：Jialong Liu, Junjie He, Yandu Chen et al.
- **方向**：World Models
- **一句话**：World Action Models (WAMs) jointly generate future video and robot actions through iterative denoising.

### 4. [Efficient World-Model Planning via Physics-Guided Search Distillation](http://arxiv.org/abs/2611.24171v1)

- **评分**：58/100
- **作者**：Hongyu Zhang, Xiaoshuai Hao, Heye Huang et al.
- **方向**：World Models
- **一句话**：World models support autonomous driving by evaluating candidate trajectories through predicted future scene evolution.

### 5. [Learning Agent-Centric Vision-Language-Action World Models for Autonomous Driving](http://arxiv.org/abs/2611.22880v1)

- **评分**：57/100
- **作者**：Guoqing Wang, Pin Tang, Xiangxuan Ren et al.
- **方向**：World Models
- **一句话**：Recent progress in integrating vision-language-action (VLA) models with world modeling has significantly advanced end-to-end autonomous driving by allowing systems to reason about…

### 6. [StrideWorld: Benchmarking Scene Rigidity and Action Consistency in Interactive Video World Model](http://arxiv.org/abs/2611.24408v1)

- **评分**：56/100
- **作者**：Chuang Wang, Rui Nie, Jie Song et al.
- **方向**：World Models
- **一句话**：Interactive video world models turn user commands into the exploration of a generated scene, which requires the scene to keep its 3D structure as the camera moves and each action…

### 7. [Plausible Videos Can Lead to Poor Decisions: Diagnosing and CURE-ing World Models for Planning](http://arxiv.org/abs/2611.22561v1)

- **评分**：55/100
- **作者**：Raphael C. Kim, Michele Santacatterina, Jingsen Zhu et al.
- **方向**：World Models
- **一句话**：Action-conditioned world models are increasingly used as world models for planning, yet a world model that makes plausible, realistic-looking videos that are consistent with the t…
