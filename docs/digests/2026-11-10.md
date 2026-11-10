# Generation Research Daily Digest

> 生成时间：2026-11-10T04:50:19+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](http://arxiv.org/abs/2611.07867v1)

- **评分**：74/100
- **作者**：Jihai Zhang, Yuhan Zhou, Junyou Li et al.
- **方向**：World Models
- **一句话**：PlayGen2提出一种面向实时可游玩世界的显式三维状态建模框架，将世界状态演化与神经视频渲染分离。模型以持久化世界记忆保存体素几何、玩家状态和按身份索引的实体状态，在玩家中心的固定大小局部区域内，根据动作、历史和几何上下文预测实体运动、补全未知几何并发现新实体；随后将状态投影为深度和语义条件，由扩散渲染器生成第一人称视频，生成的RGB帧不再反馈到状态预测…
- **精读笔记**：[打开笔记](../notes/2026-11-10/2611.07867-playgen2-learning-real-time-playable-worlds-with.md)

### 2. [Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](http://arxiv.org/abs/2611.07551v2)

- **评分**：73/100
- **作者**：Jia Li, Xurui Peng, Xing Wang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文针对少步自回归视频扩散模型的推理加速问题，分析了跨帧静态内容和跨去噪步收敛令牌两类冗余，并利用模型自身产生的早期干净估计在线识别它们。提出的PreSTP通过统一令牌掩码跳过冗余令牌计算，以最近计算值维持输出与KV缓存一致性，并通过首帧密集预热、内容自适应掩码复用和定期重新锚定控制误差累积。在CausVid、Self-Forcing、AnyFlow、Lo…
- **精读笔记**：[打开笔记](../notes/2026-11-10/2611.07551-training-free-predictive-spatio-temporal-token-p.md)

### 3. [GPWM: Modeling the World as 3D Particle Motion](http://arxiv.org/abs/2611.08338v1)

- **评分**：73/100
- **作者**：Robert Ren, Matthew Bronars, He Zhu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文提出 GPWM，一种直接在三维粒子和刚体运动空间中建模物理世界的生成式世界模型。它采用共享的粒子/刚体表示、多分辨率时空 Transformer、流匹配和扩散强制，能够统一处理刚体、可变形物体、布料、颗粒材料及机器人交互，并通过流式自回归生成实现远超训练窗口的长期预测。基于 2550 万帧的 ParticleWorlds 数据集，GPWM 在六类物理任…
- **精读笔记**：[打开笔记](../notes/2026-11-10/2611.08338-gpwm-modeling-the-world-as-3d-particle-motion.md)

## 快速浏览

### 1. [AR-Edit: Training-Free Autoregressive Video Editing without Inversion](http://arxiv.org/abs/2611.09795v1)

- **评分**：73/100
- **作者**：Hovhannes Margaryan, Quentin Bammey, Christian Sandor et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Editing a video stream in real time, without access to future frames, is essential for interactive applications.

### 2. [Learning Robotic World Models with Semantic and Visual Feedback](http://arxiv.org/abs/2611.07850v1)

- **评分**：72/100
- **作者**：Hao Wu, Yuqi Li, Yizhou Zhao et al.
- **方向**：World Models
- **一句话**：Robot world models predict action-conditioned future visual states to support robotic planning and decision making.

### 3. [TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](http://arxiv.org/abs/2611.06061v1)

- **评分**：70/100
- **作者**：Jiaao Yu, Yanjian Zhang, Haoyang Jiang et al.
- **方向**：World Models
- **一句话**：Recent video world models allow users to explore generated environments through camera navigation.

### 4. [Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation](http://arxiv.org/abs/2611.09096v1)

- **评分**：70/100
- **作者**：Bohan Wang, Shuo Chen, Yunzhi Li et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) modeling is arguably the only way to extend a fixed-length video diffusion model to longer or even streaming videos.

### 5. [Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning](http://arxiv.org/abs/2611.10660v1)

- **评分**：68/100
- **作者**：Yinuo Jiang, Guangzhi Wang, Yiran Wang et al.
- **方向**：World Models
- **一句话**：Latent world models enable visual control by planning action sequences in compact representation spaces, but a gap remains between how latent dynamics are learned and how they are…

### 6. [WorldFoundry: Towards Unified Infrastructure for World Intelligence](http://arxiv.org/abs/2611.10771v1)

- **评分**：67/100
- **作者**：Juanxi Tian, Jiadong Hou, Baiang Li et al.
- **方向**：World Models
- **一句话**：Visual generative models increasingly blur the line between synthesizing observations and simulating environments.

### 7. [ReactWorld: Structuring Interaction Responses for Embodied Video Generation](http://arxiv.org/abs/2611.06120v1)

- **评分**：67/100
- **作者**：Hanwei Liu, Huijia Zhang, Hanzhang Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Embodied video world models predict scene changes caused by robot actions, yet generated object responses may remain inconsistent with task intent and contact dynamics.
