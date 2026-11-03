# Generation Research Daily Digest

> 生成时间：2026-11-03T04:07:43+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](http://arxiv.org/abs/2610.40614v1)

- **评分**：78/100
- **作者**：Jinhyeok Choi, JoungBin Lee, Jongmin Lee et al.
- **方向**：World Models
- **一句话**：本文提出 L3G-World，一个从单张图像和相机轨迹出发、能够实时生成可探索且空间一致的长时域世界模型。其核心是潜空间三维高斯记忆 L3G：L3G-Mem 仅在记忆未覆盖或重建误差较大的区域生成新高斯，并对已有高斯进行残差细化，使记忆规模主要随场景空间范围增长；每个高斯同时存储 VAE 潜特征，可直接渲染为视频 DiT 的条件，避免 RGB 渲染后的 V…
- **精读笔记**：[打开笔记](../notes/2026-11-03/2610.40614-l3g-world-real-time-infinite-world-generation-wi.md)

### 2. [Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence](http://arxiv.org/abs/2611.01677v1)

- **评分**：74/100
- **作者**：Zhenxin Zhu, Zhijian Huang, Cheng Chi et al.
- **方向**：World Models
- **一句话**：论文提出 Xiaomi Auto World Model 2.0，一个统一的流式因果世界模型，面向自动驾驶、机器人和通用视频生成。模型以 Wan2.2-5B 为基础，通过 VTA 分解视角与时间注意力，引入多视角 RoPE 和 Fused-PRoPE 处理可变视角及相机位姿，并以 VAE 潜空间拼接统一图像、动作、布局和场景上下文等条件。WorldRec…
- **精读笔记**：[打开笔记](../notes/2026-11-03/2611.01677-xiaomi-auto-world-model-2-0-causal-world-models.md)

### 3. [X-World 1.6: Building Controllable Virtual Cities with World Models](http://arxiv.org/abs/2611.00596v1)

- **评分**：72/100
- **作者**：XPeng,  :, Boyang Wang et al.
- **方向**：World Models
- **一句话**：X-World 1.6 是面向自动驾驶的可控多摄像机生成式世界模型和闭环模拟器。它在 X-World 1.0 基础上扩大并筛选驾驶数据，增强自车运动、交通参与者、道路几何、交通信号灯和道路标线控制，并利用点云、3D 高斯场景、参考图像等实现绝对静态场景控制。模型通过双向基础训练以及因果少步适配、Connected Self Forcing、长时域调优和奖励…
- **精读笔记**：[打开笔记](../notes/2026-11-03/2611.00596-x-world-1-6-building-controllable-virtual-cities.md)

## 快速浏览

### 1. [Learning-to-Memorize: Dynamic Context Management for Long-Horizon Autoregressive Video Generation](http://arxiv.org/abs/2611.01858v1)

- **评分**：72/100
- **作者**：Haowei Zhu, Qijie Wang, Jia Li et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video generation has achieved impressive results on short clips, yet generating long videos remains challenging due to error accumulation over extended horizons, wh…

### 2. [Wave Forcing: Towards Speed-of-Light Streaming Video Generation](http://arxiv.org/abs/2611.00859v1)

- **评分**：72/100
- **作者**：Yijie Jin, Yuxuan Liu, Jiajun Xu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Real-time long-video generation requires continuous output with consistent appearance and natural motion.

### 3. [Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation](http://arxiv.org/abs/2610.42031v1)

- **评分**：71/100
- **作者**：Jiahua Xu, Yijie Fang, Nannan Wang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video generation enables efficient inference through streaming prediction.

### 4. [When Does Latent Prediction Error Support Physical Surprise Claims in Video World Models?](http://arxiv.org/abs/2611.01815v1)

- **评分**：67/100
- **作者**：Anton Hristov, Aleksandar Slavov, Vasil Vasilev
- **方向**：World Models
- **一句话**：Prediction errors from video world models are often treated as physical surprise, but they can also reflect appearance, static content, motion, or ordinary prediction difficulty.

### 5. [TacMind: Benchmarking and Modeling Tactile Interaction States for Robotic Manipulation](http://arxiv.org/abs/2611.00455v1)

- **评分**：65/100
- **作者**：Jiaxin Shi, Zibin Wu, Yichi Zhang et al.
- **方向**：World Models
- **一句话**：Tactile sensing provides robots with direct observations of contact physics, local geometry, and interaction dynamics, making it a vital source of feedback for contact-rich manipu…

### 6. [SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts](http://arxiv.org/abs/2611.01600v1)

- **评分**：59/100
- **作者**：Amir Hossain Raj, Xuesu Xiao
- **方向**：World Models
- **一句话**：Robots manipulating in cluttered spaces must often plan from partial views where foreground objects occlude the target, surrounding geometry, and usable free space.

### 7. [OpenNWM: A Generalist Navigation World Model with Latent Action Pretraining](http://arxiv.org/abs/2611.01844v1)

- **评分**：58/100
- **作者**：Dujun Nie, Ruiqi Song, Zixuan Wang et al.
- **方向**：World Models
- **一句话**：Navigation world models predict future observations conditioned on navigation actions to support planning, but their generalization across real-world environments remains constrai…
