# Generation Research Daily Digest

> 生成时间：2026-09-09T15:22:17+00:00 · 筛选方式：规则评分（未配置模型 API Key）
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

### 2. [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](http://arxiv.org/abs/2609.03602v1)

- **评分**：66/100
- **作者**：Jinyang Wang, Shiwei Li, Junjian Wang et al.
- **方向**：World Models
- **摘要摘录**：World models (WMs) have demonstrated strong potential for end-to-end autonomous driving by learning predictive representations of future scene dynamics.
- **核心贡献**：To address this limitation, we propose SV-WAM, a surround-view world-action model (WAM) that preserves full six-camera observations while maintaining efficient inference.
- **与你课题的关系**：匹配研究线：world model, efficient generation；关键词：world model, closed-loop, driving, efficient
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 3. [Earth System World Model for What-If Simulations: A Case Study for Terrestrial Ecosystems](http://arxiv.org/abs/2609.08855v1)

- **评分**：63/100
- **作者**：Zhihao Wang, Ruichen Wang, Ruohan Li et al.
- **方向**：World Models
- **摘要摘录**：Machine learning emulators have become essential for accelerating expensive Earth-system simulations, but most existing approaches remain passive forecasters: they reproduce simulator trajectories under prescribed forcings without an explicit interaction mechanism for user-specified interventions.
- **核心贡献**：We propose an action-conditioned world-modeling framework for Earth-system emulation that reformulates simulator trajectories as supervision for controllable state-transition learning.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, interactive, simulation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 4. [DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation](http://arxiv.org/abs/2609.04031v1)

- **评分**：60/100
- **作者**：Shuaiting Li, Zelin Gao, Haibin Shen et al.
- **方向**：Video Generation
- **摘要摘录**：Video diffusion models (VDMs) have achieved impressive progress in text-to-video generation, but their high memory and computational costs hinder practical deployment.
- **核心贡献**：Based on this insight, we propose DSAQuant, a Denoising-Stage-Aligned Quantization-aware training framework for VDMs.
- **与你课题的关系**：匹配研究线：video generation, efficient generation；关键词：distillation, video generation, text-to-video, video diffusion
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 5. [APEX-RBD: Mixed-Precision Exploration Framework for Hardware-Efficient Robot Dynamics Accelerator Design](http://arxiv.org/abs/2609.05161v1)

- **评分**：57/100
- **作者**：Xingyu Liu, Hanwei Fan, Chaofang Ma et al.
- **方向**：World Models
- **摘要摘录**：Rigid Body Dynamics (RBD) forms the computational core of real-time robotic control, but its immense computational complexity creates a performance bottleneck that necessitates dedicated hardware accelerators.
- **核心贡献**：To address these challenges, we introduce APEX-RBD, an automated framework that makes mixed-precision exploration computationally tractable while effectively identifying hardware-efficient configurations.
- **与你课题的关系**：匹配研究线：efficient generation, world model；关键词：closed-loop, simulation, real-time, efficient
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 6. [Learning Counterfactual World Models for Embodied Reasoning under Partial Observability](http://arxiv.org/abs/2609.05834v1)

- **评分**：57/100
- **作者**：Todd Y. Zhou, Daniel Zhang
- **方向**：World Models
- **摘要摘录**：World models promise a general route to embodied intelligence: learn predictive dynamics once, then reason, plan, and act with them.
- **核心贡献**：We introduce Counterfactual Latent World Models (CLWM), which combine a recurrent belief-state encoder, action-conditioned latent dynamics, and a contrastive counterfactual objective that separates futures induced by distinct interventions even when their observations look alike.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned, embodied
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 7. [PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](http://arxiv.org/abs/2609.05918v1)

- **评分**：56/100
- **作者**：Bangxun Tang, Heyuan Gao, Yiren Song et al.
- **方向**：Autoregressive and Streaming Video
- **摘要摘录**：We present PAI-Actor, a cinematic multi-character animation framework for character replacement in dynamic movie scenes.
- **核心贡献**：We present PAI-Actor, a cinematic multi-character animation framework for character replacement in dynamic movie scenes.
- **与你课题的关系**：匹配研究线：efficient generation, streaming video；关键词：autoregressive, distillation, efficient, video generation
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。

### 8. [WM-Craftnet: World Synesthesia Model for Generalizable and Robust Dexterous In-Hand Manipulation](http://arxiv.org/abs/2609.07002v1)

- **评分**：56/100
- **作者**：Jie Yin, Zeyuan Zhao, Xiaojing Tan et al.
- **方向**：World Models
- **摘要摘录**：Generalizable and robust dexterous in-hand manipulation requires a policy to infer object pose, geometry, contact, and potential slip from partial and noisy observations.
- **核心贡献**：We propose WM-Craftnet, a world-model-conditioned framework that learns compact action-conditioned latent dynamics from proprioception, depth, tactile sensing, and actions, supervised by multimodal reconstruction and reward prediction.
- **与你课题的关系**：匹配研究线：world model；关键词：world model, action-conditioned
- **局限 / 待核实**：规则模式无法可靠判断实验质量与论文局限。
