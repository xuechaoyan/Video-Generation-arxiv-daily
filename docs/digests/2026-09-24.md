# Generation Research Daily Digest

> 生成时间：2026-09-24T15:58:20+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](http://arxiv.org/abs/2609.24984v1)

- **评分**：76/100
- **作者**：Wangbo Yu, Kunhao Liu, Wenbo Hu et al.
- **方向**：World Models
- **一句话**：WorldCrafter 是一种面向交互式场景探索的相机可控自回归视频世界模型。它使用从历史潜空间帧和相机参数中学习得到的隐式三维感知记忆，并通过目标相机轨迹引导的读出模块，将与当前视角相关的信息压缩为固定数量的记忆令牌，再与近期上下文共同输入视频 DiT。模型采用最大视场覆盖的历史帧检索、记忆编码器与生成器联合优化，以及少步蒸馏，实现了长时程闭环探索和实…
- **精读笔记**：[打开笔记](../notes/2026-09-24/2609.24984-worldcrafter-consistent-video-world-model-with-i.md)

### 2. [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](http://arxiv.org/abs/2609.26425v2)

- **评分**：76/100
- **作者**：Jiaqi Zhao, Xiaobin Hu, Bo Yin et al.
- **方向**：World Models
- **一句话**：论文研究视频生成和世界模型中2比特KV缓存量化造成的隐性视觉退化。作者发现，Key量化虽然重建误差小于Value量化，却会通过扰动QKᵀ改变时空token选择，造成闪烁、模糊和伪影。为此提出无需训练、严格因果的QuantWM：QSAC依据历史Query敏感性和残差量化难度选择Key质心，PSAC则在主导Query子空间中以低秩方式补偿剩余Key误差。五个视…
- **精读笔记**：[打开笔记](../notes/2026-09-24/2609.26425-quantwm-temporally-consistent-2-bit-kv-cache-qua.md)

### 3. [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](http://arxiv.org/abs/2609.26792v1)

- **评分**：75/100
- **作者**：Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：本文提出 DreamStream，将物理交通模拟器与自回归视频扩散模型结合，用模拟器中的交通布局和动态状态生成面向策略的视觉观测，从而支持端到端驾驶策略的长时域闭环评估。其三阶段蒸馏流程结合交通布局引导、多样场景蒸馏和自生成上下文训练，并利用早期时间步潜变量作为 KV 缓存以减轻长序列漂移。作者提出 FDπ，通过多个端到端驾驶策略实际使用的场景特征衡量仿真…
- **精读笔记**：[打开笔记](../notes/2026-09-24/2609.26792-dreamstream-towards-policy-oriented-generative-s.md)

## 快速浏览

### 1. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](http://arxiv.org/abs/2609.17521v2)

- **评分**：75/100
- **作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang et al.
- **方向**：Video Generation
- **一句话**：Interactive control for video generation is moving from coarse prompts toward fine-grained, physically meaningful manipulation of dynamic scenes.

### 2. [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](http://arxiv.org/abs/2609.25652v1)

- **评分**：73/100
- **作者**：Zijun Lin, Zhiyang Deng, Yuzhe Wu et al.
- **方向**：World Models
- **一句话**：Recent game world models support realistic visual simulation and interactive gameplay based on player inputs.

### 3. [Streaming Video Editing with Easy Adaptation](http://arxiv.org/abs/2609.24788v1)

- **评分**：72/100
- **作者**：Yujia Hu, Jiajun Li, Zihao He et al.
- **方向**：Video Generation
- **一句话**：In this paper, we propose SVEET, a framework that requires merely training on a pretrained bidirectional video diffusion model but supports high-quality streaming video editing in…

### 4. [Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning](http://arxiv.org/abs/2609.24033v1)

- **评分**：69/100
- **作者**：Kejia Hu, Wentong Zhai, Bo Zhao et al.
- **方向**：World Models
- **一句话**：Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences.

### 5. [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](http://arxiv.org/abs/2609.26458v1)

- **评分**：66/100
- **作者**：Zixun Fang, Yawen Shao, Kai Zhu et al.
- **方向**：Video Generation, World Models
- **一句话**：We introduce \textbf{CoDeR}, a new paradigm for world modeling.

### 6. [CrossDistill: Balancing Quality and Diversity via Trajectory-Level Hybrid Few-Step Distillation](http://arxiv.org/abs/2609.14725v2)

- **评分**：65/100
- **作者**：Yuxi Liu, Haoyu Li, Yixiang Cai et al.
- **方向**：Video Generation
- **一句话**：Few-step distillation accelerates diffusion models but must balance diversity and fidelity: trajectory-based distillation preserves mode coverage, while distribution matching shar…

### 7. [The Past Frames the Future: Memory for Autoregressive Video Generation](http://arxiv.org/abs/2609.28466v1)

- **评分**：65/100
- **作者**：Harold Haodong Chen, Rongjin Guo, Disen Lan et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Advances in generative models have improved video fidelity, enabling long-horizon generation, interactive world modeling, and evolving visual environments.
