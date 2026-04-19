---
categories:
- delete
- get
- info
- 'no'
- openapi
- operation
- parameter
- response
- schema
- security
- servers
description: Spectral linting rules defining API design standards and conventions for Amazon Elastic Load Balancing.
layout: rules
name: Amazon Elastic Load Balancing API Rules
provider_name: Amazon Elastic Load Balancing
provider_slug: amazon-elastic-load-balancing
rule_count: 20
rules:
- description: OpenAPI info must have a title.
  given: $.info
  name: info-title-required
  severity: error
- description: OpenAPI info must have a description.
  given: $.info
  name: info-description-required
  severity: warn
- description: OpenAPI info must have a version.
  given: $.info
  name: info-version-required
  severity: error
- description: Must use OpenAPI 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: OpenAPI must define at least one server.
  given: $
  name: servers-required
  severity: error
- description: All server URLs must use HTTPS.
  given: $.servers[*]
  name: servers-https-required
  severity: error
- description: All operations must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: All operations must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: All operations must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-operationId-required
  severity: error
- description: operationId must use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options].operationId
  name: operation-operationId-camelCase
  severity: warn
- description: All operations must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: warn
- description: All parameters must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options].parameters[*]
  name: parameter-description-required
  severity: warn
- description: All operations must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete,head,options].responses
  name: operation-success-response-required
  severity: error
- description: All responses must have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options].responses[*]
  name: response-description-required
  severity: error
- description: Security schemes must be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: Schema properties should specify a type.
  given: $.components.schemas[*].properties[*]
  name: schema-properties-have-types
  severity: warn
- description: Top-level component schemas should have a description.
  given: $.components.schemas[*]
  name: schema-description-required
  severity: info
- description: GET operations must not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions must not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amazon-elastic-load-balancing-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-load-balancing/refs/heads/main/rules/amazon-elastic-load-balancing-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 1
  warn: 9
slug: amazon-elastic-load-balancing-spectral-rules
tags:
- Amazon Web Services
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
- Spectral
- Linting
- API Governance
---
