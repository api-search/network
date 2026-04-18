---
aid: palo-alto-networks:dns-security-api
baseURL: https://api.dns.service.paloaltonetworks.com
description: A REST API (currently in beta) for retrieving DNS domain details, categorization information, and contextual network access statistics from the Palo Alto Networks DNS Security service. Supports querying domain reputation, categorization data, and related threat intelligence. Requires a DNS Security subscription and uses API key authentication via the X-DNS-API-APIKEY header.
humanURL: https://pan.dev/dns-security/api/
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: DNS Security API
properties:
- type: Documentation
  url: https://pan.dev/dns-security/api/
- type: GettingStarted
  url: https://pan.dev/cdss/docs/getstarted/
- type: Authentication
  url: https://pan.dev/cdss/docs/authentication/
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/openapi/palo-alto-dns-security-api-openapi-original.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/dns-security-api-domain-detail-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/dns-security-api-network-stats-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/dns-security-api-domain-detail-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/dns-security-api-network-stats-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-dns-security-api-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/dns-security-api-domain-detail-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/dns-security-api-network-stats-example.json
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: dns-security-api
tags:
- Beta
- DNS
- Domain Categorization
- Domain Security
- Threat Intelligence
---
