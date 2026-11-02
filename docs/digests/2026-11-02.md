# Generation Research Daily Digest

> 生成时间：2026-11-02T20:54:39+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](http://arxiv.org/abs/2610.39619v1)

- **评分**：81/100
- **作者**：Guangyuan Li, Kelu Yao, Shuolin Xu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：本文针对交互式视频世界模型在长时间动作控制下复用有缺陷历史而导致的错误循环传播问题，提出FutureWorld及其核心模块C-NCP。C-NCP根据当前生成潜变量和下一步动作，因果地预测完整的下一潜变量片段，并通过通道级残差调制引导冻结的自回归视频DiT生成下一片段。方法使用VAE特定输入适配器和输出头适应不同生成器的潜变量空间，采用两阶段训练以及状态、平…
- **精读笔记**：[打开笔记](../notes/2026-11-02/2610.39619-futureworld-a-plug-and-play-causal-next-state-pr.md)

### 2. [L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](http://arxiv.org/abs/2610.40614v1)

- **评分**：78/100
- **作者**：Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.
- **方向**：World Models
- **一句话**：本文提出 L3G-World，一个从单张图像和相机轨迹出发进行实时、长时域世界生成的交互式视频世界模型。其核心是潜在三维高斯记忆 L3G：记忆更新器只在未覆盖或重建误差较大的区域生成新高斯，并对已存在的高斯进行残差细化；每个高斯同时保存几何信息和 VAE 潜特征。视频扩散 Transformer 将记忆直接渲染到目标视角的潜空间中，以生成下一段视频，再由生…
- **精读笔记**：[打开笔记](../notes/2026-11-02/2610.40614-l3g-world-real-time-infinite-world-generation-wi.md)

### 3. [Wizard: Manipulate Any World in Real Time via Agentic Control](http://arxiv.org/abs/2610.40339v1)

- **评分**：77/100
- **作者**：Yuzhe Wu, Zijun Lin, Yeying Jin
- **方向**：Video Generation, World Models
- **一句话**：Wizard 是一种面向可定制游戏世界的智能体视频世界模型。它将场景几何、角色骨骼和显式游戏状态与视频生成解耦：场景图像被重建为可编辑的几何环境，角色图像被转换为带骨骼的可控角色，智能体负责动作检索与重定向、场景编辑、战斗状态跟踪和规则执行，视频模型则根据这些结构化代理生成视觉结果。作者构建了包含 50.3 小时数据、750 个场景和 178 个角色的数据…
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

### 3. [Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation](http://arxiv.org/abs/2610.42031v1)

- **评分**：71/100
- **作者**：Jiahua Xu, Yijie Fang, Nannan Wang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video generation enables efficient inference through streaming prediction.

### 4. [Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](http://arxiv.org/abs/2610.39232v2)

- **评分**：61/100
- **作者**：Haitang Feng, Zhuoman Liu, Zhennan Wang et al.
- **方向**：World Models
- **一句话**：Embodied world models should not only imagine plausible futures, but also perceive the geometric, semantic, and motion structure of the evolving world.

### 5. [Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics](http://arxiv.org/abs/2610.41330v1)

- **评分**：55/100
- **作者**：Zhidong Wang, Zirui Li, Haoran Xu et al.
- **方向**：World Models
- **一句话**：Motion planning in clutter is embodiment-specific: the feasible free space and reachable commands depend on each robot's geometry and dynamics.

### 6. [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining](http://arxiv.org/abs/2610.39278v1)

- **评分**：55/100
- **作者**：Yuhao Lu, Jiongxu Chen, Hexiang Wei et al.
- **方向**：World Models
- **一句话**：Predicting future physical states stands as a central challenge in embodied intelligence.

### 7. [Context Compaction for World Models](http://arxiv.org/abs/2610.38980v1)

- **评分**：54/100
- **作者**：Hayder Tirmazi
- **方向**：World Models
- **一句话**：World models let observers explore and interact with generated worlds.
