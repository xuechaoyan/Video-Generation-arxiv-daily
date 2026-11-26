# Generation Research Daily Digest

> 生成时间：2026-11-26T20:35:20+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions](http://arxiv.org/abs/2611.34730v1)

- **评分**：77/100
- **作者**：Ahmed Hatem, Caoliwen Wang, Robert Hoang et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：WorldInteract 提出一种面向多材料物理交互的可控流式视频生成框架。其核心是将材料自身在速度变化下的行为学习，与物体接触时的动量交换计算分离：生成器从3万个无物体间接触的视频中学习22类材料的运动规律，物理控制器则根据视觉语言模型估计的质量和恢复系数预测接触并生成速度增量，再由因果视频生成器执行。框架结合场景记忆、目标跟踪、深度信息和物理图来支持…
- **精读笔记**：[打开笔记](../notes/2026-11-26/2611.34730-worldinteract-controllable-streaming-video-gener.md)

### 2. [ShowNow: Fine-Grained Speculative Streaming for Responsive World Models](http://arxiv.org/abs/2611.34693v1)

- **评分**：76/100
- **作者**：Yiren Song, Guian Fang, Mike Zheng Shou
- **方向**：World Models
- **一句话**：本文提出 ShowNow，用于降低动作条件视频世界模型的交互延迟。它在视频播放期间提前生成一至八种可能动作对应的未来，并在用户输入到达时选择匹配分支继续生成；单潜变量提交缩短了动作决策间隔，共享历史树式注意力、缓存复用和融合提交则降低了多分支推理成本。基于 SolarWM/Wan2.2 5B、匹配多未来 ViZDoom 数据集、AnyFlow 蒸馏和 Se…
- **精读笔记**：[打开笔记](../notes/2026-11-26/2611.34693-shownow-fine-grained-speculative-streaming-for-r.md)

### 3. [LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE](http://arxiv.org/abs/2611.34912v1)

- **评分**：74/100
- **作者**：Jiachen An, Sijie Zhao, Le Li et al.
- **方向**：Video Generation
- **一句话**：本文针对实时视频生成、流式编辑中视频 VAE 编码和解码延迟高的问题，分析发现预训练视频 VAE 的有效依赖主要集中在局部空间邻域和短期时间邻域。作者提出 LiveVAE，以因果窗口注意力构建流式编码器和解码器，通过固定大小的空间窗口与短时间窗口降低计算量，并使用有界 KV 缓存支持持续处理。三阶段蒸馏先分别对齐编码器和解码器，再进行联合微调，从而保持原有…
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

### 6. [DexWAC: A Unified World-Actor-Critic Model for Dexterous Robot Manipulation](http://arxiv.org/abs/2611.32654v1)

- **评分**：62/100
- **作者**：Hongjia Liu, Dacheng Zhou, Minghao Fu et al.
- **方向**：World Models
- **一句话**：Robot demonstrations provide more than actions to imitate: they reveal how actions change the world and how those changes contribute to task success.

### 7. [AnyCam: Anything Can Represent Camera for Video Generation](http://arxiv.org/abs/2611.34944v1)

- **评分**：62/100
- **作者**：Weijie Lyu, Zhixin Shu, Yuntian Ke et al.
- **方向**：Video Generation
- **一句话**：Camera-controlled video generation re-renders a video along a target camera trajectory, yet moving the camera around an object, the most natural way to change the viewpoint of an…
