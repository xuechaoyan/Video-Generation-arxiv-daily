# Generation Research Daily Digest

> 生成时间：2026-10-01T17:32:28+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](http://arxiv.org/abs/2609.39096v1)

- **评分**：82/100
- **作者**：Zeqi Xiao, Qingle Liu, Kaiwen Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文针对自回归视频扩散中 KV 缓存随视频历史增长、导致显存和注意力开销不断上升的问题，提出无需训练的 DeCoPrune。方法利用中间干净预测与最终去噪结果之间的差异评估每个视频标记的重要性，保留高差异标记、剪除低差异标记，并结合近期窗口、RoPE 时间位置重索引和可选的注意力头专用策略来压缩历史缓存。论文还提出 CMBench，通过 58 个约一分钟的…
- **精读笔记**：[打开笔记](../notes/2026-10-01/2609.39096-decoprune-efficient-kv-cache-pruning-for-autoreg.md)

### 2. [LongLive-Plug: Once-for-All Distillation for Video Generation](http://arxiv.org/abs/2609.38154v1)

- **评分**：80/100
- **作者**：Shuai Yang, Luozhou Wang, Wei Huang et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：Video diffusion models are increasingly developed into specialized models for diverse downstream tasks, and this development often includes a distillation stage, for example to ac…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](http://arxiv.org/abs/2609.38059v1)

- **评分**：76/100
- **作者**：Shenghe Zheng, Wenbo Li, Jiyao Zhang et al.
- **方向**：Video Generation
- **一句话**：Real-world robot learning is constrained by the cost of collecting experience and evaluating candidate behaviors.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [LOCI: Spatial Linear Memory for Streaming World Models](http://arxiv.org/abs/2609.40222v1)

- **评分**：75/100
- **作者**：Ji Xia, Tingting Liao, Xuezhi Liang et al.
- **方向**：World Models
- **一句话**：When a camera revisits a previously observed region, a video world model should reproduce what was there before.

### 2. [HelixWorld: A Real-time Interactive Audio-Visual World Model](http://arxiv.org/abs/2609.38123v1)

- **评分**：74/100
- **作者**：Lei Ke, Jiahao Pan, Zeyue Tian et al.
- **方向**：World Models
- **一句话**：World simulation is inherently multisensory, demanding synchronized visual and acoustic dynamics in real time.

### 3. [In-Flight KV Cache with Clean Anchors for Faster Autoregressive Video Diffusion](http://arxiv.org/abs/2609.32540v2)

- **评分**：74/100
- **作者**：Yikai Wang, Xiao Han, Mengmeng Xu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video diffusion generates a long video by splitting the video into temporal chunks and generating chunk-by-chunk, each through a short sequence of denoisin…

### 4. [Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware](http://arxiv.org/abs/2609.37107v2)

- **评分**：73/100
- **作者**：Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn et al.
- **方向**：Video Generation, World Models
- **一句话**：We present Waypoint 1.5, a real-time diffusion world model for interactive video generation on consumer-grade hardware.

### 5. [Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](http://arxiv.org/abs/2609.40153v1)

- **评分**：73/100
- **作者**：Xiangyu Zhu, Jin Xu, Yue Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：Video generation models (VGMs) offer strong spatiotemporal priors for embodied observation--action modeling.

### 6. [Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](http://arxiv.org/abs/2609.40037v1)

- **评分**：72/100
- **作者**：Fangyu Lin, Xingtong Ge, Lunjie Zhu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video generation enables efficient streaming synthesis, but errors introduced in early temporal blocks are reused as context and can propagate through subs…

### 7. [FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon Video Generation](http://arxiv.org/abs/2609.38839v1)

- **评分**：72/100
- **作者**：Bo Yin, Xiaobin Hu, Jiaqi Zhao et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Long-horizon video generation requires models to effectively leverage an increasingly long generation history.
