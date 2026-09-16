# Generation Research Daily Digest

> 生成时间：2026-09-16T09:29:36+00:00 · 筛选方式：规则评分 + Cursor 全文阅读
> 优先精读由 Cursor 读全文；快速浏览只看摘要、方法图和主实验表。

## 优先精读

### 1. [World in World: Explore the World with World Models](http://arxiv.org/abs/2609.11548v1)

- **评分**：77/100
- **作者**：Chenxi Song, Yanming Yang, Chi Zhang
- **方向**：World Models, Autoregressive and Streaming Video
- **Abstract 中文翻译**：自回归视频世界模型能够支持交互式、长时域探索，但灵活控制仍然具有挑战性。从新的视角探索源视频，需要生成的轨迹与记录事件保持同步，将观察到的内容放置在所请求的视角中，合理补全新暴露的区域，并在重新访问时恢复先前生成的外观。现有方法通常通过任务专用模块或额外训练来满足这些要求。我们提出 World in World，这是一种无需训练的推理时接口，可将异构控制证据转换为带有相机和时间标注的干净视觉状态，并通过冻结因果视频模型原生的自注意力读取这些状态。证据包括源视频观测、目标视角场景投影、用于引导新暴露主体区域补全的几何渲染，以及滚动缓存之外检索到的生成状态。每种证据都带有标记级支持信息和各自的可用时间表。对应关系路由器结合持久点身份与几何信息建立标记对应关系，引导受支持的查询关注匹配的源视频标记。随后，证据级注意力 CFG（EWA）利用同一次去噪前向传播中的注意力响应，独立调节每个辅助通道的额外贡献。该共享接口在使用同一个冻结骨干的情况下，支持相机控制的重新渲染、长时域重访和人体运动迁移。我们在不同视角变化下的相机控制视频重新渲染任务上评估 World in World，考察感知质量、时间一致性和相机跟随准确性。
- **全文总结**：论文提出 World in World（WiW），一种无需训练的视觉证据接口，用于扩展冻结因果视频世界模型的控制能力。方法将源视频观测、目标视角投影、几何渲染和历史生成状态统一表示为带相机、时间及空间有效性信息的干净视觉状态，并通过模型原生自注意力注入。对应关系引导注意力路由（CGAR）利用持久点身份和几何对应关系定位相关证据；证据级注意力 CFG（EWA）则按证据来源调节其影响，且无需额外的网络函数评估。WiW支持事件同步的多视角视频重渲染、新暴露区域补全、长时域重访，以及子弹时间、视频稳定、视频编辑、人体运动迁移和 K/V 共享等应用。在 DAVIS 和 OpenVid-1M 上的实验表明，该方法在平均 VBench 指标和相机轨迹误差方面具有竞争力，并且消融实验验证了目标视角变形、几何证据、历史检索和注意力控制的作用。
- **核心贡献**：提出 WiW，一种无需训练、面向冻结因果视频世界模型的统一视觉证据接口；构建源视频观测、目标视角场景投影、渲染几何和生成历史等互补证据，以支持事件同步、空间对齐和长时域一致性；提出对应关系引导注意力路由（CGAR），利用持久点身份与相机几何建立标记级对应关系；提出证据级注意力 CFG（EWA），在原生自注意力中独立调节不同证据通道的贡献，且不增加额外去噪网络前向评估；在单一冻结骨干上展示相机控制重渲染及多种下游应用。
- **与你课题的关系**：该工作直接面向视频生成、视频扩散及因果自回归视频世界模型，重点解决动态场景中的相机控制、长视频探索、时间同步和跨视角一致性。其通过滚动缓存与历史 K/V 检索实现超出有限上下文的状态复用，涉及缓存复用和长时域生成；通过原生自注意力中的稀疏辅助证据、对应关系路由和按证据调节的 CFG 提升控制效率。方法无需重新训练或专用控制模块，并在同一次去噪前向传播中完成 EWA，因此与实时生成、推理时控制和低额外计算开销密切相关。它还可用于动作或人体运动迁移，具有面向闭环交互式模拟和可控视觉世界探索的潜在价值。
- **局限 / 待核实**：论文未明确说明系统性的局限性。根据论文描述，该方法依赖源视频的深度估计、持久点跟踪、相机信息以及可用的主体几何表示，并在冻结的 LingBot-World 2.0 因果模型上主要通过 DAVIS 和 OpenVid-1M 的相机控制视频重渲染进行评估；这些依赖和评估范围可能限制其对复杂场景、长时域误差累积及其他模型架构的泛化能力。

### 2. [PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](http://arxiv.org/abs/2609.17521v1)

- **评分**：75/100
- **作者**：Chuhao Chen, Peter Wonka, Chaoyang Wang et al.
- **方向**：Video Generation
- **Abstract 中文翻译**：视频生成的交互式控制正从粗粒度提示转向对动态场景进行细粒度、具有物理意义的操纵。然而，现有可控方法要么要求在生成开始前提供完整的控制计划，要么使用决定物体位置而非物理动力学的像素空间信号。为解决这些局限，我们提出 PhysStream：一种用于物理 grounded 图像到视频合成的自回归模型。该模型引入结构化场景记忆，包括根据先前生成帧在线获得的位置图和物体跟踪图；同时通过稀疏的速度增量信号实现细粒度运动控制。这些信号编码物理量，使模型能够学习潜在动力学。我们分两个阶段训练模型：首先对双向模型进行运动控制条件微调，然后训练加入额外结构化场景记忆的因果自回归模型，从而进一步提升物理一致性。PhysStream 支持对多物体桌面刚体场景进行交互式的生成中途控制，这是以往方法不具备的能力。在合成基准上，相比最强基线，该方法将运动分布距离（FVMD）降低了 33%，将轨迹误差降低了 12%；在真实世界比较中，超过 85% 的人工评估者更偏好该方法。详情请参阅我们的网站：https://czzzzh.github.io/PhysStream
- **全文总结**：本文提出 PhysStream，一种面向多物体桌面刚体场景的物理 grounded、自回归图像到视频生成模型。用户可在生成过程中针对指定物体、指定时刻输入稀疏的三维速度增量，模型据此逐帧生成具有碰撞、摩擦和运动响应的视频。为保持长期几何与物体身份一致性，模型从已生成帧在线估计位置图和物体跟踪图，并将其作为结构化场景记忆反馈给后续生成。训练采用两阶段方案：先让双向模型学习速度控制，再将其转为带因果注意力和场景记忆的自回归模型。实验表明，该方法在合成数据、真实场景、非刚体迁移和长时域控制中具有较好的物理合理性与控制遵循能力，但长时间生成会出现外观漂移，且当前系统尚未达到实时速度。
- **核心贡献**：1. 提出 PhysStream，实现直接作用于生成视频本身的、端到端的场景级物理交互控制，支持多物体刚体场景中的生成中途干预。2. 提出结构化场景记忆机制，通过在线更新的位置图和物体跟踪图向自回归生成器反馈历史几何与物体状态。3. 设计稀疏速度增量控制，将用户操作表达为物理量，而不是预先规定完整轨迹或逐像素位置。4. 提出双向运动控制微调加因果自回归场景记忆训练的两阶段训练流程，并通过时间偏移的条件拼接避免未来信息泄漏。5. 构建约 10 万个包含多物体刚体运动、碰撞、摩擦和多帧速度扰动的合成视频数据集。6. 在物理运动分布、轨迹误差、交互控制、真实场景和长视频任务上进行系统评估，并展示了蒸馏和更快深度估计器对降低延迟的效果。
- **与你课题的关系**：与研究重点高度相关。PhysStream 是自回归、因果、流式视频生成模型，逐帧生成并使用 KV 缓存，允许用户观察已生成内容后在中途注入新的控制信号。其速度增量条件直接对应物理动作，结构化场景记忆构成由模型自身生成结果驱动的闭环反馈，可用于动作条件视觉世界模型和闭环物理模拟。方法面向视频扩散模型的因果化训练，并通过分阶段训练、条件缓存和在线深度/跟踪估计增强长时域一致性。论文还研究了 301 帧长时域生成，并使用分布匹配蒸馏将 50 步去噪压缩至 4 步，使系统吞吐量从 0.74 FPS 提升至 2.54 FPS；不过作者明确将实时生成留作未来工作。
- **局限 / 待核实**：论文明确指出，模型在极其复杂的运动，尤其是翻滚运动上仍存在困难；验证范围主要限于刚体动力学，非刚体材料需要针对每种材料额外构建数据并进行微调。长时域自回归生成会累积外观漂移，且一致性会随生成时长下降。当前系统仍未达到实时生成速度，主要延迟来自视频去噪和在线深度估计。方法依赖在线单目深度估计、实例分割与跟踪，这些估计误差可能影响场景记忆和生成质量。实验主要基于静态摄像机的桌面场景和合成数据，复杂相机运动及更广泛场景的有效性论文未充分验证。论文还指出，一致性指标可能被物体静止或刚性像素漂移等退化结果虚高。

### 3. [LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](http://arxiv.org/abs/2609.15863v1)

- **评分**：75/100
- **作者**：Xiaofeng Mao, Peijia Lin, Shaohao Rui et al.
- **方向**：Video Generation, Autoregressive and Streaming Video
- **摘要摘录**：Video diffusion models are stochastic and hard to control: precise content often requires repeated sampling without guaranteed success, and long-horizon scenes drift in appearance, interactions, and temporal coherence.
- **核心贡献**：To realize this combination, we present LynnReal-Omni, a native multimodal video generation framework built on a 32B shared multimodal diffusion transformer that unifies text-to-video, image-conditioned generation, reference-guided generation, structural control, editing, degraded video restoration, and long-video generation.
- **与你课题的关系**：匹配研究线：efficient generation, video generation；关键词：streaming, real-time, acceleration, efficient, video generation, text-to-video
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [Uncertainty DMD: Restoring Diversity in Few-Step Autoregressive Video Distillation](http://arxiv.org/abs/2609.11265v1)

- **评分**：75/100
- **作者**：Zixuan Duan, Xunzhi Xiang, Yabo Chen et al.
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：Few-step distillation improves the efficiency of autoregressive (AR) video generation, but often causes diversity collapse: under the same prompt, different noise samples tend to produce highly similar videos with weakened motion dynamics.
- **核心贡献**：Based on this analysis, we propose Uncertainty DMD, a simple uncertainty-injection framework that restores stochasticity at two key stages of AR generation: a timestep perturbation for the first chunk to increase first-chunk diversity, and a stochastic cache-writing mechanism for later chunks to preserve uncertainty in autoregressive conditioning.
- **与你课题的关系**：匹配研究线：efficient generation, streaming video；关键词：autoregressive, few-step, distillation, cache, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [AlayaVista: Streaming World Modeling from Panoramic States to Perspective Video](http://arxiv.org/abs/2609.14462v1)

- **评分**：74/100
- **作者**：Jiaming Tan, Mingliang Zhai, Zhen Li et al.
- **方向**：World Models
- **摘要摘录**：Interactive video world models must maintain broad scene context under camera motion while producing high-fidelity observations with low latency.
- **核心贡献**：Motivated by the complementary roles of global context and selective local acuity in visual perception, we present AlayaVista, a camera-controllable streaming video world model that decouples panoramic world evolution from perspective observation synthesis.
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, video world model, interactive, autoregressive, streaming, few-step
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](http://arxiv.org/abs/2608.10519v3)

- **评分**：74/100
- **作者**：Jongbeom Lee, Hyunwoo Yu, Jincheol Yang et al.
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：InfinityStar extends visual autoregressive generation to video through a sequence of image and clip pyramids.
- **核心贡献**：We introduce SparSTAR, a training-free block-sparse attention method tailored to this setting.
- **与你课题的关系**：匹配研究线：video generation, streaming video；关键词：autoregressive, sparse attention, video generation, text-to-video, image-to-video, video synthesis
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](http://arxiv.org/abs/2609.00610v2)

- **评分**：72/100
- **作者**：Xiaoyan Liu, Jiaxin Liu, Kangrui Li et al.
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：Current 4D generation paradigms are often bottlenecked by a sequential decoupling design: video is generated first, followed by 3D reconstruction, leading to high interaction latency.
- **核心贡献**：To this end, we propose \textbf{Streaming4D}, a tightly coupled synchronous pipeline that integrates block-wise autoregressive video generation with incremental 3D reconstruction.
- **与你课题的关系**：匹配研究线：streaming video, world model；关键词：world model, interactive, autoregressive, streaming, self-forcing, real-time
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [Decoupled Self-Forcing Distillation for Streaming Talking Head Generation](http://arxiv.org/abs/2609.10317v1)

- **评分**：70/100
- **作者**：Yanru An, Ruiyan Wang, Wenwu Wei et al.
- **方向**：Video Generation
- **摘要摘录**：Streaming talking-head generation produces each frame as its driving audio arrives, yet fidelity and efficiency have so far pulled in opposite directions: end-to-end methods condition a video diffusion model on audio directly and achieve high quality but only at large scale, while cheaper two-stage methods generate an intermediate motion representation and trail in fidelity.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：streaming video, efficient generation；关键词：driving, autoregressive, streaming, self-forcing, distillation, video diffusion
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence](http://arxiv.org/abs/2609.17210v1)

- **评分**：69/100
- **作者**：Yinhao Li, Weixin Mao, Zihan Lan et al.
- **方向**：World Models
- **摘要摘录**：Vision-language-action (VLA) models, world-action models (WAMs), and offline reinforcement learning methods are rapidly expanding the design space of embodied policies, yet turning these algorithms into reliable robot systems remains constrained by fragmented data formats, training stacks, evaluation protocols, inference runtimes, and embodiment-specific interfaces.
- **核心贡献**：We present $\mathrm{FluxVLA}$ Engine, an open, configuration-driven platform that turns heterogeneous embodied-policy components into a reproducible data-to-deployment workflow.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, simulation, embodied, real-time
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy](http://arxiv.org/abs/2609.09941v1)

- **评分**：66/100
- **作者**：Zengjue Chen, Peidong Liu, Jiawei Li et al.
- **方向**：World Models
- **摘要摘录**：Generalist robot policies have demonstrated strong generalization across robotic manipulation tasks, yet their success rates remain limited in com- plex long-horizon scenarios.
- **核心贡献**：To address this issue, we propose Hallucination-aware World Model-based Pol- icy Optimization (HaWMPO), a closed-loop reinforcement learning pipeline for VLA policy post-training with world models.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, closed-loop
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
