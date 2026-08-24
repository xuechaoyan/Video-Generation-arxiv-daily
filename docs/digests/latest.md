# Generation Research Daily Digest

> 生成时间：2026-08-24T07:52:55+00:00 · 筛选方式：规则评分（未配置模型 API Key）
> 建议先读“优先精读”，快速浏览只看摘要、方法图和主实验表。

## 优先精读

### 1. [Omni-LiveAvatar: Minute-Level Real-Time Streaming Joint Audio-Video Avatar Generation](http://arxiv.org/abs/2608.13602v2)

- **评分**：82/100
- **作者**：Lunjie Zhu, Xingtong Ge, Fangyu Lin et al.
- **方向**：Video Generation
- **摘要摘录**：Joint audio-video generative models serve as foundation for immersive and interactive digital-human generation.
- **核心贡献**：We present Omni-LiveAvatar, the first framework for minute-level, real-time streaming joint audio-video avatar generation.
- **与你课题的关系**：匹配研究线：efficient generation, streaming video；关键词：interactive, autoregressive, streaming, real-time, few-step, distillation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [DriveCache: Action-Aware Caching for Driving World Model Inference](http://arxiv.org/abs/2608.16354v1)

- **评分**：74/100
- **作者**：Jianchun Yang, Jian Liang, Xianda Guo et al.
- **方向**：Video Generation
- **摘要摘录**：Driving video generation models support autonomous-driving development by predicting controllable future scenes for simulation, planning evaluation, and offline data generation.
- **核心贡献**：We propose DriveCache, a training-free, action-aware controller that uses planned motion to allocate reuse across scenes and dynamic programming to place it across denoising steps under a calibrated response budget.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, driving, simulation, acceleration, cache, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](http://arxiv.org/abs/2608.10519v2)

- **评分**：73/100
- **作者**：Jongbeom Lee, Hyunwoo Yu, Jincheol Yang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **摘要摘录**：InfinityStar extends visual autoregressive generation to video through a sequence of image and clip pyramids.
- **核心贡献**：We introduce SparSTAR, a training-free block-sparse attention method tailored to this setting.
- **与你课题的关系**：匹配研究线：video generation, streaming video；关键词：autoregressive, sparse attention, video generation, text-to-video, image-to-video, video synthesis
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [Visko Orbis 1.0: A Live Model for Real-Time Interactive Long Video Generation](http://arxiv.org/abs/2607.26694v2)

- **评分**：72/100
- **作者**：Xiangbo Gao, Siyuan Yang, Ping He et al.
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：We present Visko Orbis 1.0, a Live Model for real-time, interactive long-video generation.
- **核心贡献**：We present Visko Orbis 1.0, a Live Model for real-time, interactive long-video generation.
- **与你课题的关系**：匹配研究线：video generation, streaming video；关键词：interactive, streaming, long video, real-time, video generation, text-to-video
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](http://arxiv.org/abs/2608.19556v1)

- **评分**：66/100
- **作者**：Yuanhao Ban, Jiaqi Feng, Hengguang Zhou et al.
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：Streaming autoregressive diffusion models enable real-time, long-horizon video generation, but their training objectives optimize local frame prediction rather than the geometry and dynamics of a coherent world: long rollouts accumulate geometric drift and degrade into static or unnatural motion.
- **核心贡献**：In this work, we propose Stream4D, which replaces the static critic with a feed-forward 4D reconstruction reward that explicitly models scene dynamics, allowing coherent motion to receive high consistency rewards.
- **与你课题的关系**：匹配研究线：streaming video, efficient generation；关键词：autoregressive, streaming, real-time, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](http://arxiv.org/abs/2608.18484v1)

- **评分**：63/100
- **作者**：Pardis Taghavi, Reza Langari, Gaurav Pandey
- **方向**：Video Generation, World Models
- **摘要摘录**：Training-free block-sparse attention can accelerate video transformers, but row-wise attention concentration does not by itself specify an executable sparse operator.
- **核心贡献**：We introduce SparsePR, which combines Response-Coupled Partitioning with Probe-Fitted Residual Reconstruction.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, sparse attention, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [DA-WAM: Decision-Aligned Future Latents for Driving World Models](http://arxiv.org/abs/2608.19085v2)

- **评分**：63/100
- **作者**：Ruiguo Zhong, Benshan Ma, Xiaolong Chen et al.
- **方向**：World Models
- **摘要摘录**：Anticipating how scenes evolve under ego actions is fundamental to safe autonomous driving, yet the full potential of world models for decision-making remains unrealized.
- **核心贡献**：To bridge this gap, we propose DA-WAM, a framework that unifies predictive representation learning, action-conditioned future modeling, and trajectory scoring under a single decision-making objective.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, driving
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [Hydra-0: Action Flow for Generalist World Modeling and Control](http://arxiv.org/abs/2608.18077v1)

- **评分**：63/100
- **作者**：Hongyu Li, Bowen Wen, Xinghao Zhu et al.
- **方向**：World Models
- **摘要摘录**：We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion.
- **核心贡献**：We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, action-conditioned, efficient
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms](http://arxiv.org/abs/2608.19661v1)

- **评分**：57/100
- **作者**：Markus Buchholz, Ignacio Carlucho, Yvan R. Petillot
- **方向**：World Models
- **摘要摘录**：Large language models can turn a natural-language mission into a sequence of robot actions, but they do not have a sense of physics: they cannot judge how long a command should run, or whether it will make the robot drift into an obstacle.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：world model；关键词：world model, closed-loop, driving
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model](http://arxiv.org/abs/2608.16143v1)

- **评分**：51/100
- **作者**：Kwan Yun, Serin Yoon, Sunjin Jung et al.
- **方向**：Video Generation
- **摘要摘录**：We present AnyTalk, a novel method for generating 3D speech animations for arbitrary characters without requiring any animation data.
- **核心贡献**：We present AnyTalk, a novel method for generating 3D speech animations for arbitrary characters without requiring any animation data.
- **与你课题的关系**：匹配研究线：video generation, efficient generation；关键词：real-time, video generation, video diffusion
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
