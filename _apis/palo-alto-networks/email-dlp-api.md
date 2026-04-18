---
aid: palo-alto-networks:email-dlp-api
baseURL: https://api.example.com
description: A REST API for programmatically reviewing and managing Email DLP incidents detected across enterprise email channels. The API supports retrieving incident details, updating verdicts on flagged emails, and managing remediation workflows for data loss prevention violations in email traffic. Uses region-specific endpoints and requires SOC_Admin, Superuser, or Data Security Administrator roles for access.
humanURL: https://pan.dev/email-dlp/api/
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Email DLP API
properties:
- type: Documentation
  url: https://pan.dev/email-dlp/api/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/openapi/palo-alto-email-dlp-api-openapi-original.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/email-dlp-api-email-attachment-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/email-dlp-api-email-dlp-incident-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/email-dlp-api-email-recipient-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/email-dlp-api-email-attachment-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/email-dlp-api-email-dlp-incident-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/email-dlp-api-email-recipient-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-email-dlp-api-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/email-dlp-api-email-attachment-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/email-dlp-api-email-dlp-incident-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/email-dlp-api-email-recipient-example.json
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: email-dlp-api
tags:
- Compliance
- Data Protection
- DLP
- Email Security
- Incident Management
---
