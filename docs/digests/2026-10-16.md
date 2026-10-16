# Generation Research Daily Digest

> 生成时间：2026-10-16T15:37:27+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](http://arxiv.org/abs/2610.19327v1)

- **评分**：75/100
- **作者**：Zefan Yang, Zheyuan Zhang, Boris Maihe et al.
- **方向**：Video Generation, World Models
- **一句话**：本文提出SonoWorld，一种面向机器人超声的因果、六自由度位姿可控世界模型。模型先从约690万帧无标注的多器官临床超声视频中学习潜在视频动态，再用少量EM跟踪的甲状腺扫描将潜动作映射到真实探头运动，最后通过分布匹配蒸馏和自强制训练实现流式自回归生成，并用选择性KV缓存支持长时域推理。实验表明，模型能够根据探头轨迹生成具有路径依赖、解剖一致性和时间一致性…
- **精读笔记**：[打开笔记](../notes/2026-10-16/2610.19327-sonoworld-towards-interactive-pose-controllable.md)

### 2. [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](http://arxiv.org/abs/2610.20220v1)

- **评分**：75/100
- **作者**：Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：论文研究如何以极少的PF-ODE轨迹监督，将双向视频扩散模型高效蒸馏为因果、少步的自回归视频生成器。作者发现，单样本监督本身足以建立少步轨迹的整体几何结构，但单一学生模型难以同时拟合高噪声阶段的布局与运动以及低噪声阶段的细节，原因在于两阶段的曲率和优化行为差异显著。为此，Glance Forcing采用双LoRA结构，将去噪过程分为负责语义和运动的Slow…
- **精读笔记**：[打开笔记](../notes/2026-10-16/2610.20220-glance-forcing-making-bidirectional-diffusion-au.md)

### 3. [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](http://arxiv.org/abs/2610.19201v1)

- **评分**：74/100
- **作者**：Henry Che, Xuanchi Ren, Sanja Fidler et al.
- **方向**：World Models
- **一句话**：We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts](http://arxiv.org/abs/2610.18873v2)

- **评分**：73/100
- **作者**：Wenxuan Guo, Yingping Liang, Zhaoguo Wang et al.
- **方向**：World Models
- **一句话**：Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment.

### 2. [TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.02779v2)

- **评分**：73/100
- **作者**：Jiaxing Song, Weiqi Yan, You Huang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video generation enables scalable long-video synthesis by sequentially generating fixed-length chunks, but incurs substantial computational cost from repeated…

### 3. [Velox: Spatial Memory Makes World Models Efficient](http://arxiv.org/abs/2610.22311v1)

- **评分**：73/100
- **作者**：Qiuhong Shen, Shizun Wang, Xinchao Wang
- **方向**：Video Generation, World Models
- **一句话**：Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation.

### 4. [Speculative Forcing for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.22347v1)

- **评分**：70/100
- **作者**：Hyunwook Choi, Seungryong Kim, Dongyoon Han et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generators enable streaming generation, yet they run every token through the final denoising step, regardless of how much refinement it needs.

### 5. [StateCraft: Augmenting Video World Models with Abstract-State Reasoning](http://arxiv.org/abs/2610.19795v1)

- **评分**：66/100
- **作者**：Lorenzo Venturoli, Nedko Savov, Xi Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Video world models aim to simulate complex environments with realistic appearance and dynamics.

### 6. [Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence](http://arxiv.org/abs/2610.18447v2)

- **评分**：64/100
- **作者**：Thinker Team, Peng Gao, Jichao Jiao et al.
- **方向**：World Models
- **一句话**：World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support.

### 7. [Orbia: Do Generated Videos Form a Consistent 3D World?](http://arxiv.org/abs/2610.20693v1)

- **评分**：63/100
- **作者**：Dongyue Lu, Guian Fang, Hur Lim et al.
- **方向**：World Models
- **一句话**：Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world.
