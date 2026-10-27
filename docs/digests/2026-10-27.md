# Generation Research Daily Digest

> 生成时间：2026-10-27T02:30:46+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
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
- **一句话**：UniWorld 面向由外部世界模型、图形引擎或物理模拟器提供几何轨迹的连续视觉渲染任务。它将不同来源的场景状态统一转换为图像对齐的深度序列，并结合参考 RGB 图像，通过共享的视频生成模型生成具有持续外观的视频。方法采用噪声对齐的重叠续生成，在每个流匹配采样步骤中固定历史潜变量，仅提交新生成的后缀；同时使用滚动深度潜状态，只读取新出现的深度位置并保留重叠…
- **精读笔记**：[打开笔记](../notes/2026-10-27/2610.32381-uniworld-a-unified-world-model-for-real-time-vis.md)

## 快速浏览

### 1. [FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](http://arxiv.org/abs/2610.34564v1)

- **评分**：73/100
- **作者**：Meryem Koksal, Yunzhe Wang, Volkan Ustun
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents.

### 2. [Direct Forcing: Single-Stage Training with Representation-Space Supervision for Few-Step Autoregressive Video Generation](http://arxiv.org/abs/2610.30861v2)

- **评分**：71/100
- **作者**：Haojun Xu, Jie Huang, Chuyang Zhao et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generation enables low-latency streaming, yet prevailing training pipelines separate causal adaptation from distribution matching.

### 3. [WMEval: Evaluating Interactive World Models Grounded on Physical Simulations](http://arxiv.org/abs/2610.33894v1)

- **评分**：63/100
- **作者**：Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta et al.
- **方向**：World Models
- **一句话**：Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on per…

### 4. [RoboWorM: Evaluating Movement Realism, Consistency and Acceleration Affects in Embodied Video World Models](http://arxiv.org/abs/2610.33807v1)

- **评分**：62/100
- **作者**：Doanh Le Thien, Viet-Thanh Nguyen, Pham Tri Quang et al.
- **方向**：World Models
- **一句话**：Video world models (VWMs) are rapidly emerging as scalable neural simulators for robotic manipulation.

### 5. [Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control](http://arxiv.org/abs/2610.34650v1)

- **评分**：61/100
- **作者**：Jonathan DeCastro, Thomas Balch, Emily Sumner et al.
- **方向**：World Models
- **一句话**：Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehe…

### 6. [TurboWAM: Learning What Matters for Fast World Action Models](http://arxiv.org/abs/2610.33941v1)

- **评分**：59/100
- **作者**：Guile Wu, Shuangzhi Li, Xingxin Chen et al.
- **方向**：World Models
- **一句话**：World action models have demonstrated promising performance in robot policy learning, yet their high inference latency remains a critical bottleneck for real-world deployment.

### 7. [ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences](http://arxiv.org/abs/2610.32222v1)

- **评分**：58/100
- **作者**：Shibo Hong, Siyu Ren, FengJiao Chen et al.
- **方向**：World Models
- **一句话**：Reinforcement learning has gained attention for improving action-conditioned world models (ACWMs), as it enables reward-driven optimization of visual quality (VQ) and action-follo…
