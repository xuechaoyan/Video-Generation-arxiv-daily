# Generation Research Daily Digest

> 生成时间：2026-10-20T15:52:27+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base](http://arxiv.org/abs/2610.25634v1)

- **评分**：81/100
- **作者**：Wenqing Wang, Joonghyuk Shin, Jonathan Tremblay et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文研究自回归视频扩散模型在长时间滚动生成中的曝光偏差问题：模型训练使用干净历史，推理却依赖自身可能带有误差的生成结果，导致画面逐渐饱和、纹理退化和场景丢失。作者通过在相同噪声状态下比较干净历史与漂移历史的预测，发现历史诱导的速度误差约95%具有跨噪声种子的系统性。基于此，论文提出Clean Forcing，在冻结的AR基础模型上训练轻量级LoRA校正器，…
- **精读笔记**：[打开笔记](../notes/2026-10-20/2610.25634-clean-forcing-drift-resistant-autoregressive-vid.md)

### 2. [PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](http://arxiv.org/abs/2610.26711v1)

- **评分**：77/100
- **作者**：Kaiwei Chen, Moran Li, Zhenye Gan et al.
- **方向**：Video Generation, World Models
- **一句话**：本文提出PVBench，用于系统评估视频生成结果的物理合理性。该基准将46个评估维度划分为语义、感知和物理三层、七个领域，其中物理层包含25个维度，覆盖几何空间、材料与场状态、运动学与持续性、机械与守恒等方面。PVBench构建了600组同场景的T2V/I2V提示词，其中30%包含具身智能体，并使用专门视觉模型提取深度、法线、尺度、6D位姿、轨迹和守恒残差…
- **精读笔记**：[打开笔记](../notes/2026-10-20/2610.26711-pvbench-quantifying-physical-plausibility-in-vid.md)

### 3. [Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion](http://arxiv.org/abs/2610.26262v1)

- **评分**：76/100
- **作者**：Yuanyu He, Zhuokun Chen, Yefei He et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：本文针对自回归扩散视频生成中的KV缓存内存膨胀和静态区域重复计算问题，提出DASA框架。该框架通过逐帧记忆管理，根据时序特征相似度压缩历史KV缓存，并利用静态令牌定期刷新避免背景细节退化；同时通过局部运动对齐识别动态区域，对静态区域提前退出并复用上一视频块的特征。为避免训练稀疏复用机制导致运动迟滞，作者进一步提出动态引导蒸馏，对高运动区域施加更大损失权重。…
- **精读笔记**：[打开笔记](../notes/2026-10-20/2610.26262-dynamics-aware-sparse-attention-for-efficient-au.md)

## 快速浏览

### 1. [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](http://arxiv.org/abs/2610.26855v1)

- **评分**：74/100
- **作者**：Tianqi Liu, Hanfei Zhao, Qifeng Liang et al.
- **方向**：World Models
- **一句话**：World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heter…

### 2. [TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation](http://arxiv.org/abs/2610.26165v1)

- **评分**：72/100
- **作者**：Jia Li, Xurui Peng, Haowei Zhu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video diffusion has emerged as a leading paradigm for efficient video generation, yet its practical deployment remains bottlenecked by the trade-off between ge…

### 3. [Structured Latent Dynamics for Long-Horizon Embodied World Models](http://arxiv.org/abs/2610.24534v1)

- **评分**：71/100
- **作者**：Kevin Chen, Yu-Wei Zhan, Haoran Liang et al.
- **方向**：World Models
- **一句话**：Reliable long-horizon prediction remains a central challenge for embodied world models.

### 4. [Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips](http://arxiv.org/abs/2610.25666v1)

- **评分**：70/100
- **作者**：Yian Zhao, Yu Yan, Hongcan Guo et al.
- **方向**：World Models
- **一句话**：Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions.

### 5. [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](http://arxiv.org/abs/2610.11756v3)

- **评分**：70/100
- **作者**：Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion enables causal video streaming without a bidirectional pass over the full clip, but existing few-step systems usually retain only the opening and mo…

### 6. [Persistent Planar Memory for Video World Models](http://arxiv.org/abs/2610.23795v1)

- **评分**：69/100
- **作者**：Yuze He, Bin Tan, Zelin Gao et al.
- **方向**：World Models
- **一句话**：Video world models that generate and explore environments at scale need a persistent 3D memory of what they have produced.

### 7. [Momentum: Persistent Dynamics for Video World Models](http://arxiv.org/abs/2610.23423v1)

- **评分**：65/100
- **作者**：Nedko Savov, Stefan Maria Ailuro, Danda Pani Paudel et al.
- **方向**：World Models
- **一句话**：Video world models must capture how a scene evolves beyond the current camera view to generate consistent observations when its content reappears.
