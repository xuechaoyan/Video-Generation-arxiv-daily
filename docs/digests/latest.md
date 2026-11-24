# Generation Research Daily Digest

> 生成时间：2026-11-24T07:09:45+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation](http://arxiv.org/abs/2611.30714v1)

- **评分**：78/100
- **作者**：Yuxuan Jiang, Zehua Chen, Yusheng Dai et al.
- **方向**：World Models
- **一句话**：本文研究实时流式视频到音频生成，目标是在视频持续到达时立即生成与画面内容和时间同步的声音。作者提出 LiveAudio，将一个离线双向视频到音频扩散模型逐步转换为自回归扩散生成器。模型采用因果音频 VAE、块因果 DiT、无前瞻的同步对齐视频条件以及已完成音频块的 KV 缓存，实现逐块生成和即时播放。训练分为四阶段：双向模型预训练、块因果微调、因果 ODE…
- **精读笔记**：[打开笔记](../notes/2026-11-24/2611.30714-liveaudio-from-bidirectional-to-autoregressive-d.md)

### 2. [Mass Forcing: On-Policy Mass-Aware Distillation for Autoregressive Video Generation](http://arxiv.org/abs/2611.29618v1)

- **评分**：75/100
- **作者**：Yiyu Li, Fei Wei, Yong Wang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：论文指出，少步自回归视频模型采用基于学生样本的反向KL蒸馏时，会在持续训练中逐渐偏向少数、近乎静态的模式；改进初始化只能延缓这一问题。Mass Forcing在学生生成的同一前缀后采样多个延续，通过教师与学生分数差异的潜空间积分估计相对概率质量，并以此进行局部条件分数重加权和基于MMD的轨迹集合匹配。该方法在MovieGen和VBench上提升了整体质量与…
- **精读笔记**：[打开笔记](../notes/2026-11-24/2611.29618-mass-forcing-on-policy-mass-aware-distillation-f.md)

### 3. [SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning](http://arxiv.org/abs/2611.27639v1)

- **评分**：73/100
- **作者**：Anqi Li, Kai Liu, Linghe Kong et al.
- **方向**：World Models
- **一句话**：论文研究冻结潜在世界模型中的规划加速问题。基于交叉熵方法的规划器需要对大量候选动作序列进行自回归滚动预测，但规划器实际只关心候选代价的排序，而不要求特征或代价数值本身完全重建。作者沿空间位置、上下文帧、滚动时间步和预测器深度四个维度进行超过 80,000 个闭环回合的系统分析，发现空间标记选择存在较低上限，第一步对后续排序最关键，上下文帧在部分操作任务中不…
- **精读笔记**：[打开笔记](../notes/2026-11-24/2611.27639-soar-training-free-rank-consistent-rollout-compr.md)

## 快速浏览

### 1. [Draft Forcing: Target-guided Speculative Drafting and Learned Verifier for Autoregressive Video Generation](http://arxiv.org/abs/2611.30328v1)

- **评分**：73/100
- **作者**：Chenkai Xu, Yuji Ren, Zihui Liu et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：Autoregressive video diffusion models enable streaming synthesis chunk by chunk, yet invoking the large model for every chunk remains costly.

### 2. [On-Policy Codec Distillation for Efficient All-in-One Video Generation](http://arxiv.org/abs/2611.31184v1)

- **评分**：71/100
- **作者**：Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.
- **方向**：Video Generation
- **一句话**：Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended…

### 3. [Plan Big, Paint Small: Semantic-Aware Computation Allocation for Efficient Autoregressive Video Generation](http://arxiv.org/abs/2611.28402v1)

- **评分**：70/100
- **作者**：Yixuan Luo, Yanjing Li
- **方向**：Autoregressive and Streaming Video
- **一句话**：Autoregressive (AR) video diffusion streams a video chunk by chunk, but large AR models are too slow for real-time use.

### 4. [AxE: Benchmarking Agent-Environment Generalization of Video World Models via Grounded Events](http://arxiv.org/abs/2611.30120v1)

- **评分**：66/100
- **作者**：Haiyu Xu, Yiyang Chen, Jiayi Zhou et al.
- **方向**：World Models
- **一句话**：Edge cases are not the long tail; they are the norm.

### 5. [Analyzing and Improving FlowMap Distillation of Autoregressive Video Models](http://arxiv.org/abs/2611.31164v1)

- **评分**：65/100
- **作者**：Yong-Hyun Park, Guande He, Joon Hyeok Kim et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：FlowMap distillation offers a natural route to few-step generative modeling by directly learning a teacher's denoising trajectories.

### 6. [Efficient VLA Reinforcement Learning via Subchunk Rollouts in Latent World Models](http://arxiv.org/abs/2611.27645v1)

- **评分**：64/100
- **作者**：Nan Tang, Han-Tao Zhang, Jing-Cheng Pang et al.
- **方向**：World Models
- **一句话**：Model-based reinforcement learning (MBRL) can improve pretrained vision-language-action (VLA) policies through imagined experiences.

### 7. [FlexVSR: Continuous-Scale Super-Resolution for Streaming Video Generation](http://arxiv.org/abs/2611.26178v2)

- **评分**：63/100
- **作者**：Ji Wang, Haonan An, Jiasheng Zhang et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：Real-time streaming video generation has gained rapid momentum in live content creation and interactive media.
