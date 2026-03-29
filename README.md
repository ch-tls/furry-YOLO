# Furry-YOLO: Specialized Detection for ACG Events
[English](#english) | [中文](#chinese)

![YOLO11](https://img.shields.io/badge/Model-YOLO11%20v8.3.168-blue.svg)
![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-red.svg)
![Target: Fursuit & Cosplay](https://img.shields.io/badge/Focus-Fursuit%20%26%20Coser-ff69b4.svg)
![Hardware: Cool & Efficient](https://img.shields.io/badge/Compute-A733%20%26%20QCS6490-green.svg)

---

<a name="chinese"></a>
## 🇨🇳 中文说明

### 🚀 项目简介
本项目旨在为 **“智慧兽装 (Smart Fursuit)”** 及二次元漫展自动化标注提供视觉感知支持。由于主流数据集对 **Fursuit (兽装)** 类别缺乏专项支持，本项目通过微调 **Ultralytics YOLO11 (v8.3.168)**，实现了对该垂直领域的识别。

### 📊 模型矩阵与性能指南
| 编号 | 模型规格 | 训练分辨率 | 建议置信度 (Conf) | 建议算力平台 |
| :--- | :--- | :--- | :--- | :--- |
| **001** | Nano | 640p | 0.25+ | 0.5T NPU / 纯 CPU (如 RK3566, Pi 5) |
| **003** | Nano | 960p | 0.35 | **主力推荐**，平衡速度与精度 |
| **005** | Small | 960p | 0.40 | **精度标杆**，推荐用于高性能边缘端 |

> **⚠️ 推理限制：** 请严格遵循训练分辨率。**禁止**交叉使用（如用 960p 模型识别 640p 图像），否则识别率将大幅下降。

### 💻 硬件与传感器建议 (Smart Fursuit 专用)
* **计算平台（散热优先）：** 
    * **推荐：** 全志 A733 (VIP9000 NPU) 或高通 QCS6490。功耗极低，适合在密闭兽装内长期佩戴。
    * **强烈建议不要使用 RK3588**。虽然性能强大，但发热严重，在兽装内可能导致中暑或设备损坏。
* **传感器选型：** 
    * **要求：** 必须使用**彩色 (Color)** 传感器。**禁止使用灰度传感器**，色彩丢失会导致模型预测能力雪崩。
    * **快门建议：** 推荐全局快门 (Global Shutter) 或高刷卷帘快门 (如 IMX415)。请勿使用 IMX219/OV5647。

### 🛡️ 数据集与局限性
* **样本量：** 约 1000 张样本，主要涵盖亚洲漫展风格。
* **弱项：** 对 **欧美系/写实系** 兽装识别率较低。
* **隐私：** 训练集严格保密，仅分发模型权重（.pt, .onnx, .rknn, .nb, .dlc）。



### 🤝 贡献与感谢
*   感谢 **Ultralytics** 提供的 YOLO11 框架支持。
*   感谢提供图片素材的同好以及 **百度贴吧“卖萌水吧”** 板块的图源参考。
*   **协助我们：** 如果你有欧美系/写实系兽装的脱敏数据，欢迎联系我们优化模型！
    *   📧 联系邮箱：**fur-yolo@protonmail.com**

---

<a name="english"></a>
## 🇺🇸 English Description

### 🚀 Introduction
Visual perception for **"Smart Fursuit"** and ACG event tagging. Based on **Ultralytics YOLO11 (v8.3.168)**, this project fills the gap in specialized **Fursuit** detection.

### 📊 Model Matrix
| ID | Scale | Resolution | Rec. Conf | Best For |
| :--- | :--- | :--- | :--- | :--- |
| **001** | Nano | 640p | 0.25+ | Ultra-low power (RK3566, RPi 5 CPU) |
| **003** | Nano | 960p | 0.35 | **Mainstream** balanced model |
| **005** | Small | 960p | 0.40 | **Best Accuracy** for high-end edge |

### 💻 Hardware & Sensors
* **Compute:** 
    * **Recommended:** Allwinner A733 / Qualcomm QCS6490 (Cool & Efficient).
    * **Warning:** **AVOID RK3588** due to excessive heat in confined Fursuit spaces.
* **Sensors:** 
    * **MUST** use Color sensors. **NO Greyscale**.
    * Global Shutter or high-refresh Rolling Shutter (e.g., IMX415) is required.

### 🛡️ Disclaimer
* **Bias:** High accuracy for **Asian-style** Fursuits; lower for **Western/Realistic** styles.
* **Privacy:** Training dataset is confidential. Only weights are released.

### 🤝 Credits & Contribution
*   Thanks to **Ultralytics** for the YOLO11 framework.
*   Special thanks to the contributors from the Fursuit community.
*   **Help us improve:** For contributing Western-style Fursuit data, please contact:
    *   📧 Email: **fur-yolo@protonmail.com**

---

## 📜 License
Licensed under **AGPL-3.0**. Derived from Ultralytics YOLO11.
