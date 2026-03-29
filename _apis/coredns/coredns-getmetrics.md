---
aid: coredns:coredns-getmetrics
name: Get Prometheus metrics
tags:
- Metrics
humanURL: 
properties: []
description: >-
  Returns all CoreDNS metrics in Prometheus text exposition format (version 0.0.4). The response includes counters, gauges, histograms, and summaries covering DNS request rates by server and zone, response code distributions, DNS query type breakdowns, cache hit rates, panics, and plugin-specific metrics such as forward latency and health check state. Requires the prometheus plugin to be configured in the Corefile.

---
