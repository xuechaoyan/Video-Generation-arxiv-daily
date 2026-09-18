# Generation Research Daily Digest

> 生成时间：2026-09-18T15:15:01+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](http://arxiv.org/abs/2609.18430v1)

- **评分**：80/100
- **作者**：Awomo-WM Team,  :, Enhui Ma et al.
- **方向**：World Models
- **一句话**：论文提出 StrucPhysVideo，围绕物理世界建模构建了从数据整理、结构化标注到视频生成和机器人动作条件生成的完整框架。其数据流程通过镜头切分、运动感知窗口选择、技术质量与内容纯度过滤，以及物理相关性验证，保留包含真实物体运动和交互的片段，并标注物体、材料、相机运动、接触、形变和状态变化。StrucPhysVideo-TI2V 使用冻结的 Qwen3…
- **精读笔记**：[打开笔记](../notes/2026-09-18/2609.18430-strucphysvideo-learning-physical-dynamics-from-s.md)

### 2. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](http://arxiv.org/abs/2609.17521v1)

- **评分**：75/100
- **作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang et al.
- **方向**：Video Generation
- **一句话**：PhysStream 面向从单张图像生成具有物理合理性的交互式视频，重点解决现有方法必须预先给出完整控制序列、缺乏场景物理状态反馈的问题。它以稀疏的逐物体三维速度增量作为用户控制，并从已生成帧在线提取位置图和物体跟踪图作为结构化场景记忆，通过因果自回归生成和 KV 缓存逐帧生成视频。作者先训练双向运动控制模型，再转换为引入场景记忆的因果模型，并构建了约 1…
- **精读笔记**：[打开笔记](../notes/2026-09-18/2609.17521-physstream-streaming-physics-grounded-video-gene.md)

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
