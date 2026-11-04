# Generation Research Daily Digest

> 生成时间：2026-11-04T03:26:13+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
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
- **一句话**：论文提出History Forcing，用于解决少步自回归视频扩散在长时间生成和视野外世界建模中的历史一致性问题。核心做法是让自回归教师模型分别在有无额外历史条件下预测同一个噪声视频块，并利用两者的预测残差表示历史信息的影响，再将该残差加到双向教师的DMD分数或EMA教师的速度目标上。对于长视频，额外历史来自学生滚动过程中较早、漂移较小的视频块；对于视野外…
- **精读笔记**：[打开笔记](../notes/2026-11-04/2611.02782-history-forcing-distilling-history-dependent-con.md)

### 3. [Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](http://arxiv.org/abs/2611.01677v1)

- **评分**：74/100
- **作者**：Zhenxin Zhu, Zhijian Huang, Cheng Chi et al.
- **方向**：World Models
- **一句话**：论文提出一个面向自动驾驶和具身机器人的统一流式因果世界模型，支持单视角至七视角、文本/图像/相机位姿/驾驶或机器人动作等异构条件输入。模型以VTA分解跨时间与跨视角注意力，以GLA降低长序列推理的计算和缓存开销，并通过WorldRec 2.0重建静态与动态3D高斯场景作为持续的几何记忆。论文构建了融合通用视频、真实物理世界数据、仿真数据和视频生成长尾数据的…
- **精读笔记**：[打开笔记](../notes/2026-11-04/2611.01677-xiaomi-auto-world-model-2-0-causal-world-models.md)

## 快速浏览

### 1. [X-World 1.6: Building Controllable Virtual Cities with World Models](http://arxiv.org/abs/2611.00596v1)

- **评分**：72/100
- **作者**：XPeng,  :, Boyang Wang et al.
- **方向**：World Models
- **一句话**：Deploying generative world models for end-to-end closed-loop evaluation and policy learning requires precise scenario control, consistent observations, and sustained generation qu…

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

### 7. [TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation](http://arxiv.org/abs/2611.00455v1)

- **评分**：65/100
- **作者**：Jiaxin Shi, Zibin Wu, Yichi Zhang et al.
- **方向**：World Models
- **一句话**：Tactile sensing provides robots with direct observations of contact physics, local geometry, and interaction dynamics, making it a vital source of feedback for contact-rich manipu…
