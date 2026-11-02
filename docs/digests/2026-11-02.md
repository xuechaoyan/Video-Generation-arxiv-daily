# Generation Research Daily Digest

> 生成时间：2026-11-02T02:51:00+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](http://arxiv.org/abs/2610.39619v1)

- **评分**：81/100
- **作者**：Guangyuan Li, Kelu Yao, Shuolin Xu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：FutureWorld针对交互式视频世界模型中历史潜变量反复复用导致的误差循环问题，提出因果下一视频块预测器C-NCP。该模块根据当前生成潜变量和下一步动作，利用真实视频转移监督预测完整的下一潜变量块，并通过通道级残差调制引导冻结的自回归视频DiT生成后续视频。C-NCP采用VAE特定输入适配器和输出头，以适应不同基础模型的潜变量空间；训练分为带真实数据辅…
- **精读笔记**：[打开笔记](../notes/2026-11-02/2610.39619-futureworld-a-plug-and-play-causal-next-state-pr.md)

### 2. [L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](http://arxiv.org/abs/2610.40614v1)

- **评分**：78/100
- **作者**：Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.
- **方向**：World Models
- **一句话**：本文研究从单张图像和相机轨迹实时生成可探索、空间一致且可长期扩展的视频世界。作者提出 L3G-World，由 L3G-Mem 和 L3G-Gen 两个模块组成：前者维护潜空间三维高斯记忆，只在记忆未覆盖或重建误差较大的区域生成新高斯，并对已存在的高斯进行残差细化；后者是以记忆为条件的自回归视频扩散 DiT，通过将高斯中保存的 VAE 特征直接渲染到目标视角…
- **精读笔记**：[打开笔记](../notes/2026-11-02/2610.40614-l3g-world-real-time-infinite-world-generation-wi.md)

### 3. [Wizard: Manipulate Any World in Real Time via Agentic Control](http://arxiv.org/abs/2610.40339v1)

- **评分**：77/100
- **作者**：Yuzhe Wu, Zijun Lin, Yeying Jin
- **方向**：Video Generation, World Models
- **一句话**：Wizard 是一个面向可定制游戏世界的智能体视频世界模型。系统从用户提供的场景图像和角色图像出发，利用几何重建、角色网格与骨骼绑定，将场景表示为可编辑的几何代理，将角色表示为可控的关节骨骼；再通过动作检索和重定向为新角色构建动作集合。智能体显式维护角色位置、姿态、生命值、攻击阶段、技能冷却等状态，并通过规则控制器和行为规划器实现具有战斗机制一致性的闭环交…
- **精读笔记**：[打开笔记](../notes/2026-11-02/2610.40339-wizard-manipulate-any-world-in-real-time-via-age.md)

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

### 3. [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](http://arxiv.org/abs/2610.37381v2)

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
