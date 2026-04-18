---
aid: palo-alto-networks:wildfire-api
baseURL: https://wildfire.paloaltonetworks.com/publicapi/
description: A cloud-based API for submitting files, URLs, and links for advanced malware analysis in the WildFire sandbox environment. The API returns threat verdicts (benign, malware, grayware, phishing) and detailed analysis reports including behavioral indicators, network activity, and file artifacts. Supports file submission via multipart form upload, verdict queries by hash (MD5, SHA-256), and retrieval of PCAP files and detailed analysis reports.
humanURL: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: WildFire API
properties:
- type: Documentation
  url: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api
- type: GettingStarted
  url: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api/get-started-with-the-wildfire-api
- type: APIReference
  url: https://docs.paloaltonetworks.com/wildfire/u-v/wildfire-api
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/openapi/palo-alto-wildfire-api-openapi-original.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/wildfire-api-analysis-report-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/wildfire-api-bulk-verdict-response-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/wildfire-api-sandbox-report-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/wildfire-api-submit-response-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/wildfire-api-verdict-response-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/wildfire-api-analysis-report-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/wildfire-api-bulk-verdict-response-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/wildfire-api-sandbox-report-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/wildfire-api-submit-response-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/wildfire-api-verdict-response-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-wildfire-api-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/wildfire-api-analysis-report-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/wildfire-api-bulk-verdict-response-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/wildfire-api-sandbox-report-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/wildfire-api-submit-response-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/wildfire-api-verdict-response-example.json
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: wildfire-api
tags:
- File Analysis
- Malware Analysis
- Sandbox
- Threat Prevention
- Verdicts
---
