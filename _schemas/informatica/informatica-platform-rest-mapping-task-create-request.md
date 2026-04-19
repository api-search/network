---
description: Request body for creating a new mapping task.
layout: schema
name: MappingTaskCreateRequest
properties_list:
- description: The resource type identifier.
  name: '@type'
  type: string
- description: The name for the new mapping task.
  name: name
  type: string
- description: A description of the mapping task.
  name: description
  type: string
- description: The ID of the mapping to execute.
  name: mappingId
  type: string
- description: The runtime environment to use for execution.
  name: runtimeEnvironmentId
  type: string
- description: The schedule to associate with the task.
  name: scheduleId
  type: string
- description: The command to run before the task.
  name: preProcessingCmd
  type: string
- description: The command to run after the task.
  name: postProcessingCmd
  type: string
- description: The source connection ID.
  name: sourceConnectionId
  type: string
- description: The target connection ID.
  name: targetConnectionId
  type: string
- description: Parameter value overrides.
  name: parameters
  type: array
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-mapping-task-create-request-schema.json
slug: informatica-platform-rest-mapping-task-create-request
tags:
- Address Verification
- B2B Gateway
- Cloud Services
- Data Governance
- Data Integration
- Data Profiling
- Data Quality
- Enterprise Software
- ETL
- IDMC
- IICS
- Master Data Management
- Reference Data Management
title: MappingTaskCreateRequest
---
