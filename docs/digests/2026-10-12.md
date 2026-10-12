# Generation Research Daily Digest

> 生成时间：2026-10-12T20:27:11+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion](http://arxiv.org/abs/2610.12625v1)

- **评分**：84/100
- **作者**：Zekai Gu, Peng Wang, Jiahao Lu et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：论文提出 ForcingBooster，用轻量级路由器在每次去噪后为不同空间图像块预测停止概率。已经充分收敛的图像块直接使用中间的干净潜变量并缓存其 KV 表示，困难区域继续去噪，从而实现空间和时间上的自适应计算分配。路由器通过冻结生成器产生的完整去噪结果作为目标，并结合重建误差损失与计算成本损失进行在线策略训练，无需额外视频数据或人工停止标签。在 Cau…
- **精读笔记**：[打开笔记](../notes/2026-10-12/2610.12625-forcingbooster-adaptive-patch-wise-denoising-for.md)

### 2. [Connected Self Forcing: Beyond Local Learning in Video Autoregression](http://arxiv.org/abs/2610.12156v1)

- **评分**：76/100
- **作者**：Dongbin Zhang, Chaoda Zheng, Kangjie Chen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文研究自回归长视频生成中的训练—推理不一致问题。Self Forcing使用模型自身生成的历史进行训练，但为节省内存而分离历史KV缓存，导致后续块的损失无法反向指导早期块的生成。Connected Self Forcing通过快捷梯度重放，使后续预测的梯度经历史KV状态回传至早期块及其生成过程，同时避免保存完整回滚计算图。该方法无需新增参数且不改变推理流…
- **精读笔记**：[打开笔记](../notes/2026-10-12/2610.12156-connected-self-forcing-beyond-local-learning-in.md)

## 快速浏览

### 1. [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](http://arxiv.org/abs/2610.12368v1)

- **评分**：71/100
- **作者**：Linkai Liu, Yuntian Zhang, Zhenshan Bing et al.
- **方向**：World Models
- **一句话**：本文提出 LiteNWM，一种面向实体机器人视觉导航的高效潜在空间世界模型。针对传统导航世界模型需要为每个候选轨迹生成 RGB 未来、推理代价高的问题，LiteNWM 共享观测历史和目标的视觉编码，在潜在空间中对多个候选动作轨迹进行联合、多时间范围预测，并通过结合候选集合上下文和当前保留轨迹的评分器进行筛选。实验显示，它在三个导航数据集上提升了轨迹选择精度…

### 2. [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](http://arxiv.org/abs/2610.11756v1)

- **评分**：70/100
- **作者**：Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion enables causal video streaming without a bidirectional pass over the full clip, but existing few-step systems usually retain only the opening and mo…

### 3. [Towards Safe World Models: Risks, Defenses, and Evaluation](http://arxiv.org/abs/2610.13372v1)

- **评分**：66/100
- **作者**：Xiaoma Wang, Litian Zhang, Xinze Shi et al.
- **方向**：World Models
- **一句话**：World models support planning, control, learning from imagined experience, and model-mediated evaluation by predicting action-conditioned consequences.

### 4. [WorldGuide: Goal-Directed Video World Model for Procedural Task Execution](http://arxiv.org/abs/2610.12459v1)

- **评分**：65/100
- **作者**：Ankan Deria, Komal Kumar, Hisham Cholakkal et al.
- **方向**：World Models
- **一句话**：Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been…

### 5. [Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](http://arxiv.org/abs/2610.13522v1)

- **评分**：65/100
- **作者**：Peiyan Tu, Cong Wang, Hanxin Zhu et al.
- **方向**：World Models
- **一句话**：Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions.

### 6. [LeWAM: End-to-End World and Action Modeling with JEPAs](http://arxiv.org/abs/2610.12818v1)

- **评分**：64/100
- **作者**：Minghao Fu, Tavis Siebert, Eryk Halicki et al.
- **方向**：World Models
- **一句话**：Joint-embedding predictive architectures (JEPAs) learn compact latent world models without pixel reconstruction.

### 7. [Golden Anchor for Video Generation](http://arxiv.org/abs/2610.13217v1)

- **评分**：61/100
- **作者**：Jinyuan Xu, Shitong Shao, Lichen Bai et al.
- **方向**：World Models
- **一句话**：Video generation supports digital content creation, with applications in virtual avatars, AI-driven filmmaking, interactive game engines, and world models.

### 8. [Unified Generative Video Compression with Autoregressive and Bidirectional Video Diffusion](http://arxiv.org/abs/2610.13023v1)

- **评分**：59/100
- **作者**：Tianyu Zhang, Shuai Huo, Dengchao Jin et al.
- **方向**：Video Generation
- **一句话**：Video diffusion models can reconstruct visually compelling content from severely compressed representations at ultra-low bitrates, but they impose a rigid deployment trade-off.
