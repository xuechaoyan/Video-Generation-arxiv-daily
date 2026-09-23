# Generation Research Daily Digest

> 生成时间：2026-09-23T15:36:52+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](http://arxiv.org/abs/2609.26425v1)

- **评分**：76/100
- **作者**：Jiaqi Zhao, Xiaobin Hu, Bo Yin et al.
- **方向**：World Models
- **一句话**：论文研究视频生成和交互式世界模型中2比特KV缓存量化引起的隐性视觉退化。作者发现，Key量化虽然重建误差小于Value量化，却会通过扰动QKᵀ改变Query对历史时空Token的选择，造成时间闪烁、模糊和伪影。为此提出无需训练、严格因果的QuantWM：QSAC依据历史Query的通道敏感性和残差动态范围选择量化质心，PSAC则利用Query主子空间的低秩…
- **精读笔记**：[打开笔记](../notes/2026-09-23/2609.26425-quantwm-temporally-consistent-2-bit-kv-cache-qua.md)

### 2. [WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](http://arxiv.org/abs/2609.24984v1)

- **评分**：76/100
- **作者**：Wangbo Yu, Kunhao Liu, Wenbo Hu et al.
- **方向**：World Models
- **一句话**：本文提出 WorldCrafter，用于交互式长时视频生成和闭环场景探索。该方法将历史潜变量帧及其相机信息编码为隐式三维感知表示，再根据未来目标相机轨迹进行位姿引导的固定预算读出，并将所得记忆令牌与近期上下文共同输入相机条件自回归视频 DiT。通过最大视野覆盖的历史检索、记忆编码器与生成器联合优化，以及少步蒸馏，模型能够实现长时间、可控且实时的场景探索。实…
- **精读笔记**：[打开笔记](../notes/2026-09-23/2609.24984-worldcrafter-consistent-video-world-model-with-i.md)

### 3. [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](http://arxiv.org/abs/2609.26792v1)

- **评分**：75/100
- **作者**：Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：论文提出 DreamStream，将物理交通模拟器与自回归视频模型结合，用模拟器提供可控的交通布局和交互行为，再生成供端到端驾驶策略使用的真实感相机观测。其核心采用多阶段视频扩散蒸馏、交通布局引导、多样场景蒸馏，以及利用早期时间步潜变量作为 KV 缓存的长时域自回归生成。为从策略视角评价视觉保真度，论文提出 FDπ，通过比较真实与生成场景在多个端到端策略中…
- **精读笔记**：[打开笔记](../notes/2026-09-23/2609.26792-dreamstream-towards-policy-oriented-generative-s.md)

## 快速浏览

### 1. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](http://arxiv.org/abs/2609.17521v2)

- **评分**：75/100
- **作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang et al.
- **方向**：Video Generation
- **一句话**：Interactive control for video generation is moving from coarse prompts toward fine-grained, physically meaningful manipulation of dynamic scenes.

### 2. [CausalWM: Causal Chain-of-Thought Reasoning for Embodied World Model](http://arxiv.org/abs/2609.23184v2)

- **评分**：74/100
- **作者**：Ziming Xu, Shuang Liang, Ruobing Han et al.
- **方向**：World Models
- **一句话**：Embodied world models learn to predict future physical dynamics from visual observations and control signals, where physical knowledge is implicitly entangled within latent repres…

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

### 5. [ConsistWorld: Evidence Routing for Consistent Multi-Agent World Models](http://arxiv.org/abs/2609.22641v1)

- **评分**：71/100
- **作者**：Qianxun Xu, Xianfang Zeng, Xinyao Liao et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Autoregressive video world models enable temporally coherent generation for a single observer.

### 6. [Imagine-RL: Residual-Confidence-Guided Cross-Attention for World-Model-Augmented VLA Reinforcement Learning](http://arxiv.org/abs/2609.24033v1)

- **评分**：69/100
- **作者**：Kejia Hu, Wentong Zhai, Bo Zhao et al.
- **方向**：World Models
- **一句话**：Reliable action evaluation in contact-rich manipulation requires looking beyond the current observation to future visual and contact consequences.

### 7. [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](http://arxiv.org/abs/2609.26458v1)

- **评分**：66/100
- **作者**：Zixun Fang, Yawen Shao, Kai Zhu et al.
- **方向**：Video Generation, World Models
- **一句话**：We introduce \textbf{CoDeR}, a new paradigm for world modeling.
