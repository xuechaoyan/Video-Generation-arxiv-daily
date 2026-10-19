# Generation Research Daily Digest

> 生成时间：2026-10-19T17:48:23+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](http://arxiv.org/abs/2610.20220v1)

- **评分**：75/100
- **作者**：Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：本文研究如何以极少的PF-ODE轨迹监督，将双向视频扩散模型高效蒸馏为可因果、自回归、少步生成的模型。作者发现，单样本监督本身足以建立少步轨迹的整体几何结构，但单一学生网络难以同时拟合高噪声阶段的布局与运动，以及低噪声阶段的纹理细节，原因在于两者的曲率和优化行为不同。为此提出Glance Forcing：使用双LoRA结构，将去噪过程划分为Slow专家和F…
- **精读笔记**：[打开笔记](../notes/2026-10-19/2610.20220-glance-forcing-making-bidirectional-diffusion-au.md)

### 2. [TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.02779v2)

- **评分**：73/100
- **作者**：Jiaxing Song, Weiqi Yan, You Huang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：本文提出一种无需训练的TRAC框架，用于加速由连续视频块组成的自回归长视频生成。针对缓存复用误差沿AR轨迹累积、CFG计算开销高以及长期低频结构漂移三个问题，TRAC分别采用RCS、ATGS和SSC进行风险感知的缓存调度、全局CFG刷新调度和自适应低频结构校正。在SkyReels-V2上，TRAC达到6.03倍加速，VBench得分为82.44，相比原始模…
- **精读笔记**：[打开笔记](../notes/2026-10-19/2610.02779-trac-trajectory-aware-reuse-and-adaptive-correct.md)

### 3. [Velox: Spatial Memory Makes World Models Efficient](http://arxiv.org/abs/2610.22311v1)

- **评分**：73/100
- **作者**：Qiuhong Shen, Shizun Wang, Xinchao Wang
- **方向**：Video Generation, World Models
- **一句话**：论文针对长时视频世界模型中 KV 缓存随生成历史增长、导致后续分块越来越慢的问题，提出无需训练的 Velox 推理路由器。它把历史视觉记忆压缩表示为带深度区间的相机视锥体 slab，通过多重变形估计当前块深度，并以世界坐标系中的 slab 重叠作为几何先验，结合每个 Transformer 层自身的注意力重要性，为当前区域选择有限的历史 KV 块。对几何覆…
- **精读笔记**：[打开笔记](../notes/2026-10-19/2610.22311-velox-spatial-memory-makes-world-models-efficien.md)

## 快速浏览

### 1. [ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation](http://arxiv.org/abs/2610.23156v1)

- **评分**：72/100
- **作者**：Yueyang Weng, Xiaopeng Zhang, Yuxi Ou et al.
- **方向**：World Models
- **一句话**：World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks.

### 2. [Speculative Forcing for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.22347v1)

- **评分**：70/100
- **作者**：Hyunwook Choi, Seungryong Kim, Dongyoon Han et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generators enable streaming generation, yet they run every token through the final denoising step, regardless of how much refinement it needs.

### 3. [Persistent Planar Memory for Video World Models](http://arxiv.org/abs/2610.23795v1)

- **评分**：69/100
- **作者**：Yuze He, Bin Tan, Zelin Gao et al.
- **方向**：World Models
- **一句话**：Video world models that generate and explore environments at scale need a persistent 3D memory of what they have produced.

### 4. [StateCraft: Augmenting Video World Models with Abstract-State Reasoning](http://arxiv.org/abs/2610.19795v1)

- **评分**：66/100
- **作者**：Lorenzo Venturoli, Nedko Savov, Xi Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Video world models aim to simulate complex environments with realistic appearance and dynamics.

### 5. [Momentum: Persistent Dynamics for Video World Models](http://arxiv.org/abs/2610.23423v1)

- **评分**：65/100
- **作者**：Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel et al.
- **方向**：World Models
- **一句话**：Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears.

### 6. [Orbia: Do Generated Videos Form a Consistent 3D World?](http://arxiv.org/abs/2610.20693v1)

- **评分**：63/100
- **作者**：Dongyue Lu, Guian Fang, Hur Lim et al.
- **方向**：World Models
- **一句话**：Video generators serve as interactive worlds for exploration and simulation, yet realistic and visually appealing frames do not necessarily depict a consistent 3D world.

### 7. [RepForcing: Representation-Space Initialization for Autoregressive Video Distillation](http://arxiv.org/abs/2610.20111v1)

- **评分**：62/100
- **作者**：Siming Fu, Zheming Fu, Lianrui Mu et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Distilling pretrained video diffusion models into few-step autoregressive (AR) generators typically combines student initialization with distribution matching distillation (DMD).
