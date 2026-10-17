# Generation Research Daily Digest

> 生成时间：2026-10-17T01:40:55+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](http://arxiv.org/abs/2610.19327v1)

- **评分**：75/100
- **作者**：Zefan Yang, Zheyuan Zhang, Boris Maihe et al.
- **方向**：Video Generation, World Models
- **一句话**：SonoWorld面向机器人超声，利用约690万帧无标注多器官临床视频学习超声视频动态，再用少量EM跟踪的甲状腺扫描将潜动作映射到实际六自由度探头运动。模型通过分布匹配蒸馏和自强制训练转换为因果、自回归生成器，并采用选择性KV缓存支持长时域流式推理。在原始轨迹、零运动、加速运动和往返运动测试中，模型能够根据探头动作生成相应的未来超声观测；在H100上以四步…
- **精读笔记**：[打开笔记](../notes/2026-10-17/2610.19327-sonoworld-towards-interactive-pose-controllable.md)

### 2. [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](http://arxiv.org/abs/2610.20220v1)

- **评分**：75/100
- **作者**：Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：本文研究如何以极少的PF-ODE轨迹监督，将双向视频扩散模型高效蒸馏为因果式少步自回归生成器。作者发现，单一轨迹已足以建立少步流的几何结构，但单一学生模型难以同时拟合高噪声阶段的布局与运动以及低噪声阶段的细节。为此提出Glance Forcing：利用双LoRA将去噪过程划分为Slow专家和Fast专家，并分别使用时间频谱损失和空间高通损失进行优化；随后通…
- **精读笔记**：[打开笔记](../notes/2026-10-17/2610.20220-glance-forcing-making-bidirectional-diffusion-au.md)

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
