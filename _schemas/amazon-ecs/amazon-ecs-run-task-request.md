---
description: ''
layout: schema
name: RunTaskRequest
properties_list:
- description: The family and revision or full ARN of the task definition to run.
  name: taskDefinition
  type: string
- description: The short name or full ARN of the cluster to run the task on.
  name: cluster
  type: string
- description: The number of instantiations of the specified task to place on your cluster (1-10).
  name: count
  type: integer
- description: The launch type on which to run your task.
  name: launchType
  type: string
- description: ''
  name: capacityProviderStrategy
  type: array
- description: The platform version the task uses (Fargate launch type only).
  name: platformVersion
  type: string
- description: ''
  name: placementConstraints
  type: array
- description: ''
  name: placementStrategy
  type: array
- description: The name of the task group to associate with the task.
  name: group
  type: string
- description: An optional tag specified when a task is started.
  name: startedBy
  type: string
- description: ''
  name: tags
  type: array
- description: ''
  name: enableECSManagedTags
  type: boolean
- description: Whether to enable Amazon ECS Exec for the task.
  name: enableExecuteCommand
  type: boolean
- description: ''
  name: propagateTags
  type: string
- description: An identifier you provide to ensure the idempotency of the request.
  name: clientToken
  type: string
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-run-task-request-schema.json
slug: amazon-ecs-run-task-request
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: RunTaskRequest
---
