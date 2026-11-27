# Generation Research Daily Digest

> 生成时间：2026-11-27T05:28:09+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 精读只保留短目录；详细笔记按日期放在 [docs/notes](../notes/index.md)。

## 优先精读

### 1. [WorldInteract: Controllable Streaming Video Generation for Multi-Material Interactions](http://arxiv.org/abs/2611.34730v1)

- **评分**：77/100
- **作者**：Ahmed Hatem, Caoliwen Wang, Robert Hoang et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **一句话**：WorldInteract 面向多材料物理交互的流式视频生成，将材料本身在速度变化下的行为学习与物体接触时的动量交换计算分开处理。模型通过共享速度增量接口，把外部推动和物理控制器预测的接触冲量统一输入因果视频生成器；场景记忆、深度位置图和目标跟踪图用于维持长时间生成中的物体状态与身份。训练分为无交互材料行为学习、因果状态传播和材料感知强化学习三阶段，并通过…
- **精读笔记**：[打开笔记](../notes/2026-11-27/2611.34730-worldinteract-controllable-streaming-video-gener.md)

### 2. [ShowNow: Fine-Grained Speculative Streaming for Responsive World Models](http://arxiv.org/abs/2611.34693v1)

- **评分**：76/100
- **作者**：Yiren Song, Guian Fang, Mike Zheng Shou
- **方向**：World Models
- **一句话**：论文提出 ShowNow，用于降低交互式世界模型的视频输入响应延迟。系统以单潜变量进行更频繁的提交，并在播放期间从同一历史状态并行准备多个动作条件化未来；用户输入到达后直接选择匹配分支，再将其作为下一轮生成的共同历史。作者构建了匹配的八动作多未来 ViZDoom 数据集，并结合因果蒸馏、自强制训练、分支树注意力、共享历史缓存和融合提交实现实时推理。在单张…
- **精读笔记**：[打开笔记](../notes/2026-11-27/2611.34693-shownow-fine-grained-speculative-streaming-for-r.md)

### 3. [LiveVAE: Causal Window Attention Makes Efficient Streaming Video VAE](http://arxiv.org/abs/2611.34912v1)

- **评分**：74/100
- **作者**：Jiachen An, Sijie Zhao, Le Li et al.
- **方向**：Video Generation
- **一句话**：论文针对实时视频生成、流式编辑和参考视频生成中的 VAE 延迟瓶颈，提出 LiveVAE。作者通过有效感受野和扰动实验发现，预训练视频 VAE 的编码与解码主要依赖局部空间邻域和短时因果邻域，因此使用固定大小的因果窗口注意力替代全局时空建模。LiveVAE 在 latent 网格上采用流式 Transformer 编码器和解码器，并通过滚动 KV 缓存实现…
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
