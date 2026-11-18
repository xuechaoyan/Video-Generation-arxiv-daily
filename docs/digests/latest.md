# Generation Research Daily Digest

> 生成时间：2026-11-18T19:39:19+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Reference Forcing: Long Video Generation with Region-Guided Drift Correction](http://arxiv.org/abs/2611.21559v1)

- **评分**：80/100
- **作者**：Sheng Zhao, Haitian Zheng, Weikai Lin et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文针对自回归长视频生成中的主体和背景外观随时间漂移问题，提出Reference Forcing。该方法以初始视频块为稳定外观参考，通过教师模型中的区域掩码注意力学习主体和背景的对应关系，并将其蒸馏为无需外部模型的独立锚点注意力路径；同时利用学习到的锚点门控，对KV缓存中较早、已漂移的值进行匹配和校正。实验基于LongLive和Self-Forcing，在…
- **精读笔记**：[打开笔记](../notes/2026-11-18/2611.21559-reference-forcing-long-video-generation-with-reg.md)

### 2. [FastFrames: Video Generation at Interactive Latency](http://arxiv.org/abs/2611.23226v1)

- **评分**：79/100
- **作者**：Gene Chou, Guandao Yang, Fujun Luan et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文针对自回归视频扩散模型端到端响应速度过慢的问题，提出 FastFrames。作者通过延迟剖析发现，VAE 解码和 KV 缓存更新等非去噪操作是主要瓶颈，因此分别使用轻量级 ConvNeXt 像素解码器和 KV 修复网络替代原组件，并结合持久化缓存、分段注意力、算子融合、CUDA Graph 及上下文并行等系统优化。在 480p 条件下，1.3B 模型单…
- **精读笔记**：[打开笔记](../notes/2026-11-18/2611.23226-fastframes-video-generation-at-interactive-laten.md)

### 3. [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](http://arxiv.org/abs/2611.20107v1)

- **评分**：76/100
- **作者**：Yansong Qu, Zilin Huang, Zihao Sheng et al.
- **方向**：World Models
- **一句话**：论文研究依赖世界模型进行自动驾驶规划时的探索—利用困境：模型在训练数据覆盖范围内较可靠但难以超越数据，超出覆盖范围后又会因模型误差偏向错误的高估动作。SAFER通过三个环节缓解该问题。首先，在仿真中利用能力较弱的驾驶策略和脚本化可恢复扰动制造失败，并由专家为每个状态提供正确动作和值标签，使世界模型同时学习错误行为的后果和应采取的恢复动作。其次，构建带有分块…
- **精读笔记**：[打开笔记](../notes/2026-11-18/2611.20107-safer-navigating-the-exploration-exploitation-di.md)

## 快速浏览

### 1. [Inertial Video World Models](http://arxiv.org/abs/2611.22314v1)

- **评分**：76/100
- **作者**：Yuan Gao, Fan Xu, Yu Guo et al.
- **方向**：World Models
- **一句话**：The physical world has inertia: it evolves from what already exists rather than being recreated at every instant.

### 2. [Code World Model 2.0: Towards Infinite Controllable Video Generation](http://arxiv.org/abs/2611.22925v1)

- **评分**：75/100
- **作者**：Ruoyu Wang, Hao Zhong, Yanming Yang et al.
- **方向**：Video Generation, World Models
- **一句话**：Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interac…

### 3. [SciWorldBench: Do Video World Models Really Understand Scientific Experiments?](http://arxiv.org/abs/2611.20899v1)

- **评分**：74/100
- **作者**：Xue Yang, Haonan Cai, Xinyu Hang et al.
- **方向**：Video Generation, World Models
- **一句话**：While the ability of video generation models to accurately depict scientific phenomena has received growing attention, determining whether these models genuinely understand the un…

### 4. [MovieRoll: A Systematic Framework for Rolling Out Long-Form Videos](http://arxiv.org/abs/2611.21339v1)

- **评分**：72/100
- **作者**：Yunyang Ge, Weijie Kong, Ryan Xu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Streaming video generation must sustain quality beyond the training horizon while handling self-generated history and growing cache costs.

### 5. [LynnReal-Hand: Unlocking World Interaction with Hand Control](http://arxiv.org/abs/2611.21479v2)

- **评分**：72/100
- **作者**：Shaohao Rui, Chaoyang Zhang, Xiaofeng Mao et al.
- **方向**：World Models
- **一句话**：Interactive video world models enable exploration through text and camera controls, yet direct object interaction requires finer control.

### 6. [ScoutCache: Efficient Few-Step Autoregressive Video Diffusion via Conditional Readout and Selective Caching](http://arxiv.org/abs/2611.21038v2)

- **评分**：72/100
- **作者**：Hao Tan, Jinghui Qin, Xuming Hu
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive video diffusion enables efficient long video generation, but inference still incurs substantial computational costs from repeated denoising and KV cache op…

### 7. [Towards Data-Efficient, Real-Time World Models](http://arxiv.org/abs/2611.22497v1)

- **评分**：72/100
- **作者**：Raluca Stevenson, David Bignell, Jennifer C. White et al.
- **方向**：World Models
- **一句话**：State-of-the-art world models have been used to produce sequences of gameplay that accord with provided user-input actions.
