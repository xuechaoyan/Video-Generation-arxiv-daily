# Generation Research Daily Digest

> 生成时间：2026-11-09T03:06:31+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)

- **评分**：74/100
- **作者**：Travis Davies, Wentao Ma, Lihao Guo et al.
- **方向**：World Models
- **一句话**：PrimeSim 将预训练视频生成器改造成面向机器人操作的动作条件、多视角、因果自回归世界模型模拟器。它在 22 个机器人平台的 30,110 小时演示上进行训练，采用统一跨具身动作表示、帧对齐双路径动作条件和视角感知交错注意力，以实现动作跟随和多视角一致性。后训练通过因果注意力、四步一致性蒸馏、自 rollout 分布匹配和分层 KV 缓存记忆，提升实时…
- **精读笔记**：[打开笔记](../notes/2026-11-09/2611.04870-primesim-a-generalist-world-model-simulator-from.md)

### 2. [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](http://arxiv.org/abs/2611.07867v1)

- **评分**：74/100
- **作者**：Jihai Zhang, Yuhan Zhou, Junyou Li et al.
- **方向**：World Models
- **一句话**：PlayGen2提出一种面向实时可玩世界的显式三维状态建模框架，将持久化世界记忆中的静态几何和动态实体状态，与负责第一人称图像合成的扩散渲染器分离。世界状态模型在玩家中心的固定大小局部体积内，根据动作、历史和几何上下文进行实体状态转移、未知几何补全和新实体发现，并将结果写回持久记忆；渲染器则依据深度、语义投影和 RGB 历史生成画面，生成图像不参与状态预测…
- **精读笔记**：[打开笔记](../notes/2026-11-09/2611.07867-playgen2-learning-real-time-playable-worlds-with.md)

### 3. [GPWM: Modeling the World as 3D Particle Motion](http://arxiv.org/abs/2611.08338v1)

- **评分**：73/100
- **作者**：Robert Ren, Matthew Bronars, He Zhu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文提出 GPWM，一个直接在三维粒子和刚体运动空间中建模物理世界的生成式世界模型。它采用统一的粒子/刚体表示、多分辨率时空 Transformer，以及流匹配和扩散强制，从观测到的三维场景历史预测多种物理系统，并通过流式生成支持远超训练窗口的长时域 rollout。作者构建了包含 2550 万帧、覆盖六类刚体、可变形体、布料、颗粒和机器人交互的数据集 P…
- **精读笔记**：[打开笔记](../notes/2026-11-09/2611.08338-gpwm-modeling-the-world-as-3d-particle-motion.md)

## 快速浏览

### 1. [Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](http://arxiv.org/abs/2611.07551v1)

- **评分**：73/100
- **作者**：Jia Li, Xurui Peng, Xing Wang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive (AR) video diffusion models generate videos chunk by chunk and have made efficient video generation practical.

### 2. [Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation](http://arxiv.org/abs/2611.05642v1)

- **评分**：72/100
- **作者**：Rohan Agarwal, Robin Andeer, Alex Armbruster et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Conversational video characters must generate video as fast as it plays, for one user at a time: at 24 fps, a sustained 166.7 ms per four-frame chunk at batch size one, with only…

### 3. [Learning Robotic World Models with Semantic and Visual Feedback](http://arxiv.org/abs/2611.07850v1)

- **评分**：72/100
- **作者**：Hao Wu, Yuqi Li, Yizhou Zhao et al.
- **方向**：World Models
- **一句话**：Robot world models predict action-conditioned future visual states to support robotic planning and decision making.

### 4. [Future Representation Distillation for Imagination-free World Action Models](http://arxiv.org/abs/2611.04527v2)

- **评分**：71/100
- **作者**：Jaehyeong Jo, Sangwon Jang, Sihyun Yu et al.
- **方向**：Video Generation, World Models
- **一句话**：World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction.

### 5. [TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](http://arxiv.org/abs/2611.06061v1)

- **评分**：70/100
- **作者**：Jiaao Yu, Yanjian Zhang, Haoyang Jiang et al.
- **方向**：World Models
- **一句话**：Recent video world models allow users to explore generated environments through camera navigation.

### 6. [Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation](http://arxiv.org/abs/2611.09096v1)

- **评分**：70/100
- **作者**：Bohan Wang, Shuo Chen, Yunzhi Li et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) modeling is arguably the only way to extend a fixed-length video diffusion model to longer or even streaming videos.

### 7. [ReactWorld: Structuring Interaction Responses for Embodied Video Generation](http://arxiv.org/abs/2611.06120v1)

- **评分**：67/100
- **作者**：Hanwei Liu, Huijia Zhang, Hanzhang Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Embodied video world models predict scene changes caused by robot actions, yet generated object responses may remain inconsistent with task intent and contact dynamics.
