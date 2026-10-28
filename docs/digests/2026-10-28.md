# Generation Research Daily Digest

> 生成时间：2026-10-28T02:39:34+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
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
- **一句话**：BoxWorld 将交互规则执行与视频渲染解耦：编码代理根据用户规则生成世界引擎，维护对象状态并决定交互结果；自回归视频渲染器则通过布局框、持久属性和动态状态，将状态流实时生成视频。作者基于开放领域视频和游戏视频的自动标注，采用布局 grounding、状态动态适配和 rollout 蒸馏三阶段训练，并提出 PairedStateBench。实验显示，该方…
- **精读笔记**：[打开笔记](../notes/2026-10-28/2610.36371-boxworld-let-world-engines-control-and-video-gen.md)

### 3. [UniWorld: A Unified World Model for Real-Time Visual World Simulation](http://arxiv.org/abs/2610.32381v2)

- **评分**：77/100
- **作者**：Xin Zhang, Yabo Chen, Shuaiwei Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：UniWorld 面向由外部世界源驱动的连续视觉模拟，将不同来源的几何状态统一转换为图像对齐深度，并与参考图像外观共同输入视频生成器。方法通过噪声对齐的重叠续接保留视频潜变量历史，通过滚动深度潜状态增量读取并固定几何条件，只提交每个窗口的新视频后缀。实验覆盖驾驶、人体活动、模拟和合成场景，表明该方法能够支持长时生成、原生或估计深度、外观切换及控制分支，并在…
- **精读笔记**：[打开笔记](../notes/2026-10-28/2610.32381-uniworld-a-unified-world-model-for-real-time-vis.md)

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
