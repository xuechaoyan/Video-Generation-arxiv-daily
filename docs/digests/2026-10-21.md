# Generation Research Daily Digest

> 生成时间：2026-10-21T16:09:35+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base](http://arxiv.org/abs/2610.25634v1)

- **评分**：81/100
- **作者**：Wenqing Wang, Joonghyuk Shin, Jonathan Tremblay et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文研究自回归视频扩散模型在长时间滚动生成中的暴露偏差和质量漂移问题。作者发现，在相同噪声状态下，由生成历史与干净历史造成的速度预测差异约95%具有跨噪声种子的系统性，因此可以被轻量修正器学习。Clean Forcing在冻结的Wan等基础模型上训练590万参数的LoRA，通过匹配干净历史下的反事实速度预测来纠正漂移，并利用DAgger式闭环数据聚合和漂移…
- **精读笔记**：[打开笔记](../notes/2026-10-21/2610.25634-clean-forcing-drift-resistant-autoregressive-vid.md)

### 2. [PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](http://arxiv.org/abs/2610.26711v1)

- **评分**：77/100
- **作者**：Kaiwei Chen, Moran Li, Zhenye Gan et al.
- **方向**：Video Generation, World Models
- **一句话**：论文提出PVBench，用于系统评估视频生成结果的物理合理性。该基准包含600组同时支持T2V和I2V的场景提示，覆盖46个维度、7个领域和语义、感知、物理三层评估，其中25个物理维度通过专用视觉模型提取深度、尺度、位姿、法线、轨迹、速度以及动量和能量守恒等数值量，并依据物理规律进行评分，难以直接量化的维度则结合MLLM判断。对12种模型配置的实验表明，物…
- **精读笔记**：[打开笔记](../notes/2026-10-21/2610.26711-pvbench-quantifying-physical-plausibility-in-vid.md)

### 3. [MoDDiT: Simple Token Routing in Diffusion Transformers](http://arxiv.org/abs/2610.28086v1)

- **评分**：76/100
- **作者**：Jarek Liesen, Matthew T. Jackson, Benjamin Ellis et al.
- **方向**：Video Generation, World Models, Efficient Video Diffusion
- **一句话**：论文提出MoDDiT，一种在扩散Transformer中分别对自注意力和MLP进行标记路由的方法，以根据内容、样本和去噪阶段动态分配计算量。路由器通过Gumbel top-K选择标记，MLP路由可跨批次共享计算预算，同时保持适合GPU并行处理的张量形状。在ImageNet上，MoDDiT在相近或更低FLOPs下取得优于或接近DiT的图像生成效果；在1X机器…
- **精读笔记**：[打开笔记](../notes/2026-10-21/2610.28086-moddit-simple-token-routing-in-diffusion-transfo.md)

## 快速浏览

### 1. [Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion](http://arxiv.org/abs/2610.26262v1)

- **评分**：76/100
- **作者**：Yuanyu He, Zhuokun Chen, Yefei He et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive Diffusion Transformers have emerged as a powerful paradigm for long video generation.

### 2. [Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning](http://arxiv.org/abs/2610.28613v1)

- **评分**：74/100
- **作者**：Zebin Xing, Yuhang Zheng, Yupeng Zheng et al.
- **方向**：World Models
- **一句话**：Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators.

### 3. [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](http://arxiv.org/abs/2610.26855v1)

- **评分**：74/100
- **作者**：Tianqi Liu, Hanfei Zhao, Qifeng Liang et al.
- **方向**：World Models
- **一句话**：World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heter…

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
