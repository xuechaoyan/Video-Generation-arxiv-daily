# Generation Research Daily Digest

> 生成时间：2026-10-10T16:24:50+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Connected Self Forcing: Beyond Local Learning in Video Autoregression](http://arxiv.org/abs/2610.12156v1)

- **评分**：76/100
- **作者**：Dongbin Zhang, Chaoda Zheng, Kangjie Chen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文指出，Self Forcing虽然通过自生成历史进行训练来缓解训练—推理不一致，但因分离历史KV缓存而切断了后续块向早期块传递的梯度。Connected Self Forcing通过Shortcut Gradient Replay，在不保留完整自回归计算图的前提下恢复从后续预测到历史KV状态及早期生成过程的部分梯度，使每个块不仅为自身生成质量负责，也根…
- **精读笔记**：[打开笔记](../notes/2026-10-10/2610.12156-connected-self-forcing-beyond-local-learning-in.md)

### 2. [Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher](http://arxiv.org/abs/2610.11479v1)

- **评分**：75/100
- **作者**：Bowen Zheng, Zhiguang Liu, Jiarong Ou et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文研究因果视频扩散模型在自回归生成中的暴露偏差问题：教师强制训练使模型过度依赖真实历史，而推理时历史由模型自身生成，早期误差会逐步累积。作者提出条件残差预测（CRP），将模型拆为历史无关分支和历史条件残差分支，前者仅依据当前噪声输入和文本预测，后者利用历史信息补充必要残差，并通过停止梯度和隐空间融合避免历史分支污染无历史分支。同时，作者以逐帧独立编码的图…
- **精读笔记**：[打开笔记](../notes/2026-10-10/2610.11479-conditional-residual-prediction-improving-autore.md)

### 3. [MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration](http://arxiv.org/abs/2610.10457v1)

- **评分**：72/100
- **作者**：Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：本文研究视频扩散模型迭代去噪中的缓存加速问题。作者指出，现有方法依据局部步骤误差决定缓存复用，但该误差不能可靠预测最终视频质量损失；同时，阈值调度难以精确满足用户指定的加速比。MORCA将缓存调度建模为带复用预算约束的MDP，利用步骤误差信号、去噪潜变量特征和预算状态，进行面向终端误差的复用/重计算决策，并采用基于IQL的离线到在线强化学习训练调度器。针对…
- **精读笔记**：[打开笔记](../notes/2026-10-10/2610.10457-morca-offline-to-online-reinforcement-learning-f.md)

## 快速浏览

### 1. [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](http://arxiv.org/abs/2610.12368v1)

- **评分**：71/100
- **作者**：Linkai Liu, Yuntian Zhang, Zhenshan Bing et al.
- **方向**：World Models
- **一句话**：Direct visual navigation policies generate trajectories efficiently but do not explicitly evaluate their future consequences.

### 2. [UltraWorld: Learning Interactive Ultrasound World Models from Untracked Clinical Videos with Acoustic Sampling Map](http://arxiv.org/abs/2610.09785v1)

- **评分**：70/100
- **作者**：Keke Yang, Erqi Wang, Sainan Guan et al.
- **方向**：World Models
- **一句话**：World models can enable autonomous ultrasound scanning by predicting the outcomes of probe motions from local observations.

### 3. [WAM-Cache: Staleness-Bounded KV Reuse for Efficient World Action Models](http://arxiv.org/abs/2610.11401v1)

- **评分**：70/100
- **作者**：Kai Ding, Yang He, Ruijie Quan et al.
- **方向**：World Models
- **一句话**：World Action Models (WAMs) enable generalist robot manipulation by conditioning an action expert on representations from a pretrained video Diffusion Transformer (DiT).

### 4. [Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](http://arxiv.org/abs/2610.11756v1)

- **评分**：70/100
- **作者**：Jiaming Zhang, Xinyu Wang, Huafeng Shi et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion enables causal video streaming without a bidirectional pass over the full clip, but existing few-step systems usually retain only the opening and mo…

### 5. [Beyond Policy Support: Interaction Constrained Offline Reinforcement Learning for Autonomous Driving](http://arxiv.org/abs/2610.09763v1)

- **评分**：69/100
- **作者**：Mahmoud Selim, Cristina Cipriani, Karl Henrik Johansson
- **方向**：World Models
- **一句话**：Offline reinforcement learning enables reward-driven policy improvement from fixed datasets without requiring online exploration, making it particularly attractive in safety-criti…

### 6. [PlanWAM: Planning-Shaped Future Representations for End-to-End Autonomous Driving](http://arxiv.org/abs/2610.11382v1)

- **评分**：69/100
- **作者**：Jinchang Xu, Hongda Yu, Fengwei Dong et al.
- **方向**：World Models
- **一句话**：World models in end-to-end autonomous driving predict future scene evolution to provide foresight for trajectory planning.

### 7. [WorldGuide: Goal-Directed Video World Model for Procedural Task Execution](http://arxiv.org/abs/2610.12459v1)

- **评分**：65/100
- **作者**：Ankan Deria, Komal Kumar, Hisham Cholakkal et al.
- **方向**：World Models
- **一句话**：Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been…
