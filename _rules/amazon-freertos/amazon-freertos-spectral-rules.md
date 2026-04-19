---
categories:
- freertos
description: Spectral linting rules defining API design standards and conventions for Amazon FreeRTOS.
layout: rules
name: Amazon FreeRTOS API Rules
provider_name: Amazon FreeRTOS
provider_slug: amazon-freertos
rule_count: 25
rules:
- description: API must include contact information
  given: $.info
  name: freertos-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: freertos-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: freertos-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: freertos-operation-id-camel-case
  severity: warn
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: freertos-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: freertos-response-500
  severity: warn
- description: Resource-by-ID operations should define 404
  given: $.paths[*~'\{[^}]+\}'][get,put,patch,delete].responses
  name: freertos-response-404
  severity: warn
- description: DELETE operations should return 204
  given: $.paths[*].delete
  name: freertos-delete-204
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: freertos-parameter-description
  severity: error
- description: Path parameters must be required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: freertos-path-param-required
  severity: error
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: freertos-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: freertos-tags-title-case
  severity: warn
- description: OTA update schema must require targets
  given: $.components.schemas.OtaUpdate.required
  name: freertos-ota-targets-required
  severity: warn
- description: OTA update status should define enum values
  given: $.components.schemas.OtaUpdate.properties.otaUpdateStatus
  name: freertos-ota-status-enum
  severity: warn
- description: Software configuration must document hardware platform
  given: $.components.schemas.SoftwareConfiguration.required
  name: freertos-sw-config-hardware-platform
  severity: warn
- description: POST creation operationIds should start with 'create'
  given: $.paths[*].post.operationId
  name: freertos-create-prefix
  severity: warn
- description: Collection GET operationIds should start with 'list'
  given: $.paths[*~'[^}]$'].get.operationId
  name: freertos-list-prefix
  severity: warn
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: freertos-schema-properties
  severity: warn
- description: POST/PUT request bodies should define application/json
  given: $.paths[*][post,put].requestBody.content
  name: freertos-request-body-json
  severity: warn
- description: OTA update create request should document protocols
  given: $.components.schemas.CreateOtaUpdateRequest.properties
  name: freertos-ota-protocols-documented
  severity: info
rules_file: rules/amazon-freertos-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-freertos/refs/heads/main/rules/amazon-freertos-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 2
  warn: 16
slug: amazon-freertos-spectral-rules
tags:
- AWS
- Embedded Systems
- IoT
- Microcontrollers
- RTOS
- Spectral
- Linting
- API Governance
---
