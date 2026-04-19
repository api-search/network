---
categories:
- delete
- examples
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
- tag
- tags
description: Spectral linting rules defining API design standards and conventions for Amazon DocumentDB.
layout: rules
name: Amazon DocumentDB API Rules
provider_name: Amazon DocumentDB
provider_slug: amazon-documentdb
rule_count: 28
rules:
- description: API title should include the provider name (Amazon DocumentDB).
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
- description: API info should include license information.
  given: $.info
  name: info-license-required
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
- description: Each server should have a description.
  given: $.servers[*]
  name: servers-description
  severity: info
- description: Every operation must have a summary.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-summary-required
  severity: error
- description: Operation summary should begin with the provider name (Amazon DocumentDB).
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
- description: OperationId should use camelCase.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-id-camel-case
  severity: warn
- description: Every operation must have at least one tag.
  given: $.paths[*][get,post,put,patch,delete,head,options]
  name: operation-tags-required
  severity: error
- description: Global tags array should be defined.
  given: $
  name: tags-global-defined
  severity: warn
- description: Each global tag should have a description.
  given: $.tags[*]
  name: tag-description-required
  severity: info
- description: All parameters must have a description.
  given: $..parameters[*]
  name: parameter-description-required
  severity: warn
- description: All parameters must have a schema.
  given: $..parameters[*]
  name: parameter-schema-required
  severity: error
- description: Every operation must define at least one 2xx response.
  given: $.paths[*][get,post,put,patch,delete]
  name: response-success-required
  severity: error
- description: Every response must have a description.
  given: $.paths[*][*].responses[*]
  name: response-description-required
  severity: error
- description: Schema properties should have descriptions.
  given: $.components.schemas[*].properties[*]
  name: schema-property-description
  severity: info
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
- description: DELETE operations should not have a request body.
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Descriptions should not be empty strings.
  given: $..description
  name: no-empty-descriptions
  severity: warn
- description: Operations should include examples for better documentation.
  given: $.paths[*][get,post,put,patch,delete]
  name: examples-encouraged
  severity: info
rules_file: rules/amazon-documentdb-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-documentdb/refs/heads/main/rules/amazon-documentdb-spectral-rules.yml
severity_counts:
  error: 11
  hint: 0
  info: 4
  warn: 13
slug: amazon-documentdb-spectral-rules
tags:
- Amazon Web Services
- AWS
- Database
- Document Database
- DocumentDB
- Managed Database
- MongoDB
- NoSQL
- Spectral
- Linting
- API Governance
---
