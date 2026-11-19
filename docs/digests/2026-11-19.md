# Generation Research Daily Digest

> 生成时间：2026-11-19T19:39:16+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [FastFrames: Video Generation at Interactive Latency](http://arxiv.org/abs/2611.23226v1)

- **评分**：79/100
- **作者**：Gene Chou, Guandao Yang, Fujun Luan et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文研究自回归视频扩散模型的端到端交互延迟，指出 VAE 解码和 KV 缓存更新等非去噪组件是主要瓶颈。FastFrames 用基于 ConvNeXt 的轻量像素解码器替代 VAE，用轻量 KV 修复网络替代额外的 DiT 缓存更新，并结合持久化缓存、注意力分段、算子融合、CUDA Graph 和上下文并行等系统优化。在 480p 和 B200 GPU 上…
- **精读笔记**：[打开笔记](../notes/2026-11-19/2611.23226-fastframes-video-generation-at-interactive-laten.md)

### 2. [Code World Model 2.0: Towards Infinite Controllable Video Generation](http://arxiv.org/abs/2611.22925v2)

- **评分**：75/100
- **作者**：Ruoyu Wang, Hao Zhong, Yanming Yang et al.
- **方向**：Video Generation, World Models
- **一句话**：本文提出 Invoker-Render，一种将双向视频创作与四步因果流式渲染统一起来的代理条件视频生成框架。模型通过共享接口接收结构代理、外观参考和语言，可同时处理粗粒度布局与精细关节几何，并在缺少细节时生成合理的局部运动。作者构建了约 200 小时的多粒度对齐数据集，并提出 Progressive Forcing：先通过教师强制和重采样强制进行因果适配，…
- **精读笔记**：[打开笔记](../notes/2026-11-19/2611.22925-code-world-model-2-0-towards-infinite-controllab.md)

### 3. [Towards Data-Efficient, Real-Time World Models](http://arxiv.org/abs/2611.22497v1)

- **评分**：72/100
- **作者**：Raluca Stevenson, David Bignell, Jennifer C. White et al.
- **方向**：World Models
- **一句话**：本文提出WHAM-RT，一种面向实时交互和低数据训练的动作条件世界模型。它以大型双向骨干Transformer一次性预测下一帧图像草稿，并利用压缩的长时上下文和轻量级离散扩散细化Transformer进行多轮掩码预测，从而缓解自回归逐词元生成的速度瓶颈。在Bleeding Edge游戏环境中，WHAM-RT在单张H100上最高达到17 FPS，相比WHAM…
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
