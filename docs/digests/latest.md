# Generation Research Daily Digest

> 生成时间：2026-11-05T19:06:06+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion](http://arxiv.org/abs/2611.02822v1)

- **评分**：78/100
- **作者**：Zhengyang Yu, Akio Hayakawa, Masato Ishii et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion models (AR-VDMs) enable real-time, long-horizon video generation but degrade rapidly once the inference horizon outruns the training horizon, due to…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 2. [History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models](http://arxiv.org/abs/2611.02782v1)

- **评分**：77/100
- **作者**：Hangyi Kuang, Chengzhi Wang, Yefei He et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文提出History Forcing，用于解决少步自回归视频扩散在长时间生成和视野外世界建模中的历史一致性问题。方法比较自回归教师模型在有、无额外历史上下文时对同一噪声视频块的预测，提取历史引起的上下文残差，并将其加权加入双向教师的分数目标或EMA教师的速度目标。长视频生成使用较早的学生生成片段约束主体和场景漂移；视野外建模则使用固定摄像机的教师滚动结果…
- **精读笔记**：[打开笔记](../notes/2026-11-05/2611.02782-history-forcing-distilling-history-dependent-con.md)

### 3. [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)

- **评分**：74/100
- **作者**：Travis Davies, Wentao Ma, Lihao Guo et al.
- **方向**：World Models
- **一句话**：PrimeSim 将 Wan2.2-TI2V-5B 视频生成器改造为面向机器人操作的动作条件、多视角、因果自回归世界模型。它在 30,110 小时、22 个机器人平台的数据上学习统一动作空间，通过帧对齐双路径条件增强动作跟随，并用视角感知交错注意力保持多摄像机一致性。后训练依次采用块因果建模、四步一致性蒸馏、自展开分布匹配和分层 KV 时间记忆，实现 10…
- **精读笔记**：[打开笔记](../notes/2026-11-05/2611.04870-primesim-a-generalist-world-model-simulator-from.md)

## 快速浏览

### 1. [Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation](http://arxiv.org/abs/2611.05642v1)

- **评分**：72/100
- **作者**：Rohan Agarwal, Robin Andeer, Alex Armbruster et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Conversational video characters must generate video as fast as it plays, for one user at a time: at 24 fps, a sustained 166.7 ms per four-frame chunk at batch size one, with only…

### 2. [Future Representation Distillation for Imagination-free World Action Models](http://arxiv.org/abs/2611.04527v2)

- **评分**：71/100
- **作者**：Jaehyeong Jo, Sangwon Jang, Sihyun Yu et al.
- **方向**：Video Generation, World Models
- **一句话**：World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction.

### 3. [TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](http://arxiv.org/abs/2611.06061v1)

- **评分**：70/100
- **作者**：Jiaao Yu, Yanjian Zhang, Haoyang Jiang et al.
- **方向**：World Models
- **一句话**：Recent video world models allow users to explore generated environments through camera navigation.

### 4. [ReactWorld: Structuring Interaction Responses for Embodied Video Generation](http://arxiv.org/abs/2611.06120v1)

- **评分**：67/100
- **作者**：Hanwei Liu, Huijia Zhang, Hanzhang Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Embodied video world models predict scene changes caused by robot actions, yet generated object responses may remain inconsistent with task intent and contact dynamics.

### 5. [Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation](http://arxiv.org/abs/2611.04492v1)

- **评分**：65/100
- **作者**：Jimmy Wang, Yifan Chou, Kaifeng Zhang et al.
- **方向**：World Models
- **一句话**：Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning.

### 6. [NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation](http://arxiv.org/abs/2611.06377v1)

- **评分**：64/100
- **作者**：Jiacheng Lu, Haoyi Zhu, Sipei Yi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video models rely on historical key-value (KV) caches to preserve scene consistency over extended rollouts, making KV storage and repeated attention over history a…

### 7. [MKD2World: A Typed Spatial MarkDown World Model For Web Agents](http://arxiv.org/abs/2611.06544v1)

- **评分**：62/100
- **作者**：Zhihao Nan, Sifan Zhou, Yiming Cheng et al.
- **方向**：World Models
- **一句话**：Graphical user interface (GUI) agents can improve decision-making with world-model foresight, provided that predicted states accurately reflect post-action interfaces.
