# Generation Research Daily Digest

> 生成时间：2026-10-15T01:56:29+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](http://arxiv.org/abs/2610.18289v1)

- **评分**：82/100
- **作者**：Ziyu Zhu, Zhaoxu Sun, Fan Jiang et al.
- **方向**：Video Generation, World Models, Autoregressive and Streaming Video
- **一句话**：论文分析了自回归视频扩散模型在超出训练时域进行闭环展开时产生漂移的原因，指出短窗口监督无法约束长轨迹中的跨窗口依赖和延迟失败。作者提出 LongForcing，在保留短时域教师强制与因果 ODE 蒸馏的基础上，使用扩展时域双向教师对学生较长的在策略自展开进行分布匹配。该方法不改变学生架构或推理成本，在文本到视频和交互式动作条件世界模型上均改善了视频质量、动…
- **精读笔记**：[打开笔记](../notes/2026-10-15/2610.18289-longforcing-scaling-temporal-manifold-matching-f.md)

### 2. [World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models](http://arxiv.org/abs/2610.17434v1)

- **评分**：76/100
- **作者**：Junyi Wu, Zekun Li, Chenhongyi Yang et al.
- **方向**：World Models
- **一句话**：论文研究视频世界模型在长时域交互中的场景持久性问题：当已观察区域离开有限上下文后，传统自回归模型会遗忘其内容，并在摄像机返回时重新生成不一致的场景。World-T3 将摄像机位姿映射为记忆键、将视觉隐藏表示作为值，并通过测试时训练把被逐出上下文的观测写入固定大小的快速权重记忆。针对平滑摄像机轨迹造成的键相关和冗余问题，作者采用在线递归最小二乘更新，以抑制已…
- **精读笔记**：[打开笔记](../notes/2026-10-15/2610.17434-world-t3-test-time-training-as-persistent-memory.md)

### 3. [Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration](http://arxiv.org/abs/2610.16545v1)

- **评分**：76/100
- **作者**：Jiyue Jiang, Zhiyu Huo, Yuhan Chen et al.
- **方向**：Video Generation, Efficient Video Diffusion
- **一句话**：本文提出 AlignCache，用于免训练加速视频扩散模型的特征缓存。该方法将去噪过程划分为早、中、晚三个阶段，使用阶段专属阈值、累计风险预算和缓存陈旧度上限进行路由；在触发精确计算时，通过比较反事实缓存草稿与真实 CFG 引导输出，在线校准阈值；同时利用带方向—幅度门控的动量残差外推和锚点引导的无条件校正，提高跳步预测质量。在 Wan2.1-1.3B、O…
- **精读笔记**：[打开笔记](../notes/2026-10-15/2610.16545-heuristics-are-not-enough-calibrated-and-correct.md)

## 快速浏览

### 1. [OccWAM: Occupancy World-Action Models with Joint Scene-to-Ego Flow Matching](http://arxiv.org/abs/2610.17688v1)

- **评分**：75/100
- **作者**：Qihang Huang, Wenhui Huang, Collister Chua et al.
- **方向**：World Models
- **一句话**：Occupancy world models provide a structured, metric representation of future driving scenes, making them a promising basis for end-to-end autonomous driving.

### 2. [CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation](http://arxiv.org/abs/2610.17926v1)

- **评分**：75/100
- **作者**：Xiaoxue Wu, Xinyu Gao, Fang Yu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive video generation relies on memory retrieval to model long-range dependencies.

### 3. [SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](http://arxiv.org/abs/2610.19327v1)

- **评分**：75/100
- **作者**：Zefan Yang, Zheyuan Zhang, Boris Maihe et al.
- **方向**：Video Generation, World Models
- **一句话**：Robotic ultrasound can standardize image acquisition and reduce operator workload and variability, but policy learning remains limited by the lack of realistic, controllable simul…

### 4. [Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors](http://arxiv.org/abs/2610.19201v1)

- **评分**：74/100
- **作者**：Henry Che, Xuanchi Ren, Sanja Fidler et al.
- **方向**：World Models
- **一句话**：We present LidarVerse, a real-time unified LiDAR world model for sensor simulation across tasks and sensors.

### 5. [LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts](http://arxiv.org/abs/2610.18873v1)

- **评分**：73/100
- **作者**：Wenxuan Guo, Yingping Liang, Zhaoguo Wang et al.
- **方向**：World Models
- **一句话**：Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment.

### 6. [H-DDCM: Hadamard Codebooks for Fast Generative Image and Video Compression](http://arxiv.org/abs/2610.18125v1)

- **评分**：72/100
- **作者**：Or Ronai, Vladimir Kulikov, Tomer Michaeli
- **方向**：Autoregressive and Streaming Video
- **一句话**：Training-free diffusion-based compression methods repurpose the generative priors of a diffusion or a flow model to compress data without retraining them as task-specific codecs.

### 7. [GreenWAM: A World Foundation Model for Robotics](http://arxiv.org/abs/2610.18774v1)

- **评分**：69/100
- **作者**：Gennady Sidorov, Valerii Kornilov, Denis Grankin et al.
- **方向**：World Models
- **一句话**：A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions.
