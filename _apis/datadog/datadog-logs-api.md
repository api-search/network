---
aid: datadog:datadog-logs-api
baseURL: https://api.datadoghq.com
description: The Logs API allows you to search and send log events to the Datadog platform over HTTP. It supports querying and aggregating log data from the Log Management product.
humanURL: https://docs.datadoghq.com/api/latest/logs/
image: https://imgix.datadoghq.com/img/dd_logo_n_70x75.png
layout: api
name: Datadog Logs API
properties:
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/openapi/datadog-logs-openapi.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/datadog/refs/heads/main/json-schema/datadog-log-event-schema.json
- type: Documentation
  url: https://docs.datadoghq.com/api/latest/logs/
- type: Reference
  url: https://docs.datadoghq.com/logs/
provider_name: Datadog
provider_slug: datadog
slug: datadog-logs-api
tags:
- Log Management
- Logs
- Search
---
