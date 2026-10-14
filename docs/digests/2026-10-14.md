# Generation Research Daily Digest

> 生成时间：2026-10-14T16:00:32+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](http://arxiv.org/abs/2610.18289v1)

- **评分**：82/100
- **作者**：Ziyu Zhu, Zhaoxu Sun, Fan Jiang et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：论文指出，自回归视频扩散模型在长时间闭环生成中会因误差递归累积而发生视觉、运动、身份和动作一致性漂移，根本原因是短时域训练与长时域部署之间存在监督时域差距。LongForcing 保留短时域教师强制和因果 ODE 蒸馏，仅在分布匹配阶段引入扩展时域双向教师，对学生更长的自生成轨迹进行在策略监督。实验表明，该方法在文本到视频和动作条件交互式世界模型上均能改善…
- **精读笔记**：[打开笔记](../notes/2026-10-14/2610.18289-longforcing-scaling-temporal-manifold-matching-f.md)

### 2. [TempoKV: Predictive KV Cache Quantization for Autoregressive Video Generation](http://arxiv.org/abs/2610.15324v1)

- **评分**：79/100
- **作者**：Jiahui Hu, Weile Mo, Peiliang Cai et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文针对自回归视频扩散模型中随视频长度线性增长的 KV 缓存内存瓶颈，提出无需训练的 TempoKV 预测式量化方法。作者发现，键可由同一空间位置的历史键较好预测，而值主要依赖当前对齐的键，并辅以短值历史。因此，TempoKV分别预测键和值，只量化预测残差，并为键分配更高精度；预测器通过少量 BF16 轨迹离线线性回归校准。Self-Forcing、Cau…
- **精读笔记**：[打开笔记](../notes/2026-10-14/2610.15324-tempokv-predictive-kv-cache-quantization-for-aut.md)

### 3. [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](http://arxiv.org/abs/2610.17434v1)

- **评分**：76/100
- **作者**：Junyi Wu, Zekun Li, Chenhongyi Yang et al.
- **方向**：World Models
- **一句话**：World-T3 面向需要长期保持场景一致性的相机控制视频世界模型。它在有限的局部上下文之外，引入基于测试时训练的持久参数记忆：将被上下文淘汰的视频块编码为相机位姿—视觉内容键值对，并通过递归最小二乘更新快速权重；生成时再根据目标相机位姿检索历史场景特征。作者从预训练视频扩散模型出发，依次进行双向相机条件训练、自回归块因果训练与 TTT 记忆学习，最后通过…
- **精读笔记**：[打开笔记](../notes/2026-10-14/2610.17434-world-t3-test-time-training-as-persistent-memory.md)

## 快速浏览

### 1. [Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration](http://arxiv.org/abs/2610.16545v1)

- **评分**：76/100
- **作者**：Jiyue Jiang, Zhiyu Huo, Yuhan Chen et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：Feature caching has become a mainstream training-free strategy for accelerating video diffusion models by reusing intermediate outputs across denoising steps.

### 2. [OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching](http://arxiv.org/abs/2610.17688v1)

- **评分**：75/100
- **作者**：Qihang Huang, Wenhui Huang, Collister Chua et al.
- **方向**：World Models
- **一句话**：Occupancy world models provide a structured, metric representation of future driving scenes, making them a promising basis for end-to-end autonomous driving.

### 3. [CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation](http://arxiv.org/abs/2610.17926v1)

- **评分**：75/100
- **作者**：Xiaoxue Wu, Xinyu Gao, Fang Yu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video generation relies on memory retrieval to model long-range dependencies.

### 4. [LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts](http://arxiv.org/abs/2610.18873v1)

- **评分**：73/100
- **作者**：Wenxuan Guo, Yingping Liang, Zhaoguo Wang et al.
- **方向**：World Models
- **一句话**：Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment.

### 5. [H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression](http://arxiv.org/abs/2610.18125v1)

- **评分**：72/100
- **作者**：Or Ronai, Vladimir Kulikov, Tomer Michaeli
- **方向**：Autoregressive and Streaming Video
- **一句话**：Training-free diffusion-based compression methods repurpose the generative priors of a diffusion or a flow model to compress data without retraining them as task-specific codecs.

### 6. [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](http://arxiv.org/abs/2610.11756v2)

- **评分**：70/100
- **作者**：Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion enables causal video streaming without a bidirectional pass over the full clip, but existing few-step systems usually retain only the opening and mo…

### 7. [Frequency-Step Cache: Separating Synchronization and Repair for Efficient Autoregressive Video Diffusion](http://arxiv.org/abs/2610.15922v1)

- **评分**：70/100
- **作者**：Kerry Xu, Param Misra, Zachary Stenglein et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video generation enables long-horizon synthesis but requires repeated forward passes through large diffusion transformers.
