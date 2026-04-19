---
categories:
- async
- get
- global
- info
- list
- oauth2
- openapi
- operation
- parameter
- paths
- response
- security
- servers
- tags
description: Spectral linting rules defining API design standards and conventions for Allianz Technology Standards.
layout: rules
name: Allianz Technology Standards API Rules
provider_name: Allianz Technology Standards
provider_slug: allianz-technology-standards
rule_count: 22
rules:
- description: API title must start with "Allianz"
  given: $.info.title
  name: info-title-allianz-prefix
  severity: warn
- description: API info must have a description
  given: $.info
  name: info-description-required
  severity: error
- description: API info must define a version
  given: $.info
  name: info-version-required
  severity: error
- description: Specs must use OpenAPI 3.x (API-first standard)
  given: $.openapi
  name: openapi-version-3
  severity: error
- description: At least one server must be defined
  given: $
  name: servers-defined
  severity: error
- description: Server URLs must use HTTPS (Allianz security standard)
  given: $.servers[*].url
  name: servers-https
  severity: error
- description: Paths must not have trailing slashes
  given: $.paths
  name: paths-no-trailing-slash
  severity: error
- description: Every operation must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-summary-required
  severity: error
- description: Every operation must have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-description-required
  severity: error
- description: Every operation must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-id-required
  severity: error
- description: Every operation must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: operation-tags-required
  severity: error
- description: List operations should support pageSize query parameter (Allianz pagination standard)
  given: $.paths[*].get.parameters[*].name
  name: list-operations-page-size
  severity: warn
- description: List operations should support page query parameter (Allianz pagination standard)
  given: $.paths[*].get.parameters[*].name
  name: list-operations-page-param
  severity: warn
- description: Async POST operations should return 202 Accepted (Allianz async pattern)
  given: $.paths[*].post.responses
  name: async-post-returns-202
  severity: info
- description: Security schemes must be defined (OAuth2 standard)
  given: $.components
  name: security-schemes-defined
  severity: error
- description: OAuth2 security scheme should be defined (Allianz OAuth2 standard)
  given: $.components.securitySchemes
  name: oauth2-scheme-required
  severity: warn
- description: Global security should be defined
  given: $
  name: global-security-defined
  severity: warn
- description: GET operations must not have request bodies
  given: $.paths[*].get
  name: get-no-request-body
  severity: error
- description: All responses must have descriptions
  given: $.paths[*][get,post,put,patch,delete].responses[*]
  name: response-description-required
  severity: error
- description: Operations should define a 401 response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: response-401-required
  severity: warn
- description: Global tags array should be defined
  given: $
  name: tags-defined
  severity: warn
- description: All parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: parameter-description-required
  severity: error
rules_file: rules/allianz-technology-standards-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/allianz-technology-standards/refs/heads/main/rules/allianz-technology-standards-spectral-rules.yml
severity_counts:
  error: 14
  hint: 0
  info: 1
  warn: 7
slug: allianz-technology-standards-spectral-rules
tags:
- Best Practices
- Enterprise Architecture
- Guidelines
- Software Development
- Technology Standards
- API Design
- OpenAPI
- Spectral
- Linting
- API Governance
---
