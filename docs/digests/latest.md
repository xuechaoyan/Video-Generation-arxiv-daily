# Generation Research Daily Digest

> 生成时间：2026-10-27T16:54:01+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Mix Forcing: Causal Pre-Training via Mixture Attention for Interactive World Models](http://arxiv.org/abs/2610.33589v1)

- **评分**：83/100
- **作者**：Zelin Gao, Hao Ouyang, Jiapeng Zhu et al.
- **方向**：Video Generation, World Models
- **一句话**：While interactive video world models require autoregressive generation, directly adapting pretrained bidirectional video diffusion models into autoregressive ones with teacher for…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 2. [DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models](http://arxiv.org/abs/2610.30781v1)

- **评分**：77/100
- **作者**：Adam Lee, Mutian Xu, Yukang Cao et al.
- **方向**：Video Generation, World Models
- **一句话**：Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [UniWorld: A Unified World Model for Real-Time Visual World Simulation](http://arxiv.org/abs/2610.32381v2)

- **评分**：77/100
- **作者**：Xin Zhang, Yabo Chen, Shuaiwei Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：本文提出 UniWorld，用于将深度轨迹转换为连续、外观一致的视频世界模拟。方法以图像空间深度作为统一几何接口，以参考 RGB 和文本提供持久外观，通过噪声对齐的重叠续接保存视频历史，并通过滚动深度潜变量状态增量维护几何条件。实验覆盖驾驶、人类活动、模拟和合成场景，验证了多场景生成、历史干预、原生深度适配、长时域模拟以及缓存与在线执行的一致性。在八张 H…
- **精读笔记**：[打开笔记](../notes/2026-10-27/2610.32381-uniworld-a-unified-world-model-for-real-time-vis.md)

## 快速浏览

### 1. [OSWAM: An Effective World Action Model with One-Step Action Generation](http://arxiv.org/abs/2610.35850v1)

- **评分**：76/100
- **作者**：Guowen Zhang, Liyi Chen, Xu Hu et al.
- **方向**：World Models
- **一句话**：Direct-policy World Action Models (WAM) have demonstrated the benefits of decoupling action generation from explicit future visual prediction for efficient inference in autonomous…

### 2. [FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](http://arxiv.org/abs/2610.34564v1)

- **评分**：73/100
- **作者**：Meryem Koksal, Yunzhe Wang, Volkan Ustun
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents.

### 3. [Direct Forcing: Single-Stage Training with Representation-Space Supervision for Few-Step Autoregressive Video Generation](http://arxiv.org/abs/2610.30861v2)

- **评分**：71/100
- **作者**：Haojun Xu, Jie Huang, Chuyang Zhao et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generation enables low-latency streaming, yet prevailing training pipelines separate causal adaptation from distribution matching.

### 4. [Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](http://arxiv.org/abs/2610.35594v1)

- **评分**：65/100
- **作者**：Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：Few-step distillation is essential for deploying modern video diffusion models.

### 5. [WMEval: Evaluating Interactive World Models Grounded on Physical Simulations](http://arxiv.org/abs/2610.33894v1)

- **评分**：63/100
- **作者**：Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta et al.
- **方向**：World Models
- **一句话**：Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on per…

### 6. [RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models](http://arxiv.org/abs/2610.33807v1)

- **评分**：62/100
- **作者**：Doanh Le Thien, Viet-Thanh Nguyen, Pham Tri Quang et al.
- **方向**：World Models
- **一句话**：Video world models (VWMs) are rapidly emerging as scalable neural simulators for robotic manipulation.

### 7. [Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control](http://arxiv.org/abs/2610.34650v1)

- **评分**：61/100
- **作者**：Jonathan DeCastro, Thomas Balch, Emily Sumner et al.
- **方向**：World Models
- **一句话**：Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehe…
