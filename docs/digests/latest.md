# Generation Research Daily Digest

> 生成时间：2026-11-11T03:14:19+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [AR-Edit: Training-Free Autoregressive Video Editing without Inversion](http://arxiv.org/abs/2611.09795v1)

- **评分**：73/100
- **作者**：Hovhannes Margaryan, Quentin Bammey, Christian Sandor et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文研究经DMD蒸馏的自回归视频扩散模型中的训练免费流式视频编辑。作者发现，自注意力中的查询和键在不同噪声水平下基本稳定，而值特征携带主要的视觉内容和身份信息；该特性在少步数模型运行的高噪声区域尤其明显。因此，方法无需传统反演，只需对每个输入视频块进行一次干净前向传播以缓存值特征，再从随机高斯噪声出发、在目标文本提示下去噪，并选择性注入缓存的源值。AR-E…
- **精读笔记**：[打开笔记](../notes/2026-11-11/2611.09795-ar-edit-training-free-autoregressive-video-editi.md)

## 快速浏览

### 1. [Trajectory Forcing: Exploiting Diffusion Trajectories for Autoregressive Long Video Generation](http://arxiv.org/abs/2611.09096v1)

- **评分**：70/100
- **作者**：Bohan Wang, Shuo Chen, Yunzhi Li et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文指出，现有自回归视频扩散方法通常只使用前一视频块的最终预测作为上下文，忽略了多步去噪过程中包含的中间生成信息。作者提出Trajectory Forcing（TraF），将每个历史视频块的去噪轨迹纳入自回归条件，同时为控制计算和显存开销，在当前去噪步骤选择历史轨迹中的单个点作为上下文。方法包含两个阶段：监督学习阶段利用真实视频和线性插值构造伪轨迹，并通过…

### 2. [Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning](http://arxiv.org/abs/2611.10660v1)

- **评分**：68/100
- **作者**：Yinuo Jiang, Guangzhi Wang, Yiran Wang et al.
- **方向**：World Models
- **一句话**：论文提出 DIAL，用于改进基于潜在世界模型的目标条件规划。方法包含三部分：通过滚动对齐训练前向动力学，使其适应自回归预测状态；通过多步逆动力学监督，使潜在状态保留触发状态转移的动作信息；在规划时递归结合逆动力学头和前向模型，生成面向目标的动作序列，并将其作为 CEM 初始提议分布的均值。CEM 后续仍执行标准采样、精英筛选和分布更新。基于四个视觉控制环境…

### 3. [WorldFoundry: Towards Unified Infrastructure for World Intelligence](http://arxiv.org/abs/2611.10771v1)

- **评分**：67/100
- **作者**：Juanxi Tian, Jiadong Hou, Baiang Li et al.
- **方向**：World Models
- **一句话**：Visual generative models increasingly blur the line between synthesizing observations and simulating environments.

### 4. [Semantically Aligned KV Cache Compression for Efficient Agentic Autoregressive Video Generation](http://arxiv.org/abs/2611.11452v1)

- **评分**：62/100
- **作者**：Weizhong Huang, Huaijia Kou, Tianyu Xie et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Agentic autoregressive video generation combines semantic planning, sequential generation, and visual verification for controllable synthesis.

### 5. [Few-Step Streaming Video Generation via Condition Shifting](http://arxiv.org/abs/2611.14033v1)

- **评分**：61/100
- **作者**：Deyuan Liu, Jungang Li, Kaiwen Zheng et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step sampling reduces the cost of streaming video generation.

### 6. [Tiresias: Towards Language-Conditioned World Models](http://arxiv.org/abs/2611.10392v1)

- **评分**：60/100
- **作者**：Fengyi Wu, Yifei Dong, Yetong Sha et al.
- **方向**：World Models
- **一句话**：World models enable planning through internal simulation, while natural language provides intuitive task specification.

### 7. [DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](http://arxiv.org/abs/2611.11166v2)

- **评分**：59/100
- **作者**：Zhongxi Chen, Yi Yang, Xinyi Chen et al.
- **方向**：World Models
- **一句话**：Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand.

### 8. [LO-World: Unified BEV Latent Modeling for Joint 4D Occupancy and LiDAR Forecasting](http://arxiv.org/abs/2611.11912v1)

- **评分**：58/100
- **作者**：Zhimin Liao, Ping Wei, Kai Mao et al.
- **方向**：World Models
- **一句话**：LiDAR point clouds and 3D semantic occupancy represent two distinct modalities capturing fine-grained metric geometry and dense volumetric semantics, respectively, holding natural…

### 9. [ProTEUS: A mutation-resolved world model for closed-loop protein evolution](http://arxiv.org/abs/2611.13348v1)

- **评分**：57/100
- **作者**：Yikun Zhang, Minghao Guo, Guangxue Xu et al.
- **方向**：World Models
- **一句话**：Protein engineering requires navigating rugged fitness landscapes, where small sequence changes can produce large functional differences, but experimental screening can only sampl…
