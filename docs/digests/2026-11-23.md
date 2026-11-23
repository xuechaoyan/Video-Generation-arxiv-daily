# Generation Research Daily Digest

> 生成时间：2026-11-23T22:57:07+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Hindsight Forcing: Learning Better History from the Future in Autoregressive Video Diffusion](http://arxiv.org/abs/2611.27074v1)

- **评分**：84/100
- **作者**：Haonan An, Yihang Tao, Yu Guo et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文针对少步自回归视频扩散中的长期生成退化问题，指出现有自滚动训练通常切断历史潜变量到早期去噪过程的梯度，使历史内容无法根据未来生成结果进行优化。作者提出 Hindsight Forcing：前向过程使用完整多步滚动结果构建真实推理分布下的历史 KV 缓存，反向过程则通过潜变量直通桥，将未来损失的梯度传递到每个历史块选定的去噪步骤。该方法只保留每块一个去噪…
- **精读笔记**：[打开笔记](../notes/2026-11-23/2611.27074-hindsight-forcing-learning-better-history-from-t.md)

### 2. [ContextRenderer: Dynamic-Context Video Generation for Interactive Game Worlds](http://arxiv.org/abs/2611.25838v1)

- **评分**：83/100
- **作者**：Runze Wang, Fei Zha, Bing He et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Interactive game world models separate executable world evolution from visual generation, using video models to render engine-provided scene representations into detailed observat…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning](http://arxiv.org/abs/2611.27639v1)

- **评分**：73/100
- **作者**：Anqi Li, Kai Liu, Linghe Kong et al.
- **方向**：World Models
- **一句话**：论文研究冻结潜在世界模型中基于 CEM 的候选动作规划加速问题。作者指出，规划器只依赖候选代价的精英排序，而不要求压缩滚动保持特征或代价数值完全一致，因此应以排序一致性而非重建质量作为压缩标准。通过超过 80,000 个闭环回合，论文发现：空间标记的选择方式影响有限；读取真实观测的第一步对后续排序最关键；上下文帧对部分操作任务很重要，但可通过 KV 缓存避…
- **精读笔记**：[打开笔记](../notes/2026-11-23/2611.27639-soar-training-free-rank-consistent-rollout-compr.md)

## 快速浏览

### 1. [ScaleWorld: High-Resolution World Generation through Shared Prediction and Refinement](http://arxiv.org/abs/2611.26615v1)

- **评分**：72/100
- **作者**：Yansong Qu, Wesker Zheng, Quanjian Song et al.
- **方向**：World Models
- **一句话**：High-resolution generation enables video world models to render fine-grained scene structures and textures, but directly generating high-resolution video incurs substantial comput…

### 2. [Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency](http://arxiv.org/abs/2611.26040v2)

- **评分**：72/100
- **作者**：Zhihao Hu, Jianqi Ma, Jun Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Controllable streaming video generation offers a promising route toward interactive game simulation, yet existing methods remain far from practical gameplay.

### 3. [Learning Interaction Dynamics via Motion-Region Guidance for Robotic Video World Models](http://arxiv.org/abs/2611.27344v1)

- **评分**：72/100
- **作者**：Yongkang He, Xiaofen Xing, Xiangmin Xu
- **方向**：World Models
- **一句话**：Action-conditioned video world models imagine future observations under candidate robot actions, providing a promising visual tool for robot policy evaluation and interaction simu…

### 4. [AURA: AUdio-dRiven streaming Avatar](http://arxiv.org/abs/2611.26540v1)

- **评分**：72/100
- **作者**：Nathaniel Cohen, Nicolas Dufour, Amélie Royer et al.
- **方向**：Video Generation
- **一句话**：Current audio-driven video diffusion models can synthesize realistic talking-head videos but generally require dozens of diffusion denoising steps over multi-second video chunks,…

### 5. [ViewDreamer: A Robot World Model beyond Fixed Camera Setups](http://arxiv.org/abs/2611.26981v1)

- **评分**：68/100
- **作者**：Ye Mao, Jinhui Xiong, Egor Larionov et al.
- **方向**：Video Generation, World Models
- **一句话**：Video generation models are increasingly important for robot learning, yet most generate each camera view separately or tile all views in a fixed layout.

### 6. [SonoAtlasWorld: Anatomy-Grounded Ultrasound World Models for Wide-Range Scanning](http://arxiv.org/abs/2611.26867v1)

- **评分**：65/100
- **作者**：Zheyuan Zhang, Boris Mailhe, Hang Yu et al.
- **方向**：World Models
- **一句话**：Learning robotic ultrasound policies requires interactive environments for scalable data generation and repeatable evaluation, while exploration on real patients is limited by acq…

### 7. [Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models](http://arxiv.org/abs/2611.27645v1)

- **评分**：64/100
- **作者**：Nan Tang, Han-Tao Zhang, Jing-Cheng Pang et al.
- **方向**：World Models
- **一句话**：Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences.
