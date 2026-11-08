# Generation Research Daily Digest

> 生成时间：2026-11-08T02:48:24+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)

- **评分**：74/100
- **作者**：Travis Davies, Wentao Ma, Lihao Guo et al.
- **方向**：World Models
- **一句话**：本文提出PrimeSim，将预训练视频生成器改造成面向机器人操作的动作条件、多视角、因果自回归世界模型模拟器。模型在30,110小时、覆盖22个平台的机器人数据上进行中期训练，通过统一跨具身动作表示、帧对齐双路径动作条件和视角感知交错注意力，提升动作控制与多视角一致性。随后通过因果适配、四步一致性蒸馏、自滚动分布匹配和分层时间记忆，实现快速生成与长时程闭环…
- **精读笔记**：[打开笔记](../notes/2026-11-08/2611.04870-primesim-a-generalist-world-model-simulator-from.md)

### 2. [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](http://arxiv.org/abs/2611.07867v1)

- **评分**：74/100
- **作者**：Jihai Zhang, Yuhan Zhou, Junyou Li et al.
- **方向**：World Models
- **一句话**：PlayGen2提出了一种将显式三维世界状态演化与神经渲染解耦的可玩世界模型。系统以持久化世界记忆保存体素几何和按身份索引的动态实体状态，在玩家中心的局部三维区域内，根据动作、实体历史和几何信息进行几何补全、实体发现及状态转移；随后由扩散渲染器依据深度、语义投影和有限RGB历史生成第一人称视频，生成帧不再反馈给状态预测。模型仅使用单张Doom地图的结构化游…
- **精读笔记**：[打开笔记](../notes/2026-11-08/2611.07867-playgen2-learning-real-time-playable-worlds-with.md)

### 3. [GPWM: Modeling the World as 3D Particle Motion](http://arxiv.org/abs/2611.08338v1)

- **评分**：73/100
- **作者**：Robert Ren, Matthew Bronars, He Zhu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文提出 GPWM，将三维场景表示为粒子和刚体，并直接生成其物理运动，而非生成视频外观。模型采用物体感知的多分辨率时空 Transformer，以流匹配和逐帧扩散强制实现可流式、长时域的轨迹生成。基于包含 2550 万帧、覆盖六类物理场景的 ParticleWorlds 数据集，GPWM 在各领域均优于既有学习动力学方法，平均降低 31% 的预测误差，并能…
- **精读笔记**：[打开笔记](../notes/2026-11-08/2611.08338-gpwm-modeling-the-world-as-3d-particle-motion.md)

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

### 6. [ReactWorld: Structuring Interaction Responses for Embodied Video Generation](http://arxiv.org/abs/2611.06120v1)

- **评分**：67/100
- **作者**：Hanwei Liu, Huijia Zhang, Hanzhang Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Embodied video world models predict scene changes caused by robot actions, yet generated object responses may remain inconsistent with task intent and contact dynamics.

### 7. [Seeing Beyond the Next Step: World-Model-Guided Human-Like Navigation in Multi-Agent Scenes](http://arxiv.org/abs/2611.07730v1)

- **评分**：66/100
- **作者**：Seong-Eun Hong, JuYeong Hwang, Jinhyun Kim et al.
- **方向**：World Models
- **一句话**：Selecting a next motion in a populated scene is not just a matter of avoiding what is currently in the way: an action can be locally feasible yet drift onto the road instead of th…
