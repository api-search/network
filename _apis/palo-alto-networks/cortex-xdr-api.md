---
aid: palo-alto-networks:cortex-xdr-api
baseURL: https://api-{fqdn}/public_api/v1/
description: A REST API for the Cortex XDR extended detection and response platform providing programmatic access to incident management, alert handling, endpoint operations, and threat hunting. Key API modules include incidents (get, update, close), alerts (get details, exclusions), endpoints (isolate, unisolate, scan, get agent info), scripts (execute, get results), and audit logs.
humanURL: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Cortex XDR API
properties:
- type: Documentation
  url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API
- type: GettingStarted
  url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-APIs
- type: APIReference
  url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/API-Reference
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/openapi/palo-alto-cortex-xdr-api-openapi-original.yml
- type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/asyncapi/palo-alto-cortex-xdr-webhooks-asyncapi-original.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-incident-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-api-alert-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-api-audit-log-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-api-endpoint-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-api-filter-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-api-incident-detail-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-api-incident-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-api-sort-order-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-webhooks-alert-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xdr-webhooks-incident-payload-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-api-alert-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-api-audit-log-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-api-endpoint-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-api-filter-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-api-incident-detail-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-api-incident-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-api-sort-order-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-incident-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-webhooks-alert-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xdr-webhooks-incident-payload-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xdr-api-context.jsonld
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xdr-webhooks-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-api-alert-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-api-audit-log-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-api-endpoint-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-api-filter-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-api-incident-detail-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-api-incident-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-api-sort-order-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-incident-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-webhooks-alert-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xdr-webhooks-incident-payload-example.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xdr-context.jsonld
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: cortex-xdr-api
tags:
- Detection
- Endpoint Security
- Incidents
- Response
- XDR
---
