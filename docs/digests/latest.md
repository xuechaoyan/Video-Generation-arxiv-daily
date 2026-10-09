# Generation Research Daily Digest

> 生成时间：2026-10-09T17:34:44+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [Connected Self Forcing: Beyond Local Learning in Video Autoregression](http://arxiv.org/abs/2610.12156v1)

- **评分**：76/100
- **作者**：Dongbin Zhang, Chaoda Zheng, Kangjie Chen et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文指出，Self Forcing 虽然通过模型自身生成的历史进行训练来缓解训练—推理不一致，但由于分离历史 KV 缓存，后续块的损失无法反向影响早期块的生成，形成跨块梯度缺口。Connected Self Forcing（CSF）通过 Shortcut Gradient Replay，使后续预测的梯度经历史 KV 状态回传至早期块的上下文写入和生成过程，…
- **精读笔记**：[打开笔记](../notes/2026-10-09/2610.12156-connected-self-forcing-beyond-local-learning-in.md)

### 2. [Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher](http://arxiv.org/abs/2610.11479v1)

- **评分**：75/100
- **作者**：Bowen Zheng, Zhiguang Liu, Jiarong Ou et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文研究因果视频扩散模型在教师强制训练与自回归推理之间的训练—推理差距。模型在训练时接触无误的真实历史，容易过度依赖历史来预测当前内容；推理时历史由模型自身生成，早期误差因此不断累积。作者提出条件残差预测（CRP），将模型分为不读取历史的History-Free分支和读取历史、仅预测残差的History-Conditioned分支，并通过停止梯度和隐状态融…
- **精读笔记**：[打开笔记](../notes/2026-10-09/2610.11479-conditional-residual-prediction-improving-autore.md)

### 3. [MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration](http://arxiv.org/abs/2610.10457v1)

- **评分**：72/100
- **作者**：Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：论文提出 MORCA，用于加速视频扩散模型的缓存调度。作者指出，现有方法依据单步缓存复用误差进行阈值决策，但单步误差不能可靠反映最终视频质量损失。MORCA 将缓存调度建模为带复用预算约束的有限时域 MDP，利用步骤误差信号、去噪潜变量特征和预算状态，预测更接近终端质量的缓存决策，并采用基于 IQL 的离线到在线强化学习进行训练。离线阶段从随机调度轨迹中学…
- **精读笔记**：[打开笔记](../notes/2026-10-09/2610.10457-morca-offline-to-online-reinforcement-learning-f.md)

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
