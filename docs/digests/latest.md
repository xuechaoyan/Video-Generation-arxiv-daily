# Generation Research Daily Digest

> 生成时间：2026-10-06T17:26:48+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](http://arxiv.org/abs/2609.39096v2)

- **评分**：84/100
- **作者**：Zeqi Xiao, Qingle Liu, Kaiwen Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文针对自回归视频扩散中历史 KV 缓存持续增长、导致显存和注意力计算成本上升的问题，提出无需训练的 DeCoPrune。该方法利用中间干净预测与最终去噪结果之间的 token 级差异判断上下文冗余：差异较大的 token 被保留，差异较小的 token 被剪除，同时结合近期窗口、初始 sink、RoPE 时间位置重索引和可选的注意力头专门化。论文还构建了…
- **精读笔记**：[打开笔记](../notes/2026-10-06/2609.39096-decoprune-efficient-kv-cache-pruning-for-autoreg.md)

### 2. [DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation](http://arxiv.org/abs/2610.03543v1)

- **评分**：81/100
- **作者**：Jiahao Zhan, Yan Wang, Yongrui Ma et al.
- **方向**：Autoregressive and Streaming Video, Efficient Video Diffusion
- **一句话**：Streaming video generation has benefited from distribution matching distillation (DMD), which matches the joint distribution of video frames to a video teacher's approximation of…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](http://arxiv.org/abs/2610.03221v1)

- **评分**：77/100
- **作者**：Yutong Wang, Xingtong Ge, Enhuai Liu et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：Video creation spans text-to-video (T2V), image-to-video (I2V), and condition-based generation, yet video diffusion models remain costly because they repeatedly evaluate large bac…
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models](http://arxiv.org/abs/2610.06598v1)

- **评分**：76/100
- **作者**：Xiaodong Wang, Tianle Li, Chuanxin Song et al.
- **方向**：World Models
- **一句话**：Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos re…

### 2. [Custom Forcing: Training-Free Subject Customization for Autoregressive Video Generation](http://arxiv.org/abs/2610.02914v2)

- **评分**：74/100
- **作者**：Yunseung Ok, Hyunsoo Kim, Minseo Kim et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video models can generate minute-long videos in real time, but they produce generic subjects from text rather than specific subjects from user-provided images.

### 3. [HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models](http://arxiv.org/abs/2610.05739v1)

- **评分**：74/100
- **作者**：Zhuokun Chen, Feng Chen, Xi Lin et al.
- **方向**：World Models
- **一句话**：Long-horizon video world models require persistent memory to preserve scene consistency over extended rollouts.

### 4. [FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning](http://arxiv.org/abs/2610.05483v1)

- **评分**：73/100
- **作者**：R. Khorrambakht, Joseph Amigo, Félix Lebel et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：World--action models (WAMs) promise a unified model that predicts action-conditioned futures, generates feasible actions, and supports planning in imagination.

### 5. [In-Distribution Forcing for Long Video Generation at Test Time](http://arxiv.org/abs/2610.03120v1)

- **评分**：70/100
- **作者**：Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Modern autoregressive (AR) video diffusion models excel at short-horizon video generation, yet generating long videos remains challenging due to drifting, where colors and texture…

### 6. [RealtimeWAM: One-Step Asynchronous World Action Models](http://arxiv.org/abs/2610.06617v1)

- **评分**：66/100
- **作者**：Chengtao Lv, Jinyang Du, Shuyi Feng et al.
- **方向**：World Models
- **一句话**：World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction.

### 7. [EpiWorld: Grounding LLM Policy Agents in Epidemiological World Models](http://arxiv.org/abs/2610.02744v1)

- **评分**：64/100
- **作者**：Zeeshan Memon, Yiqi Su, Kai Shu et al.
- **方向**：World Models
- **一句话**：Epidemic intervention policies are textual artefacts that human decision-makers interpret, justify, and revise through natural language, making large language models a natural can…
