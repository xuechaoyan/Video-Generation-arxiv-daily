# Generation Research Daily Digest

> 生成时间：2026-11-04T18:54:45+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
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
- **一句话**：论文提出History Forcing，用于解决少步自回归视频扩散在长时生成和视野外世界建模中的历史一致性问题。方法比较自回归教师在有无额外历史条件下对同一噪声视频块的预测，提取历史引起的上下文残差，并将其加到双向教师的分数目标或EMA教师的速度目标中，从而把历史监督与整体视觉质量监督解耦。长视频任务使用学生滚动过程中较早且漂移较小的视频块作为历史；视野外…
- **精读笔记**：[打开笔记](../notes/2026-11-04/2611.02782-history-forcing-distilling-history-dependent-con.md)

### 3. [PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations](http://arxiv.org/abs/2611.04870v1)

- **评分**：74/100
- **作者**：Travis Davies, Wentao Ma, Lihao Guo et al.
- **方向**：World Models
- **一句话**：PrimeSim 将预训练视频生成器改造为面向机器人操作的动作条件、多视角、长时域自回归世界模型。模型在 30,110 小时、22 个机器人平台的数据上进行中期训练，通过统一跨具身动作表示、帧对齐双路径动作条件和视角感知交错注意力提升动作执行与多视角一致性。后训练阶段结合因果分块生成、四步一致性蒸馏、自 rollout 分布匹配和分层 KV-cache 时…
- **精读笔记**：[打开笔记](../notes/2026-11-04/2611.04870-primesim-a-generalist-world-model-simulator-from.md)

## 快速浏览

### 1. [Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](http://arxiv.org/abs/2611.01677v1)

- **评分**：74/100
- **作者**：Zhenxin Zhu, Zhijian Huang, Cheng Chi et al.
- **方向**：World Models
- **一句话**：We present Xiaomi Auto World Model 2.0, a unified streaming causal world model for Physical AI.

### 2. [Learning-to-Memorize: Dynamic Context Management for Long-Horizon Autoregressive Video Generation](http://arxiv.org/abs/2611.01858v1)

- **评分**：72/100
- **作者**：Haowei Zhu, Qijie Wang, Jia Li et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video generation has achieved impressive results on short clips, yet generating long videos remains challenging due to error accumulation over extended horizons, wh…

### 3. [Wave Forcing: Towards Speed-of-Light Streaming Video Generation](http://arxiv.org/abs/2611.00859v1)

- **评分**：72/100
- **作者**：Yijie Jin, Yuxuan Liu, Jiajun Xu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Real-time long-video generation requires continuous output with consistent appearance and natural motion.

### 4. [When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?](http://arxiv.org/abs/2611.01815v1)

- **评分**：67/100
- **作者**：Anton Hristov, Aleksandar Slavov, Vasil Vasilev
- **方向**：World Models
- **一句话**：Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty.

### 5. [Future Representation Distillation for Imagination-Free World Action Models](http://arxiv.org/abs/2611.04527v1)

- **评分**：67/100
- **作者**：Jaehyeong Jo, Sangwon Jang, Sihyun Yu et al.
- **方向**：Video Generation, World Models
- **一句话**：World Action Models (WAMs) use the predictive knowledge of pretrained video diffusion models for robot control through future video prediction.

### 6. [Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation](http://arxiv.org/abs/2611.04492v1)

- **评分**：65/100
- **作者**：Jimmy Wang, Yifan Chou, Kaifeng Zhang et al.
- **方向**：World Models
- **一句话**：Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning.

### 7. [INTERACT: Learning Interaction-Aware World Dynamics from Driving Videos for Autonomous Driving](http://arxiv.org/abs/2611.02526v1)

- **评分**：61/100
- **作者**：Zhan Chen, Songyan Zhang, Wenhui Huang et al.
- **方向**：World Models
- **一句话**：Safe autonomous driving requires more than recognizing the current scene: the ego vehicle must anticipate how surrounding traffic participants will evolve under its own motion.
