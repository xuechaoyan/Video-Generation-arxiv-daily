# Generation Research Daily Digest

> 生成时间：2026-11-15T18:01:31+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [OnlyAct: Extracting Action Representations from Foundation Models for World Models](http://arxiv.org/abs/2611.14420v1)

- **评分**：74/100
- **作者**：Runjia Li, Minghao Chen, Junyu Xie et al.
- **方向**：World Models
- **一句话**：OnlyAct研究如何从无标注视频中学习可迁移的动作表示，以训练动作条件视频世界模型。方法以预训练视频基础模型V-JEPA 2为起点，通过低秩适配器和无标签对比学习进行适应：利用光流引导的跨场景动作保持样本作为正样本，并利用同一视频中不同时间窗口的帧对作为困难负样本，使嵌入更关注动作而非场景。所得表示既可从示范视频中提取动作并迁移到新场景，也可通过少量带动…
- **精读笔记**：[打开笔记](../notes/2026-11-15/2611.14420-onlyact-extracting-action-representations-from-f.md)

### 2. [BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model](http://arxiv.org/abs/2611.14815v1)

- **评分**：74/100
- **作者**：Junyoung Seo, Jaewoo Seo, Seungryong Kim et al.
- **方向**：World Models
- **一句话**：Driving world models aim to simulate how a scene unfolds under different ego actions.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [Duo: A Reciprocal World Model for Full-Duplex Interaction](http://arxiv.org/abs/2611.15131v1)

- **评分**：74/100
- **作者**：Hengyuan Cao, Biao Gong, Guoshan Lu et al.
- **方向**：World Models
- **一句话**：论文提出互惠世界模型RWM，将世界建模从单纯模拟物理环境扩展为同时建模环境与其中的智能交互者。Duo v1由自回归多模态意图模块和因果视听实现模块组成：前者按约0.71秒的时间块持续决定说话或等待并生成文本，后者依据意图隐藏状态、用户视听输入、参考图像和历史媒体生成同步的语音与视频。系统通过统一时间线、跨块因果注意力、双重 rollout 蒸馏、四步生成、…
- **精读笔记**：[打开笔记](../notes/2026-11-15/2611.15131-duo-a-reciprocal-world-model-for-full-duplex-int.md)

## 快速浏览

### 1. [ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving](http://arxiv.org/abs/2611.16579v1)

- **评分**：65/100
- **作者**：Ziying Song, Shengkai Zhang, Caiyan Jia et al.
- **方向**：World Models
- **一句话**：Joint-Embedding Predictive Architectures (JEPAs) enable future prediction in latent space without pixel reconstruction.

### 2. [Few-Step Streaming Video Generation via Condition Shifting](http://arxiv.org/abs/2611.14033v1)

- **评分**：61/100
- **作者**：Deyuan Liu, Jungang Li, Kaiwen Zheng et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step sampling reduces the cost of streaming video generation.

### 3. [Prediction or Persistence? What Future-Prediction Scores Miss About World Models](http://arxiv.org/abs/2611.15082v1)

- **评分**：60/100
- **作者**：Animesh Maheshwari
- **方向**：World Models
- **一句话**：Pretrained video world models are compared and chosen as components for robot learning largely by future-prediction scores.

### 4. [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](http://arxiv.org/abs/2611.11912v1)

- **评分**：58/100
- **作者**：Zhimin Liao, Ping Wei, Kai Mao et al.
- **方向**：World Models
- **一句话**：LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural…

### 5. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](http://arxiv.org/abs/2611.13348v1)

- **评分**：57/100
- **作者**：Yikun Zhang, Minghao Guo, Guangxue Xu et al.
- **方向**：World Models
- **一句话**：Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sampl…

### 6. [Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs](http://arxiv.org/abs/2611.12319v1)

- **评分**：56/100
- **作者**：Junha Ryu, Hoi-Jun Yoo
- **方向**：World Models
- **一句话**：3D Gaussian Splatting (3DGS) enables photorealistic, real-time rendering on commodity GPUs and is increasingly adopted in generative world models and autonomous driving simulators.

### 7. [WanderBench: Can World Models Explore Dynamic Worlds from Video?](http://arxiv.org/abs/2611.12557v1)

- **评分**：53/100
- **作者**：Yuhang Chen, Jiheng Li, Jiale Wang et al.
- **方向**：World Models
- **一句话**：Video world models conditioned on an input video make it possible to explore real, recorded dynamic scenes, enabling re-shooting of footage, free-viewpoint replay, and real-to-sim…
