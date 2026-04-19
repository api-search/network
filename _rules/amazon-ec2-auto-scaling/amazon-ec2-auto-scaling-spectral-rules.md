---
categories:
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
description: Spectral linting rules defining API design standards and conventions for Amazon EC2 Auto Scaling.
layout: rules
name: Amazon EC2 Auto Scaling API Rules
provider_name: Amazon EC2 Auto Scaling
provider_slug: amazon-ec2-auto-scaling
rule_count: 19
rules:
- description: API title should include the provider name (Amazon EC2 Auto Scaling).
  given: $.info
  name: info-title-matches-provider
  severity: warn
- description: API info must include a description.
  given: $.info
  name: info-description-required
  severity: error
- description: API version must be defined.
  given: $.info
  name: info-version-required
  severity: error
- description: API info should include contact information.
  given: $.info
  name: info-contact-required
  severity: warn
- description: OpenAPI specification should use version 3.x.
  given: $
  name: openapi-version-3
  severity: error
- description: At least one server must be defined.
  given: $
  name: servers-defined
  severity: error
- description: Server URLs should use HTTPS.
  given: $.servers[*]
  name: servers-https
  severity: warn
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summary should begin with the provider name (Amazon EC2 Auto Scaling).
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-provider-prefix
  severity: warn
- description: Every operation should have a description.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-description-required
  severity: warn
- description: Every operation must have an operationId.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: All parameters must have a description.
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema.
  given: $..parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schemas should define a type.
  given: $.components.schemas[*]
  name: schema-type-defined
  severity: warn
- description: Security schemes should be defined in components.
  given: $.components
  name: security-schemes-defined
  severity: warn
- description: GET operations should not have a request body.
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: Descriptions should not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
rules_file: rules/amazon-ec2-auto-scaling-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-ec2-auto-scaling/refs/heads/main/rules/amazon-ec2-auto-scaling-spectral-rules.yml
severity_counts:
  error: 10
  hint: 0
  info: 0
  warn: 9
slug: amazon-ec2-auto-scaling-spectral-rules
tags:
- Amazon Web Services
- Auto Scaling
- AWS
- Compute
- EC2
- High Availability
- Scaling
- Spectral
- Linting
- API Governance
---
