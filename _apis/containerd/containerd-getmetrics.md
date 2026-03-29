---
aid: containerd:containerd-getmetrics
name: Get Prometheus metrics
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Returns all containerd metrics in Prometheus text exposition format. Metrics include gRPC server request counts and latency histograms (when grpc_histogram is enabled), snapshotter usage statistics, content store byte counts, task start and exit counters, and container count gauges. Each metric is labeled by namespace, snapshotter, or plugin type as appropriate. Requires the metrics address to be configured in the containerd config.toml.

---
