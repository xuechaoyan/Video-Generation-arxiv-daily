# Generation Research Daily Digest

> 生成时间：2026-10-29T17:38:01+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Mix Forcing: Causal Pre-Training via Mixture Attention for Interactive World Models](http://arxiv.org/abs/2610.33589v1)

- **评分**：83/100
- **作者**：Zelin Gao, Hao Ouyang, Jiapeng Zhu et al.
- **方向**：Video Generation, World Models
- **一句话**：While interactive video world models require autoregressive generation, directly adapting pretrained bidirectional video diffusion models into autoregressive ones with teacher for…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 2. [BoxWorld: Let World Engines Control and Video Generators Render](http://arxiv.org/abs/2610.36371v1)

- **评分**：78/100
- **作者**：Zike Wu, Ahmed Hatem, Chintan Trivedi et al.
- **方向**：World Models
- **一句话**：BoxWorld 面向具有用户定义行为的实时交互式视频世界，将“世界如何交互”与“画面如何呈现”分离。编码代理根据规则生成 Box World Engine，显式维护对象的布局框、持久属性和动态状态，并异步向视频渲染器提供状态流；基于 LongLive 初始化的 Box-State Generative Renderer 则以自回归、少步数方式生成视频。作…
- **精读笔记**：[打开笔记](../notes/2026-10-29/2610.36371-boxworld-let-world-engines-control-and-video-gen.md)

### 3. [UniWorld: A Unified World Model for Real-Time Visual World Simulation](http://arxiv.org/abs/2610.32381v2)

- **评分**：77/100
- **作者**：Xin Zhang, Yabo Chen, Shuaiwei Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：UniWorld 面向由不断变化的场景几何驱动的连续视觉世界模拟，将深度轨迹和参考 RGB 外观输入统一到共享的视频生成器中。系统以共同时间轴维护视频历史与深度状态：通过噪声对齐的重叠续接，在每次流匹配采样中固定历史潜变量；通过滚动深度潜状态，仅增量读取新的几何位置，并在窗口内固定深度条件。每个窗口只提交新生成的视频后缀，从而避免改写已生成内容，并使活动状…
- **精读笔记**：[打开笔记](../notes/2026-10-29/2610.32381-uniworld-a-unified-world-model-for-real-time-vis.md)

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

### 3. [Hy-Nomas: Towards Free-form Interactive World Generation](http://arxiv.org/abs/2610.36729v1)

- **评分**：72/100
- **作者**：Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng et al.
- **方向**：World Models
- **一句话**：Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences.

### 4. [Direct Forcing: Single-Stage Training with Representation-Space Supervision for Few-Step Autoregressive Video Generation](http://arxiv.org/abs/2610.30861v2)

- **评分**：71/100
- **作者**：Haojun Xu, Jie Huang, Chuyang Zhao et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generation enables low-latency streaming, yet prevailing training pipelines separate causal adaptation from distribution matching.

### 5. [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](http://arxiv.org/abs/2610.37381v1)

- **评分**：67/100
- **作者**：Hanqing Wang, Zhaotian Cai, Ruichuan An et al.
- **方向**：World Models
- **一句话**：Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited.

### 6. [Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](http://arxiv.org/abs/2610.35594v1)

- **评分**：65/100
- **作者**：Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：Few-step distillation is essential for deploying modern video diffusion models.

### 7. [WMEval: Evaluating Interactive World Models Grounded on Physical Simulations](http://arxiv.org/abs/2610.33894v2)

- **评分**：63/100
- **作者**：Lanxiang Hu, Yixin Huang, Abhilash Shankarampeta et al.
- **方向**：World Models
- **一句话**：Interactive world models hold immense potential for high-stakes applications in robotics, game engines, and immersive digital twins, yet existing benchmarks primarily focus on per…
