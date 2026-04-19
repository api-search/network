---
description: Request body for updating an existing mapping task.
layout: schema
name: MappingTaskUpdateRequest
properties_list:
- description: The resource type identifier.
  name: '@type'
  type: string
- description: The updated name.
  name: name
  type: string
- description: The updated description.
  name: description
  type: string
- description: The updated runtime environment.
  name: runtimeEnvironmentId
  type: string
- description: The updated schedule ID.
  name: scheduleId
  type: string
- description: The updated pre-processing command.
  name: preProcessingCmd
  type: string
- description: The updated post-processing command.
  name: postProcessingCmd
  type: string
- description: The updated source connection ID.
  name: sourceConnectionId
  type: string
- description: The updated target connection ID.
  name: targetConnectionId
  type: string
- description: Updated parameter values.
  name: parameters
  type: array
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-mapping-task-update-request-schema.json
slug: informatica-platform-rest-mapping-task-update-request
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
title: MappingTaskUpdateRequest
---
