# Generation Research Daily Digest

> 生成时间：2026-10-08T18:01:30+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldSonus: Bringing Sound to Worlds](http://arxiv.org/abs/2610.08760v1)

- **评分**：82/100
- **作者**：Pengjun Fang, Jingyi Fa, Kam Man Wu et al.
- **方向**：World Models
- **一句话**：本文提出 WorldSonus，用于为交互式世界模型从流式视频实时生成可控的空间立体声音频。模型采用带有有界 Ring-KV 缓存的流式因果自回归扩散架构，以 100 毫秒为单位生成音频；通过双时间尺度视觉条件同时保持长程语义连续性和帧级时空细节；通过训练阶段的 ShiftNCE 目标改善因果条件下的视听同步；并利用按片段更新的提示机制支持生成过程中的实时…
- **精读笔记**：[打开笔记](../notes/2026-10-08/2610.08760-worldsonus-bringing-sound-to-worlds.md)

### 2. [SPW-Nav: A Streaming Panoramic World Model for Language-Guided Navigation](http://arxiv.org/abs/2610.08941v1)

- **评分**：76/100
- **作者**：Yunheng Liu, Ziqi Cai, Siqi Yang et al.
- **方向**：World Models
- **一句话**：Language-guided panoramic video generation benefits various downstream applications, such as interactive 3D scene exploration, virtual reality experiences, and embodied agent trai…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching](http://arxiv.org/abs/2610.08777v1)

- **评分**：74/100
- **作者**：Shangye Song, Dong Gong, Hong Jia et al.
- **方向**：World Models
- **一句话**：论文针对交互式视频世界模型中按块自回归、少步扩散推理仍然昂贵的问题，提出无需训练的CtrlCache。该方法利用预先到达的控制序列判断视频块处于初始、过渡、转向还是稳态：初始和过渡状态执行完整DiT计算并刷新缓存，转向和稳态状态在一个内部去噪步骤复用残差。同时，稳态块利用前一块最后一帧干净潜变量构造频率混合历史先验，保留低频场景结构并逐步削弱高频细节。实验…
- **精读笔记**：[打开笔记](../notes/2026-10-08/2610.08777-ctrlcache-accelerating-interactive-video-world-m.md)

## 快速浏览

### 1. [In-Distribution Forcing for Long Video Generation at Test Time](http://arxiv.org/abs/2610.03120v2)

- **评分**：74/100
- **作者**：Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Modern autoregressive (AR) video diffusion models excel at short-horizon video generation, yet generating long videos remains challenging due to drifting, where colors and texture…

### 2. [MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration](http://arxiv.org/abs/2610.10457v1)

- **评分**：72/100
- **作者**：Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：Diffusion Transformers (DiTs) achieve remarkable performance in video synthesis, but their iterative denoising process suffers from high inference latency.

### 3. [UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map](http://arxiv.org/abs/2610.09785v1)

- **评分**：70/100
- **作者**：Keke Yang, Erqi Wang, Sainan Guan et al.
- **方向**：World Models
- **一句话**：World models can enable autonomous ultrasound scanning by predicting the outcomes of probe motions from local observations.

### 4. [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](http://arxiv.org/abs/2610.09763v1)

- **评分**：69/100
- **作者**：Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson
- **方向**：World Models
- **一句话**：Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-criti…

### 5. [World Models' Last Exam in Physics](http://arxiv.org/abs/2610.08791v1)

- **评分**：67/100
- **作者**：Mingju Gao, Qingle Liu, Yuzhao Peng et al.
- **方向**：Video Generation, World Models
- **一句话**：Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI syste…

### 6. [Long-WAM: Scaling the Context of World-Action Models](http://arxiv.org/abs/2610.10528v1)

- **评分**：62/100
- **作者**：Wei Huang, Bohan Zhang, Chenzhi Liu et al.
- **方向**：World Models
- **一句话**：Real-time robot control demands enough visual history to infer motion and task progress, but processing that history can delay action.

### 7. [Kuration SDK: Addressing the Virtual2Real Gap via Data Curation](http://arxiv.org/abs/2610.09305v1)

- **评分**：61/100
- **作者**：Nirmit Desai, Eric Song, Mayank Sengupta et al.
- **方向**：World Models
- **一句话**：Benchmarks for measuring the quality of action-conditioned world models are still evolving and shifting away from visual similarity-based metrics to action-semantic and physically…
