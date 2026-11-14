# Generation Research Daily Digest

> 生成时间：2026-11-14T03:40:31+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [OnlyAct: Extracting Action Representations from Foundation Models for World Models](http://arxiv.org/abs/2611.14420v1)

- **评分**：74/100
- **作者**：Runjia Li, Minghao Chen, Junyu Xie et al.
- **方向**：World Models
- **一句话**：OnlyAct研究如何从无标签视频中学习适用于视频世界模型的可迁移动作表示。作者以预训练的视频基础模型V-JEPA 2为起点，通过低秩适配器和无需动作标签的对比学习，将帧对嵌入从同时包含场景与运动信息，调整为更偏向动作且具有场景不变性的表示。训练时利用光流引导的跨场景动作保留样本作为正样本，并利用同一视频中不同时间窗口的帧对作为困难负样本。适应后的表示被输…
- **精读笔记**：[打开笔记](../notes/2026-11-14/2611.14420-onlyact-extracting-action-representations-from-f.md)

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
- **一句话**：本文提出互惠世界模型RWM及其模块化实现Duo v1，目标是让世界模型同时具备对用户视听输入的持续感知、交互推理、参与时机决策和视听行为生成能力。系统由多模态Intent模块与因果视听Realization模块组成，以约0.71秒的17帧视频块为基本单位，在统一时间线上处理用户输入、助手文本意图和生成的音视频历史。Intent模块自回归地产生<speak>…
- **精读笔记**：[打开笔记](../notes/2026-11-14/2611.15131-duo-a-reciprocal-world-model-for-full-duplex-int.md)

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
