---
description: Represents a mapping task that executes a mapping with specific source and target connections and runtime parameters.
layout: schema
name: MappingTask
properties_list:
- description: The resource type identifier.
  name: '@type'
  type: string
- description: The unique identifier for the mapping task.
  name: id
  type: string
- description: The organization ID that owns the task.
  name: orgId
  type: string
- description: The name of the mapping task.
  name: name
  type: string
- description: A description of the mapping task.
  name: description
  type: string
- description: The time the mapping task was created.
  name: createTime
  type: string
- description: The time the mapping task was last updated.
  name: updateTime
  type: string
- description: The user who created the mapping task.
  name: createdBy
  type: string
- description: The user who last updated the mapping task.
  name: updatedBy
  type: string
- description: The ID of the mapping that this task executes.
  name: mappingId
  type: string
- description: The runtime environment to use for execution.
  name: runtimeEnvironmentId
  type: string
- description: The schedule ID if the task is scheduled.
  name: scheduleId
  type: string
- description: The command to run before the task executes.
  name: preProcessingCmd
  type: string
- description: The command to run after the task executes.
  name: postProcessingCmd
  type: string
- description: The parameter values for this task execution. Overrides default mapping parameters.
  name: parameters
  type: array
- description: The source connection ID for the mapping task.
  name: sourceConnectionId
  type: string
- description: The target connection ID for the mapping task.
  name: targetConnectionId
  type: string
- description: The federated task ID.
  name: frsId
  type: string
- description: Whether the mapping task is active.
  name: active
  type: boolean
provider_name: Informatica
provider_slug: informatica
schema_file: json-schema/informatica-platform-rest-mapping-task-schema.json
slug: informatica-platform-rest-mapping-task
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
title: MappingTask
---
