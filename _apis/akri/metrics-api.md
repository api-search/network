---
aid: akri:metrics-api
baseURL: http://localhost:8080
description: Akri exposes Prometheus metrics on port 8080 at /metrics for the Agent, Controller, and broker pods. Metrics include instance count, discovery response results and latency, and broker pod count. Supports Prometheus Operator ServiceMonitor for metric scraping.
humanURL: https://docs.akri.sh/
image: ''
layout: api
name: Akri Metrics API
properties:
- type: Documentation
  url: https://docs.akri.sh/
- type: GitHubRepository
  url: https://github.com/project-akri/akri
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/openapi/akri-metrics-openapi.yaml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-schema/akri-prometheus-metrics-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-schema/akri-akri-instance-count-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-schema/akri-akri-discovery-response-result-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-schema/akri-akri-discovery-response-time-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-schema/akri-akri-broker-pod-count-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-schema/akri-akri-configuration-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-schema/akri-akri-instance-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-structure/akri-prometheus-metrics-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-structure/akri-akri-instance-count-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-structure/akri-akri-discovery-response-result-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-structure/akri-akri-discovery-response-time-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-structure/akri-akri-broker-pod-count-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-structure/akri-akri-configuration-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/json-structure/akri-akri-instance-structure.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/examples/akri-prometheus-metrics-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/examples/akri-akri-instance-count-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/examples/akri-akri-discovery-response-result-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/examples/akri-akri-discovery-response-time-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/examples/akri-akri-broker-pod-count-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/examples/akri-akri-configuration-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/akri/refs/heads/main/examples/akri-akri-instance-example.json
provider_name: Akri
provider_slug: akri
slug: metrics-api
tags:
- Monitoring
- Prometheus
- Metrics
- Observability
---
