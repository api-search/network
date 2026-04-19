---
categories:
- anchore
description: Spectral linting rules defining API design standards and conventions for Anchore.
layout: rules
name: Anchore API Rules
provider_name: Anchore
provider_slug: anchore
rule_count: 9
rules:
- description: OpenAPI info object must have a description
  given: $.info
  name: anchore-openapi-info-description
  severity: error
- description: OpenAPI info object must have a version
  given: $.info
  name: anchore-openapi-info-version
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: anchore-operation-operationId
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: anchore-operation-summary
  severity: warn
- description: Every GET operation must have a 200 response
  given: $.paths[*].get.responses
  name: anchore-response-200
  severity: warn
- description: API must define security requirements
  given: $
  name: anchore-security-defined
  severity: error
- description: Schema properties must have a type
  given: $.components.schemas[*].properties[*]
  name: anchore-schema-type
  severity: warn
- description: Vulnerability severity must use standard values
  given: $.components.schemas.Vulnerability.properties.severity
  name: anchore-severity-enum
  severity: warn
- description: Image digest fields should follow SHA256 format
  given: $.components.schemas[*].properties.imageDigest
  name: anchore-digest-format
  severity: hint
rules_file: rules/anchore-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/anchore/refs/heads/main/rules/anchore-spectral-rules.yml
severity_counts:
  error: 4
  hint: 1
  info: 0
  warn: 4
slug: anchore-spectral-rules
tags:
- Container Security
- Containers
- SBOM
- Software Supply Chain
- Vulnerability Scanning
- Spectral
- Linting
- API Governance
---
