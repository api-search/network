---
description: Real-time performance metrics for a GPU instance.
layout: schema
name: InstanceMetrics
properties_list:
- description: ''
  name: instanceId
  type: string
- description: GPU utilization %.
  name: gpuUtilization
  type: number
- description: Memory used GB.
  name: memoryUsed
  type: number
- description: Total memory GB.
  name: memoryTotal
  type: number
- description: Temperature Celsius.
  name: temperature
  type: integer
- description: Power draw watts.
  name: powerDraw
  type: number
provider_name: Advanced Micro Devices
provider_slug: advanced-micro-devices
schema_file: json-schema/cloud-api-instance-metrics-schema.json
slug: cloud-api-instance-metrics
tags:
- AI
- Cloud Computing
- GPU
- HPC
- Machine Learning
- Semiconductor
title: InstanceMetrics
---
