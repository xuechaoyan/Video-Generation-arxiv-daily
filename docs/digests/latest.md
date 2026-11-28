# Generation Research Daily Digest

> 生成时间：2026-11-28T05:03:23+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions](http://arxiv.org/abs/2611.34730v1)

- **评分**：77/100
- **作者**：Ahmed Hatem, Caoliwen Wang, Robert Hoang et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：WorldInteract 面向具有多种材料和物体接触的可控流式视频生成，将材料在速度变化下的行为学习与碰撞接触响应计算分开处理。模型通过速度增量接口连接因果视频生成器和物理控制器：生成器从3万个涵盖22类材料的无物体接触模拟视频中学习材料行为，控制器则依据视觉语言模型估计的质量、恢复系数以及场景中的深度和跟踪信息计算接触冲量。场景记忆、对象跟踪和物理图使…
- **精读笔记**：[打开笔记](../notes/2026-11-28/2611.34730-worldinteract-controllable-streaming-video-gener.md)

### 2. [ShowNow: Fine-Grained Speculative Streaming for Responsive World Models](http://arxiv.org/abs/2611.34693v1)

- **评分**：76/100
- **作者**：Yiren Song, Guian Fang, Mike Zheng Shou
- **方向**：World Models
- **一句话**：论文提出 ShowNow，用于降低交互式世界模型中的动作响应延迟。系统在播放已生成视频时，利用空闲计算提前生成多个动作条件化的未来，并在用户输入到达后选择相应分支继续生成。其核心包括单潜变量的细粒度提交、匹配多未来数据集、共享历史的分支树注意力、缓存复用和融合提交。在 ViZDoom 上，5B 模型可在单张 H100 以 480p、16 fps 生成并准备…
- **精读笔记**：[打开笔记](../notes/2026-11-28/2611.34693-shownow-fine-grained-speculative-streaming-for-r.md)

### 3. [LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE](http://arxiv.org/abs/2611.34912v1)

- **评分**：74/100
- **作者**：Jiachen An, Sijie Zhao, Le Li et al.
- **方向**：Video Generation
- **一句话**：论文指出，视频 VAE 的编码和解码主要依赖局部空间邻域及短时因果邻域，而不需要全局时空建模。LiveVAE 使用固定大小的因果窗口注意力构建流式编码器和解码器，并通过滚动 KV 缓存支持长视频持续处理。三阶段蒸馏和联合微调使其保持与原 VAE 及现有扩散 Transformer 的潜空间兼容；算子融合、区域编译和 FP8 量化感知训练进一步降低推理开销。…
- **精读笔记**：[打开笔记](../notes/2026-11-28/2611.34912-livevae-causal-window-attention-makes-efficient.md)

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
