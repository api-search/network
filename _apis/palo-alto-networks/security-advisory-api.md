---
aid: palo-alto-networks:security-advisory-api
baseURL: https://security.paloaltonetworks.com
description: A REST API (currently in beta) for programmatically querying Palo Alto Networks security advisories published by the Product Security Incident Response Team (PSIRT). The API supports filtering advisories by CVE ID, severity, product, and date range. Returns advisory details including vulnerability descriptions, affected versions, CVSS scores, and remediation guidance. Also available as an RSS feed for continuous monitoring of new security advisories.
humanURL: https://security.paloaltonetworks.com/api
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: api
name: Security Advisory API
properties:
- type: Documentation
  url: https://security.paloaltonetworks.com/api
- type: Feed
  url: https://security.paloaltonetworks.com/rss.xml
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/openapi/palo-alto-security-advisory-api-openapi-original.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/palo-alto-security-advisory-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/security-advisory-api-advisory-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/security-advisory-api-affected-product-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-schema/security-advisory-api-product-schema.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/palo-alto-security-advisory-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/security-advisory-api-advisory-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/security-advisory-api-affected-product-structure.json
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-structure/security-advisory-api-product-structure.json
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-security-advisory-api-context.jsonld
- type: JSON-LD
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/json-ld/palo-alto-security-advisory-context.jsonld
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/palo-alto-security-advisory-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/security-advisory-api-advisory-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/security-advisory-api-affected-product-example.json
- type: Example
  url: https://raw.githubusercontent.com/api-evangelist/palo-alto-networks/refs/heads/main/examples/security-advisory-api-product-example.json
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
slug: security-advisory-api
tags:
- CVE
- Patching
- PSIRT
- Security Advisories
- Vulnerabilities
---
