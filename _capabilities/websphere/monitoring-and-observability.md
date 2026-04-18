---
consumed_apis:
- open-liberty
- admin-rest
- liberty-admin
description: Workflow for monitoring WebSphere environments combining health checks, metrics, performance data, logging, and batch job tracking from Open Liberty and traditional WAS APIs for operations teams.
layout: capability
name: WebSphere Monitoring and Observability
operations:
- description: Get Open Liberty overall health
  method: GET
  name: get-liberty-health
  path: /v1/health
- description: Get WAS server health
  method: GET
  name: get-was-health
  path: /v1/health
- description: Get all Open Liberty metrics
  method: GET
  name: get-all-metrics
  path: /v1/metrics
- description: Get Liberty admin metrics
  method: GET
  name: get-liberty-metrics
  path: /v1/metrics
- description: Get WAS performance monitoring data
  method: GET
  name: get-performance-data
  path: /v1/performance
- description: Get Liberty log messages
  method: GET
  name: get-log-messages
  path: /v1/logs
- description: List batch job instances
  method: GET
  name: list-batch-jobs
  path: /v1/batch-jobs
personas: []
provider_name: IBM WebSphere
provider_slug: websphere
search_terms:
- get was performance monitoring data
- list batch job instances
- check if liberty server is alive
- j2ee
- application server
- get batch job
- get batch job instance details
- get open liberty overall health
- metrics
- check if liberty server is ready for traffic
- get liberty health
- get was health
- get was server health status
- cloud native
- health check endpoints
- enterprise java
- batch job monitoring
- get liberty admin metrics
- get log messages
- monitoring
- get liberty metrics
- observability
- metrics collection
- performance data
- get was server health
- get liberty log messages
- get all metrics
- list batch jobs
- get liveness
- get recent liberty log messages
- microservices
- get performance data
- get log config
- get readiness
- log management
- list jakarta batch job instances
- middleware
- get open liberty overall health status
- get liberty logging configuration
- get all open liberty metrics
- ibm websphere
slug: monitoring-and-observability
tags:
- IBM WebSphere
- Monitoring
- Observability
- Metrics
tools:
- description: Get Open Liberty overall health status
  hints:
    readOnly: true
  name: get-liberty-health
- description: Check if Liberty server is ready for traffic
  hints:
    readOnly: true
  name: get-readiness
- description: Check if Liberty server is alive
  hints:
    readOnly: true
  name: get-liveness
- description: Get WAS server health status
  hints:
    readOnly: true
  name: get-was-health
- description: Get all Open Liberty metrics
  hints:
    readOnly: true
  name: get-all-metrics
- description: Get WAS performance monitoring data
  hints:
    readOnly: true
  name: get-performance-data
- description: Get recent Liberty log messages
  hints:
    readOnly: true
  name: get-log-messages
- description: Get Liberty logging configuration
  hints:
    readOnly: true
  name: get-log-config
- description: List Jakarta Batch job instances
  hints:
    readOnly: true
  name: list-batch-jobs
- description: Get batch job instance details
  hints:
    readOnly: true
  name: get-batch-job
---
