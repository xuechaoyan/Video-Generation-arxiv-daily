# Generation Research Daily Digest

> 生成时间：2026-09-21T17:13:46+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](http://arxiv.org/abs/2609.18430v1)

- **评分**：80/100
- **作者**：Awomo-WM Team,  :, Enhui Ma et al.
- **方向**：World Models
- **一句话**：本文提出 StrucPhysVideo，用于建模物体运动、接触、形变和状态变化。系统首先通过镜头切分、运动感知窗口选择、质量与内容过滤、物理相关性验证，构建物理导向视频数据，并生成包含场景、相机运动、材料属性及时间定位行为的结构化字幕和标签。基于此，StrucPhysVideo-TI2V 使用稀疏 MoE 视频 Transformer 和课程式训练进行文本…
- **精读笔记**：[打开笔记](../notes/2026-09-21/2609.18430-strucphysvideo-learning-physical-dynamics-from-s.md)

### 2. [Astronex-World 1.0: Real-Time Interactive World Model Foundation](http://arxiv.org/abs/2609.20034v1)

- **评分**：74/100
- **作者**：Xin Zhou, Cong Miao
- **方向**：World Models
- **一句话**：Astronex-World 1.0 是一个基于 Wan2.2-TI2V-5B 的 5B 可控视频世界模型基础，提供双向和因果两种形态，统一支持文本、图像、相机、连续动作、具身标识符及事件控制。模型通过 PRoPE 注入相机几何信息，并在每个 Transformer 层调制动作条件；因果版本采用块因果注意力、局部历史窗口、持久注意力汇聚帧、KV 缓存和少步…
- **精读笔记**：[打开笔记](../notes/2026-09-21/2609.20034-astronex-world-1-0-real-time-interactive-world-m.md)

### 3. [ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation](http://arxiv.org/abs/2609.21712v1)

- **评分**：74/100
- **作者**：Boni Hu, Xiong Wei, Haoming Huang et al.
- **方向**：World Models
- **一句话**：论文提出面向自动驾驶闭环仿真的 ZYT-World。它使用单一 5B 参数视频 DiT，在原生分辨率下联合生成四个超广角鱼眼视图和三个针孔视图，并通过 Plücker 射线、运动 AdaLN、像素对齐布局和可插拔隐式记忆实现相机几何、车辆运动、交通参与者及地点身份控制。通过教师强制、因果一致性蒸馏、自回滚 DMD 和 RigCritic，将 40 步双向扩…
- **精读笔记**：[打开笔记](../notes/2026-09-21/2609.21712-zyt-world-a-real-time-controllable-world-model-f.md)

## 快速浏览

### 1. [WM-VS: Progress-Aligned World Models for Closed-Loop Visual Servoing](http://arxiv.org/abs/2609.20892v1)

- **评分**：66/100
- **作者**：Guanzhong Sun, Junyi Ma, Yixuan Zhou et al.
- **方向**：World Models
- **一句话**：Closed-loop visual servoing requires predictions that indicate whether an action reduces task error, not only whether the action is plausible.

### 2. [FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision-Language-Action Models](http://arxiv.org/abs/2609.21228v1)

- **评分**：61/100
- **作者**：Zhiyuan Gao, Di Wen, Yanxiang Zhan et al.
- **方向**：World Models
- **一句话**：Vision-language-action (VLA) models built on pretrained vision-language models have demonstrated strong performance across diverse robotic manipulation tasks.

### 3. [Recency Forcing: Bridging the Long-Horizon Gap in Autoregressive Video Generation](http://arxiv.org/abs/2609.19729v1)

- **评分**：59/100
- **作者**：Tri Cao, Hung Nguyen, Phong Nguyen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video generation degrades over long horizons due to an overlooked train-inference discrepancy we term KV eviction mismatch: models train on short clips where a…

### 4. [PointZero: 3D Point Track Completion for Learning Transferable 3D Dynamics](http://arxiv.org/abs/2609.19142v1)

- **评分**：58/100
- **作者**：Bardienus P. Duisterhof, Kaifeng Zhang, Adam Hung et al.
- **方向**：World Models
- **一句话**：World models endow perceptual systems with the ability to predict how scenes evolve under interaction.

### 5. [DART: Distillation-Aware Reparameterization for Training-Free LoRA Reuse in Few-Step Video Diffusion Models](http://arxiv.org/abs/2609.20051v1)

- **评分**：58/100
- **作者**：Shihong Li, Juntao Xu,  JinCao et al.
- **方向**：Video Generation
- **一句话**：Step distillation reduces the cost of video generation, but reusing a LoRA trained for a longer trajectory can alter its functional effect or degrade target quality.

### 6. [Feeling Terrain Before Crossing: World Models for Off-Road Navigation](http://arxiv.org/abs/2609.19863v1)

- **评分**：57/100
- **作者**：E-In Son, Dong-Wook Kim, Ji-Hoon Hwang et al.
- **方向**：World Models
- **一句话**：Navigation world models plan by foresight, predicting the future that each candidate action sequence produces and selecting the best, rather than mapping observations to actions d…

### 7. [Semantic SLAM in Precision Agriculture using Bayesian Inference](http://arxiv.org/abs/2609.20604v1)

- **评分**：56/100
- **作者**：Ruben Beumer, Sander Doodeman, René van de Molengraft et al.
- **方向**：World Models
- **一句话**：This paper presents a real-time semantic world modeling framework specialized for precision agriculture using autonomous robots.
