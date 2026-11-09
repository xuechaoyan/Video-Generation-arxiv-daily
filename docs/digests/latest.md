# Generation Research Daily Digest

> 生成时间：2026-11-09T21:39:38+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)

- **评分**：74/100
- **作者**：Travis Davies, Wentao Ma, Lihao Guo et al.
- **方向**：World Models
- **一句话**：PrimeSim 将预训练视频生成器改造为面向机器人操作的动作条件、多视角、因果自回归世界模型模拟器。模型在 30,110 小时、22 个机器人平台的数据上进行中期训练，通过统一跨具身动作表示、帧对齐双路径动作条件和视角感知交错注意力，实现动作跟随与多视角一致性。随后，因果适配、四步一致性蒸馏、自回归自 rollout 训练以及分层时间记忆，使其能够以约…
- **精读笔记**：[打开笔记](../notes/2026-11-09/2611.04870-primesim-a-generalist-world-model-simulator-from.md)

### 2. [PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State](http://arxiv.org/abs/2611.07867v1)

- **评分**：74/100
- **作者**：Jihai Zhang, Yuhan Zhou, Junyou Li et al.
- **方向**：World Models
- **一句话**：PlayGen2提出一种面向实时可玩世界的显式三维状态建模框架，将世界状态演化与神经视频渲染解耦。系统用持久化体素占用网格表示静态几何，用带身份索引的三维实体状态表示玩家、怪物、投射物和物品；在以玩家为中心的固定大小局部区域内，模型根据动作、历史状态和几何上下文进行几何补全、实体发现与实体动力学预测，并把结果写回世界记忆。渲染器再依据深度图、语义图、动作和…
- **精读笔记**：[打开笔记](../notes/2026-11-09/2611.07867-playgen2-learning-real-time-playable-worlds-with.md)

### 3. [Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](http://arxiv.org/abs/2611.07551v2)

- **评分**：73/100
- **作者**：Jia Li, Xurui Peng, Xing Wang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文研究少步自回归视频扩散模型的推理加速问题。作者发现，即使少步蒸馏削弱了去噪步之间的冗余，视频中仍存在跨相邻帧的静态令牌冗余，以及在去噪过程中提前稳定的令牌。PreSTP利用模型自身早期干净估计在线识别这两类冗余，以统一令牌掩码跳过后续计算，并通过最近计算值恢复、首帧密集预热和内容自适应掩码复用来保持轨迹与KV缓存一致性。实验覆盖CausVid、Self…
- **精读笔记**：[打开笔记](../notes/2026-11-09/2611.07551-training-free-predictive-spatio-temporal-token-p.md)

## 快速浏览

### 1. [GPWM: Modeling the World as 3D Particle Motion](http://arxiv.org/abs/2611.08338v1)

- **评分**：73/100
- **作者**：Robert Ren, Matthew Bronars, He Zhu et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：We introduce GPWM, a Generative Particle World Model that predicts how 3D scenes evolve by generating the motion of particles and rigid bodies over time.

### 2. [AR-Edit: Training-Free Autoregressive Video Editing without Inversion](http://arxiv.org/abs/2611.09795v1)

- **评分**：73/100
- **作者**：Hovhannes Margaryan, Quentin Bammey, Christian Sandor et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Editing a video stream in real time, without access to future frames, is essential for interactive applications.

### 3. [Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation](http://arxiv.org/abs/2611.05642v1)

- **评分**：72/100
- **作者**：Rohan Agarwal, Robin Andeer, Alex Armbruster et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Conversational video characters must generate video as fast as it plays, for one user at a time: at 24 fps, a sustained 166.7 ms per four-frame chunk at batch size one, with only…

### 4. [Learning Robotic World Models with Semantic and Visual Feedback](http://arxiv.org/abs/2611.07850v1)

- **评分**：72/100
- **作者**：Hao Wu, Yuqi Li, Yizhou Zhao et al.
- **方向**：World Models
- **一句话**：Robot world models predict action-conditioned future visual states to support robotic planning and decision making.

### 5. [Future Representation Distillation for Imagination-free World Action Models](http://arxiv.org/abs/2611.04527v2)

- **评分**：71/100
- **作者**：Jaehyeong Jo, Sangwon Jang, Sihyun Yu et al.
- **方向**：Video Generation, World Models
- **一句话**：World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction.

### 6. [TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](http://arxiv.org/abs/2611.06061v1)

- **评分**：70/100
- **作者**：Jiaao Yu, Yanjian Zhang, Haoyang Jiang et al.
- **方向**：World Models
- **一句话**：Recent video world models allow users to explore generated environments through camera navigation.

### 7. [Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation](http://arxiv.org/abs/2611.09096v1)

- **评分**：70/100
- **作者**：Bohan Wang, Shuo Chen, Yunzhi Li et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) modeling is arguably the only way to extend a fixed-length video diffusion model to longer or even streaming videos.
