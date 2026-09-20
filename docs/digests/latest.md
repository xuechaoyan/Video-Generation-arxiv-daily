# Generation Research Daily Digest

> 生成时间：2026-09-20T14:56:38+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](http://arxiv.org/abs/2609.18430v1)

- **评分**：80/100
- **作者**：Awomo-WM Team,  :, Enhui Ma et al.
- **方向**：World Models
- **一句话**：本文提出 StrucPhysVideo，通过物理相关视频筛选、结构化物理字幕和物理现象标签，为视频世界模型提供关于物体、材料、接触、形变、状态变化及时间顺序的监督。StrucPhysVideo-TI2V 基于稀疏 MoE 视频 Transformer，在图像和文本条件下生成物理上更合理的视频，在 Physics-IQ Verified 上达到 45.5%。…
- **精读笔记**：[打开笔记](../notes/2026-09-20/2609.18430-strucphysvideo-learning-physical-dynamics-from-s.md)

### 2. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](http://arxiv.org/abs/2609.17521v1)

- **评分**：75/100
- **作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang et al.
- **方向**：Video Generation
- **一句话**：本文提出 PhysStream，一个面向物理基础图像到视频生成的自回归流式模型。用户可以在生成过程中针对场景中的特定物体，在任意选定时刻施加稀疏的三维速度增量，而无需预先规划完整轨迹。模型通过位置图和物体跟踪图构成的结构化场景记忆，将先前生成帧中的几何与对象状态反馈给后续生成。训练采用两阶段方案：先在双向 Wan2.2-TI2V-5B 模型上学习速度控制，…
- **精读笔记**：[打开笔记](../notes/2026-09-20/2609.17521-physstream-streaming-physics-grounded-video-gene.md)

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
