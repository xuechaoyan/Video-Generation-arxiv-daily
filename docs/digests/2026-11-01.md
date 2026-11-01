# Generation Research Daily Digest

> 生成时间：2026-11-01T17:16:16+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](http://arxiv.org/abs/2610.39619v1)

- **评分**：81/100
- **作者**：Guangyuan Li, Kelu Yao, Shuolin Xu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文针对交互式视频世界模型在长时间闭环交互中的错误循环传播问题，提出即插即用的因果下一片段预测器C-NCP。该模块根据当前生成潜变量和下一步动作，预测完整的下一潜变量片段，并通过通道级残差调制引导冻结的自回归视频DiT生成下一片段。C-NCP使用VAE特定适配器连接不同生成器的潜空间，采用因果时空注意力、动作条件和时间差分监督，并通过两阶段训练适应跨片段的…
- **精读笔记**：[打开笔记](../notes/2026-11-01/2610.39619-futureworld-a-plug-and-play-causal-next-state-pr.md)

### 2. [L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](http://arxiv.org/abs/2610.40614v1)

- **评分**：78/100
- **作者**：Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.
- **方向**：World Models
- **一句话**：本文提出 L3G-World，一个面向交互式世界模型的实时长时域视频生成框架。它使用带有几何参数和 VAE 潜特征的潜在三维高斯记忆：L3G-Mem 在新区域自适应生成高斯、在已探索区域细化已有高斯；L3G-Gen 则将记忆直接渲染到视频 DiT 的潜空间中，生成下一段视频。两者交替构成自回归闭环，避免了密集三维基元不断累积以及 RGB 渲染后的 VAE…
- **精读笔记**：[打开笔记](../notes/2026-11-01/2610.40614-l3g-world-real-time-infinite-world-generation-wi.md)

### 3. [Wizard: Manipulate Any World in Real Time via Agentic Control](http://arxiv.org/abs/2610.40339v1)

- **评分**：77/100
- **作者**：Yuzhe Wu, Zijun Lin, Yeying Jin
- **方向**：Video Generation, World Models
- **一句话**：Wizard 是一个面向可定制游戏的智能体视频世界模型。系统从用户提供的场景图像和角色图像出发，利用场景几何代理与角色关节骨骼控制视频生成，并由智能体显式维护角色状态、战斗规则、场景几何和动作规划。作者构建了包含 50.3 小时数据、750 个场景和 178 个角色的数据集，通过动作检索与重定向支持新角色，通过自适应角色注意力掩码保持外观与位置对应。模型基…
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

### 5. [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](http://arxiv.org/abs/2610.39232v1)

- **评分**：61/100
- **作者**：Haitang Feng, Zhuoman Liu, Zhennan Wang et al.
- **方向**：World Models
- **一句话**：Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world.

### 6. [ReferStream: Interactive Subject Injection for Streaming Video Generation](http://arxiv.org/abs/2610.37566v1)

- **评分**：61/100
- **作者**：Shuolin Xu, Guanyuan Li, Boyu Li et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subje…

### 7. [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](http://arxiv.org/abs/2610.39278v1)

- **评分**：55/100
- **作者**：Yuhao Lu, Jiongxu Chen, Hexiang Wei et al.
- **方向**：World Models
- **一句话**：Predicting future physical states stands as a central challenge in embodied intelligence.
