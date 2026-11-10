# Generation Research Daily Digest

> 生成时间：2026-11-10T18:56:10+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](http://arxiv.org/abs/2611.07551v2)

- **评分**：73/100
- **作者**：Jia Li, Xurui Peng, Xing Wang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文提出 PreSTP，用模型去噪过程中产生的早期干净估计在线识别两类逐令牌冗余：相邻帧间静态区域的跨帧冗余，以及同一帧内较早稳定令牌的跨步冗余。方法通过统一掩码跳过冗余令牌，并用最近计算值保持输出和 KV 缓存一致；同时根据内容变化复用静态掩码，以减少探测开销。实验覆盖 CausVid、Self-Forcing、AnyFlow、LongLive 以及 O…
- **精读笔记**：[打开笔记](../notes/2026-11-10/2611.07551-training-free-predictive-spatio-temporal-token-p.md)

### 2. [GPWM: Modeling the World as 3D Particle Motion](http://arxiv.org/abs/2611.08338v1)

- **评分**：73/100
- **作者**：Robert Ren, Matthew Bronars, He Zhu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文提出 GPWM，将三维场景表示为粒子、刚体和执行器的运动，并用物体感知的多分辨率时空 Transformer 建模刚体、可变形体、布料和颗粒材料的动力学。流匹配与扩散强制支持流式、自回归的长时域生成，使模型能够在固定训练窗口之外持续推演。基于包含 2550 万帧、六类物理场景的 ParticleWorlds 数据集，GPWM 在各领域取得优于已有方法的…
- **精读笔记**：[打开笔记](../notes/2026-11-10/2611.08338-gpwm-modeling-the-world-as-3d-particle-motion.md)

### 3. [AR-Edit: Training-Free Autoregressive Video Editing without Inversion](http://arxiv.org/abs/2611.09795v1)

- **评分**：73/100
- **作者**：Hovhannes Margaryan, Quentin Bammey, Christian Sandor et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文研究DMD蒸馏自回归视频扩散模型上的实时、因果、免训练视频编辑。作者发现，在不同噪声时间步中，自注意力的查询和键基本稳定，而值特征显著变化并承载视频身份与内容。基于此，AR-Edit通过一次源视频前向传播缓存干净值特征，从随机高斯噪声出发，在目标提示词引导的少步去噪中选择性注入这些值，并利用Commit-then-Anchor策略保护未编辑区域。实验在…
- **精读笔记**：[打开笔记](../notes/2026-11-10/2611.09795-ar-edit-training-free-autoregressive-video-editi.md)

## 快速浏览

### 1. [Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation](http://arxiv.org/abs/2611.09096v1)

- **评分**：70/100
- **作者**：Bohan Wang, Shuo Chen, Yunzhi Li et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) modeling is arguably the only way to extend a fixed-length video diffusion model to longer or even streaming videos.

### 2. [Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning](http://arxiv.org/abs/2611.10660v1)

- **评分**：68/100
- **作者**：Yinuo Jiang, Guangzhi Wang, Yiran Wang et al.
- **方向**：World Models
- **一句话**：Latent world models enable visual control by planning action sequences in compact representation spaces, but a gap remains between how latent dynamics are learned and how they are…

### 3. [WorldFoundry: Towards Unified Infrastructure for World Intelligence](http://arxiv.org/abs/2611.10771v1)

- **评分**：67/100
- **作者**：Juanxi Tian, Jiadong Hou, Baiang Li et al.
- **方向**：World Models
- **一句话**：Visual generative models increasingly blur the line between synthesizing observations and simulating environments.

### 4. [Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](http://arxiv.org/abs/2611.11452v1)

- **评分**：62/100
- **作者**：Weizhong Huang, Huaijia Kou, Tianyu Xie et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Agentic autoregressive video generation combines semantic planning, sequential generation, and visual verification for controllable synthesis.

### 5. [Tiresias: Towards Language-Conditioned World Models](http://arxiv.org/abs/2611.10392v1)

- **评分**：60/100
- **作者**：Fengyi Wu, Yifei Dong, Yetong Sha et al.
- **方向**：World Models
- **一句话**：World models enable planning through internal simulation, while natural language provides intuitive task specification.

### 6. [DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](http://arxiv.org/abs/2611.11166v1)

- **评分**：59/100
- **作者**：Zhongxi Chen, Yi Yang, Xinyi Chen et al.
- **方向**：World Models
- **一句话**：Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand.

### 7. [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](http://arxiv.org/abs/2611.11912v1)

- **评分**：58/100
- **作者**：Zhimin Liao, Ping Wei, Kai Mao et al.
- **方向**：World Models
- **一句话**：LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural…
