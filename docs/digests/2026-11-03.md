# Generation Research Daily Digest

> 生成时间：2026-11-03T18:42:11+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
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
- **一句话**：论文提出 History Forcing，用于解决少步自回归视频扩散在长时间生成和视野外世界建模中的历史依赖与一致性问题。核心做法是让自回归教师模型对同一噪声样本分别使用有、无额外历史上下文进行预测，以二者差异提取历史影响，并将其作为残差加到双向教师的得分目标或EMA教师的速度目标中。这样既保留双向教师对视觉质量的监督，又独立强化历史约束，避免将历史一致性…
- **精读笔记**：[打开笔记](../notes/2026-11-03/2611.02782-history-forcing-distilling-history-dependent-con.md)

### 3. [Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](http://arxiv.org/abs/2611.01677v1)

- **评分**：74/100
- **作者**：Zhenxin Zhu, Zhijian Huang, Cheng Chi et al.
- **方向**：World Models
- **一句话**：论文提出小米汽车世界模型2.0，一个统一的流式因果视频世界模型，面向自动驾驶和具身机器人等物理人工智能任务。模型通过VTA和多视角RoPE处理可变视角，通过VAE潜变量拼接统一文本、图像、动作、布局和场景上下文等条件，并利用WorldRec 2.0重建静态与动态3D高斯作为持久场景记忆。数据方面融合通用视频、驾驶与机器人数据，以及由仿真器和视频生成器构造的…
- **精读笔记**：[打开笔记](../notes/2026-11-03/2611.01677-xiaomi-auto-world-model-2-0-causal-world-models.md)

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

### 4. [Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation](http://arxiv.org/abs/2610.42031v1)

- **评分**：71/100
- **作者**：Jiahua Xu, Yijie Fang, Nannan Wang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video generation enables efficient inference through streaming prediction.

### 5. [When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?](http://arxiv.org/abs/2611.01815v1)

- **评分**：67/100
- **作者**：Anton Hristov, Aleksandar Slavov, Vasil Vasilev
- **方向**：World Models
- **一句话**：Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty.

### 6. [TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation](http://arxiv.org/abs/2611.00455v1)

- **评分**：65/100
- **作者**：Jiaxin Shi, Zibin Wu, Yichi Zhang et al.
- **方向**：World Models
- **一句话**：Tactile sensing provides robots with direct observations of contact physics, local geometry, and interaction dynamics, making it a vital source of feedback for contact-rich manipu…

### 7. [INTERACT: Learning Interaction-Aware World Dynamics from Driving Videos for Autonomous Driving](http://arxiv.org/abs/2611.02526v1)

- **评分**：61/100
- **作者**：Zhan Chen, Songyan Zhang, Wenhui Huang et al.
- **方向**：World Models
- **一句话**：Safe autonomous driving requires more than recognizing the current scene: the ego vehicle must anticipate how surrounding traffic participants will evolve under its own motion.
