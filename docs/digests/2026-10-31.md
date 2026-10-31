# Generation Research Daily Digest

> 生成时间：2026-10-31T16:21:11+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](http://arxiv.org/abs/2610.39619v1)

- **评分**：81/100
- **作者**：Guangyuan Li, Kelu Yao, Shuolin Xu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文针对交互式视频世界模型在长时域滚动生成中的错误循环问题，提出FutureWorld框架。其核心是因果下一片段预测器C-NCP：根据当前生成潜变量和下一步动作，预测完整的下一潜变量片段，并通过保形的通道级残差调制引导冻结的自回归视频DiT生成后续片段。C-NCP使用真实视频转移进行两阶段训练，结合因果时空注意力、动作条件、VAE特定适配器以及状态和时间差…
- **精读笔记**：[打开笔记](../notes/2026-10-31/2610.39619-futureworld-a-plug-and-play-causal-next-state-pr.md)

### 2. [L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](http://arxiv.org/abs/2610.40614v1)

- **评分**：78/100
- **作者**：Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.
- **方向**：World Models
- **一句话**：本文针对交互式视频世界模型在长时域探索中空间一致性差、记忆开销随视频长度增长以及显式三维记忆渲染速度慢的问题，提出 L3G-World。该系统由 L3G-Mem 和 L3G-Gen 组成：前者通过自适应生成新高斯并残差细化已有高斯，维护随场景空间范围增长的紧凑三维记忆；后者将记忆中存储的 VAE 潜特征直接渲染到目标视角的潜空间，并利用视频扩散 DiT 生…
- **精读笔记**：[打开笔记](../notes/2026-10-31/2610.40614-l3g-world-real-time-infinite-world-generation-wi.md)

### 3. [Wizard: Manipulate Any World in Real Time via Agentic Control](http://arxiv.org/abs/2610.40339v1)

- **评分**：77/100
- **作者**：Yuzhe Wu, Zijun Lin, Yeying Jin
- **方向**：Video Generation, World Models
- **一句话**：Wizard将智能体世界状态管理、场景几何代理、角色关节骨骼控制与视频生成结合起来。系统从用户提供的场景和角色图像重建可编辑几何、角色网格及骨骼，并通过动作检索和重定向生成适配的动作库；智能体根据玩家输入和战斗状态更新场景、角色动作、生命值、距离及技能冷却等状态，再由视频模型渲染连续画面。模型使用覆盖750个场景和178个角色的50.3小时代理—视频数据训…
- **精读笔记**：[打开笔记](../notes/2026-10-31/2610.40339-wizard-manipulate-any-world-in-real-time-via-age.md)

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
