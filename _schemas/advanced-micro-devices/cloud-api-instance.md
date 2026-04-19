---
description: An AMD GPU compute instance.
layout: schema
name: Instance
properties_list:
- description: Instance identifier.
  name: id
  type: string
- description: Instance display name.
  name: name
  type: string
- description: GPU hardware type.
  name: gpuType
  type: string
- description: Number of GPUs.
  name: gpuCount
  type: integer
- description: Instance status.
  name: status
  type: string
- description: Deployment region.
  name: region
  type: string
- description: ROCm image.
  name: imageId
  type: string
- description: Creation timestamp.
  name: createdAt
  type: string
provider_name: Advanced Micro Devices
provider_slug: advanced-micro-devices
schema_file: json-schema/cloud-api-instance-schema.json
slug: cloud-api-instance
tags:
- AI
- Cloud Computing
- GPU
- HPC
- Machine Learning
- Semiconductor
title: Instance
---
