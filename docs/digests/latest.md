# Generation Research Daily Digest

> 生成时间：2026-10-07T17:59:35+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](http://arxiv.org/abs/2609.39096v2)

- **评分**：84/100
- **作者**：Zeqi Xiao, Qingle Liu, Kaiwen Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文针对自回归视频扩散在长时间生成中 KV 缓存持续膨胀、导致内存和注意力开销增加的问题，提出无需训练的 DeCoPrune。该方法比较生成轨迹中的中间干净预测与最终去噪结果，认为差异较大的令牌包含当前上下文尚未充分表达的重要视觉证据，因此保留这些令牌并剪除低差异令牌；同时结合近期窗口、初始 sink chunk 保护和 RoPE 时间位置重索引。论文还提…
- **精读笔记**：[打开笔记](../notes/2026-10-07/2609.39096-decoprune-efficient-kv-cache-pruning-for-autoreg.md)

### 2. [WorldSonus: Bringing Sound to Worlds](http://arxiv.org/abs/2610.08760v1)

- **评分**：82/100
- **作者**：Pengjun Fang, Jingyi Fa, Kam Man Wu et al.
- **方向**：World Models
- **一句话**：WorldSonus 是一个为交互式世界模型补充声音的模块化视频到音频系统。它以流式因果自回归扩散方式，每次生成100毫秒的48 kHz立体声音频，并通过有界5秒 Ring-KV缓存保持恒定的内存和计算开销。系统采用双时间尺度视觉条件：块级语义特征维持长程连续性，帧级特征帮助流匹配头进行精细的时空对齐；训练阶段的 ShiftNCE 则利用同步教师改善事件时…
- **精读笔记**：[打开笔记](../notes/2026-10-07/2610.08760-worldsonus-bringing-sound-to-worlds.md)

### 3. [SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models](http://arxiv.org/abs/2610.06598v1)

- **评分**：76/100
- **作者**：Xiaodong Wang, Tianle Li, Chuanxin Song et al.
- **方向**：World Models
- **一句话**：SimForcing 旨在利用仿真数据提升动作条件真实机器人视频预测。方法先用增强后的仿真轨迹训练仿真世界模型，再将其作为冻结教师和学生初始化，通过相邻潜变量差分的运动蒸馏，把仿真中的动作相关运动先验迁移到真实域，同时在仿真和真实视频上联合进行流匹配训练。为利用但不过度依赖不准确的仿真预测，模型在多个视频 Transformer 模块中注入带噪仿真潜变量，…
- **精读笔记**：[打开笔记](../notes/2026-10-07/2610.06598-simforcing-distilling-simulation-motion-priors-i.md)

## 快速浏览

### 1. [Custom Forcing: Training-Free Subject Customization for Autoregressive Video Generation](http://arxiv.org/abs/2610.02914v2)

- **评分**：74/100
- **作者**：Yunseung Ok, Hyunsoo Kim, Minseo Kim et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video models can generate minute-long videos in real time, but they produce generic subjects from text rather than specific subjects from user-provided images.

### 2. [CtrlCache: Accelerating Interactive Video World Models with Control-Aware Caching](http://arxiv.org/abs/2610.08777v1)

- **评分**：74/100
- **作者**：Shangye Song, Dong Gong, Hong Jia et al.
- **方向**：World Models
- **一句话**：Interactive video world models need to generate each video chunk efficiently while responding faithfully to user controls.

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

### 5. [World Models' Last Exam in Physics](http://arxiv.org/abs/2610.08791v1)

- **评分**：67/100
- **作者**：Mingju Gao, Qingle Liu, Yuzhao Peng et al.
- **方向**：Video Generation, World Models
- **一句话**：Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI syste…

### 6. [RealtimeWAM: One-Step Asynchronous World Action Models](http://arxiv.org/abs/2610.06617v1)

- **评分**：66/100
- **作者**：Chengtao Lv, Jinyang Du, Shuyi Feng et al.
- **方向**：World Models
- **一句话**：World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction.

### 7. [PWM: Personalized World Models with Online Reinforcement Learning](http://arxiv.org/abs/2610.04920v1)

- **评分**：62/100
- **作者**：Zhexin Lou, Guancheng Lu, Zeyu Zhang et al.
- **方向**：World Models
- **一句话**：Pretrained world models can generate diverse environments, yet users often want to explore a particular scene specified by their own video.
