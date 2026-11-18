# Generation Research Daily Digest

> 生成时间：2026-11-18T04:46:40+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Reference Forcing: Long Video Generation with Region-Guided Drift Correction](http://arxiv.org/abs/2611.21559v1)

- **评分**：80/100
- **作者**：Sheng Zhao, Haitian Zheng, Weikai Lin et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文针对自回归长视频生成中的外观漂移问题提出Reference Forcing。该方法将初始视频块作为稳定的外观参考：通过带有主体分割和背景光流掩码的教师注意力，将区域匹配行为蒸馏到学生模型独立的锚点注意力路径中，并学习锚点门控以区分初始帧中已有内容和后来出现的新内容。同时，方法在KV缓存中通过键相似度匹配，将较早缓存块的漂移值向初始帧对应值校正，但保留最…
- **精读笔记**：[打开笔记](../notes/2026-11-18/2611.21559-reference-forcing-long-video-generation-with-reg.md)

### 2. [FastFrames: Video Generation at Interactive Latency](http://arxiv.org/abs/2611.23226v1)

- **评分**：79/100
- **作者**：Gene Chou, Guandao Yang, Fujun Luan et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文针对自回归视频扩散模型端到端响应延迟过高的问题，提出 FastFrames。作者通过延迟剖析发现，VAE 像素解码和 KV 缓存更新等非去噪环节是主要瓶颈，而不仅仅是扩散采样步骤。为此，FastFrames 使用基于 ConvNeXt 的轻量级像素解码器替代 VAE，使用轻量级网络修复 KV 缓存，并结合持久化缓存、条件预计算、分段注意力、算子融合、C…
- **精读笔记**：[打开笔记](../notes/2026-11-18/2611.23226-fastframes-video-generation-at-interactive-laten.md)

### 3. [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](http://arxiv.org/abs/2611.20107v1)

- **评分**：76/100
- **作者**：Yansong Qu, Zilin Huang, Zihao Sheng et al.
- **方向**：World Models
- **一句话**：本文提出 SAFER，用于解决依赖世界模型的自动驾驶规划中的探索—利用困境。其核心思路是先在仿真中利用较弱驾驶策略和可恢复扰动主动制造失败，再由专家为失败轨迹中的每个状态提供动作和值标注，使世界模型同时学习错误行为的后果和正确恢复方式。模型采用可一次性预测未来动作块的因果分块潜在动力学、奖励与价值预测、行为克隆动作先验以及碰撞风险头；规划器使用带风险惩罚的…
- **精读笔记**：[打开笔记](../notes/2026-11-18/2611.20107-safer-navigating-the-exploration-exploitation-di.md)

## 快速浏览

### 1. [Inertial Video World Models](http://arxiv.org/abs/2611.22314v1)

- **评分**：76/100
- **作者**：Yuan Gao, Fan Xu, Yu Guo et al.
- **方向**：World Models
- **一句话**：The physical world has inertia: it evolves from what already exists rather than being recreated at every instant.

### 2. [Code World Model 2.0: Towards Infinite Controllable Video Generation](http://arxiv.org/abs/2611.22925v1)

- **评分**：75/100
- **作者**：Ruoyu Wang, Hao Zhong, Yanming Yang et al.
- **方向**：Video Generation, World Models
- **一句话**：Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interac…

### 3. [SciWorldBench: Do Video World Models Really Understand Scientific Experiments?](http://arxiv.org/abs/2611.20899v1)

- **评分**：74/100
- **作者**：Xue Yang, Haonan Cai, Xinyu Hang et al.
- **方向**：Video Generation, World Models
- **一句话**：While the ability of video generation models to accurately depict scientific phenomena has received growing attention, determining whether these models genuinely understand the un…

### 4. [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](http://arxiv.org/abs/2611.21339v1)

- **评分**：72/100
- **作者**：Yunyang Ge, Weijie Kong, Ryan Xu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs.

### 5. [LynnReal-Hand: Unlocking World Interaction with Hand Control](http://arxiv.org/abs/2611.21479v2)

- **评分**：72/100
- **作者**：Shaohao Rui, Chaoyang Zhang, Xiaofeng Mao et al.
- **方向**：World Models
- **一句话**：Interactive video world models enable exploration through text and camera controls, yet direct object interaction requires finer control.

### 6. [ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching](http://arxiv.org/abs/2611.21038v2)

- **评分**：72/100
- **作者**：Hao Tan, Jinghui Qin, Xuming Hu
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video diffusion enables efficient long video generation, but inference still incurs substantial computational costs from repeated denoising and KV cache op…

### 7. [Towards Data-Efficient, Real-Time World Models](http://arxiv.org/abs/2611.22497v1)

- **评分**：72/100
- **作者**：Raluca Stevenson, David Bignell, Jennifer C. White et al.
- **方向**：World Models
- **一句话**：State-of-the-art world models have been used to produce sequences of gameplay that accord with provided user-input actions.
