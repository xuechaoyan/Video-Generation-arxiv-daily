# Generation Research Daily Digest

> 生成时间：2026-11-11T18:54:01+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [OnlyAct: Extracting Action Representations from Foundation Models for World Models](http://arxiv.org/abs/2611.14420v1)

- **评分**：74/100
- **作者**：Runjia Li, Minghao Chen, Junyu Xie et al.
- **方向**：World Models
- **一句话**：OnlyAct提出利用预训练视频基础模型V-JEPA 2提取动作表示，而不是从无标签视频中从零学习潜在动作。方法通过光流引导的跨场景正样本和同视频难负样本进行无标签对比适应，使嵌入突出运动信息并抑制场景信息，同时避免重建瓶颈造成的表达能力损失。实验覆盖机器人操作、相机导航、游戏和驾驶等领域，结果表明该表示具有更强的动作表达能力、相当的场景不变性，并能提升动…
- **精读笔记**：[打开笔记](../notes/2026-11-11/2611.14420-onlyact-extracting-action-representations-from-f.md)

## 快速浏览

### 1. [Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning](http://arxiv.org/abs/2611.10660v1)

- **评分**：68/100
- **作者**：Yinuo Jiang, Guangzhi Wang, Yiran Wang et al.
- **方向**：World Models
- **一句话**：论文提出 DIAL，用于改进基于潜在世界模型的目标条件视觉规划。方法针对两个问题：教师强制训练与规划时自回归滚动之间存在分布不匹配，以及 CEM 通常使用与目标无关的初始动作分布。DIAL 通过轨迹对齐训练前向动力学，使其适应自身生成的潜在状态；通过多步逆动力学监督和对模型生成转移的逆动力学约束，保留潜在状态中的动作相关信息。规划时，逆动力学头根据当前预测…

### 2. [WorldFoundry: Towards Unified Infrastructure for World Intelligence](http://arxiv.org/abs/2611.10771v1)

- **评分**：67/100
- **作者**：Juanxi Tian, Jiadong Hou, Baiang Li et al.
- **方向**：World Models
- **一句话**：Visual generative models increasingly blur the line between synthesizing observations and simulating environments.

### 3. [Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](http://arxiv.org/abs/2611.11452v1)

- **评分**：62/100
- **作者**：Weizhong Huang, Huaijia Kou, Tianyu Xie et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Agentic autoregressive video generation combines semantic planning, sequential generation, and visual verification for controllable synthesis.

### 4. [Few-Step Streaming Video Generation via Condition Shifting](http://arxiv.org/abs/2611.14033v1)

- **评分**：61/100
- **作者**：Deyuan Liu, Jungang Li, Kaiwen Zheng et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step sampling reduces the cost of streaming video generation.

### 5. [Tiresias: Towards Language-Conditioned World Models](http://arxiv.org/abs/2611.10392v1)

- **评分**：60/100
- **作者**：Fengyi Wu, Yifei Dong, Yetong Sha et al.
- **方向**：World Models
- **一句话**：World models enable planning through internal simulation, while natural language provides intuitive task specification.

### 6. [DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](http://arxiv.org/abs/2611.11166v2)

- **评分**：59/100
- **作者**：Zhongxi Chen, Yi Yang, Xinyi Chen et al.
- **方向**：World Models
- **一句话**：Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand.

### 7. [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](http://arxiv.org/abs/2611.11912v1)

- **评分**：58/100
- **作者**：Zhimin Liao, Ping Wei, Kai Mao et al.
- **方向**：World Models
- **一句话**：LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural…

### 8. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](http://arxiv.org/abs/2611.13348v1)

- **评分**：57/100
- **作者**：Yikun Zhang, Minghao Guo, Guangxue Xu et al.
- **方向**：World Models
- **一句话**：Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sampl…

### 9. [Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs](http://arxiv.org/abs/2611.12319v1)

- **评分**：56/100
- **作者**：Junha Ryu, Hoi-Jun Yoo
- **方向**：World Models
- **一句话**：3D Gaussian Splatting (3DGS) enables photorealistic, real-time rendering on commodity GPUs and is increasingly adopted in generative world models and autonomous driving simulators.
