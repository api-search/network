---
categories:
- fsx
description: Spectral linting rules defining API design standards and conventions for Amazon FSx.
layout: rules
name: Amazon FSx API Rules
provider_name: Amazon FSx
provider_slug: amazon-fsx
rule_count: 26
rules:
- description: API must include contact information
  given: $.info
  name: fsx-info-contact
  severity: warn
- description: API must have a description
  given: $.info
  name: fsx-info-description
  severity: error
- description: Server URLs must use HTTPS
  given: $.servers[*].url
  name: fsx-server-https
  severity: error
- description: Operations must have a summary
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-summary
  severity: error
- description: Operations should have a description
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-description
  severity: warn
- description: Operations must have at least one tag
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-tags
  severity: error
- description: Operations must have operationId
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-operation-id
  severity: error
- description: operationId should use camelCase
  given: $.paths[*][get,post,put,patch,delete].operationId
  name: fsx-operation-id-camel-case
  severity: warn
- description: POST operations should define 200 response
  given: $.paths[*][post]
  name: fsx-response-200
  severity: warn
- description: Operations should define 400 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-response-400
  severity: warn
- description: Operations should define 500 response
  given: $.paths[*][get,post,put,patch,delete]
  name: fsx-response-500
  severity: warn
- description: Schema components should have descriptions
  given: $.components.schemas[*]
  name: fsx-schema-description
  severity: warn
- description: Operation tags should use Title Case
  given: $.paths[*][*].tags[*]
  name: fsx-tags-title-case
  severity: warn
- description: FileSystem schema should define FileSystemType field
  given: $.components.schemas.FileSystem.properties
  name: fsx-filesystem-type-documented
  severity: warn
- description: FileSystem lifecycle should define enum values
  given: $.components.schemas.FileSystem.properties.Lifecycle
  name: fsx-lifecycle-enum
  severity: info
- description: Backup type should define enum values
  given: $.components.schemas.Backup.properties.Type
  name: fsx-backup-type-enum
  severity: info
- description: Parameters must have descriptions
  given: $.paths[*][get,post,put,patch,delete].parameters[*]
  name: fsx-parameter-description
  severity: error
- description: Path parameters must be required
  given: $.paths[*][get,post,put,patch,delete].parameters[?(@.in=='path')]
  name: fsx-path-param-required
  severity: error
- description: Object schemas should define properties
  given: $.components.schemas[?(@.type=='object')]
  name: fsx-schema-properties
  severity: warn
- description: POST request bodies should define application/json content
  given: $.paths[*].post.requestBody.content
  name: fsx-request-body-json
  severity: warn
- description: POST creation operationIds should start with 'create'
  given: $.paths[*].post.operationId
  name: fsx-create-prefix
  severity: warn
- description: DELETE operations should have a description
  given: $.paths[*].delete
  name: fsx-delete-operation
  severity: warn
- description: FileSystem schema should document StorageCapacity
  given: $.components.schemas.FileSystem.properties
  name: fsx-storage-capacity-documented
  severity: warn
- description: Resource ARN field should be named ResourceARN
  given: $.components.schemas[*].properties.ResourceARN
  name: fsx-resource-arn-consistent
  severity: info
- description: Tag schema must require Key field
  given: $.components.schemas.Tag.required
  name: fsx-tag-schema-required
  severity: warn
- description: StorageVirtualMachine must reference FileSystemId
  given: $.components.schemas.StorageVirtualMachine.required
  name: fsx-svm-filesystem-required
  severity: warn
rules_file: rules/amazon-fsx-spectral-rules.yml
rules_url: https://raw.githubusercontent.com/api-evangelist/amazon-fsx/refs/heads/main/rules/amazon-fsx-spectral-rules.yml
severity_counts:
  error: 7
  hint: 0
  info: 3
  warn: 16
slug: amazon-fsx-spectral-rules
tags:
- AWS
- File Systems
- Lustre
- NetApp
- OpenZFS
- Storage
- Windows
- Spectral
- Linting
- API Governance
---
