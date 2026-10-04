# Generation Research Daily Digest

> 生成时间：2026-10-04T16:00:50+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LOCI: Spatial Linear Memory for Streaming World Models](http://arxiv.org/abs/2609.40222v1)

- **评分**：75/100
- **作者**：Ji Xia, Tingting Liao, Xuezhi Liang et al.
- **方向**：World Models
- **一句话**：本文研究摄像机控制视频世界模型在长时间离开后重新访问场景时的空间记忆问题。LOCI 将两种记忆结合起来：一方面，在部分 Transformer 层中保留历史观测的显式键值缓存，以直接访问视觉细节；另一方面，使用由摄像机投影几何条件化的循环线性注意力状态，压缩保存完整历史并帮助后续查询定位相关观测。模型采用块级因果生成、块级遗忘和可选的有界观测库，从而支持完…
- **精读笔记**：[打开笔记](../notes/2026-10-04/2609.40222-loci-spatial-linear-memory-for-streaming-world-m.md)

### 2. [Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](http://arxiv.org/abs/2609.40153v1)

- **评分**：73/100
- **作者**：Xiangyu Zhu, Jin Xu, Yue Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：Video generation models (VGMs) offer strong spatiotemporal priors for embodied observation--action modeling.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](http://arxiv.org/abs/2609.40037v1)

- **评分**：72/100
- **作者**：Fangyu Lin, Xingtong Ge, Lunjie Zhu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文提出 Radian，用冻结视觉基础模型的多层表示对解码后的真实帧和生成帧进行对抗判别，并将该监督与基于学生自回归展开的 DMD 联合训练。方法通过稀疏解码、局部时间邻域和轻量级判别器减少训练开销，训练后移除 VFM 与判别器，不增加推理成本。基于 Wan2.1-1.3B 的实验显示，Radian 在四步分块生成、一步逐帧生成和约一分钟长视频生成中改善了…
- **精读笔记**：[打开笔记](../notes/2026-10-04/2609.40037-enhancing-autoregressive-video-generation-via-re.md)

## 快速浏览

### 1. [FutureWorlds: Learning Robotic World Models from Alternative Futures](http://arxiv.org/abs/2610.01019v1)

- **评分**：70/100
- **作者**：Hao Wu, Shengju Qian, Weiyan Wang et al.
- **方向**：World Models
- **一句话**：Robotic world models predict action-conditioned future scenes, providing a foundation for understanding action outcomes.

### 2. [DashVMC: Real-Time Discrete World Model Control in Geometry Dash](http://arxiv.org/abs/2609.40003v1)

- **评分**：67/100
- **作者**：Florent Tariolle, Florian Yger
- **方向**：World Models
- **一句话**：World-model agents are usually evaluated in simulators that can wait for the policy; live games impose the opposite constraint, requiring capture, prediction, and action before th…

### 3. [JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts](http://arxiv.org/abs/2610.00722v1)

- **评分**：66/100
- **作者**：Zheyuan Zhang, Suyu Ye, Nakul Agarwal et al.
- **方向**：World Models
- **一句话**：World models enable agents to plan by predicting future states of the environment, but their predictions can become unreliable when test-time dynamics differ from those seen durin…

### 4. [SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.00686v1)

- **评分**：65/100
- **作者**：Mikhail Dereviannykh, Vikram Voleti, Simon Donne et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Recent video-based world models pair the scalability of autoregressive (AR) prediction with the visual quality of diffusion models.

### 5. [MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](http://arxiv.org/abs/2610.02153v1)

- **评分**：63/100
- **作者**：Yiwen Zhang, Haocheng Xi, Michael Tian-Yue Liu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Long-horizon autoregressive video generation is limited by a finite context window.

### 6. [Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](http://arxiv.org/abs/2610.01092v1)

- **评分**：62/100
- **作者**：Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana et al.
- **方向**：Video Generation, World Models
- **一句话**：Video generation models are increasingly being explored as world simulators for embodied planning and learning.

### 7. [RoboCoach: World Models as Active Coaches for Compositional Robot Skills](http://arxiv.org/abs/2609.39685v1)

- **评分**：61/100
- **作者**：Jiajun Liu, Yifan Chen, Yichao Liu et al.
- **方向**：World Models
- **一句话**：Long-horizon robot manipulation reuses skills across many task compositions, but improving these compositions with additional end-to-end demonstrations is costly.
