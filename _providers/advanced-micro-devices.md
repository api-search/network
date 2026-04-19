---
api_count: 2
apis:
- description: The AMD Developer Cloud API provides access to AMD Instinct GPU instances for AI inference, training, and HPC workloads. Supports managing compute instances, deploying AI models, monitoring GPU utiliz
  name: AMD Developer Cloud API
  slug: ''
- description: The AMD ROCm (Radeon Open Compute) platform provides the runtime and library APIs for GPU-accelerated computing on AMD hardware. Includes HIP (Heterogeneous-compute Interface for Portability), math li
  name: AMD ROCm API
  slug: ''
capabilities:
- description: 'Unified workflow capability for AI and HPC workloads on AMD Instinct GPUs — provision instances, deploy LLMs, monitor performance, and manage cloud credits. Designed for AI researchers, ML engineers, '
  name: AMD AI GPU Computing
  slug: ai-gpu-computing
common:
- title: ''
  type: Website
  url: https://www.amd.com
- title: ''
  type: Portal
  url: https://developer.amd.com
- title: ''
  type: Documentation
  url: https://rocm.docs.amd.com
- title: ''
  type: GettingStarted
  url: https://developer.amd.com/resources/rocm-resources/
- title: ''
  type: Support
  url: https://developer.amd.com/support/
- title: ''
  type: Blog
  url: https://www.amd.com/en/corporate/blog.html
- title: ''
  type: TermsOfService
  url: https://www.amd.com/en/legal/terms-and-conditions.html
- title: ''
  type: PrivacyPolicy
  url: https://www.amd.com/en/legal/privacy.html
- title: ''
  type: GitHubOrganization
  url: https://github.com/ROCm
- title: ''
  type: Academy
  url: https://academy.amd.com
- title: ''
  type: SignUp
  url: https://developer.amd.com/amd-developer-cloud/
created: '2024-01-01'
description: Advanced Micro Devices (AMD) is a global semiconductor company that develops high-performance computing, graphics, and visualization technologies for data centers, gaming, and embedded markets. AMD provides the ROCm open software platform for GPU computing, HIP programming interface, and the AMD Developer Cloud for AI workloads using AMD Instinct GPUs.
features:
- description: On-demand access to MI300X, MI250, and MI210 GPU instances for AI training, inference, and HPC workloads.
  name: AMD Instinct GPU Instances
- description: Open-source GPU compute platform with HIP programming model, math libraries, and deep learning framework support.
  name: ROCm Software Platform
- description: CUDA-compatible GPU programming interface enabling portable code across AMD and NVIDIA hardware.
  name: HIP Programming Interface
- description: Deploy and serve large language models using vLLM, TGI, and other inference engines on AMD Instinct GPUs.
  name: AI Model Serving
- description: Optimized libraries including rocBLAS, rocFFT, rocRAND, and rocSPARSE for scientific computing and deep learning.
  name: ROCm Math Libraries
- description: RCCL (ROCm Communication Collectives Library) for efficient multi-GPU and multi-node collective operations.
  name: Multi-GPU Communication
- description: Free GPU cloud credits for qualifying researchers, startups, and developers through the AMD AI Developer Program.
  name: AI Developer Cloud Credits
- description: Full compatibility with PyTorch, TensorFlow, JAX, and other ML frameworks via ROCm backend support.
  name: Framework Compatibility
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
integrations:
- description: Full ROCm support for PyTorch including autograd, distributed training, and all major model architectures.
  name: PyTorch
- description: TensorFlow-ROCm integration enabling GPU-accelerated training and inference on AMD hardware.
  name: TensorFlow
- description: AMD Instinct Day-0 support in vLLM for high-performance LLM inference serving.
  name: vLLM
- description: Transformers and Diffusers library compatibility with ROCm for loading and running models from Hugging Face Hub.
  name: Hugging Face
- description: AMD GPU operator for Kubernetes enabling GPU-accelerated containerized workloads on AMD hardware.
  name: Kubernetes
- description: Official ROCm Docker images for containerized GPU computing environments.
  name: Docker
- description: ONNX Runtime ROCm execution provider for cross-framework model deployment on AMD GPUs.
  name: ONNX Runtime
jsonld:
- class_count: 33
  name: Amd Developer Cloud Api Context
  property_count: 2
  slug: amd-developer-cloud-api-context
- class_count: 30
  name: Amd Rocm Management Api Context
  property_count: 0
  slug: amd-rocm-management-api-context
layout: provider
modified: '2026-04-19'
name: Advanced Micro Devices
rules:
- name: Advanced Micro Devices API Rules
  rule_count: 31
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 11
  slug: amd-spectral-rules
skills: []
slug: advanced-micro-devices
solutions: []
tags:
- AI
- Cloud Computing
- GPU
- HPC
- Machine Learning
- Semiconductor
url: https://raw.githubusercontent.com/api-evangelist/advanced-micro-devices/refs/heads/main/apis.yml
use_cases:
- description: Train and fine-tune large language models on AMD Instinct GPU clusters with ROCm-optimized PyTorch.
  name: Large Language Model Training
- description: Deploy LLM inference endpoints using vLLM on AMD Instinct GPUs for high-throughput token generation.
  name: AI Inference Serving
- description: Run HPC simulations, molecular dynamics, and fluid dynamics workloads on AMD GPU clusters with ROCm.
  name: Scientific Computing
- description: Train and deploy image classification, object detection, and segmentation models using AMD GPU acceleration.
  name: Computer Vision
- description: Accelerate data processing and analytics workloads using GPU-accelerated computing with ROCm.
  name: Data Analytics
- description: Develop and iterate on generative AI applications using AMD Developer Cloud free GPU credits.
  name: Generative AI Development
---
