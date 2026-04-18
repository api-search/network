---
aid: palo-alto-networks:cortex-xsiam-api
baseURL: https://api-{fqdn}/public_api/v1/
description: A REST API for Cortex XSIAM, the AI-driven security operations platform that combines SIEM, XDR, SOAR, and ASM capabilities. The API provides endpoints for incident management, alert handling, data ingestion configuration, XQL query execution, asset management, and automation rule management. Shares endpoint patterns with Cortex XDR but includes additional capabilities for log collection configuration, data model management, and AI-assisted investigation.
humanURL: https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM-REST-API
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Cortex XSIAM API
properties:
- type: Documentation
  url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XSIAM-REST-API
- type: GettingStarted
  url: https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-APIs
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/openapi/palo-alto-cortex-xsiam-api-openapi-original.yml
- type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/asyncapi/palo-alto-cortex-xsiam-data-ingestion-asyncapi-original.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-api-alert-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-api-asset-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-api-audit-log-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-api-endpoint-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-api-filter-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-api-incident-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-api-sort-order-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-data-ingestion-event-data-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-data-ingestion-log-data-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/cortex-xsiam-data-ingestion-xdr-data-payload-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-api-alert-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-api-asset-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-api-audit-log-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-api-endpoint-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-api-filter-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-api-incident-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-api-sort-order-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-data-ingestion-event-data-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-data-ingestion-log-data-payload-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/cortex-xsiam-data-ingestion-xdr-data-payload-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xsiam-api-context.jsonld
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-cortex-xsiam-data-ingestion-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-api-alert-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-api-asset-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-api-audit-log-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-api-endpoint-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-api-filter-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-api-incident-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-api-sort-order-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-data-ingestion-event-data-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-data-ingestion-log-data-payload-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/cortex-xsiam-data-ingestion-xdr-data-payload-example.json
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: cortex-xsiam-api
tags:
- AI-Driven SOC
- Automation
- Security Analytics
- SIEM
- XDR
---
