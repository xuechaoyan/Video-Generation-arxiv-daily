# Generation Research Daily Digest

> 生成时间：2026-09-10T15:15:39+00:00 · 筛选方式：规则评分（未配置模型 API Key）
> 建议先读“优先精读”，快速浏览只看摘要、方法图和主实验表。

## 优先精读

### 1. [Mask Forcing: Improving Autoregressive Video Diffusion Distillation via Dual-Noise Masking Rollout](http://arxiv.org/abs/2609.09123v1)

- **评分**：82/100
- **作者**：Zhuoran Zhao, Shengju Qian, Tongtong Liang et al.
- **方向**：Video Generation, Autoregressive and Streaming Video, Efficient Video Diffusion
- **摘要摘录**：Autoregressive (AR) video diffusion models have shown great potential in real-time video generation.
- **核心贡献**：To address this, we propose Mask Forcing, a Dual-Noise Masking Rollout strategy that perturbs the AR student self-rollout to mitigate mode collapse induced by reverse-KL mode seeking.
- **与你课题的关系**：匹配研究线：efficient generation, video generation；关键词：autoregressive, real-time, distillation, efficient, video generation, video diffusion
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image](http://arxiv.org/abs/2609.04911v2)

- **评分**：73/100
- **作者**：Xin Zhang, Yabo Chen, Zixuan Duan et al.
- **方向**：Video Generation, World Models
- **摘要摘录**：Interactive visual world models must distinguish observation from physical intervention.
- **核心贡献**：We present TourPhysics, an online framework initialized from a single image and a declarative physical configuration.
- **与你课题的关系**：匹配研究线：world model, video generation；关键词：world model, video world model, interactive, simulation, video generation, video synthesis
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

## 快速浏览

### 1. [ActionSplice: In-Flight Action Editing for Interactive World Models](http://arxiv.org/abs/2609.08230v1)

- **评分**：71/100
- **作者**：Pardis Taghavi, Tingyu Guo, Jonas Lossner et al.
- **方向**：World Models, Autoregressive and Streaming Video
- **摘要摘录**：Chunk-autoregressive video world models typically condition each generated chunk on one action.
- **核心贡献**：We introduce ActionSplice, an inference framework that formulates this problem as Counterfactual State Transport (CST).
- **与你课题的关系**：匹配研究线：world model, streaming video；关键词：world model, video world model, interactive, autoregressive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 2. [Decoupled Self-Forcing Distillation for Streaming Talking Head Generation](http://arxiv.org/abs/2609.10317v1)

- **评分**：70/100
- **作者**：Yanru An, Ruiyan Wang, Wenwu Wei et al.
- **方向**：Video Generation
- **摘要摘录**：Streaming talking-head generation produces each frame as its driving audio arrives, yet fidelity and efficiency have so far pulled in opposite directions: end-to-end methods condition a video diffusion model on audio directly and achieve high quality but only at large scale, while cheaper two-stage methods generate an intermediate motion representation and trail in fidelity.
- **核心贡献**：请快速查看方法图和主要实验表确认具体贡献。
- **与你课题的关系**：匹配研究线：streaming video, efficient generation；关键词：driving, autoregressive, streaming, self-forcing, distillation, video diffusion
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Valerant: An Automatic Navigable Game Map Generator via Action-Conditioned World Model Exploration](http://arxiv.org/abs/2609.09418v1)

- **评分**：67/100
- **作者**：Yiran Qiao, Feng Wang, Jing Ma
- **方向**：World Models
- **摘要摘录**：World Action Models (WAMs) couple predictive world modeling with action generation, allowing anticipated future states to guide agent behavior.
- **核心贡献**：We present \textsc{Valerant}, a training-free framework that transforms a pretrained action-conditioned world model into a WAM for exploring and constructing 3D game maps.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, driving, simulation, embodied
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [HaWMPO: Hallucination-Aware World Model-based Policy Optimization for Generalist Robot Policy](http://arxiv.org/abs/2609.09941v1)

- **评分**：66/100
- **作者**：Zengjue Chen, Peidong Liu, Jiawei Li et al.
- **方向**：World Models
- **摘要摘录**：Generalist robot policies have demonstrated strong generalization across robotic manipulation tasks, yet their success rates remain limited in com- plex long-horizon scenarios.
- **核心贡献**：To address this issue, we propose Hallucination-aware World Model-based Pol- icy Optimization (HaWMPO), a closed-loop reinforcement learning pipeline for VLA policy post-training with world models.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, closed-loop
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [Earth System World Model for What-If Simulations: A Case Study for Terrestrial Ecosystems](http://arxiv.org/abs/2609.08855v1)

- **评分**：63/100
- **作者**：Zhihao Wang, Ruichen Wang, Ruohan Li et al.
- **方向**：World Models
- **摘要摘录**：Machine learning emulators have become essential for accelerating expensive Earth-system simulations, but most existing approaches remain passive forecasters: they reproduce simulator trajectories under prescribed forcings without an explicit interaction mechanism for user-specified interventions.
- **核心贡献**：We propose an action-conditioned world-modeling framework for Earth-system emulation that reformulates simulator trajectories as supervision for controllable state-transition learning.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, interactive, simulation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation](http://arxiv.org/abs/2609.10506v1)

- **评分**：60/100
- **作者**：Nisarga Nilavadi, Ralf Römer, Moritz Reuss et al.
- **方向**：World Models
- **摘要摘录**：Action-conditioned latent world models predict future visual representations, enabling zero-shot goal-conditioned robot planning and control.
- **核心贡献**：To address this gap, we introduce DUET-DINO, a simultaneous cross-view latent world model that jointly learns action-conditioned predictions from static side- and wrist-camera observations through cross-view conditioning.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [Arti-JEPA: Adapting Video World Model to Real-Time MRI of the Vocal Tract for Speech-Production Analysis](http://arxiv.org/abs/2609.09757v1)

- **评分**：59/100
- **作者**：Hong Nguyen, Sean Foley, Christina Hagedorn et al.
- **方向**：World Models
- **摘要摘录**：Real-time MRI (rtMRI) captures the dynamics of the entire vocal tract during speech, but labeled data are scarce and the modality - single-slice, grayscale, low-resolution - differs substantially from the natural videos that video foundation models are trained on.
- **核心贡献**：We introduce Arti-JEPA, a joint embedding predictive architecture to model vocal tract rtMRI by continuing its self-supervised objective on about 62h of unlabelled vocal-tract videos, and evaluate the frozen representation on three tasks: cross-domain phoneme prediction (on typical speakers), fluent-vs-disfluent classification (a corpus containing stuttered speech), and characterizing pre/post-operative transfer (after partial glossectomy).
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, video world model, real-time
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 8. [Programmable World Model](http://arxiv.org/abs/2609.10540v1)

- **评分**：58/100
- **作者**：Zheng-Hui Huang, Guixu Lin, Jiacheng Lin et al.
- **方向**：World Models
- **摘要摘录**：Recent video world models generate increasingly realistic and interactive visual experiences, yet lack reliable mechanisms for maintaining persistent world state and enforcing programmable rules over extended interactions.
- **核心贡献**：We introduce Programmable World Model, a framework that decouples world-state evolution from visual observation generation.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, video world model, interactive
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
