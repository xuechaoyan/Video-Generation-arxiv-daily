# Generation Research Daily Digest

> 生成时间：2026-10-12T02:43:57+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion](http://arxiv.org/abs/2610.12625v1)

- **评分**：84/100
- **作者**：Zekai Gu, Peng Wang, Jiahao Lu et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：论文提出ForcingBooster，用轻量级路由器根据每个潜在图像块的内容、历史上下文和条件信号，动态决定其是否继续去噪。已收敛的简单区域使用中间干净潜变量提前退出，并将其键值表示缓存供其他区域使用；复杂或条件敏感区域继续细化。作者通过停止损失和计算成本损失进行在线策略训练，以冻结的完整去噪结果作为监督，无需额外视频数据或人工停止标签。在Causal F…
- **精读笔记**：[打开笔记](../notes/2026-10-12/2610.12625-forcingbooster-adaptive-patch-wise-denoising-for.md)

### 2. [Connected Self Forcing: Beyond Local Learning in Video Autoregression](http://arxiv.org/abs/2610.12156v1)

- **评分**：76/100
- **作者**：Dongbin Zhang, Chaoda Zheng, Kangjie Chen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文指出，Self Forcing 虽然通过自生成历史缓解了训练与推理不一致问题，但为节省内存而分离历史 KV 缓存，导致后续分块的损失无法反向指导早期分块及其上下文生成。Connected Self Forcing 通过快捷梯度重放，将后续分块的梯度经历史 KV 状态传回早期分块的 KV 写入和生成过程，同时避免保留完整自回归计算图。实验基于 Wan2.…
- **精读笔记**：[打开笔记](../notes/2026-10-12/2610.12156-connected-self-forcing-beyond-local-learning-in.md)

## 快速浏览

### 1. [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](http://arxiv.org/abs/2610.12368v1)

- **评分**：71/100
- **作者**：Linkai Liu, Yuntian Zhang, Zhenshan Bing et al.
- **方向**：World Models
- **一句话**：本文提出 LiteNWM，用于在视觉导航中高效评估候选轨迹。系统冻结导航策略，利用共享的 DINOv3 视觉编码、动作条件的潜在空间预测器以及相对于当前最优轨迹的评分器，联合预测 H1–H4 多个时间范围的未来特征，并据此筛选候选轨迹，从而避免为每条候选轨迹生成 RGB 视频。RECON、SCAND 和 SACSoN 实验显示，LiteNWM 在轨迹误差和…

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
