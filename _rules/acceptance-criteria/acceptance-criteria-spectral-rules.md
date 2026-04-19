---
categories:
- ac
description: Spectral linting rules defining API design standards and conventions for Acceptance Criteria.
layout: rules
name: Acceptance Criteria API Rules
provider_name: Acceptance Criteria
provider_slug: acceptance-criteria
rule_count: 27
rules:
- description: APIs managing acceptance criteria must require authentication
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-require-security-scheme
  severity: error
- description: API paths must use kebab-case naming
  given: $.paths[*]~
  name: ac-path-kebab-case
  severity: warn
- description: API paths must not have trailing slashes
  given: $.paths[*]~
  name: ac-no-trailing-slash
  severity: warn
- description: All operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-summary
  severity: error
- description: All operations must have an operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-operation-id
  severity: error
- description: OperationIds must use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: ac-operation-id-camel-case
  severity: warn
- description: All operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-tags
  severity: warn
- description: All operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: ac-operations-require-description
  severity: info
- description: GET operations must define a 200 response
  given: $.paths[*].get.responses
  name: ac-require-200-response
  severity: error
- description: POST operations should define a 201 created response
  given: $.paths[*].post.responses
  name: ac-require-201-on-post
  severity: warn
- description: Operations must define a 401 unauthorized response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: ac-require-401-response
  severity: warn
- description: Operations on parameterized paths must define a 404 response
  given: $.paths[?(@~.match(/\{.*\}/))][get,put,patch,delete].responses
  name: ac-require-404-on-parameterized-paths
  severity: warn
- description: All operations must define a 500 server error response
  given: $.paths[*][get,post,put,patch,delete].responses
  name: ac-require-500-response
  severity: warn
- description: All schema components must have a description
  given: $.components.schemas[*]
  name: ac-schema-require-description
  severity: warn
- description: Schema properties should have descriptions for self-documenting APIs
  given: $.components.schemas[*].properties[*]
  name: ac-schema-properties-require-description
  severity: info
- description: Resource schemas must include an id property
  given: $.components.schemas[?(!@.title =~ /(List|Request)$/)]
  name: ac-require-id-property
  severity: warn
- description: Timestamp fields must use date-time format
  given: $.components.schemas[*].properties[?(@.description =~ /[Tt]imestamp|At$|[Dd]ate/)]
  name: ac-timestamp-format
  severity: error
- description: Gherkin-format acceptance criteria must include given, when, and then fields
  given: $.components.schemas.AcceptanceCriterion.properties
  name: ac-gherkin-given-when-then
  severity: info
- description: Status fields must use defined enum values
  given: $.components.schemas[*].properties.status
  name: ac-status-enum-values
  severity: warn
- description: Priority fields must use defined enum values
  given: $.components.schemas[*].properties.priority
  name: ac-priority-enum-values
  severity: warn
- description: Request bodies must use application/json content type
  given: $.paths[*][post,put,patch].requestBody.content
  name: ac-require-json-request-body
  severity: error
- description: Success responses must return application/json
  given: $.paths[*][get,post,put,patch].responses[200,201].content
  name: ac-require-json-response
  severity: error
- description: List schema responses must include a total count
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: ac-list-responses-require-total
  severity: warn
- description: List schema responses must include page for pagination
  given: $.components.schemas[?(@.title =~ /List$/)]
  name: ac-list-responses-require-page
  severity: warn
- description: API spec must include a version
  given: $.info
  name: ac-info-require-version
  severity: error
- description: API spec must include a description
  given: $.info
  name: ac-info-require-description
  severity: error
- description: API spec should include contact information
  given: $.info
  name: ac-info-require-contact
  severity: info
rules_file: rules/acceptance-criteria-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/acceptance-criteria/refs/heads/main/rules/acceptance-criteria-spectral-rules.yml
severity_counts:
  error: 9
  hint: 0
  info: 4
  warn: 14
slug: acceptance-criteria-spectral-rules
tags:
- Agile
- Behavior Driven Development
- Gherkin
- Quality Assurance
- Requirements
- Testing
- User Stories
- Spectral
- Linting
- API Governance
---
