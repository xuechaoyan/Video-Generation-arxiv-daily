# Generation Research Daily Digest

> 生成时间：2026-09-27T15:50:49+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](http://arxiv.org/abs/2609.24984v1)

- **评分**：76/100
- **作者**：Wangbo Yu, Kunhao Liu, Wenbo Hu et al.
- **方向**：World Models
- **一句话**：WorldCrafter 是一种面向交互式探索的相机可控自回归视频世界模型。它使用从预训练多视角三维表示初始化的记忆编码器，将历史潜变量帧及其相机姿态压缩为隐式三维感知表示，再通过姿态引导的读出模块提取与未来相机轨迹相关的固定数量记忆令牌，并与近期上下文共同输入视频 DiT。系统采用最大视野覆盖的历史帧检索、联合优化和少步蒸馏，实现了长时闭环探索与实时流式…
- **精读笔记**：[打开笔记](../notes/2026-09-27/2609.24984-worldcrafter-consistent-video-world-model-with-i.md)

### 2. [HelloWorld: Towards Practical Applications of Generative Driving World Models](http://arxiv.org/abs/2609.28931v1)

- **评分**：76/100
- **作者**：Fan Lu, Hanshi Wang, Zijing Wang et al.
- **方向**：World Models
- **一句话**：Driving world models provide a promising route toward scalable counterfactual data generation and interactive simulation beyond recorded driving logs.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](http://arxiv.org/abs/2609.26425v2)

- **评分**：76/100
- **作者**：Jiaqi Zhao, Xiaobin Hu, Bo Yin et al.
- **方向**：World Models
- **一句话**：论文发现，现有 2 比特 KV 缓存量化虽然在 VBench 上接近无损，却会引发视频时间闪烁、模糊和伪影，主要原因是 Key 量化扰动了注意力 logits，导致 Query 选择不同的历史时空 token。为此，QuantWM 采用 QSAC 根据 Query 通道敏感性和残差量化难度选择 Key 聚类中心，并采用 PSAC 沿主导 Query 子空间…
- **精读笔记**：[打开笔记](../notes/2026-09-27/2609.26425-quantwm-temporally-consistent-2-bit-kv-cache-qua.md)

## 快速浏览

### 1. [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](http://arxiv.org/abs/2609.26792v1)

- **评分**：75/100
- **作者**：Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to ma…

### 2. [ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](http://arxiv.org/abs/2609.28923v1)

- **评分**：74/100
- **作者**：Zichong Meng, Chongjian Ge, Chun-Hao P. Huang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive (AR) video diffusion enables low-latency streaming generation, but existing post-training methods predominantly rely on Distribution Matching Distillation…

### 3. [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](http://arxiv.org/abs/2609.25652v1)

- **评分**：73/100
- **作者**：Zijun Lin, Zhiyang Deng, Yuzhe Wu et al.
- **方向**：World Models
- **一句话**：Recent game world models support realistic visual simulation and interactive gameplay based on player inputs.

### 4. [Streaming Video Editing with Easy Adaptation](http://arxiv.org/abs/2609.24788v1)

- **评分**：72/100
- **作者**：Yujia Hu, Jiajun Li, Zihao He et al.
- **方向**：Video Generation
- **一句话**：In this paper, we propose SVEET, a framework that requires merely training on a pretrained bidirectional video diffusion model but supports high-quality streaming video editing in…

### 5. [Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning](http://arxiv.org/abs/2609.24033v1)

- **评分**：69/100
- **作者**：Kejia Hu, Wentong Zhai, Bo Zhao et al.
- **方向**：World Models
- **一句话**：Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences.

### 6. [DeltaWAM: Delta World Action Models for Bimanual Manipulation](http://arxiv.org/abs/2609.28811v1)

- **评分**：68/100
- **作者**：Han Yan, Zishang Xiang, Haokai Jiang et al.
- **方向**：World Models
- **一句话**：World-action models (WAMs) transfer visual and motion priors from pretrained video generators to robot control by jointly modeling visual dynamics and actions.

### 7. [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](http://arxiv.org/abs/2609.26458v1)

- **评分**：66/100
- **作者**：Zixun Fang, Yawen Shao, Kai Zhu et al.
- **方向**：Video Generation, World Models
- **一句话**：We introduce \textbf{CoDeR}, a new paradigm for world modeling.
