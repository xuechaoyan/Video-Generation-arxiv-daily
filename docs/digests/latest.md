# Generation Research Daily Digest

> 生成时间：2026-11-27T20:22:02+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions](http://arxiv.org/abs/2611.34730v1)

- **评分**：77/100
- **作者**：Ahmed Hatem, Caoliwen Wang, Robert Hoang et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：WorldInteract 提出一种可控流式视频生成框架，将材料自身在速度变化下的行为学习与物体接触时的动量交换计算分离。模型使用共享速度增量接口，把外部推动和接触冲量统一起来；因果视频生成器负责生成材料行为，物理控制器则根据视觉估计的质量、恢复系数和场景状态计算接触响应。方法通过3万段覆盖22类材料的无物交互模拟视频进行训练，并结合场景记忆、物体跟踪、位…
- **精读笔记**：[打开笔记](../notes/2026-11-27/2611.34730-worldinteract-controllable-streaming-video-gener.md)

### 2. [ShowNow: Fine-Grained Speculative Streaming for Responsive World Models](http://arxiv.org/abs/2611.34693v1)

- **评分**：76/100
- **作者**：Yiren Song, Guian Fang, Mike Zheng Shou
- **方向**：World Models
- **一句话**：论文提出 ShowNow，用于解决交互式世界模型中实时播放与低输入延迟难以兼顾的问题。系统在播放当前视频时，提前生成多个动作条件下的未来，输入到达后选择对应分支并提交为后续历史；同时采用单潜变量细粒度提交、匹配多未来数据、共享历史树状注意力、缓存复用和融合提交来降低开销。基于 ViZDoom 的实验显示，5B 模型在单张 H100 上可于 480p、16…
- **精读笔记**：[打开笔记](../notes/2026-11-27/2611.34693-shownow-fine-grained-speculative-streaming-for-r.md)

### 3. [LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE](http://arxiv.org/abs/2611.34912v1)

- **评分**：74/100
- **作者**：Jiachen An, Sijie Zhao, Le Li et al.
- **方向**：Video Generation
- **一句话**：论文针对实时视频生成、流式编辑和参考视频生成中视频 VAE 成为延迟瓶颈的问题，提出了 LiveVAE。作者通过有效感受野和扰动实验发现，预训练视频 VAE 的编码与解码主要依赖局部空间邻域及当前和短历史时间邻域。LiveVAE 使用因果窗口注意力，以固定的空间窗口和有限时间窗口处理视频帧，并通过滚动 KV 缓存实现流式推理。其三阶段蒸馏流程分别对编码器、…
- **精读笔记**：[打开笔记](../notes/2026-11-27/2611.34912-livevae-causal-window-attention-makes-efficient.md)

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
