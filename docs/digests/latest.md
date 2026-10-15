# Generation Research Daily Digest

> 生成时间：2026-10-15T15:48:43+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](http://arxiv.org/abs/2610.18289v1)

- **评分**：82/100
- **作者**：Ziyu Zhu, Zhaoxu Sun, Fan Jiang et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：论文指出，自回归视频扩散模型在长时间闭环生成中会因误差递归积累而产生视觉、运动、身份和动作一致性漂移，根源在于短训练窗口与长部署时域之间的监督差距。LongForcing 保留短时域教师强制和因果 ODE 蒸馏，仅将最终分布匹配阶段的教师扩展到更长时域，并直接监督学生自生成的连续轨迹。实验表明，延长监督时域可改善文生视频质量、长视频稳定性以及交互式世界模型…
- **精读笔记**：[打开笔记](../notes/2026-10-15/2610.18289-longforcing-scaling-temporal-manifold-matching-f.md)

### 2. [OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching](http://arxiv.org/abs/2610.17688v1)

- **评分**：75/100
- **作者**：Qihang Huang, Wenhui Huang, Collister Chua et al.
- **方向**：World Models
- **一句话**：论文提出 OccWAM，将稠密度量占用与连续自车轨迹置于同一个条件流匹配生成过程中。模型采用共享的三专家 Mixture-of-Transformers，使世界专家与动作专家在每一层双向交换信息。两阶段场景到自车流程先在固定场景坐标系中生成占用和绝对轨迹，再依据预测轨迹将占用重索引到未来自车坐标系，并联合细化占用与相邻运动增量。实验显示，该方法在 Benc…
- **精读笔记**：[打开笔记](../notes/2026-10-15/2610.17688-occwam-occupancy-world-action-models-with-joint.md)

### 3. [CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation](http://arxiv.org/abs/2610.17926v1)

- **评分**：75/100
- **作者**：Xiaoxue Wu, Xinyu Gao, Fang Yu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：CineMem 面向需要流式、长时域生成的自回归多镜头视频生成。作者先将双向视频模型适配为按块自回归生成的多镜头模型，并通过重采样历史上下文缓解训练与推理不一致造成的误差累积。注意力分析显示，历史令牌具有跨帧的语义聚类结构，而不同查询令牌和注意力头对历史记忆的偏好差异显著。基于此，CineMem 使用按相似度在线组织的聚类 KV 缓存，并让每个查询-注意力…
- **精读笔记**：[打开笔记](../notes/2026-10-15/2610.17926-cinemem-attention-aligned-fine-grained-memory-re.md)

## 快速浏览

### 1. [SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](http://arxiv.org/abs/2610.19327v1)

- **评分**：75/100
- **作者**：Zefan Yang, Zheyuan Zhang, Boris Maihe et al.
- **方向**：Video Generation, World Models
- **一句话**：Robotic ultrasound can standardize image acquisition and reduce operator workload and variability, but policy learning remains limited by the lack of realistic, controllable simul…

### 2. [Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](http://arxiv.org/abs/2610.20220v1)

- **评分**：75/100
- **作者**：Zhuobai Dong, Junchao Yi, Hu Jian Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：Autoregressive generation underlies real-time, causal video synthesis and is the backbone of video world models.

### 3. [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](http://arxiv.org/abs/2610.19201v1)

- **评分**：74/100
- **作者**：Henry Che, Xuanchi Ren, Sanja Fidler et al.
- **方向**：World Models
- **一句话**：We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors.

### 4. [LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts](http://arxiv.org/abs/2610.18873v1)

- **评分**：73/100
- **作者**：Wenxuan Guo, Yingping Liang, Zhaoguo Wang et al.
- **方向**：World Models
- **一句话**：Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment.

### 5. [H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression](http://arxiv.org/abs/2610.18125v1)

- **评分**：72/100
- **作者**：Or Ronai, Vladimir Kulikov, Tomer Michaeli
- **方向**：Autoregressive and Streaming Video
- **一句话**：Training-free diffusion-based compression methods repurpose the generative priors of a diffusion or a flow model to compress data without retraining them as task-specific codecs.

### 6. [GreenWAM: A World Foundation Model for Robotics](http://arxiv.org/abs/2610.18774v1)

- **评分**：69/100
- **作者**：Gennady Sidorov, Valerii Kornilov, Denis Grankin et al.
- **方向**：World Models
- **一句话**：A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions.

### 7. [SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation](http://arxiv.org/abs/2610.18135v1)

- **评分**：69/100
- **作者**：Yifei Yang, Zehua Fan, Zike Yan et al.
- **方向**：World Models
- **一句话**：World-model-based visual navigation enables action planning by predicting future states under candidate trajectories.
