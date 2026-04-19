---
categories:
- fms
description: Spectral linting rules defining API design standards and conventions for Amazon Firewall Manager.
layout: rules
name: Amazon Firewall Manager API Rules
provider_name: Amazon Firewall Manager
provider_slug: amazon-firewall-manager
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: fms-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: fms-info-description
  severity: error
- description: All server URLs must use HTTPS
  given: $.servers[*].url
  name: fms-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: fms-operation-id-camel-case
  severity: warn
- description: GET and POST operations should define 200 response
  given: $.paths[*][get,post]
  name: fms-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fms-response-500
  severity: warn
- description: Operations accessing resources by ID should define 404
  given: $.paths[*~'\{[^}]+\}'][get,put,patch,delete].responses
  name: fms-response-404
  severity: warn
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: fms-parameter-description
  severity: error
- description: Path parameters must be marked as required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: fms-path-param-required
  severity: error
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: fms-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: fms-tags-title-case
  severity: warn
- description: Collection GET operationIds should start with 'list'
  given: $.paths[*~'[^}]$'].get.operationId
  name: fms-list-operation-prefix
  severity: warn
- description: PUT policy requests should define a request body
  given: $.paths[*].post.requestBody
  name: fms-put-policy-request
  severity: error
- description: Policies should document RemediationEnabled field in schema
  given: $.components.schemas.Policy.properties
  name: fms-policy-remediation-documented
  severity: warn
- description: SecurityServicePolicyData Type should define allowed enum values
  given: $.components.schemas.SecurityServicePolicyData.properties.Type
  name: fms-security-service-type-enum
  severity: warn
- description: DELETE operations should have a description
  given: $.paths[*].delete
  name: fms-delete-operation
  severity: warn
- description: Admin account endpoint should be documented
  given: $.paths
  name: fms-admin-account-documented
  severity: info
- description: Compliance endpoint should be documented
  given: $.paths
  name: fms-compliance-endpoint-documented
  severity: info
- description: Resource set endpoint should be documented
  given: $.paths
  name: fms-resource-set-documented
  severity: info
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: fms-schema-properties-defined
  severity: warn
rules_file: rules/amazon-firewall-manager-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-firewall-manager/refs/heads/main/rules/amazon-firewall-manager-spectral-rules.yml
severity_counts:
  error: 8
  hint: 0
  info: 3
  warn: 14
slug: amazon-firewall-manager-spectral-rules
tags:
- AWS
- Compliance
- Firewall
- Network Security
- Security
- Spectral
- Linting
- API Governance
---
