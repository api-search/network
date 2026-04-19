---
description: BatchDeleteConfigurationTask schema from Amazon Application Discovery Service API
layout: schema
name: BatchDeleteConfigurationTask
properties_list:
- description: The deletion task's unique identifier.
  name: taskId
  type: string
- description: The current execution status of the deletion task.
  name: status
  type: string
- description: An epoch seconds timestamp (Unix) of when the deletion task was started.
  name: startTime
  type: string
- description: An epoch seconds timestamp (Unix) of when the deletion task was completed.
  name: endTime
  type: string
- description: The type of configuration item to delete.
  name: configurationType
  type: string
- description: The list of configuration IDs that were originally requested to be deleted by this task.
  name: requestedConfigurations
  type: array
- description: The list of configuration IDs that were successfully deleted by this task.
  name: deletedConfigurations
  type: array
- description: A list of configuration IDs that produced an associated error.
  name: failedConfigurations
  type: array
- description: A list of warnings associated with this deletion task.
  name: deletionWarnings
  type: array
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-batch-delete-configuration-task-schema.json
slug: application-discovery-service-batch-delete-configuration-task
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: BatchDeleteConfigurationTask
---
