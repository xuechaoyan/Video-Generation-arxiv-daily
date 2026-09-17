# Generation Research Daily Digest

> 生成时间：2026-09-17T15:42:18+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](http://arxiv.org/abs/2609.18430v1)

- **评分**：80/100
- **作者**：Awomo-WM Team,  :, Enhui Ma et al.
- **方向**：World Models
- **一句话**：论文提出 StrucPhysVideo，目标是让视频世界模型更准确地学习物体运动、接触、形变和状态变化。作者构建了包含镜头切分、运动感知选段、技术质量过滤、内容纯度过滤、物理相关性验证以及结构化物理字幕和标签的数据流程，并将相机运动与物体行为分开描述。在模型方面，StrucPhysVideo-TI2V 使用冻结的多模态编码器、首帧约束的流匹配和稀疏 MoE…
- **精读笔记**：[打开笔记](../notes/2026-09-17/2609.18430-strucphysvideo-learning-physical-dynamics-from-s.md)

### 2. [World in World: Explore the World with World Models](http://arxiv.org/abs/2609.11548v1)

- **评分**：77/100
- **作者**：Chenxi Song, Yanming Yang, Chi Zhang
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：本文提出 World in World（WiW），一种无需训练的视觉证据接口，用于扩展冻结因果视频世界模型的控制能力。方法将源视频、目标视角投影、几何渲染和生成历史统一表示为带相机、时间及空间有效性信息的干净视觉状态，并通过模型原生自注意力注入。针对证据定位和证据强度控制，WiW分别提出对应关系引导注意力路由（CGAR）和证据级注意力 CFG（EWA）。其…
- **精读笔记**：[打开笔记](../notes/2026-09-17/2609.11548-world-in-world-explore-the-world-with-world-mode.md)

### 3. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](http://arxiv.org/abs/2609.17521v1)

- **评分**：75/100
- **作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang et al.
- **方向**：Video Generation
- **一句话**：本文提出 PhysStream，用于从单张图像自回归生成具有物理合理性的可控视频。用户只需在指定时刻向特定物体施加稀疏的三维速度增量，模型便可逐帧生成多物体之间的碰撞、摩擦和运动响应。方法的核心是在线更新的结构化场景记忆：利用深度估计得到位置图，并利用 SAM2 得到目标跟踪图，将模型自身历史生成结果反馈给后续生成。训练分为两个阶段，先让双向视频模型学习速…
- **精读笔记**：[打开笔记](../notes/2026-09-17/2609.17521-physstream-streaming-physics-grounded-video-gene.md)

## 快速浏览

### 1. [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](http://arxiv.org/abs/2609.15863v1)

- **评分**：75/100
- **作者**：Xiaofeng Mao, Peijia Lin, Shaohao Rui et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Video diffusion models are stochastic and hard to control: precise content often requires repeated sampling without guaranteed success, and long-horizon scenes drift in appearance…

### 2. [AlayaVista: Streaming World Modeling from Panoramic States to Perspective Video](http://arxiv.org/abs/2609.14462v1)

- **评分**：74/100
- **作者**：Jiaming Tan, Mingliang Zhai, Zhen Li et al.
- **方向**：World Models
- **一句话**：Interactive video world models must maintain broad scene context under camera motion while producing high-fidelity observations with low latency.

### 3. [Zing-0.5: Toward Playable Worlds with Real-Time Joint Action and Text Control](http://arxiv.org/abs/2609.17909v1)

- **评分**：74/100
- **作者**：Mingyang Chen, Shengdong Chen, Xiaoxiao Fu et al.
- **方向**：World Models
- **一句话**：We introduce Zing-0.5, a 5B autoregressive world model designed for playability: users can explore generated worlds, influence unfolding events, and respond to the resulting feedb…

### 4. [FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence](http://arxiv.org/abs/2609.17210v1)

- **评分**：69/100
- **作者**：Yinhao Li, Weixin Mao, Zihan Lan et al.
- **方向**：World Models
- **一句话**：Vision-language-action (VLA) models, world-action models (WAMs), and offline reinforcement learning methods are rapidly expanding the design space of embodied policies, yet turnin…

### 5. [World-Action Models for Robot Learning and Control: A Survey](http://arxiv.org/abs/2609.16074v1)

- **评分**：66/100
- **作者**：Zuxing Lu, Hongjia Zhai, Guanzhi Wang et al.
- **方向**：World Models
- **一句话**：Robots operating in open environments act under partial observability, physical constraints, and dynamic task contexts.

### 6. [CrossDistill: Balancing Quality and Diversity via Trajectory-Level Hybrid Few-Step Distillation](http://arxiv.org/abs/2609.14725v1)

- **评分**：65/100
- **作者**：Yuxi Liu, Haoyu Li, Yixiang Cai et al.
- **方向**：Video Generation
- **一句话**：Few-step distillation accelerates diffusion models but must balance diversity and fidelity: trajectory-based distillation preserves mode coverage, while distribution matching shar…

### 7. [From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation](http://arxiv.org/abs/2609.15382v1)

- **评分**：60/100
- **作者**：Ailing Zhang, Fan Gao, Song Zhang et al.
- **方向**：World Models
- **一句话**：Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions.
