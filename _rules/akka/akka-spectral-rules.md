---
categories:
- get
- info
- openapi
- operation
- paths
- response
- servers
description: Spectral linting rules defining API design standards and conventions for Akka.
layout: rules
name: Akka API Rules
provider_name: Akka
provider_slug: akka
rule_count: 12
rules:
- description: ''
  given: $.info.title
  name: info-title-akka-prefix
  severity: warn
- description: ''
  given: $.info
  name: info-description-required
  severity: error
- description: ''
  given: $.info
  name: info-version-required
  severity: error
- description: ''
  given: $
  name: openapi-version-3
  severity: error
- description: ''
  given: $
  name: servers-defined
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-akka-prefix
  severity: warn
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: ''
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: ''
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: ''
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: ''
  given: $.paths[*]~
  name: paths-kebab-case
  severity: info
rules_file: rules/akka-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/akka/refs/heads/main/rules/akka-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 1
  warn: 4
slug: akka-spectral-rules
tags:
- Actor Model
- Distributed Systems
- Frameworks
- Java
- Microservices
- Reactive
- Scala
- Spectral
- Linting
- API Governance
---
