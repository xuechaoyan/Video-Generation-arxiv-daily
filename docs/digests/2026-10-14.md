# Generation Research Daily Digest

> 生成时间：2026-10-14T02:15:58+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering](http://arxiv.org/abs/2610.14685v1)

- **评分**：84/100
- **作者**：Hanxin Zhu, Jianqi Ma, Cong Wang et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：Demiurge针对现有新视角视频生成方法逐条独立处理相机轨迹、难以保持跨视角一致性的问题，提出基于动态4D点云记忆的自回归视频重渲染框架。它通过“生成—恢复—更新”循环，将生成的外观和恢复的几何持续写入共享记忆，并结合记忆引导的外观扩散、记忆一致的视频深度补全、双流变形和几何感知细化，实现连贯的多视角时空世界构建。实验显示，该方法在视频质量、跨轨迹一致性…
- **精读笔记**：[打开笔记](../notes/2026-10-14/2610.14685-demiurge-forging-navigable-4d-worlds-via-autoreg.md)

### 2. [TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation](http://arxiv.org/abs/2610.15324v1)

- **评分**：79/100
- **作者**：Jiahui Hu, Weile Mo, Peiliang Cai et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文针对自回归视频扩散模型中 KV 缓存随视频时长线性增长、严重占用 GPU 内存的问题，提出免训练的 TempoKV 预测式量化方法。作者发现，键缓存能够由同一空间位置的历史键有效预测，而值缓存的主要预测信号是当前对齐的键，历史值仅提供有限补充信息。TempoKV 先预测并量化键残差，再利用重建的当前键和历史值预测并量化值残差，同时为键分配更高精度。预测…
- **精读笔记**：[打开笔记](../notes/2026-10-14/2610.15324-tempokv-predictive-kv-cache-quantization-for-aut.md)

### 3. [AnyRank: Reliable Anytime Policy Ranking via Sequential Testing](http://arxiv.org/abs/2610.14603v1)

- **评分**：76/100
- **作者**：Apurva Badithela, David Snyder, Tenny Yin et al.
- **方向**：World Models
- **一句话**：论文提出 AnyRank，用于在硬件试验次数有限且成本高昂的情况下可靠地对多个机器人策略进行排序。该方法将策略排序建模为多重假设检验问题，结合安全的任意时刻有效推断、序贯的非参数两两比较和图式多重检验。它根据当前证据自适应选择下一个要评估的策略，并动态重新分配统计风险预算，从而优先处理难以区分的策略，同时在任意停止时刻控制家族错误率并输出完整或部分排序。A…
- **精读笔记**：[打开笔记](../notes/2026-10-14/2610.14603-anyrank-reliable-anytime-policy-ranking-via-sequ.md)

## 快速浏览

### 1. [VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](http://arxiv.org/abs/2610.03221v2)

- **评分**：74/100
- **作者**：Yutong Wang, Xingtong Ge, Enhuai Liu et al.
- **方向**：Efficient Video Diffusion
- **一句话**：Video creation spans text-to-video (T2V), image-to-video (I2V), and condition-based generation, yet video diffusion models remain costly because they repeatedly evaluate large bac…

### 2. [Remembering What Matters for Long-Horizon Robotic World Models](http://arxiv.org/abs/2610.14583v1)

- **评分**：72/100
- **作者**：Hao Wu, Tianyu Shao, Shengju Qian et al.
- **方向**：World Models
- **一句话**：Autoregressive robot video world models based on discrete visual tokens remain unreliable over long rollout horizons.

### 3. [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](http://arxiv.org/abs/2610.11756v2)

- **评分**：70/100
- **作者**：Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion enables causal video streaming without a bidirectional pass over the full clip, but existing few-step systems usually retain only the opening and mo…

### 4. [Frequency-Step Cache: Separating Synchronization and Repair for Efficient Autoregressive Video Diffusion](http://arxiv.org/abs/2610.15922v1)

- **评分**：70/100
- **作者**：Kerry Xu, Param Misra, Zachary Stenglein et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video generation enables long-horizon synthesis but requires repeated forward passes through large diffusion transformers.

### 5. [FrameFold: Response-Guided KV Cache Consolidation for Autoregressive Long Video Generation](http://arxiv.org/abs/2610.14568v1)

- **评分**：69/100
- **作者**：Muyu Liu, Mingming Liu, Hong Gu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：In autoregressive video generation, retaining all historical key-value (KV) states increases memory usage and per-step attention costs as videos grow longer.

### 6. [ProWorld: Multi-View World Model with Proprioceptive Feedback for Closed-Loop Policy Evaluation](http://arxiv.org/abs/2610.15294v1)

- **评分**：69/100
- **作者**：Zijun Wang, Tianyi Yan, Haokun Lin et al.
- **方向**：World Models
- **一句话**：Evaluating robot manipulation policies through repeated physical trials is costly.

### 7. [Towards Safe World Models: Risks, Defenses, and Evaluation](http://arxiv.org/abs/2610.13372v1)

- **评分**：66/100
- **作者**：Xiaoma Wang, Litian Zhang, Xinze Shi et al.
- **方向**：World Models
- **一句话**：World models support planning, control, learning from imagined experience, and model-mediated evaluation by predicting action-conditioned consequences.
