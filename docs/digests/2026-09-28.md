# Generation Research Daily Digest

> 生成时间：2026-09-28T18:47:45+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [DyMD: Preserving Interaction Dynamics through Distribution Matching Distillation in Few-Step Video World Models](http://arxiv.org/abs/2609.31349v1)

- **评分**：78/100
- **作者**：Haojun Xu, Jie Huang, Xin Lu et al.
- **方向**：Video Generation, World Models, Efficient Video Diffusion
- **一句话**：论文研究少步视频扩散蒸馏中交互动态丢失的问题，指出DMD的弱重新加噪会使教师后验锁定在近乎静止的轨迹附近，而运动较强的样本又更难被伪分数模型拟合。DyMD通过时间亲和度条件化的重新加噪采样和动态引导的伪分数跟踪，分别改进教师监督和评论器训练。将14B的PF-Wan教师蒸馏为四步1.3B学生后，DyMD在R-Bench、PAI-Bench-G和EZS-Ben…
- **精读笔记**：[打开笔记](../notes/2026-09-28/2609.31349-dymd-preserving-interaction-dynamics-through-dis.md)

### 2. [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](http://arxiv.org/abs/2609.26425v2)

- **评分**：76/100
- **作者**：Jiaqi Zhao, Xiaobin Hu, Bo Yin et al.
- **方向**：World Models
- **一句话**：论文发现，现有2比特KV缓存量化虽然在VBench上接近无损，却会引发视频时间闪烁、模糊和伪影，主要原因是Key量化扰动了注意力logits并改变了Query对历史时空Token的选择。为此提出无需训练、严格因果的QuantWM，通过QSAC按Query敏感性和残差量化难度选择Key质心，并通过PSAC沿主导Query子空间补偿剩余Key误差。五个视频生成…
- **精读笔记**：[打开笔记](../notes/2026-09-28/2609.26425-quantwm-temporally-consistent-2-bit-kv-cache-qua.md)

### 3. [HelloWorld: Towards Practical Applications of Generative Driving World Models](http://arxiv.org/abs/2609.28931v1)

- **评分**：76/100
- **作者**：Fan Lu, Hanshi Wang, Zijing Wang et al.
- **方向**：World Models
- **一句话**：Driving world models provide a promising route toward scalable counterfactual data generation and interactive simulation beyond recorded driving logs.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving](http://arxiv.org/abs/2609.26792v1)

- **评分**：75/100
- **作者**：Ziyang Leng, Sicheng Mo, Seth Z. Zhao et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to ma…

### 2. [ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](http://arxiv.org/abs/2609.28923v1)

- **评分**：74/100
- **作者**：Zichong Meng, Chongjian Ge, Chun-Hao P. Huang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Few-step autoregressive (AR) video diffusion enables low-latency streaming generation, but existing post-training methods predominantly rely on Distribution Matching Distillation…

### 3. [GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](http://arxiv.org/abs/2609.25652v1)

- **评分**：73/100
- **作者**：Zijun Lin, Zhiyang Deng, Yuzhe Wu et al.
- **方向**：World Models
- **一句话**：Recent game world models support realistic visual simulation and interactive gameplay based on player inputs.

### 4. [Where and When to Force: Routed Forcing for Streaming Avatars](http://arxiv.org/abs/2609.30963v1)

- **评分**：72/100
- **作者**：Zihan Su, Siwen Lu, Junhao Zhuang et al.
- **方向**：Video Generation
- **一句话**：Audio-driven streaming avatar generation requires real-time synthesis of speech-synchronized videos with dynamic and diverse motion.

### 5. [DeltaWAM: Delta World Action Models for Bimanual Manipulation](http://arxiv.org/abs/2609.28811v1)

- **评分**：68/100
- **作者**：Han Yan, Zishang Xiang, Haokai Jiang et al.
- **方向**：World Models
- **一句话**：World-action models (WAMs) transfer visual and motion priors from pretrained video generators to robot control by jointly modeling visual dynamics and actions.

### 6. [Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](http://arxiv.org/abs/2609.26458v1)

- **评分**：66/100
- **作者**：Zixun Fang, Yawen Shao, Kai Zhu et al.
- **方向**：Video Generation, World Models
- **一句话**：We introduce \textbf{CoDeR}, a new paradigm for world modeling.

### 7. [Streaming-WAM: Action-Conditioned World-Action Model for Asynchronous Robot Manipulation](http://arxiv.org/abs/2609.28927v1)

- **评分**：65/100
- **作者**：Xuyao Huang, Yixuan Wang, Zengyao Ye et al.
- **方向**：World Models
- **一句话**：World action models (WAMs) that use future visual prediction at inference time incur substantial generation costs.
