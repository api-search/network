---
consumed_apis:
- xray
description: Unified workflow for developers and operations teams to analyze distributed traces, visualize service maps, manage sampling rules, and investigate application performance insights using Amazon X-Ray.
layout: capability
name: Amazon X-Ray Distributed Tracing
operations:
- description: Get trace summaries for a time range.
  method: GET
  name: get-trace-summaries
  path: /v1/traces
- description: Get the service map.
  method: GET
  name: get-service-graph
  path: /v1/service-map
- description: Get sampling rules.
  method: GET
  name: get-sampling-rules
  path: /v1/sampling-rules
- description: Get trace groups.
  method: GET
  name: get-groups
  path: /v1/groups
- description: Get insight summaries.
  method: GET
  name: get-insight-summaries
  path: /v1/insights
personas: []
provider_name: Amazon X-Ray
provider_slug: amazon-xray
search_terms:
- get sampling rules.
- distributed tracing
- get the service map.
- service dependency visualization.
- batch get traces
- get summaries of x-ray insights identifying anomalies and performance issues.
- application performance insights.
- get insight summaries.
- get trace summaries for a time range.
- trace filtering groups.
- root cause analysis using distributed trace data
- monitors service health and performance using x-ray.
- get the service map showing inter-service dependencies and request flow.
- latency analysis and bottleneck identification
- observability
- get service graph
- get all trace sampling rules to understand data collection configuration.
- analyzes traces to debug application issues.
- monitoring
- Site Reliability Engineer
- debugging
- application tracing and service map visualization
- Developer
- application performance
- trace sampling configuration.
- get sampling rules
- workflow for developers and operations teams to analyze traces, service maps, sampling rules, groups, and performance insights.
- get summaries of distributed traces for a specified time range.
- get insight summaries
- retrieve complete trace documents for specific trace ids.
- aws
- trace data access and analysis.
- get trace groups.
- get trace summaries
- get groups
- get x-ray groups used to filter and organize traces.
slug: distributed-tracing
tags:
- AWS
- Distributed Tracing
- Observability
- Application Performance
- Debugging
tools:
- description: Get summaries of distributed traces for a specified time range.
  hints:
    openWorld: true
    readOnly: true
  name: get-trace-summaries
- description: Retrieve complete trace documents for specific trace IDs.
  hints:
    openWorld: false
    readOnly: true
  name: batch-get-traces
- description: Get the service map showing inter-service dependencies and request flow.
  hints:
    openWorld: true
    readOnly: true
  name: get-service-graph
- description: Get all trace sampling rules to understand data collection configuration.
  hints:
    openWorld: true
    readOnly: true
  name: get-sampling-rules
- description: Get X-Ray groups used to filter and organize traces.
  hints:
    openWorld: true
    readOnly: true
  name: get-groups
- description: Get summaries of X-Ray insights identifying anomalies and performance issues.
  hints:
    openWorld: true
    readOnly: true
  name: get-insight-summaries
---
