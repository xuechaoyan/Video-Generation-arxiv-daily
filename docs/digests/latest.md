# Generation Research Daily Digest

> 生成时间：2026-11-17T20:05:48+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Reference Forcing: Long Video Generation with Region-Guided Drift Correction](http://arxiv.org/abs/2611.21559v1)

- **评分**：80/100
- **作者**：Sheng Zhao, Haitian Zheng, Weikai Lin et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文针对自回归长视频生成中主体与背景随时间漂移的问题，提出Reference Forcing。该方法以初始视频块作为无漂移的外观参考，通过独立的锚点注意力路径让当前内容匹配初始帧中的对应区域，并利用训练得到的锚点门控控制不同内容使用参考的强度；同时，通过值校正修复近期KV缓存中的漂移值。教师模型使用主体分割和光流构造区域掩码，学生模型通过LoRA和门控蒸馏…
- **精读笔记**：[打开笔记](../notes/2026-11-17/2611.21559-reference-forcing-long-video-generation-with-reg.md)

### 2. [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](http://arxiv.org/abs/2611.20107v1)

- **评分**：76/100
- **作者**：Yansong Qu, Zilin Huang, Zihao Sheng et al.
- **方向**：World Models
- **一句话**：论文研究依赖世界模型进行自动驾驶规划时的探索—利用困境：模型在训练数据覆盖范围内较可靠，但规划器若探索覆盖范围之外的动作，模型误差会使其偏好被高估的危险动作。SAFER 通过“阶段化失败—专家标注—世界模型规划—在线适应”解决这一问题。离线阶段利用较弱策略、动作噪声和可恢复的延迟制动或保持制动扰动制造失败，并记录真实后果及专家动作和值；模型采用分块式因果潜…
- **精读笔记**：[打开笔记](../notes/2026-11-17/2611.20107-safer-navigating-the-exploration-exploitation-di.md)

### 3. [SciWorldBench: Do Video World Models Really Understand Scientific Experiments?](http://arxiv.org/abs/2611.20899v1)

- **评分**：74/100
- **作者**：Xue Yang, Haonan Cai, Xinyu Hang et al.
- **方向**：Video Generation, World Models
- **一句话**：论文提出 SciWorldBench，用222对、覆盖八个科学类别的成对实验评估视频世界模型是否能根据单一条件变化生成相应的不同结果。每对实验固定场景、过程和摄像机设置，仅改变一个条件；提示词不给出结果，VLM在不知道条件和正确标签的情况下独立评估视频。对十个TI2V模型的评测显示，成对准确率仅为1.4%至24.8%，模型常在两种条件下生成相同结果；即使明…
- **精读笔记**：[打开笔记](../notes/2026-11-17/2611.20899-sciworldbench-do-video-world-models-really-under.md)

## 快速浏览

### 1. [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](http://arxiv.org/abs/2611.21339v1)

- **评分**：72/100
- **作者**：Yunyang Ge, Weijie Kong, Ryan Xu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs.

### 2. [ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching](http://arxiv.org/abs/2611.21038v1)

- **评分**：72/100
- **作者**：Hao Tan, Jinghui Qin, Xuming Hu
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video diffusion enables efficient long video generation, but inference still incurs substantial computational costs from repeated denoising and KV cache op…

### 3. [LynnReal-Hand: Unlocking World Interaction with Hand Control](http://arxiv.org/abs/2611.21479v1)

- **评分**：72/100
- **作者**：Shaohao Rui, Chaoyang Zhang, Xiaofeng Mao et al.
- **方向**：World Models
- **一句话**：Interactive video world models enable exploration through text and camera controls, yet direct object interaction requires finer control.

### 4. [A Unified Control Framework, Mathematical Model, and Five-layer Closed-loop Case Study for Embodied Intelligence Control Systems](http://arxiv.org/abs/2611.19187v1)

- **评分**：66/100
- **作者**：Yiwei Zhou, Zhongcheng Lei, Xiaoran Dai et al.
- **方向**：World Models
- **一句话**：Embodied intelligence holds that an agent develops cognition and behavior through real-time body-environment interaction, so its control system must tightly couple perception, dec…

### 5. [ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving](http://arxiv.org/abs/2611.16579v1)

- **评分**：65/100
- **作者**：Ziying Song, Shengkai Zhang, Caiyan Jia et al.
- **方向**：World Models
- **一句话**：Joint-Embedding Predictive Architectures (JEPAs) enable future prediction in latent space without pixel reconstruction.

### 6. [ResWAM: Learning What Changes, Not What Stays, for World-Action Models](http://arxiv.org/abs/2611.19559v1)

- **评分**：62/100
- **作者**：Chongyu Fan, Gaowen Liu, Ramana Rao Kompella et al.
- **方向**：Video Generation, World Models
- **一句话**：World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world.

### 7. [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](http://arxiv.org/abs/2611.18078v1)

- **评分**：61/100
- **作者**：Ruiqi Shu, Xufeng Zhan, Yuanzhi Liang et al.
- **方向**：Video Generation
- **一句话**：Direct image-to-video diffusion models entangle pixel synthesis with implicit latent motion, precluding persistent 3D mechanical equilibrium, mid-rollout intervention, and counter…
