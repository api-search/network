---
categories:
- amazon
description: Spectral linting rules defining API design standards and conventions for Amazon App Mesh.
layout: rules
name: Amazon App Mesh API Rules
provider_name: Amazon App Mesh
provider_slug: amazon-app-mesh
rule_count: 3
rules:
- description: API must have a title.
  given: $.info
  name: amazon-app-mesh-info-title
  severity: error
- description: Operations must have summaries.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-app-mesh-operation-summary
  severity: error
- description: Operations must have operationIds.
  given: $.paths[*][get,post,put,patch,delete]
  name: amazon-app-mesh-operation-id
  severity: error
rules_file: rules/amazon-app-mesh-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-app-mesh/refs/heads/main/rules/amazon-app-mesh-spectral-rules.yml
severity_counts:
  error: 3
  hint: 0
  info: 0
  warn: 0
slug: amazon-app-mesh-spectral-rules
tags:
- AWS
- Microservices
- Networking
- Service Mesh
- Spectral
- Linting
- API Governance
---
