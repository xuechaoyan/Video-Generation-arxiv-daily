# Generation Research Daily Digest

> 生成时间：2026-10-30T03:03:12+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [BoxWorld: Let World Engines Control and Video Generators Render](http://arxiv.org/abs/2610.36371v1)

- **评分**：78/100
- **作者**：Zike Wu, Ahmed Hatem, Chintan Trivedi et al.
- **方向**：World Models
- **一句话**：BoxWorld 将交互逻辑从视频生成器中剥离出来：编码代理根据用户规则生成 Box World Engine，负责维护对象状态、执行条件交互并输出由布局框、持久属性和动态状态组成的对象中心状态接口；视频生成器则依据该状态流自回归地实时渲染视觉结果。作者基于 LongLive 构建 Box-State Generative Renderer，并通过掩码布局…
- **精读笔记**：[打开笔记](../notes/2026-10-30/2610.36371-boxworld-let-world-engines-control-and-video-gen.md)

### 2. [UniWorld: A Unified World Model for Real-Time Visual World Simulation](http://arxiv.org/abs/2610.32381v3)

- **评分**：77/100
- **作者**：Xin Zhang, Yabo Chen, Shuaiwei Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：UniWorld 面向由外部世界模型、图形引擎或模拟器提供几何轨迹的连续视觉渲染任务，将异构场景状态统一转换为图像对齐深度，并结合参考图像生成具有持续外观的视频。方法在共享时间轴上同步维护视频历史和深度历史：通过噪声对齐的重叠续生成固定旧潜变量并仅提交新后缀，通过滚动深度潜状态仅读取新几何、复用重叠区域。实验覆盖驾驶、人类活动、模拟和合成场景，表明该方法支…
- **精读笔记**：[打开笔记](../notes/2026-10-30/2610.32381-uniworld-a-unified-world-model-for-real-time-vis.md)

### 3. [OSWAM: An Effective World Action Model with One-Step Action Generation](http://arxiv.org/abs/2610.35850v1)

- **评分**：76/100
- **作者**：Guowen Zhang, Liyi Chen, Xu Hu et al.
- **方向**：World Models
- **一句话**：本文提出OSWAM，一种面向自动驾驶和具身控制的直接策略世界动作模型。它通过动作想象令牌（AIT）从视频DiT中提取结构化动作先验，并利用场景想象令牌（SIT）聚合场景上下文，以替代动作扩散从高斯噪声开始的多步去噪初始化。同时，特权信息蒸馏将教师模型利用完整未来视频获得的长时域表征迁移到仅使用当前帧的学生模型中。OSWAM在NAVSIM、RoboTwin…
- **精读笔记**：[打开笔记](../notes/2026-10-30/2610.35850-oswam-an-effective-world-action-model-with-one-s.md)

## 快速浏览

### 1. [FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](http://arxiv.org/abs/2610.34564v1)

- **评分**：73/100
- **作者**：Meryem Koksal, Yunzhe Wang, Volkan Ustun
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Most action-conditioned video world models remain limited to a single player, while existing multiplayer models support only small, fixed groups of agents.

### 2. [Hy-Nomas: Towards Free-form Interactive World Generation](http://arxiv.org/abs/2610.36729v1)

- **评分**：72/100
- **作者**：Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng et al.
- **方向**：World Models
- **一句话**：Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences.

### 3. [PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](http://arxiv.org/abs/2610.37381v1)

- **评分**：67/100
- **作者**：Hanqing Wang, Zhaotian Cai, Ruichuan An et al.
- **方向**：World Models
- **一句话**：Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited.

### 4. [Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](http://arxiv.org/abs/2610.35594v1)

- **评分**：65/100
- **作者**：Junyi Chen, Haiyu Zhang, Zhoujie Fu et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：Few-step distillation is essential for deploying modern video diffusion models.

### 5. [Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation](http://arxiv.org/abs/2610.37983v1)

- **评分**：62/100
- **作者**：Kaihua Chen, Yiming Gong, Deva Ramanan et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：We address the task of long-video, camera-controlled generation from a single image.

### 6. [Dream to Assist: Intent-Conditioned World Models for Shared Vehicle Control](http://arxiv.org/abs/2610.34650v1)

- **评分**：61/100
- **作者**：Jonathan DeCastro, Thomas Balch, Emily Sumner et al.
- **方向**：World Models
- **一句话**：Assistive agents in shared-control settings face a dual challenge: acting proactively to align with the human's intentions while remaining legible enough for the human to comprehe…

### 7. [ReferStream: Interactive Subject Injection for Streaming Video Generation](http://arxiv.org/abs/2610.37566v1)

- **评分**：61/100
- **作者**：Shuolin Xu, Guanyuan Li, Boyu Li et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Injecting new subjects naturally during streaming video generation requires integrating newly supplied visual references into the existing video while preserving established subje…
