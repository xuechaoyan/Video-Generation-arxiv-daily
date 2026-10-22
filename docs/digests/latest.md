# Generation Research Daily Digest

> 生成时间：2026-10-22T16:07:28+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [MoDDiT: Simple Token Routing in Diffusion Transformers](http://arxiv.org/abs/2610.28086v1)

- **评分**：76/100
- **作者**：Jarek Liesen, Matthew T. Jackson, Benjamin Ellis et al.
- **方向**：Video Generation, World Models, Efficient Video Diffusion
- **一句话**：论文提出 MoDDiT，通过轻量级路由器分别决定 token 是否经过自注意力和 MLP，从而根据内容、样本和去噪阶段动态分配计算。在 ImageNet 上，MoDDiT 在相近或更低 FLOPs 下取得优于或接近 DiT 的图像生成效果，最低可处理 12.5% 的 token。在 1X 机器人第一视角动作条件视频预测中，12.5% 容量的 ST-MoDD…
- **精读笔记**：[打开笔记](../notes/2026-10-22/2610.28086-moddit-simple-token-routing-in-diffusion-transfo.md)

### 2. [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](http://arxiv.org/abs/2610.29989v1)

- **评分**：74/100
- **作者**：Ruopeng Gao, Yukun Huang, Jiarui Hu et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces](http://arxiv.org/abs/2610.29408v1)

- **评分**：74/100
- **作者**：Xinyu Wang, Huafeng Shi, Yue Ma et al.
- **方向**：World Models
- **一句话**：Interactive video world models predict how an environment evolves under user actions, but most existing systems assume one controlled agent and one task-specific action interface.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](http://arxiv.org/abs/2610.26855v1)

- **评分**：74/100
- **作者**：Tianqi Liu, Hanfei Zhao, Qifeng Liang et al.
- **方向**：World Models
- **一句话**：World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heter…

### 2. [Physical Canvas: A Vision Tactile World Model For Robot Policy Evaluation And Learning](http://arxiv.org/abs/2610.28613v1)

- **评分**：74/100
- **作者**：Zebin Xing, Yuhang Zheng, Yupeng Zheng et al.
- **方向**：World Models
- **一句话**：Evaluating and post-training robot policies through physical interaction is costly and difficult to scale, motivating action-conditioned world models as interactive simulators.

### 3. [OccJEPA: Occlusion as Masking for Amodal Video Segmentation](http://arxiv.org/abs/2610.29061v1)

- **评分**：64/100
- **作者**：Genpei Zhang
- **方向**：Video Generation, World Models
- **一句话**：Amodal video segmentation asks for the complete mask of an object in every frame, including the parts hidden behind other objects.

### 4. [StreamEval: Evaluating Interactive Streaming Video Generation Models](http://arxiv.org/abs/2610.28402v1)

- **评分**：63/100
- **作者**：StreamEval Team
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：As streaming video generation advances, enabling real-time interaction with generated video is becoming increasingly important.

### 5. [AEON: Unifying Video and 3D World Models](http://arxiv.org/abs/2610.28631v1)

- **评分**：62/100
- **作者**：Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu et al.
- **方向**：Video Generation, World Models
- **一句话**：Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail…

### 6. [LaLa-World: Scaling Latent World Models with Natural Language Actions](http://arxiv.org/abs/2610.27851v2)

- **评分**：62/100
- **作者**：Junha Song, Geonmo Gu, Jeongeun Park et al.
- **方向**：Video Generation, World Models
- **一句话**：This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation mo…

### 7. [RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation](http://arxiv.org/abs/2610.27782v1)

- **评分**：59/100
- **作者**：Siyuan Ma, Yu Qi, Cheng Ye et al.
- **方向**：Video Generation, World Models
- **一句话**：Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions.
