# Generation Research Daily Digest

> 生成时间：2026-10-19T01:54:56+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](http://arxiv.org/abs/2610.19327v1)

- **评分**：75/100
- **作者**：Zefan Yang, Zheyuan Zhang, Boris Maihe et al.
- **方向**：Video Generation, World Models
- **一句话**：论文提出 SonoWorld，用于机器人超声的交互式仿真。模型先从约690万帧无位姿标注的多器官临床超声视频中学习潜在动态，再用42名受试者中的少量 EM 跟踪甲状腺扫描，将动态映射到实际六自由度探头动作，最后通过自强制分布匹配蒸馏转化为带 KV 缓存的因果自回归生成器。实验表明，模型能响应零动作、加速、往返及逐轴动作，并在256×256分辨率、4步去噪下…
- **精读笔记**：[打开笔记](../notes/2026-10-19/2610.19327-sonoworld-towards-interactive-pose-controllable.md)

### 2. [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](http://arxiv.org/abs/2610.20220v1)

- **评分**：75/100
- **作者**：Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：论文研究如何以极少PF-ODE轨迹监督，将双向视频扩散模型高效蒸馏为因果少步自回归模型。作者发现，单样本监督本身足以提供轨迹几何校正，但单一学生模型难以同时拟合高噪声阶段的布局与运动以及低噪声阶段的纹理细节。为此，Glance Forcing采用双LoRA结构，将去噪过程分为负责语义和运动的Slow专家与负责细节的Fast专家，并分别引入时间频谱损失和空间…
- **精读笔记**：[打开笔记](../notes/2026-10-19/2610.20220-glance-forcing-making-bidirectional-diffusion-au.md)

### 3. [TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.02779v2)

- **评分**：73/100
- **作者**：Jiaxing Song, Weiqi Yan, You Huang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：本文针对自回归长视频生成中逐块去噪、历史上下文增长以及误差跨块累积导致的高推理成本和质量下降问题，提出无需训练的TRAC框架。RCS根据跨视频块和提示词的累积误差、尾部风险及最终状态偏差，利用动态规划选择缓存复用计划，并为首个视频块分配更密集的计算；ATGS将CFG残差刷新建模为覆盖全局AR路径的调度问题，在误差较大的位置刷新、其余位置复用；SSC利用首个…
- **精读笔记**：[打开笔记](../notes/2026-10-19/2610.02779-trac-trajectory-aware-reuse-and-adaptive-correct.md)

## 快速浏览

### 1. [Velox: Spatial Memory Makes World Models Efficient](http://arxiv.org/abs/2610.22311v1)

- **评分**：73/100
- **作者**：Qiuhong Shen, Shizun Wang, Xinchao Wang
- **方向**：Video Generation, World Models
- **一句话**：Video world models turn actions and camera motion into long visual rollouts, making video a natural interface for interactive simulation.

### 2. [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](http://arxiv.org/abs/2610.23156v1)

- **评分**：72/100
- **作者**：Yueyang Weng, Xiaopeng Zhang, Yuxi Ou et al.
- **方向**：World Models
- **一句话**：World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks.

### 3. [Speculative Forcing for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.22347v1)

- **评分**：70/100
- **作者**：Hyunwook Choi, Seungryong Kim, Dongyoon Han et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generators enable streaming generation, yet they run every token through the final denoising step, regardless of how much refinement it needs.

### 4. [StateCraft: Augmenting Video World Models with Abstract-State Reasoning](http://arxiv.org/abs/2610.19795v1)

- **评分**：66/100
- **作者**：Lorenzo Venturoli, Nedko Savov, Xi Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Video world models aim to simulate complex environments with realistic appearance and dynamics.

### 5. [Orbia: Do Generated Videos Form a Consistent 3D World?](http://arxiv.org/abs/2610.20693v1)

- **评分**：63/100
- **作者**：Dongyue Lu, Guian Fang, Hur Lim et al.
- **方向**：World Models
- **一句话**：Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world.

### 6. [RepForcing: Representation-Space Initialization for Autoregressive Video Distillation](http://arxiv.org/abs/2610.20111v1)

- **评分**：62/100
- **作者**：Siming Fu, Zheming Fu, Lianrui Mu et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Distilling pretrained video diffusion models into few-step autoregressive (AR) generators typically combines student initialization with distribution matching distillation (DMD).

### 7. [SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving](http://arxiv.org/abs/2610.20609v1)

- **评分**：61/100
- **作者**：Shaoyuan Xie, Zihan Zhang, Jingxuan Wang et al.
- **方向**：World Models
- **一句话**：Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interf…
