# Generation Research Daily Digest

> 生成时间：2026-10-16T01:46:35+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](http://arxiv.org/abs/2610.18289v1)

- **评分**：82/100
- **作者**：Ziyu Zhu, Zhaoxu Sun, Fan Jiang et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：论文指出，自回归视频扩散模型在长时域闭环生成中会因短时域训练与长时域部署之间的监督差距而逐步漂移，表现为画质下降、运动不一致、身份丢失和动作响应退化。LongForcing 保留短时域教师强制与因果 ODE 蒸馏，仅将最终分布匹配阶段的教师监督扩展到更长的学生自生成轨迹。理论分析说明，短窗口边缘分布无法确定长轨迹，而长轨迹匹配能够覆盖延迟失败。实验表明，该…
- **精读笔记**：[打开笔记](../notes/2026-10-16/2610.18289-longforcing-scaling-temporal-manifold-matching-f.md)

### 2. [SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](http://arxiv.org/abs/2610.19327v1)

- **评分**：75/100
- **作者**：Zefan Yang, Zheyuan Zhang, Boris Maihe et al.
- **方向**：Video Generation, World Models
- **一句话**：论文提出 SonoWorld，用于根据六自由度探头运动生成未来超声观测，从而构建面向机器人超声的交互式世界模型。模型先在约 690 万帧无标注的腹部、心脏和甲状腺临床超声视频上学习潜在动作和视频动态，再利用 42 名受试者的少量 EM 跟踪甲状腺扫描将动态对齐到实际探头位姿，最后通过自强制分布匹配蒸馏转换为支持流式长时域生成的因果模型。模型在原始轨迹、零运…
- **精读笔记**：[打开笔记](../notes/2026-10-16/2610.19327-sonoworld-towards-interactive-pose-controllable.md)

### 3. [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](http://arxiv.org/abs/2610.20220v1)

- **评分**：75/100
- **作者**：Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：论文研究如何以极少的PF-ODE轨迹监督，将双向视频扩散模型高效蒸馏为因果少步自回归生成器。作者发现，高噪声阶段主要负责布局与运动，低噪声阶段主要负责细节，二者的轨迹曲率和优化行为差异导致单一学生模型在单样本训练下发生表示干扰。为此，Glance Forcing采用双LoRA结构，将去噪过程分为负责语义和运动的Slow专家与负责纹理细节的Fast专家，并配…
- **精读笔记**：[打开笔记](../notes/2026-10-16/2610.20220-glance-forcing-making-bidirectional-diffusion-au.md)

## 快速浏览

### 1. [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](http://arxiv.org/abs/2610.19201v1)

- **评分**：74/100
- **作者**：Henry Che, Xuanchi Ren, Sanja Fidler et al.
- **方向**：World Models
- **一句话**：We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors.

### 2. [LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts](http://arxiv.org/abs/2610.18873v1)

- **评分**：73/100
- **作者**：Wenxuan Guo, Yingping Liang, Zhaoguo Wang et al.
- **方向**：World Models
- **一句话**：Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment.

### 3. [H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression](http://arxiv.org/abs/2610.18125v1)

- **评分**：72/100
- **作者**：Or Ronai, Vladimir Kulikov, Tomer Michaeli
- **方向**：Autoregressive and Streaming Video
- **一句话**：Training-free diffusion-based compression methods repurpose the generative priors of a diffusion or a flow model to compress data without retraining them as task-specific codecs.

### 4. [GreenWAM: A World Foundation Model for Robotics](http://arxiv.org/abs/2610.18774v1)

- **评分**：69/100
- **作者**：Gennady Sidorov, Valerii Kornilov, Denis Grankin et al.
- **方向**：World Models
- **一句话**：A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions.

### 5. [SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation](http://arxiv.org/abs/2610.18135v1)

- **评分**：69/100
- **作者**：Yifei Yang, Zehua Fan, Zike Yan et al.
- **方向**：World Models
- **一句话**：World-model-based visual navigation enables action planning by predicting future states under candidate trajectories.

### 6. [GAD: Geometry Attention Distillation for Consistent Video Generation](http://arxiv.org/abs/2610.18779v1)

- **评分**：68/100
- **作者**：Junfeng Ni, Ziyu Zhu, Fan Jiang et al.
- **方向**：Video Generation
- **一句话**：Video diffusion models generate visually compelling short-term sequences but often struggle to preserve scene geometry and object structure over time.

### 7. [StateCraft: Augmenting Video World Models with Abstract-State Reasoning](http://arxiv.org/abs/2610.19795v1)

- **评分**：66/100
- **作者**：Lorenzo Venturoli, Nedko Savov, Xi Wang et al.
- **方向**：Video Generation, World Models
- **一句话**：Video world models aim to simulate complex environments with realistic appearance and dynamics.
