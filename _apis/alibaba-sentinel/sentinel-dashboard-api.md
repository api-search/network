---
aid: alibaba-sentinel:sentinel-dashboard-api
baseURL: https://localhost:8080
description: The Sentinel Dashboard API provides a REST interface for the Sentinel dashboard application, which allows real-time monitoring of clients and dynamic configuration of flow control, circuit breaking, and system protection rules. The dashboard supports cluster aggregation of runtime info for up to 500 nodes and enables operators to manage resources and rules without application restarts.
humanURL: https://sentinelguard.io/en-us/docs/dashboard.html
image: ''
layout: api
name: Sentinel Dashboard API
properties:
- type: Documentation
  url: https://sentinelguard.io/en-us/docs/dashboard.html
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/alibaba-sentinel/refs/heads/main/openapi/sentinel-dashboard-api.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/alibaba-sentinel/refs/heads/main/json-schema/flow-rule.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/alibaba-sentinel/refs/heads/main/json-schema/degrade-rule.json
provider_name: Alibaba Sentinel
provider_slug: alibaba-sentinel
slug: sentinel-dashboard-api
tags:
- Dashboard
- Monitoring
- Flow Control
- Circuit Breaker
- Rate Limiting
---
