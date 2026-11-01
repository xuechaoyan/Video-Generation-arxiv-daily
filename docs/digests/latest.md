# Generation Research Daily Digest

> 生成时间：2026-11-01T02:42:15+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](http://arxiv.org/abs/2610.39619v1)

- **评分**：81/100
- **作者**：Guangyuan Li, Kelu Yao, Shuolin Xu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：本文针对交互式视频世界模型在长时间动作控制过程中因复用不完美历史而产生的错误循环传播问题，提出FutureWorld框架。其核心是因果下一视频块预测器（C-NCP）：根据当前生成潜变量和下一步动作，预测完整的下一潜变量块，再通过保持张量形状的通道级残差调制引导冻结的自回归视频生成器。C-NCP采用VAE特定输入适配器和输出头以支持不同潜变量空间，并结合因果…
- **精读笔记**：[打开笔记](../notes/2026-11-01/2610.39619-futureworld-a-plug-and-play-causal-next-state-pr.md)

### 2. [L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](http://arxiv.org/abs/2610.40614v1)

- **评分**：78/100
- **作者**：Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.
- **方向**：World Models
- **一句话**：本文提出 L3G-World，一种从单张图像和相机轨迹出发、面向实时长时域交互式世界生成的框架。其核心是 L3G-Mem：采用紧凑的潜在三维高斯记忆，仅在未覆盖或重建误差较大的区域生成新高斯，并通过残差更新细化已有高斯，使记忆主要随场景空间范围增长。每个高斯同时保存几何信息和 VAE 潜特征，因此可直接在视频 DiT 的潜空间中渲染记忆，避免 RGB 渲染…
- **精读笔记**：[打开笔记](../notes/2026-11-01/2610.40614-l3g-world-real-time-infinite-world-generation-wi.md)

### 3. [Wizard: Manipulate Any World in Real Time via Agentic Control](http://arxiv.org/abs/2610.40339v1)

- **评分**：77/100
- **作者**：Yuzhe Wu, Zijun Lin, Yeying Jin
- **方向**：Video Generation, World Models
- **一句话**：Wizard 是一种面向可定制游戏世界的智能体视频世界模型。它将场景几何、角色骨骼和显式游戏状态与视频生成解耦：用户可通过图像、语言和操作控制场景、角色动作及战斗逻辑。模型使用覆盖 50.3 小时数据、750 个场景和 178 个角色的数据集，以统一视觉代理训练 Wan2.2 视频生成模型，并通过角色感知自适应注意力掩码保持角色身份和空间对齐。结合因果适配…
- **精读笔记**：[打开笔记](../notes/2026-11-01/2610.40339-wizard-manipulate-any-world-in-real-time-via-age.md)

## 快速浏览

### 1. [UniWorld: A Unified World Model for Real-Time Visual World Simulation](http://arxiv.org/abs/2610.32381v3)

- **评分**：77/100
- **作者**：Xin Zhang, Yabo Chen, Shuaiwei Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Continuous visual world simulation requires coupling evolving scene geometry with temporally persistent appearance.

### 2. [Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](http://arxiv.org/abs/2610.40191v1)

- **评分**：76/100
- **作者**：Liaoyuan Fan, Yuhao Zheng, Dongxing Mao et al.
- **方向**：World Models
- **一句话**：Video generation is shifting from end-to-end synthesis toward agentic generation, where planning, tool use, and feedback enable coherent, controllable multi-shot videos.

### 3. [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](http://arxiv.org/abs/2610.37381v1)

- **评分**：67/100
- **作者**：Hanqing Wang, Zhaotian Cai, Ruichuan An et al.
- **方向**：World Models
- **一句话**：Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited.

### 4. [Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation](http://arxiv.org/abs/2610.37983v1)

- **评分**：62/100
- **作者**：Kaihua Chen, Yiming Gong, Deva Ramanan et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：We address the task of long-video, camera-controlled generation from a single image.

### 5. [ReferStream: Interactive Subject Injection for Streaming Video Generation](http://arxiv.org/abs/2610.37566v1)

- **评分**：61/100
- **作者**：Shuolin Xu, Guanyuan Li, Boyu Li et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subje…

### 6. [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](http://arxiv.org/abs/2610.39232v1)

- **评分**：61/100
- **作者**：Haitang Feng, Zhuoman Liu, Zhennan Wang et al.
- **方向**：World Models
- **一句话**：Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world.

### 7. [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](http://arxiv.org/abs/2610.39278v1)

- **评分**：55/100
- **作者**：Yuhao Lu, Jiongxu Chen, Hexiang Wei et al.
- **方向**：World Models
- **一句话**：Predicting future physical states stands as a central challenge in embodied intelligence.
