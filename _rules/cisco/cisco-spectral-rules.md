---
categories:
- info
- operation
- parameter
- paths
- response
- schema
- security
description: Spectral linting rules defining API design standards and conventions for Cisco.
layout: rules
name: Cisco API Rules
provider_name: Cisco
provider_slug: cisco
rule_count: 12
rules:
- description: Info title should start with "Cisco"
  given: $.info
  name: info-title-prefix
  severity: warn
- description: Info description must be present
  given: $.info
  name: info-description-required
  severity: error
- description: Paths should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationId-required
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operation summaries should start with "Cisco"
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-prefix
  severity: warn
- description: Every operation must have tags
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Every parameter must have a description
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Every operation must have a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Global security must be defined
  given: $
  name: security-global-defined
  severity: error
- description: API keys should be sent in headers
  given: $.components.securitySchemes[*]
  name: security-api-key-header
  severity: warn
- description: Schema properties should have descriptions
  given: $.components.schemas[*].properties[*]
  name: schema-properties-description
  severity: info
rules_file: rules/cisco-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/cisco/refs/heads/main/rules/cisco-spectral-rules.yml
severity_counts:
  error: 5
  hint: 0
  info: 1
  warn: 6
slug: cisco-spectral-rules
tags:
- Collaboration
- Enterprise
- Networking
- Security
- SD-WAN
- Spectral
- Linting
- API Governance
---
