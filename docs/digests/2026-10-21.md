# Generation Research Daily Digest

> 生成时间：2026-10-21T02:06:49+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base](http://arxiv.org/abs/2610.25634v1)

- **评分**：81/100
- **作者**：Wenqing Wang, Joonghyuk Shin, Jonathan Tremblay et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文研究自回归视频扩散模型在长时间滚动生成中的暴露偏差和质量漂移问题。作者发现，生成历史引起的速度误差在不同噪声种子间约95%具有系统性，因此提出在冻结基础模型上训练轻量LoRA修正器，学习相同噪声状态下干净历史与生成历史之间的反事实速度差距。方法结合DAgger式闭环数据聚合、漂移收缩训练和模型自身单次生成的合成监督，在50秒视频上显著降低漂移，零真实视…
- **精读笔记**：[打开笔记](../notes/2026-10-21/2610.25634-clean-forcing-drift-resistant-autoregressive-vid.md)

### 2. [PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](http://arxiv.org/abs/2610.26711v1)

- **评分**：77/100
- **作者**：Kaiwei Chen, Moran Li, Zhenye Gan et al.
- **方向**：Video Generation, World Models
- **一句话**：论文提出PVBench，用于系统评估视频生成结果的物理合理性。该基准将46个评估维度组织为语义、感知和物理三层以及七个领域，其中物理层包含几何空间、材料与场状态、运动学与持续性、机械与守恒等25个维度。PVBench构建了600组配对的文本到视频和图像到视频提示，30%包含具身智能体、遮挡、视觉杂乱或相机运动等困难因素。评估主要利用VGGT、深度估计、法线…
- **精读笔记**：[打开笔记](../notes/2026-10-21/2610.26711-pvbench-quantifying-physical-plausibility-in-vid.md)

### 3. [MoDDiT: Simple Token Routing in Diffusion Transformers](http://arxiv.org/abs/2610.28086v1)

- **评分**：76/100
- **作者**：Jarek Liesen, Matthew T. Jackson, Benjamin Ellis et al.
- **方向**：Video Generation, World Models, Efficient Video Diffusion
- **一句话**：论文提出MoDDiT，一种在扩散Transformer中对自注意力和MLP分别进行token路由的方法，使模型能够依据内容复杂度、去噪阶段和视频运动动态分配计算。该方法使用Gumbel top-K路由，MLP路由可在批次范围内共享计算预算，同时保持适合GPU并行计算的张量形状。ImageNet实验表明，在相近或更低FLOPs下，MoDDiT可取得优于或接近…
- **精读笔记**：[打开笔记](../notes/2026-10-21/2610.28086-moddit-simple-token-routing-in-diffusion-transfo.md)

## 快速浏览

### 1. [Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion](http://arxiv.org/abs/2610.26262v1)

- **评分**：76/100
- **作者**：Yuanyu He, Zhuokun Chen, Yefei He et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive Diffusion Transformers have emerged as a powerful paradigm for long video generation.

### 2. [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](http://arxiv.org/abs/2610.26855v1)

- **评分**：74/100
- **作者**：Tianqi Liu, Hanfei Zhao, Qifeng Liang et al.
- **方向**：World Models
- **一句话**：World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heter…

### 3. [Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning](http://arxiv.org/abs/2610.28613v1)

- **评分**：74/100
- **作者**：Zebin Xing, Yuhang Zheng, Yupeng Zheng et al.
- **方向**：World Models
- **一句话**：Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators.

### 4. [TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation](http://arxiv.org/abs/2610.26165v1)

- **评分**：72/100
- **作者**：Jia Li, Xurui Peng, Haowei Zhu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video diffusion has emerged as a leading paradigm for efficient video generation, yet its practical deployment remains bottlenecked by the trade-off between ge…

### 5. [Frechet Forcing: Training Long-Horizon Streaming World Models from Short Clips](http://arxiv.org/abs/2610.25666v1)

- **评分**：70/100
- **作者**：Yian Zhao, Yu Yan, Hongcan Guo et al.
- **方向**：World Models
- **一句话**：Streaming video world models generate the future chunk by chunk, conditioned on their own past and a stream of actions.

### 6. [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](http://arxiv.org/abs/2610.11756v3)

- **评分**：70/100
- **作者**：Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion enables causal video streaming without a bidirectional pass over the full clip, but existing few-step systems usually retain only the opening and mo…

### 7. [StreamEval: Evaluating Interactive Streaming Video Generation Models](http://arxiv.org/abs/2610.28402v1)

- **评分**：63/100
- **作者**：StreamEval Team
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：As streaming video generation advances, enabling real-time interaction with generated video is becoming increasingly important.
