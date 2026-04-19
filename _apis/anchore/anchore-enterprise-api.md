---
aid: anchore:anchore-enterprise-api
baseURL: https://anchore.example.com/v2
description: REST API for Anchore Enterprise providing image analysis, vulnerability scanning, policy evaluation, SBOM generation, subscription management, and reporting endpoints for enterprise container security workflows.
humanURL: https://docs.anchore.com/current/docs/using/api_usage/
image: ''
layout: api
name: Anchore Enterprise API
properties:
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/openapi/anchore-enterprise-api.yaml
- type: Documentation
  url: https://docs.anchore.com/current/docs/using/api_usage/
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/json-schema/anchore-image-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/json-schema/anchore-vulnerability-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/json-schema/anchore-sbom-schema.json
- type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/rules/anchore-spectral-rules.yml
- type: NaftikoCapability
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/capabilities/anchore-container-security.yaml
- type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/json-structure/anchore-image-structure.json
- type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/json-ld/anchore-enterprise-api-context.jsonld
- type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/vocabulary/anchore-vocabulary.yaml
provider_name: Anchore
provider_slug: anchore
slug: anchore-enterprise-api
tags:
- Container Security
- Enterprise
- Policy
- Vulnerability Scanning
---
