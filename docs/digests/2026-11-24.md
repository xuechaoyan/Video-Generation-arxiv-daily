# Generation Research Daily Digest

> 生成时间：2026-11-24T21:35:33+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation](http://arxiv.org/abs/2611.30714v1)

- **评分**：78/100
- **作者**：Yuxuan Jiang, Zehua Chen, Yusheng Dai et al.
- **方向**：World Models
- **一句话**：本文提出 LiveAudio，将离线双向视频到音频扩散模型逐步转换为可实时运行的自回归流式生成器。模型采用因果音频 VAE、块因果 DiT、同步对齐的视频条件和块级 KV 缓存，使音频能够随着视频到达逐块生成、解码和播放，且不使用未来视频信息。训练包含四个阶段：双向模型预训练、块因果微调、因果 ODE 蒸馏以及利用双向教师的非对称分布匹配蒸馏。前两阶段建立…
- **精读笔记**：[打开笔记](../notes/2026-11-24/2611.30714-liveaudio-from-bidirectional-to-autoregressive-d.md)

### 2. [Mass Forcing: On-Policy Mass-Aware Distillation for Autoregressive Video Generation](http://arxiv.org/abs/2611.29618v1)

- **评分**：75/100
- **作者**：Yiyu Li, Fei Wei, Yong Wang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **一句话**：本文研究少步自回归视频扩散蒸馏中的模式坍缩问题。作者发现，DMD 的反向 KL 目标会使学生模型逐渐偏向少数、尤其是静态的视频模式，且改进初始化只能暂时延缓动态性下降。Mass Forcing 从学生生成的共享前缀出发采样多个延续，通过教师与学生分数差的潜空间积分估计相对概率质量，并以此进行局部条件分数蒸馏和集合级 MMD 匹配。该方法在训练阶段保持模式覆…
- **精读笔记**：[打开笔记](../notes/2026-11-24/2611.29618-mass-forcing-on-policy-mass-aware-distillation-f.md)

### 3. [SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning](http://arxiv.org/abs/2611.27639v1)

- **评分**：73/100
- **作者**：Anqi Li, Kai Liu, Linghe Kong et al.
- **方向**：World Models
- **一句话**：本文研究冻结潜在世界模型在闭环规划中的滚动加速问题。作者指出，CEM 规划器最终只依据候选代价的排序选择精英样本，因此压缩的关键不是保持预测特征或代价数值不变，而是避免候选排序发生改变。通过在七个导航和操作任务上开展超过 80,000 个闭环回合的系统研究，论文发现空间标记选择本身收益有限，滚动的第一步对排序最关键，上下文帧对部分任务不可或缺但无需重复计算…
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
