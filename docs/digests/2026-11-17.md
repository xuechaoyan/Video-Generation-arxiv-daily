# Generation Research Daily Digest

> 生成时间：2026-11-17T05:18:48+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [SAFER: Navigating the Exploration-Exploitation Dilemma in World-Model-Based Planning for Autonomous Driving](http://arxiv.org/abs/2611.20107v1)

- **评分**：76/100
- **作者**：Yansong Qu, Zilin Huang, Zihao Sheng et al.
- **方向**：World Models
- **一句话**：论文研究依赖世界模型进行自动驾驶规划时的探索—利用两难：在训练数据覆盖范围内规划难以超越示范，超出范围后模型误差又会使规划器偏好错误动作。SAFER通过“阶段化失败并由专家标注”扩展离线覆盖范围，再用分块潜在世界模型预测候选动作序列的未来，并结合奖励、价值、持续性和碰撞风险进行MPPI规划。其风险头以累积安全事件为目标，并加入“更强制动不应增加风险预测”的…
- **精读笔记**：[打开笔记](../notes/2026-11-17/2611.20107-safer-navigating-the-exploration-exploitation-di.md)

## 快速浏览

### 1. [A Unified Control Framework, Mathematical Model, and Five-layer Closed-loop Case Study for Embodied Intelligence Control Systems](http://arxiv.org/abs/2611.19187v1)

- **评分**：66/100
- **作者**：Yiwei Zhou, Zhongcheng Lei, Xiaoran Dai et al.
- **方向**：World Models
- **一句话**：论文提出具身智能控制系统的五层统一架构：L4认知与任务、L3表示与学习、L2优化与推理、L1约束与接触、L0物理与动力学。作者认为，操作空间控制、全身控制、MPC、强化学习、主动推理以及扩散/流策略在更高层次上都可视为配置流形上的约束序贯决策，并可由确定性最优控制和概率推理两种数学语言描述，再通过控制即推理等方法连接。论文重点强调以约束优化实现工程统一，同…

### 2. [ActWorld-JEPA: Action-Conditioned JEPA World Models Meet Latent Planning for End-to-End Autonomous Driving](http://arxiv.org/abs/2611.16579v1)

- **评分**：65/100
- **作者**：Ziying Song, Shengkai Zhang, Caiyan Jia et al.
- **方向**：World Models
- **一句话**：本文提出 ActWorld-JEPA，用于端到端自动驾驶中的候选轨迹选择。方法首先通过规划条件 JEPA 将每条候选轨迹编码为全局和逐步意图，并递归预测其对应的未来潜表示；随后利用门控交叉注意力融合当前场景与候选未来，再通过关系残差重排序模块建模规划意图与预测未来之间的一致性和差异性，对基础规划分数进行带置信度的有界修正。实验表明，该方法在 NAVSIM…

### 3. [ResWAM: Learning What Changes, Not What Stays, for World-Action Models](http://arxiv.org/abs/2611.19559v1)

- **评分**：62/100
- **作者**：Chongyu Fan, Gaowen Liu, Ramana Rao Kompella et al.
- **方向**：Video Generation, World Models
- **一句话**：World-action models (WAMs) augment vision-language-action policies (VLAs) with future prediction so that the policy can anticipate how its actions will affect the physical world.

### 4. [TelePhysica: Agentic Reconstruction of Physically Interactive Scenes](http://arxiv.org/abs/2611.18078v1)

- **评分**：61/100
- **作者**：Ruiqi Shu, Xufeng Zhan, Yuanzhi Liang et al.
- **方向**：Video Generation
- **一句话**：Direct image-to-video diffusion models entangle pixel synthesis with implicit latent motion, precluding persistent 3D mechanical equilibrium, mid-rollout intervention, and counter…

### 5. [Cache or Denoise Less? Residual Reuse in a Flow-Matching World Action Model](http://arxiv.org/abs/2611.19709v1)

- **评分**：55/100
- **作者**：Abhinav Gupta, Nissan Pow
- **方向**：World Models
- **一句话**：Flow-matching robot policies generate each action chunk through repeated network evaluations, one per denoising step.

### 6. [CoCode-World: Shared 3D Proxy Representation for Multi-Player World Models](http://arxiv.org/abs/2611.15602v1)

- **评分**：53/100
- **作者**：Qirui Li, Xin Zhang, Yabo Chen et al.
- **方向**：World Models
- **一句话**：Multiplayer generative world models must produce observations that agree on shared entities despite different camera motions and occlusions.

### 7. [PoCoAttn: Position-Content Collaborative Sparse Attention for Fast and High-Fidelity Video Generation](http://arxiv.org/abs/2611.20307v1)

- **评分**：51/100
- **作者**：Jianwen Wu, Meiling Wang, Junkang Zhou et al.
- **方向**：Video Generation
- **一句话**：Video diffusion transformers rely on 3D full attention over tens of thousands of spatiotemporal tokens, and its quadratic cost dominates inference latency.

### 8. [JEPA4R: Embodied JEPA World Models with 4D Point Planning](http://arxiv.org/abs/2611.19771v1)

- **评分**：50/100
- **作者**：Jiarui Dong, Zhiheng Liang, Yanjun Li et al.
- **方向**：World Models
- **一句话**：Joint-embedding predictive architecture (JEPA) world models predict future embeddings instead of pixels and plan in latent space.

### 9. [GameWM: Toward Next-Generation Video Games with Interaction-Centric World Models](http://arxiv.org/abs/2611.19247v1)

- **评分**：49/100
- **作者**：Bing He, Runze Wang, Fei Zha et al.
- **方向**：World Models
- **一句话**：For more than half a century, video games have pursued better graphics, more natural interaction, and more engaging gameplay.
