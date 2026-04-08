---
aid: triton:triton-getmetrics
name: Triton Inference Server Get Prometheus metrics
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Retrieve all available metrics in Prometheus text exposition format. Includes server-level metrics (request counts, latencies, GPU utilization, memory usage) and per-model metrics (inference counts, queue times, compute times). Metrics are labeled with model name, version, GPU UUID, and other dimensions.  Key metric families include: - `nv_inference_request_success` - Successful inference request count - `nv_inference_request_failure` - Failed inference request count - `nv_inference_count` - ...

---
