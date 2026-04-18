---
description: Details on a task in a cluster.
layout: schema
name: Task
properties_list:
- description: The ARN of the task.
  name: taskArn
  type: string
- description: The ARN of the cluster that hosts the task.
  name: clusterArn
  type: string
- description: The ARN of the task definition that creates the task.
  name: taskDefinitionArn
  type: string
- description: The ARN of the container instances that host the task.
  name: containerInstanceArn
  type: string
- description: The last known status for the task.
  name: lastStatus
  type: string
- description: The desired status of the task.
  name: desiredStatus
  type: string
- description: ''
  name: cpu
  type: string
- description: ''
  name: memory
  type: string
- description: ''
  name: containers
  type: array
- description: ''
  name: startedBy
  type: string
- description: ''
  name: version
  type: integer
- description: ''
  name: stoppedReason
  type: string
- description: ''
  name: stopCode
  type: string
- description: ''
  name: connectivity
  type: string
- description: ''
  name: connectivityAt
  type: number
- description: ''
  name: pullStartedAt
  type: number
- description: ''
  name: pullStoppedAt
  type: number
- description: ''
  name: executionStoppedAt
  type: number
- description: ''
  name: createdAt
  type: number
- description: ''
  name: startedAt
  type: number
- description: ''
  name: stoppingAt
  type: number
- description: ''
  name: stoppedAt
  type: number
- description: ''
  name: group
  type: string
- description: ''
  name: launchType
  type: string
- description: ''
  name: platformVersion
  type: string
- description: ''
  name: platformFamily
  type: string
- description: ''
  name: capacityProviderName
  type: string
- description: ''
  name: availabilityZone
  type: string
- description: ''
  name: attachments
  type: array
- description: ''
  name: healthStatus
  type: string
- description: ''
  name: enableExecuteCommand
  type: boolean
- description: ''
  name: tags
  type: array
- description: ''
  name: inferenceAccelerators
  type: array
- description: ''
  name: attributes
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-task-schema.json
slug: amazon-ecs-task
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: Task
---
