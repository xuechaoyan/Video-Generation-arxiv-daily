# Generation Research Daily Digest

> 生成时间：2026-11-07T03:18:56+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)

- **评分**：74/100
- **作者**：Travis Davies, Wentao Ma, Lihao Guo et al.
- **方向**：World Models
- **一句话**：本文提出 PrimeSim，将预训练视频生成器改造成面向机器人操作的动作条件、多视角、长时域世界模型模拟器。模型在 30,110 小时、22 个机器人平台的数据上进行中训练，采用统一跨具身动作表示、帧对齐双路径动作条件和视角感知交错注意力，以实现动作跟随和多视角一致性。随后通过因果适配、四步一致性蒸馏、基于自身历史的 rollout 训练以及分层 KV-c…
- **精读笔记**：[打开笔记](../notes/2026-11-07/2611.04870-primesim-a-generalist-world-model-simulator-from.md)

### 2. [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](http://arxiv.org/abs/2611.07867v1)

- **评分**：74/100
- **作者**：Jihai Zhang, Yuhan Zhou, Junyou Li et al.
- **方向**：World Models
- **一句话**：PlayGen2提出一种将显式三维世界状态演化与神经渲染分离的实时可玩世界模型。模型以持久世界记忆保存体素几何和按身份索引的动态实体，在玩家中心的固定局部区域内，根据动作、历史状态和几何上下文联合完成未知几何、发现新实体并预测实体动力学；随后由扩散渲染器依据深度、语义投影和有限 RGB 历史生成第一人称画面，生成图像不参与状态预测。基于约500小时、单张…
- **精读笔记**：[打开笔记](../notes/2026-11-07/2611.07867-playgen2-learning-real-time-playable-worlds-with.md)

### 3. [GPWM: Modeling the World as 3D Particle Motion](http://arxiv.org/abs/2611.08338v1)

- **评分**：73/100
- **作者**：Robert Ren, Matthew Bronars, He Zhu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文提出 GPWM，一种直接在三维粒子和刚体运动空间中建模物理世界的生成式世界模型。它采用统一的粒子/刚体表示、多分辨率时空 Transformer、流匹配和扩散强制，能够处理刚体、可变形体、布料和颗粒材料，并通过流式去噪进行远超训练窗口的自回归生成。在包含 2550 万帧、六类物理场景的 ParticleWorlds 数据集上，GPWM 平均将预测误差较…
- **精读笔记**：[打开笔记](../notes/2026-11-07/2611.08338-gpwm-modeling-the-world-as-3d-particle-motion.md)

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
