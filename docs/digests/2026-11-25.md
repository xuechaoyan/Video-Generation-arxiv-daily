# Generation Research Daily Digest

> 生成时间：2026-11-25T05:44:29+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [OmniPersist: Persistent Dynamic World Modeling via Coupled Panoramic Evolution](http://arxiv.org/abs/2611.32473v1)

- **评分**：81/100
- **作者**：Zhilu Zhang, Xiaoyu Liu, Wenxi Liu et al.
- **方向**：Video Generation, World Models
- **一句话**：论文针对摄像机转离后再返回时，世界模型中的动态物体容易突变、消失或运动不连续的问题，提出 OmniPersist。该方法在共享的视频扩散模型中联合生成高帧率透视视频和低帧率全景视频，使全景空间持续记录视野外实体的运动状态；GeoAnch 负责同步时刻的跨视图几何特征对齐，TemComp 负责利用邻近时间的特征弥补全景流的时间稀疏。方法无需辅助模型或初始全景…
- **精读笔记**：[打开笔记](../notes/2026-11-25/2611.32473-omnipersist-persistent-dynamic-world-modeling-vi.md)

### 2. [LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation](http://arxiv.org/abs/2611.30714v1)

- **评分**：78/100
- **作者**：Yuxuan Jiang, Zehua Chen, Yusheng Dai et al.
- **方向**：World Models
- **一句话**：LiveAudio 将离线双向视频到音频扩散模型转换为因果、自回归、实时流式生成器。模型采用因果音频 VAE、块因果 DiT、无前视的同步对齐视频条件和块级 KV 缓存，按块生成并立即播放音频。训练分为双向预训练、块因果微调、ODE 少步蒸馏和非对称 DMD 四个阶段，其中 DMD 使用双向教师恢复因果化造成的同步损失。VGGSound 实验显示，Live…
- **精读笔记**：[打开笔记](../notes/2026-11-25/2611.30714-liveaudio-from-bidirectional-to-autoregressive-d.md)

### 3. [A Mesh to Remember: Persistent Appearance for Interactive Video Worlds](http://arxiv.org/abs/2611.32445v1)

- **评分**：76/100
- **作者**：Joonghyuk Shin, Alex Trevithick, Katarína Tóthová et al.
- **方向**：World Models
- **一句话**：Video world models synthesize photorealistic observations in response to user actions but struggle to remain consistent over long interactions.
- **精读笔记**：待 Cursor 读完全文后写入 `docs/notes/`

## 快速浏览

### 1. [DraftKV: Protecting Persistent Worlds through Hierarchical Streaming Retrieval](http://arxiv.org/abs/2611.31944v1)

- **评分**：72/100
- **作者**：Xiaoling Zhou, Haopeng Li, Yufa Zhou et al.
- **方向**：Video Generation
- **一句话**：Interactive video world models enable action- and camera-controlled exploration, yet struggle to maintain consistent spatial geometry and appearance when revisiting previously exp…

### 2. [On-Policy Codec Distillation for Efficient All-in-One Video Generation](http://arxiv.org/abs/2611.31184v1)

- **评分**：71/100
- **作者**：Boyang Wang, Kevin Blackburn-Matzen, Oindrila Saha et al.
- **方向**：Video Generation
- **一句话**：Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended…

### 3. [Residual Guidance for Real-Time Interactive Video Generation](http://arxiv.org/abs/2611.32820v1)

- **评分**：68/100
- **作者**：NaHyeon Park, Kyeong-Hwan Moon, Youjin Jeon et al.
- **方向**：Efficient Video Diffusion
- **一句话**：Real-time interactive video generation allows users to change the prompt during generation to steer the evolving video.

### 4. [DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models](http://arxiv.org/abs/2611.32665v1)

- **评分**：67/100
- **作者**：Sichen Wu, Qian Sun, Mengfan Liu et al.
- **方向**：World Models
- **一句话**：Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled fu…

### 5. [Analyzing and Improving FlowMap Distillation of Autoregressive Video Models](http://arxiv.org/abs/2611.31164v1)

- **评分**：65/100
- **作者**：Yong-Hyun Park, Guande He, Joon Hyeok Kim et al.
- **方向**：Autoregressive and Streaming Video
- **一句话**：FlowMap distillation offers a natural route to few-step generative modeling by directly learning a teacher's denoising trajectories.

### 6. [DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation](http://arxiv.org/abs/2611.32654v1)

- **评分**：62/100
- **作者**：Hongjia Liu, Dacheng Zhou, Minghao Fu et al.
- **方向**：World Models
- **一句话**：Robot demonstrations provide more than actions to imitate: they reveal how actions change the world and how those changes contribute to task success.

### 7. [Interactive Neural Computers](http://arxiv.org/abs/2611.32811v1)

- **评分**：62/100
- **作者**：Ross Murphy, Marcel Hedman, Gabriel Brostow
- **方向**：World Models
- **一句话**：Computers and their interfaces are usually treated as fixed, so a person, or increasingly an AI agent, must adapt to whatever the operating system presents.
