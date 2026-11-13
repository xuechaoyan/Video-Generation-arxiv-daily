# Generation Research Daily Digest

> 生成时间：2026-11-13T03:41:25+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [OnlyAct: Extracting Action Representations from Foundation Models for World Models](http://arxiv.org/abs/2611.14420v1)

- **评分**：74/100
- **作者**：Runjia Li, Minghao Chen, Junyu Xie et al.
- **方向**：World Models
- **一句话**：OnlyAct 旨在从无标签视频中学习可迁移、场景不变且表达能力强的动作表示，用于动作条件视频世界模型。方法以预训练视频基础模型 V-JEPA 2 的帧对嵌入为起点，通过低秩适配器和无标签对比学习进行调整：利用光流引导的场景替换构造保持运动、改变场景的正样本，并从同一视频的其他时间窗口构造共享场景但动作不同的困难负样本。该目标使表示空间突出动作信息、抑制场…
- **精读笔记**：[打开笔记](../notes/2026-11-13/2611.14420-onlyact-extracting-action-representations-from-f.md)

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
- **一句话**：论文提出互惠世界模型RWM及其模块化实现Duo v1，将世界模型从单纯模拟物理环境扩展为同时包含交互智能与视听现实。系统由自回归多模态Intent模块和因果视听Realization模块组成，以约0.71秒的17帧视频块为基本单位，在统一时间线上持续接收用户音频、视频和文本，并生成文本决策、视频和立体声音频。Intent模块决定说话或等待并生成语义隐藏状态…
- **精读笔记**：[打开笔记](../notes/2026-11-13/2611.15131-duo-a-reciprocal-world-model-for-full-duplex-int.md)

## 快速浏览

### 1. [Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](http://arxiv.org/abs/2611.11452v1)

- **评分**：62/100
- **作者**：Weizhong Huang, Huaijia Kou, Tianyu Xie et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Agentic autoregressive video generation combines semantic planning, sequential generation, and visual verification for controllable synthesis.

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

### 4. [DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](http://arxiv.org/abs/2611.11166v2)

- **评分**：59/100
- **作者**：Zhongxi Chen, Yi Yang, Xinyi Chen et al.
- **方向**：World Models
- **一句话**：Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand.

### 5. [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](http://arxiv.org/abs/2611.11912v1)

- **评分**：58/100
- **作者**：Zhimin Liao, Ping Wei, Kai Mao et al.
- **方向**：World Models
- **一句话**：LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural…

### 6. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](http://arxiv.org/abs/2611.13348v1)

- **评分**：57/100
- **作者**：Yikun Zhang, Minghao Guo, Guangxue Xu et al.
- **方向**：World Models
- **一句话**：Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sampl…

### 7. [Mitigating SM-Level Load Imbalance in 3D Gaussian Splatting on GPUs](http://arxiv.org/abs/2611.12319v1)

- **评分**：56/100
- **作者**：Junha Ryu, Hoi-Jun Yoo
- **方向**：World Models
- **一句话**：3D Gaussian Splatting (3DGS) enables photorealistic, real-time rendering on commodity GPUs and is increasingly adopted in generative world models and autonomous driving simulators.
