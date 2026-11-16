# Generation Research Daily Digest

> 生成时间：2026-11-16T03:18:43+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [OnlyAct: Extracting Action Representations from Foundation Models for World Models](http://arxiv.org/abs/2611.14420v1)

- **评分**：74/100
- **作者**：Runjia Li, Minghao Chen, Junyu Xie et al.
- **方向**：World Models
- **一句话**：OnlyAct研究如何从无标签视频中提取可迁移的动作表示，用于训练动作条件视频世界模型。它以预训练视频基础模型V-JEPA 2的帧对表示为起点，通过光流引导的跨场景正样本和同视频硬负样本进行低秩对比适应，使表示突出运动而抑制场景信息。实验覆盖机器人操作、相机导航、游戏和驾驶等任务，结果表明OnlyAct相比现有无标注潜在动作方法具有更强的动作表达能力、相当…
- **精读笔记**：[打开笔记](../notes/2026-11-16/2611.14420-onlyact-extracting-action-representations-from-f.md)

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
- **一句话**：论文提出互惠世界模型RWM，将负责交互认知的Intent模块与负责视听行为生成的Realization模块结合，构建Duo v1全双工实时交互系统。系统以约0.71秒的视频块为单位，在统一时间线上因果地处理用户音频、视频和文本，并持续生成助手的语言、视频和音频。训练包括Intent自回归监督、因果联合视听生成，以及结合自生成语言和视听历史的双重rollou…
- **精读笔记**：[打开笔记](../notes/2026-11-16/2611.15131-duo-a-reciprocal-world-model-for-full-duplex-int.md)

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

### 3. [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](http://arxiv.org/abs/2611.18078v1)

- **评分**：61/100
- **作者**：Ruiqi Shu, Xufeng Zhan, Yuanzhi Liang et al.
- **方向**：Video Generation
- **一句话**：Direct image-to-video diffusion models entangle pixel synthesis with implicit latent motion, precluding persistent 3D mechanical equilibrium, mid-rollout intervention, and counter…

### 4. [Prediction or Persistence? What Future-Prediction Scores Miss About World Models](http://arxiv.org/abs/2611.15082v1)

- **评分**：60/100
- **作者**：Animesh Maheshwari
- **方向**：World Models
- **一句话**：Pretrained video world models are compared and chosen as components for robot learning largely by future-prediction scores.

### 5. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](http://arxiv.org/abs/2611.13348v1)

- **评分**：57/100
- **作者**：Yikun Zhang, Minghao Guo, Guangxue Xu et al.
- **方向**：World Models
- **一句话**：Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sampl…

### 6. [CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models](http://arxiv.org/abs/2611.15602v1)

- **评分**：53/100
- **作者**：Qirui Li, Xin Zhang, Yabo Chen et al.
- **方向**：World Models
- **一句话**：Multiplayer generative world models must produce observations that agree on shared entities despite different camera motions and occlusions.

### 7. [An Energy-Based Perspective on Machine Learning](http://arxiv.org/abs/2611.14383v1)

- **评分**：48/100
- **作者**：Bo Dai, Yilun Du
- **方向**：World Models
- **一句话**：Energy-based models (EBMs) define a distribution through a scalar energy, $p_θ(x)\propto\exp(-E_θ(x))$, and are usually presented as one model family among many.
