# Generation Research Daily Digest

> 生成时间：2026-11-06T03:46:20+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion](http://arxiv.org/abs/2611.02822v1)

- **评分**：78/100
- **作者**：Zhengyang Yu, Akio Hayakawa, Masato Ishii et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion models (AR-VDMs) enable real-time, long-horizon video generation but degrade rapidly once the inference horizon outruns the training horizon, due to…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 2. [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)

- **评分**：74/100
- **作者**：Travis Davies, Wentao Ma, Lihao Guo et al.
- **方向**：World Models
- **一句话**：本文提出 PrimeSim，将 Wan2.2-TI2V-5B 视频生成骨干改造成面向机器人操作的动作条件、多视角、因果自回归世界模型模拟器。模型首先利用 30,110 小时、22 个机器人平台的数据进行中期训练：以 31 维统一动作表示处理跨具身控制，以帧对齐双路径条件增强动作跟随，并用带摄像机身份的视角感知交错注意力保持多视角一致性。随后通过分块因果建模…
- **精读笔记**：[打开笔记](../notes/2026-11-06/2611.04870-primesim-a-generalist-world-model-simulator-from.md)

### 3. [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](http://arxiv.org/abs/2611.07867v1)

- **评分**：74/100
- **作者**：Jihai Zhang, Yuhan Zhou, Junyou Li et al.
- **方向**：World Models
- **一句话**：PlayGen2提出一种面向实时可玩世界的显式三维状态建模框架，将世界状态演化与神经渲染分离。模型以持久世界记忆保存体素几何和按身份索引的动态实体，在玩家中心的固定大小局部区域内，根据动作、历史和几何上下文进行实体状态转移、未知几何补全与新实体发现；渲染器则依据状态投影得到的深度图、语义图和有限 RGB 历史生成第一人称视频。基于仅在单张 Freedoom…
- **精读笔记**：[打开笔记](../notes/2026-11-06/2611.07867-playgen2-learning-real-time-playable-worlds-with.md)

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
