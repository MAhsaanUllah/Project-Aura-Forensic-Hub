---
title: Project Aura
emoji: 🔍
colorFrom: green
colorTo: gray
sdk: docker
pinned: false
---

<div align="center">

![AMD MI300X](https://img.shields.io/badge/Hardware-AMD_MI300X-ED1C24?style=for-the-badge&logo=amd&logoColor=white)
![ROCm](https://img.shields.io/badge/Platform-ROCm_6.0-00539B?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![vLLM](https://img.shields.io/badge/Engine-vLLM-orange?style=for-the-badge)

# Project Aura: Intelligence Redefined
### *Forensic Artifact Reconstruction via AMD Instinct™ MI300X Acceleration*

[**🎥 Project Aura Video Demo**](https://youtu.be/YilCJiH-B7w) | [**🤗 Hugging Face Space**](#)

</div>

---

## 🌌 Executive Summary

**Project Aura** is a high-performance forensic intelligence engine engineered for the **AMD Global Hackathon**. It leverages the massive parallel compute capabilities of the **AMD Instinct™ MI300X** to perform real-time reconstruction of digital forensic artifacts. By integrating **vLLM** and **ROCm™ 6.0**, Aura provides investigators with a high-entropy reasoning pipeline capable of auditing complex system logs, memory dumps, and metadata anomalies with unprecedented speed and precision.

## 🏆 Key Features

| Feature | Description |
| :--- | :--- |
| **Neural Forensic Analysis** | Deep-trace reconstruction using the Qwen-72B-Agentic model. |
| **Case Metadata Hub** | Integrated Case ID and Investigator tracking for official audit trails. |
| **Forensic Quick Presets** | Instant templates for Kernel, Network, and Metadata investigations. |
| **MI300X Acceleration** | Optimized inference leveraging 192GB HBM3 VRAM for massive context windows. |
| **ROCm™ Integration** | Native execution on AMD's open software platform for maximum GPU throughput. |
| **Automated Reporting** | Instant generation of tamper-proof, court-ready PDF forensic reports. |
| **Real-time Pipeline** | Low-latency response via vLLM's continuous batching on AMD hardware. |

---

## 🛠️ Infrastructure & Stack

Project Aura is built on a Tier-1 AI infrastructure designed for enterprise-grade forensic auditing.

- **Compute:** [AMD Instinct™ MI300X](https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html) (HBM3 192GB)
- **Software Platform:** AMD ROCm™ 6.0 (Open Software Stack)
- **Inference Engine:** [vLLM](https://github.com/vllm-project/vllm) (Optimized for AMD)
- **Language Model:** Qwen-72B-Agentic-Reasoner
- **Orchestration:** Python 3.12 & Streamlit

---

## 📸 System Preview

### Unified Forensic Interface
![Aura Preview](assets/aura_preview.png)

### Court-Ready Forensic Reporting
![PDF Report Example](assets/aura_pdf_report.png)

---

## 🚀 Setup & Installation

### 1. Environment Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/MAhsaanUllah/Project-Aura-Forensic-Hub.git
cd Project-Aura-Forensic-Hub
pip install -r requirements.txt
```

### 2. Launching Project Aura
Run the Streamlit application:
```bash
streamlit run app.py
```

---

## 🔍 Investigation Case Studies

| Case Type | Inquiry Pattern | Resulting Intelligence |
| :--- | :--- | :--- |
| **Metadata Audit** | "Analyze suspicious PDF for 'Incremental Updates'." | **ALERT:** DocChecksum mismatch at Offset 0x4A2. |
| **Ransomware Timeline** | "Reconstruct kernel-level API call logs." | **TIMELINE:** Shadow Copy deletion identified at 14:02 UTC. |
| **Network Forensic** | "Identify C2 heartbeat in encrypted traffic logs." | **SIGNAL:** Entropy spike detected in TLS handshake. |

---

## 📄 License & Attribution

Developed for the **AMD Global Hackathon 2026** by **Muhammad Ahsaan Ullah**.
Built with ❤️ on the **AMD Instinct™ MI300X**.

---
<div align="center">
  <sub>© 2026 Project Aura | Secure • Scalable • Intelligent</sub>
</div>
