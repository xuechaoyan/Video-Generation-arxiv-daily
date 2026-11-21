# Generation Research Daily Digest

> 生成时间：2026-11-21T18:18:41+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds](http://arxiv.org/abs/2611.25838v1)

- **评分**：83/100
- **作者**：Runze Wang, Fei Zha, Bing He et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observat…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 2. [ScaleWorld: High-Resolution World Generation through Shared Prediction and Refinement](http://arxiv.org/abs/2611.26615v1)

- **评分**：72/100
- **作者**：Yansong Qu, Wesker Zheng, Quanjian Song et al.
- **方向**：World Models
- **一句话**：论文提出 SCALEWORLD，用一个共享因果视频骨干同时完成低分辨率、摄像机控制的流式世界预测和高分辨率流式细化。模型先逐块生成低分辨率结果，再基于该结果执行单步高分辨率细化；两种任务使用独立的因果状态，预测保留较长的低分辨率清洁历史，细化保留较短的高分辨率噪声前向 KV 历史。训练上先分别优化预测和细化专家，再通过 TA-OPD 将能力整合到共享模型。…
- **精读笔记**：[打开笔记](../notes/2026-11-21/2611.26615-scaleworld-high-resolution-world-generation-thro.md)

### 3. [Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency](http://arxiv.org/abs/2611.26040v1)

- **评分**：72/100
- **作者**：Zhihao Hu, Jianqi Ma, Jun Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文提出 Streaming-AAA，用于根据玩家动作、天气和时间等条件，以流式方式无限生成 AAA 游戏视频。系统针对高分辨率解码、长时域一致性和实时推理三类瓶颈，采用高效视频 VAE、因子化 3D UNet 潜空间扩散模型、Diffusion Forcing 长上下文预训练、DMD 训练后蒸馏以及混合长短期 KV 缓存。基于《原神》数据，系统在 NVI…
- **精读笔记**：[打开笔记](../notes/2026-11-21/2611.26040-streaming-aaa-streaming-aaa-game-video-generatio.md)

## 快速浏览

### 1. [AURA: AUdio-dRiven streaming Avatar](http://arxiv.org/abs/2611.26540v1)

- **评分**：72/100
- **作者**：Nathaniel Cohen, Nicolas Dufour, Amélie Royer et al.
- **方向**：Video Generation
- **一句话**：Current audio-driven video diffusion models can synthesize realistic talking-head videos but generally require dozens of diffusion denoising steps over multi-second video chunks,…

### 2. [Risk-Triggered Search: Behavior-Preserving Safe Control](http://arxiv.org/abs/2611.24409v1)

- **评分**：64/100
- **作者**：Xinyu Deng, Bohao Lan, Kunpeng Li et al.
- **方向**：World Models
- **一句话**：Pre-trained visual world models generate multi-step action plans from current and goal observations, yet terminal-proximity objectives fail to prevent forbidden-zone traversal or…

### 3. [SpecWM: Turning Verification into Refinement for Streaming World Models](http://arxiv.org/abs/2611.26211v1)

- **评分**：64/100
- **作者**：Jiaming Li, Lingzhen Li, Xiaze Yang et al.
- **方向**：World Models
- **一句话**：Recently, video world models have advanced interactive generation, with large models offering higher quality and smaller models enabling faster inference.

### 4. [FlexVSR: Continuous-Scale Super-Resolution for Streaming Video Generation](http://arxiv.org/abs/2611.26178v1)

- **评分**：63/100
- **作者**：Ji Wang, Haonan An, Jiasheng Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Real-time streaming video generation has gained rapid momentum in live content creation and interactive media.

### 5. [CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control](http://arxiv.org/abs/2611.25667v1)

- **评分**：58/100
- **作者**：Xu Pan, Chubin Zhang, Xingrui Yu et al.
- **方向**：World Models
- **一句话**：Vision-Language-Action (VLA) policies must react while visual inference is still running.

### 6. [WorldRuler: Interactive World Modeling under Configurable Rules](http://arxiv.org/abs/2611.24869v2)

- **评分**：57/100
- **作者**：Mingliang Zhai, Chuanhao Li, Jiaming Tan et al.
- **方向**：World Models
- **一句话**：Rules govern how player actions change interactive worlds.

### 7. [Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers](http://arxiv.org/abs/2611.26334v1)

- **评分**：56/100
- **作者**：Ryan Lucas, Petros Prastakos, Rahul Mazumder
- **方向**：Autoregressive and Streaming Video
- **一句话**：Video diffusion transformers reuse key--value (KV) caches across denoising steps, which quickly becomes a bottleneck for long video generation.
