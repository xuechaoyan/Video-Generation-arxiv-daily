# Generation Research Daily Digest

> 生成时间：2026-11-26T05:33:59+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions](http://arxiv.org/abs/2611.34730v1)

- **评分**：77/100
- **作者**：Ahmed Hatem, Caoliwen Wang, Robert Hoang et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：WorldInteract提出了一种面向多材料物理交互的可控流式视频生成框架。其核心思想是将材料行为与接触响应分离：生成器从无物体接触的视频中学习不同材料在速度变化后的运动方式，物理控制器则根据视觉语言模型估计的质量和恢复系数预测碰撞并计算速度增量，二者通过统一接口连接。模型采用三阶段训练，包括全注意力下的材料行为学习、结合场景记忆和物理图的因果状态传播，…
- **精读笔记**：[打开笔记](../notes/2026-11-26/2611.34730-worldinteract-controllable-streaming-video-gener.md)

### 2. [ShowNow: Fine-Grained Speculative Streaming for Responsive World Models](http://arxiv.org/abs/2611.34693v1)

- **评分**：76/100
- **作者**：Yiren Song, Guian Fang, Mike Zheng Shou
- **方向**：World Models
- **一句话**：ShowNow 面向需要连续视频生成和即时动作响应的交互式世界模型，提出“准备未来—选择—提交”的推测式流式机制。在播放当前内容时，系统根据同一已提交状态预先生成多个动作条件化的候选未来，用户输入到达后直接选择对应分支。方法采用单潜变量细粒度提交、匹配的多未来 ViZDoom 数据集、共享历史的树形注意力与缓存、分区注意力及融合提交。在单张 H100 上，…
- **精读笔记**：[打开笔记](../notes/2026-11-26/2611.34693-shownow-fine-grained-speculative-streaming-for-r.md)

### 3. [LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE](http://arxiv.org/abs/2611.34912v1)

- **评分**：74/100
- **作者**：Jiachen An, Sijie Zhao, Le Li et al.
- **方向**：Video Generation
- **一句话**：论文提出 LiveVAE，用因果窗口注意力替代视频 VAE 中计算昂贵的全局时空建模。作者通过有效感受野和扰动分析发现，预训练视频 VAE 的编码与解码主要依赖局部空间邻域和短时间邻域，因此采用固定大小的空间窗口及因果时间窗口，实现逐潜帧流式处理和有界 KV 缓存。三阶段蒸馏分别对齐编码器潜表示、解码器重建结果，并通过联合微调使两者协同工作，同时保持与原有…
- **精读笔记**：[打开笔记](../notes/2026-11-26/2611.34912-livevae-causal-window-attention-makes-efficient.md)

## 快速浏览

### 1. [Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation](http://arxiv.org/abs/2611.34907v1)

- **评分**：74/100
- **作者**：Shaoteng Liu, Shuai Yang, Wei Huang et al.
- **方向**：Autoregressive and Streaming Video, Efficient Video Diffusion
- **一句话**：Real-time autoregressive video generators stream minutes of video and accept new prompts on the fly, but struggle to keep people, objects, and places consistent over a long intera…

### 2. [Understanding Diffusion Acceleration: Methods, Trade-Offs, and Open Questions](http://arxiv.org/abs/2611.34056v1)

- **评分**：74/100
- **作者**：Xiaofeng Mao, Fu-yun Wang, Le Zhuo et al.
- **方向**：Video Generation
- **一句话**：Diffusion and flow-based generative models support high-quality image, audio, and video synthesis.

### 3. [VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors](http://arxiv.org/abs/2611.33591v1)

- **评分**：70/100
- **作者**：Ying Jiang, Donglai Xiang, Anita Hu et al.
- **方向**：Video Generation
- **一句话**：Long-horizon video generation is key to interactive world modeling, physical intelligence, and spatial reasoning, yet maintaining geometric consistency and accurate camera control…

### 4. [Residual Guidance for Real-Time Interactive Video Generation](http://arxiv.org/abs/2611.32820v1)

- **评分**：68/100
- **作者**：NaHyeon Park, Kyeong-Hwan Moon, Youjin Jeon et al.
- **方向**：Efficient Video Diffusion
- **一句话**：Real-time interactive video generation allows users to change the prompt during generation to steer the evolving video.

### 5. [DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models](http://arxiv.org/abs/2611.32665v2)

- **评分**：67/100
- **作者**：Sichen Wu, Qian Sun, Mengfan Liu et al.
- **方向**：World Models
- **一句话**：Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled fu…

### 6. [AnyCam: Anything Can Represent Camera for Video Generation](http://arxiv.org/abs/2611.34944v1)

- **评分**：62/100
- **作者**：Weijie Lyu, Zhixin Shu, Yuntian Ke et al.
- **方向**：Video Generation
- **一句话**：Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an…

### 7. [DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation](http://arxiv.org/abs/2611.32654v1)

- **评分**：62/100
- **作者**：Hongjia Liu, Dacheng Zhou, Minghao Fu et al.
- **方向**：World Models
- **一句话**：Robot demonstrations provide more than actions to imitate: they reveal how actions change the world and how those changes contribute to task success.
