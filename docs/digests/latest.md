# Generation Research Daily Digest

> 生成时间：2026-09-19T14:51:52+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](http://arxiv.org/abs/2609.18430v1)

- **评分**：80/100
- **作者**：Awomo-WM Team,  :, Enhui Ma et al.
- **方向**：World Models
- **一句话**：本文提出 StrucPhysVideo，旨在学习物体运动、接触、形变和状态变化等物理动力学。工作首先构建物理导向的数据流程，通过镜头与运动感知分割、技术质量过滤、内容纯度过滤、物理相关性验证，以及包含物体、材料、相机运动和时间定位交互的结构化描述，筛选并标注视频数据。基于这些数据，作者训练了稀疏 MoE 文本-图像到视频模型 StrucPhysVideo-…
- **精读笔记**：[打开笔记](../notes/2026-09-19/2609.18430-strucphysvideo-learning-physical-dynamics-from-s.md)

### 2. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](http://arxiv.org/abs/2609.17521v1)

- **评分**：75/100
- **作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang et al.
- **方向**：Video Generation
- **一句话**：PhysStream 面向静态摄像机下的多物体桌面场景，提出一种支持交互式中途控制的物理约束图像到视频自回归生成方法。用户只需在指定时刻对目标物体输入稀疏的三维速度增量，模型便逐帧生成后续视频，并根据自身历史帧在线更新位置图和物体跟踪图作为结构化场景记忆。方法先训练带速度控制的双向模型，再转换为带因果注意力、KV 缓存和场景记忆的自回归模型。作者构建了约…
- **精读笔记**：[打开笔记](../notes/2026-09-19/2609.17521-physstream-streaming-physics-grounded-video-gene.md)

### 3. [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](http://arxiv.org/abs/2609.15863v1)

- **评分**：75/100
- **作者**：Xiaofeng Mao, Peijia Lin, Shaohao Rui et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Video diffusion models are stochastic and hard to control: precise content often requires repeated sampling without guaranteed success, and long-horizon scenes drift in appearance…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [Zing-0.5: Toward Playable Worlds with Real-Time Joint Action and Text Control](http://arxiv.org/abs/2609.17909v1)

- **评分**：74/100
- **作者**：Mingyang Chen, Shengdong Chen, Xiaoxiao Fu et al.
- **方向**：World Models
- **一句话**：We introduce Zing-0.5, a 5B autoregressive world model designed for playability: users can explore generated worlds, influence unfolding events, and respond to the resulting feedb…

### 2. [Astronex-World 1.0: Real-Time Interactive World Model Foundation](http://arxiv.org/abs/2609.20034v1)

- **评分**：74/100
- **作者**：Xin Zhou, Cong Miao
- **方向**：World Models
- **一句话**：We present Astronex-World 1.0, an open controllable video world-model foundation.

### 3. [FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence](http://arxiv.org/abs/2609.17210v1)

- **评分**：69/100
- **作者**：Yinhao Li, Weixin Mao, Zihan Lan et al.
- **方向**：World Models
- **一句话**：Vision-language-action (VLA) models, world-action models (WAMs), and offline reinforcement learning methods are rapidly expanding the design space of embodied policies, yet turnin…

### 4. [From Prediction to Decision: World-Model-Guided Action Selection for Continuous Pile Excavation](http://arxiv.org/abs/2609.15382v1)

- **评分**：60/100
- **作者**：Ailing Zhang, Fan Gao, Song Zhang et al.
- **方向**：World Models
- **一句话**：Wheel-loader excavation is a sequential decision problem in which every scoop changes the terrain available to subsequent actions.

### 5. [Recency Forcing: Bridging the Long-Horizon Gap in Autoregressive Video Generation](http://arxiv.org/abs/2609.19729v1)

- **评分**：59/100
- **作者**：Tri Cao, Hung Nguyen, Phong Nguyen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video generation degrades over long horizons due to an overlooked train-inference discrepancy we term KV eviction mismatch: models train on short clips where a…

### 6. [World Models for Embodied Intelligence: From Plausible to Controllable to Actionable](http://arxiv.org/abs/2609.16697v1)

- **评分**：58/100
- **作者**：Nanjie Yao, Hao Wang, Chong Cheng et al.
- **方向**：World Models
- **一句话**：World models connect perception and decision-making in embodied intelligence by maintaining hidden state, anticipating consequences, comparing interventions, and adapting when exe…

### 7. [PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](http://arxiv.org/abs/2609.19142v1)

- **评分**：58/100
- **作者**：Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung et al.
- **方向**：World Models
- **一句话**：World models endow perceptual systems with the ability to predict how scenes evolve under interaction.
