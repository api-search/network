---
aid: new-relic:new-relic-event-api
baseURL: https://insights-collector.newrelic.com/v1/accounts
description: The New Relic Event API allows you to send custom event data to the New Relic platform via HTTP POST. Custom events submitted through this API can be queried and visualized using NRQL, making it suitable for tracking arbitrary business or application events.
humanURL: https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/
image: https://newrelic.com/themes/custom/erno/assets/mediakit/new_relic_logo_horizontal.png
layout: api
name: New Relic Event API
properties:
- type: Documentation
  url: https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/
- type: Authentication
  url: https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/openapi/new-relic-event-api-openapi.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-schema/new-relic-event-payload-schema.json
- type: RateLimits
  url: https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/data-requirements-limits-custom-event-data/
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-schema/event-api-success-response-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-schema/event-api-custom-event-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-schema/event-api-event-payload-schema.json
- type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/new-relic/refs/heads/main/json-ld/new-relic-event-api-context.jsonld
provider_name: New Relic
provider_slug: new-relic
slug: new-relic-event-api
tags:
- Custom Data
- Events
- Ingest
- Telemetry
---
