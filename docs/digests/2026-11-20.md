# Generation Research Daily Digest

> 生成时间：2026-11-20T04:28:02+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
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
- **一句话**：ScaleWorld 提出一种面向相机控制视频世界模型的共享因果骨干，将低分辨率流式世界预测与高分辨率流式细化统一在同一个模型中。模型先按块生成可独立使用的低分辨率预测，再利用其上采样潜变量进行单步高分辨率细化；高分辨率结果不会反馈到低分辨率预测历史。为适应两种任务不同的时序需求，预测端维护较长的低分辨率干净 KV 历史，细化端维护较短的高分辨率带噪前向…
- **精读笔记**：[打开笔记](../notes/2026-11-20/2611.26615-scaleworld-high-resolution-world-generation-thro.md)

### 3. [Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency](http://arxiv.org/abs/2611.26040v1)

- **评分**：72/100
- **作者**：Zhihao Hu, Jianqi Ma, Jun Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：本文提出 Streaming-AAA，用于根据玩家动作、天气和时间等条件，因果地持续生成高分辨率 AAA 游戏视频。系统面向《原神》构建了自动化数据采集系统，收集约 2.2 万段 1080p、30 FPS 视频和约 4000 万帧数据。方法采用高分辨率视频 VAE、因子化时空 3D-UNet 扩散模型、Diffusion Forcing 长上下文预训练、D…
- **精读笔记**：[打开笔记](../notes/2026-11-20/2611.26040-streaming-aaa-streaming-aaa-game-video-generatio.md)

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
