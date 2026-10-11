# Generation Research Daily Digest

> 生成时间：2026-10-11T02:19:34+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Connected Self Forcing: Beyond Local Learning in Video Autoregression](http://arxiv.org/abs/2610.12156v1)

- **评分**：76/100
- **作者**：Dongbin Zhang, Chaoda Zheng, Kangjie Chen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文指出，Self Forcing虽然通过自生成历史训练来匹配推理分布，但因历史KV缓存被detach，后续块对早期块的反向监督会丢失。Connected Self Forcing通过Shortcut Gradient Replay重建从后续预测到历史KV状态及早期生成过程的跨块梯度，在不保留完整自回归计算图的前提下，以较低激活内存换取重计算。该方法结合D…
- **精读笔记**：[打开笔记](../notes/2026-10-11/2610.12156-connected-self-forcing-beyond-local-learning-in.md)

### 2. [Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher](http://arxiv.org/abs/2610.11479v1)

- **评分**：75/100
- **作者**：Bowen Zheng, Zhiguang Liu, Jiarong Ou et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文研究了因果视频扩散模型在教师强制训练与自回归推理之间的分布差异：模型在训练时看到正确历史，容易依赖历史中本可由当前输入预测的信息，导致推理时历史误差累积并造成质量下降。作者提出条件残差预测（CRP），将模型分为不使用历史的History-Free分支和仅预测历史相关残差的History-Conditioned分支，并结合停止梯度与隐状态融合；同时以逐帧…
- **精读笔记**：[打开笔记](../notes/2026-10-11/2610.11479-conditional-residual-prediction-improving-autore.md)

### 3. [MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration](http://arxiv.org/abs/2610.10457v1)

- **评分**：72/100
- **作者**：Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：论文提出 MORCA，用于加速视频扩散模型的缓存调度。作者指出，现有方法依据单步缓存复用误差进行阈值决策，但单步误差不能可靠反映最终视频质量损失；同时，阈值调度难以精确满足用户指定的加速比。MORCA 将调度建模为带复用预算的马尔可夫决策过程，引入当前及历史潜变量的紧凑特征，并采用离线到在线的隐式Q学习进行训练。该方法先利用随机轨迹离线初始化，再通过在线轨…
- **精读笔记**：[打开笔记](../notes/2026-10-11/2610.10457-morca-offline-to-online-reinforcement-learning-f.md)

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
