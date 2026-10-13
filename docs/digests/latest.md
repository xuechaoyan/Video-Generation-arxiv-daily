# Generation Research Daily Digest

> 生成时间：2026-10-13T04:01:33+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion](http://arxiv.org/abs/2610.12625v1)

- **评分**：84/100
- **作者**：Zekai Gu, Peng Wang, Jiahao Lu et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：论文针对少步数自回归视频扩散模型仍对所有空间块使用统一去噪预算的问题，提出ForcingBooster。该方法利用轻量级路由器在每个去噪步骤后判断各潜在块是否已经收敛：简单区域提前停止并缓存其键值表示，复杂或受条件影响的区域继续细化。路由器通过冻结生成器产生的完整去噪结果作为目标，并结合停止误差损失和计算成本损失进行在线策略训练，无需额外视频数据或人工停止…
- **精读笔记**：[打开笔记](../notes/2026-10-13/2610.12625-forcingbooster-adaptive-patch-wise-denoising-for.md)

### 2. [Connected Self Forcing: Beyond Local Learning in Video Autoregression](http://arxiv.org/abs/2610.12156v1)

- **评分**：76/100
- **作者**：Dongbin Zhang, Chaoda Zheng, Kangjie Chen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文指出，Self Forcing 虽然通过自生成历史进行训练以缓解训练—推理不一致，但为节省内存而分离历史 KV 缓存，导致后续块的损失无法反向指导早期块的生成。Connected Self Forcing 通过快捷梯度重放，将后续预测的梯度经历史 KV 状态传回早期块，同时避免保存完整自回归计算图。该方法结合 DMD 训练，无需增加参数或改变推理流程。…
- **精读笔记**：[打开笔记](../notes/2026-10-13/2610.12156-connected-self-forcing-beyond-local-learning-in.md)

## 快速浏览

### 1. [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](http://arxiv.org/abs/2610.12368v1)

- **评分**：71/100
- **作者**：Linkai Liu, Yuntian Zhang, Zhenshan Bing et al.
- **方向**：World Models
- **一句话**：本文提出 LiteNWM，用于解决导航世界模型在评估多个候选轨迹时因逐候选生成 RGB 未来观测而产生的高计算成本。系统冻结导航策略，使用共享的 DINOv3 编码器提取观测历史和目标特征，再根据候选动作及其累计位姿，在潜在空间中联合预测 H1 至 H4 的多时间范围未来表征。一个结合目标、当前状态、候选集合上下文和相对基准轨迹信息的评分器，预测候选轨迹相…

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

### 4. [Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](http://arxiv.org/abs/2610.13522v1)

- **评分**：65/100
- **作者**：Peiyan Tu, Cong Wang, Hanxin Zhu et al.
- **方向**：World Models
- **一句话**：Action-conditioned world models offer a promising foundation for generalist robotic intelligence by predicting the consequences of actions.

### 5. [WorldGuide: Goal-Directed Video World Model for Procedural Task Execution](http://arxiv.org/abs/2610.12459v1)

- **评分**：65/100
- **作者**：Ankan Deria, Komal Kumar, Hisham Cholakkal et al.
- **方向**：World Models
- **一句话**：Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been…

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
