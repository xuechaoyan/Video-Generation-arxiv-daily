# Generation Research Daily Digest

> 生成时间：2026-09-29T17:04:11+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldAttention: An Efficient Attention Architecture for Interactive Video World Models](http://arxiv.org/abs/2609.34606v1)

- **评分**：78/100
- **作者**：Zeyu Zhang, Jinyuan Mao, Dakai An et al.
- **方向**：World Models
- **一句话**：论文面向文本条件的交互式长视频世界模型，解决完整历史上下文带来的注意力计算和 KV 缓存内存开销问题。方法由分层 KV 缓存（HKV）和混合稀疏注意力（HSA）组成：HKV 将历史缓存分页并跨 GPU、CPU 和 NVMe 分层管理，通过提示级和页面级检索选择相关视觉记忆；HSA 以线性全局注意力建模长程依赖，并以头部自适应的块稀疏注意力保留局部细节。配合…
- **精读笔记**：[打开笔记](../notes/2026-09-29/2609.34606-worldattention-an-efficient-attention-architectu.md)

### 2. [WorldPlay2: Extending Real-Time Interactive World Models in Control and Horizon](http://arxiv.org/abs/2609.35560v1)

- **评分**：78/100
- **作者**：Haiyu Zhang, Wenqiang Sun, Tengfei Wang et al.
- **方向**：World Models
- **一句话**：Interactive world models require responding in real time to versatile controls and maintaining long-horizon consistency.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [Precise Editing and Flexible Referencing for Interactable Worlds](http://arxiv.org/abs/2609.34470v1)

- **评分**：72/100
- **作者**：Xinyao Liao, Xianfang Zeng, Zhu Liang et al.
- **方向**：World Models
- **一句话**：本文提出 EditWorld，将视频世界模型从以导航和探索为主扩展到支持持续、精确的世界编辑与参考图像注入。模型基于自回归视频生成，通过门控因果注意力处理随时间变化的编辑指令和参考图像，通过稀疏上下文限制长视频历史记忆的规模，并结合自回归/双向联合训练、退火式自重采样及少步蒸馏，提高条件跟随能力、长时域稳定性和生成效率。作者还利用导航与视频编辑数据合成带有…
- **精读笔记**：[打开笔记](../notes/2026-09-29/2609.34470-precise-editing-and-flexible-referencing-for-int.md)

## 快速浏览

### 1. [From Scores to Samples: Elastic Forcing for Autoregressive Video Generation](http://arxiv.org/abs/2609.35491v1)

- **评分**：70/100
- **作者**：Chi Zhang, Yueyi Liu, Haoyang Shi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generation commonly relies on Distribution Matching Distillation (DMD), requiring a bidirectional diffusion teacher and an online fake-score model.

### 2. [Learning to Act under Visual Interruptions with Vision-Language-Action Models](http://arxiv.org/abs/2609.35003v1)

- **评分**：70/100
- **作者**：Mingle Jiang, Rui Xu, Yunke Wang et al.
- **方向**：World Models
- **一句话**：Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, but they are typically developed and evaluated with all camera streams available…

### 3. [SLIP-VLA: Single-Step Latent Imagination for Policy Learning in Vision-Language-Action Models](http://arxiv.org/abs/2609.33575v1)

- **评分**：68/100
- **作者**：Tianfu Li, Haoxuan Xu, Wenbo Chen et al.
- **方向**：World Models
- **一句话**：Vision-Language-Action models are increasingly effective for robotic manipulation, yet most predict actions directly from current observations without explicitly modeling future s…

### 4. [CoDrive: Cross-Vehicle World-Consistent Video Generation with Precise Trajectory Control for Cooperative Driving](http://arxiv.org/abs/2609.34749v1)

- **评分**：63/100
- **作者**：Yu Meng, Baining Zhao, Junta Wu et al.
- **方向**：World Models
- **一句话**：Real-world driving is inherently multi-agent, yet most existing driving world models generate observations from a single ego vehicle.

### 5. [Beyond One-Step Accuracy: State-Affine Latent Transition for Reliable Visual Planning](http://arxiv.org/abs/2609.33595v1)

- **评分**：62/100
- **作者**：Boyuan Zhang, Yingjun Du, Xiantong Zhen et al.
- **方向**：World Models
- **一句话**：Joint-embedding world models enable visual planning by learning action-conditioned dynamics in latent space.

### 6. [OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](http://arxiv.org/abs/2609.35052v1)

- **评分**：61/100
- **作者**：Hao Wang, Tao Yu, Liuzhou Zhang et al.
- **方向**：World Models
- **一句话**：Video world models must preserve the visual state of the world over time, but existing evaluation protocols often rely on generated histories, video reference, or selected revisit…

### 7. [RoGSW4RLD: Feed-Forward 4D Gaussian Lifting for Robot World Model Rollouts](http://arxiv.org/abs/2609.35311v1)

- **评分**：60/100
- **作者**：Jin Hyun Kim, Min Young Kim, Soohwan Song et al.
- **方向**：World Models
- **一句话**：Action-conditioned video world models predict future robot interactions from multiple cameras, yet their outputs remain disparate video collections rather than a shared metric sce…
