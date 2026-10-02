# Generation Research Daily Digest

> 生成时间：2026-10-02T16:51:40+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LOCI: Spatial Linear Memory for Streaming World Models](http://arxiv.org/abs/2609.40222v1)

- **评分**：75/100
- **作者**：Ji Xia, Tingting Liao, Xuezhi Liang et al.
- **方向**：World Models
- **一句话**：论文研究摄像机控制视频世界模型在长时间间隔后返回旧场景时的空间记忆问题。作者指出，纯键值历史缓存能保留细节但内存随时长增长，纯循环状态虽节省内存却会丢失可直接检索的观测。LOCI在30层Wan视频Transformer中交错使用15个带Kimi Delta Attention和PRoPE相机几何条件的循环记忆模块，以及15个保留历史KV的Softmax模块…
- **精读笔记**：[打开笔记](../notes/2026-10-02/2609.40222-loci-spatial-linear-memory-for-streaming-world-m.md)

### 2. [Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](http://arxiv.org/abs/2609.40153v1)

- **评分**：73/100
- **作者**：Xiangyu Zhu, Jin Xu, Yue Guo et al.
- **方向**：Video Generation, World Models
- **一句话**：Video generation models (VGMs) offer strong spatiotemporal priors for embodied observation--action modeling.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

### 3. [Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](http://arxiv.org/abs/2609.40037v1)

- **评分**：72/100
- **作者**：Fangyu Lin, Xingtong Ge, Lunjie Zhu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：论文提出 Radian，用冻结视觉基础模型的多层特征对解码后的真实视频帧和生成帧进行对抗判别，并将该监督与基于学生自身自回归展开的 DMD 联合训练。该方法通过 ODE 初始化、DMD 稳定化与判别器校准、联合表示对抗蒸馏三个阶段，缓解误差在因果视频生成中的累积传播。实验基于 Wan2.1-1.3B，覆盖四步分块生成、单步逐帧生成和 60 秒长视频生成；结…
- **精读笔记**：[打开笔记](../notes/2026-10-02/2609.40037-enhancing-autoregressive-video-generation-via-re.md)

## 快速浏览

### 1. [FutureWorlds: Learning Robotic World Models from Alternative Futures](http://arxiv.org/abs/2610.01019v1)

- **评分**：70/100
- **作者**：Hao Wu, Shengju Qian, Weiyan Wang et al.
- **方向**：World Models
- **一句话**：Robotic world models predict action-conditioned future scenes, providing a foundation for understanding action outcomes.

### 2. [DashVMC: Real-Time Discrete World Model Control in Geometry Dash](http://arxiv.org/abs/2609.40003v1)

- **评分**：67/100
- **作者**：Florent Tariolle, Florian Yger
- **方向**：World Models
- **一句话**：World-model agents are usually evaluated in simulators that can wait for the policy; live games impose the opposite constraint, requiring capture, prediction, and action before th…

### 3. [JEPA-TTT: Persistent Test-Time Training of Latent World Models for Planning under Dynamics Shifts](http://arxiv.org/abs/2610.00722v1)

- **评分**：66/100
- **作者**：Zheyuan Zhang, Suyu Ye, Nakul Agarwal et al.
- **方向**：World Models
- **一句话**：World models enable agents to plan by predicting future states of the environment, but their predictions can become unreliable when test-time dynamics differ from those seen durin…

### 4. [SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2610.00686v1)

- **评分**：65/100
- **作者**：Mikhail Dereviannykh, Vikram Voleti, Simon Donne et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Recent video-based world models pair the scalability of autoregressive (AR) prediction with the visual quality of diffusion models.

### 5. [MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](http://arxiv.org/abs/2610.02153v1)

- **评分**：63/100
- **作者**：Yiwen Zhang, Haocheng Xi, Michael Tian-Yue Liu et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Long-horizon autoregressive video generation is limited by a finite context window.

### 6. [Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](http://arxiv.org/abs/2610.01092v1)

- **评分**：62/100
- **作者**：Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana et al.
- **方向**：Video Generation, World Models
- **一句话**：Video generation models are increasingly being explored as world simulators for embodied planning and learning.

### 7. [RoboCoach: World Models as Active Coaches for Compositional Robot Skills](http://arxiv.org/abs/2609.39685v1)

- **评分**：61/100
- **作者**：Jiajun Liu, Yifan Chen, Yichao Liu et al.
- **方向**：World Models
- **一句话**：Long-horizon robot manipulation reuses skills across many task compositions, but improving these compositions with additional end-to-end demonstrations is costly.
