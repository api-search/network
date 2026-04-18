---
categories:
- delete
- get
- info
- operation
- pagination
- parameter
- paths
- response
- schema
- security
- tag
description: Spectral linting rules defining API design standards and conventions for Bitbucket.
layout: rules
name: Bitbucket API Rules
provider_name: Bitbucket
provider_slug: bitbucket
rule_count: 19
rules:
- description: Info object must have a title
  given: $.info
  name: info-title-required
  severity: error
- description: Info object must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: Info object must have a version
  given: $.info
  name: info-version-required
  severity: error
- description: Path segments should use kebab-case
  given: $.paths
  name: paths-kebab-case
  severity: warn
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Operations must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: warn
- description: Operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-operationid-required
  severity: error
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: warn
- description: Operation summaries should start with Bitbucket
  given: $.paths[*][get,post,put,patch,delete].summary
  name: operation-summary-prefix
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: warn
- description: Operations must define a success response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-success-required
  severity: error
- description: Schemas should have a type defined
  given: $.definitions[*]
  name: schema-type-required
  severity: warn
- description: Schema properties should use snake_case
  given: $.definitions[*].properties
  name: schema-property-snake-case
  severity: warn
- description: Global security should be defined
  given: $
  name: security-global-defined
  severity: warn
- description: GET operations must not have a request body
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: DELETE operations should not have a request body
  given: $.paths[*].delete
  name: delete-no-request-body
  severity: warn
- description: Paginated endpoints should use page-based pagination
  given: $.paths[*].get.parameters[?(@.name=='page')]
  name: pagination-use-page
  severity: info
- description: Tag names should use Title Case
  given: $.tags[*].name
  name: tag-title-case
  severity: warn
rules_file: rules/bitbucket-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/bitbucket/refs/heads/main/rules/bitbucket-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 2
  warn: 9
slug: bitbucket-spectral-rules
tags:
- Atlassian
- CI/CD
- Code Collaboration
- Code Review
- DevOps
- Git
- Pull Requests
- Repository Hosting
- Version Control
- Spectral
- Linting
- API Governance
---
