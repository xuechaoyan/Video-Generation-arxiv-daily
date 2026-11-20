# Generation Research Daily Digest

> 生成时间：2026-11-20T19:17:13+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
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
- **一句话**：本文提出 ScaleWorld，用一个共享的因果视频骨干网络同时完成低分辨率世界预测和高分辨率视频细化。模型按视频块先生成低分辨率预测，再利用同一模型对其进行一步高分辨率细化；低分辨率预测保持独立可用，高分辨率结果不会反馈到预测历史。为满足流式生成需求，系统为预测和细化维护不同的因果缓存：预测使用较长的低分辨率干净历史，细化使用较短的高分辨率带噪前向历史。…
- **精读笔记**：[打开笔记](../notes/2026-11-20/2611.26615-scaleworld-high-resolution-world-generation-thro.md)

### 3. [Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency](http://arxiv.org/abs/2611.26040v1)

- **评分**：72/100
- **作者**：Zhihao Hu, Jianqi Ma, Jun Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文提出 Streaming-AAA，用于根据玩家动作、天气和时间等条件，以流式方式生成可持续交互的 AAA 游戏视频。系统结合高分辨率视频 VAE、因子化 3D-UNet 潜空间扩散模型、Diffusion Forcing 长上下文预训练、DMD 训练后蒸馏以及混合长短期 KV 缓存，在《原神》数据上实现 1080p、43 FPS 和约 198 毫秒延迟…
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
