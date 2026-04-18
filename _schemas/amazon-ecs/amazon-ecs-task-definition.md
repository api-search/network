---
description: The details of a task definition which describes the container and volume definitions of an Amazon ECS task.
layout: schema
name: TaskDefinition
properties_list:
- description: The full ARN of the task definition.
  name: taskDefinitionArn
  type: string
- description: ''
  name: containerDefinitions
  type: array
- description: The family of your task definition.
  name: family
  type: string
- description: ''
  name: taskRoleArn
  type: string
- description: ''
  name: executionRoleArn
  type: string
- description: ''
  name: networkMode
  type: string
- description: The revision of the task in a particular family.
  name: revision
  type: integer
- description: ''
  name: volumes
  type: array
- description: ''
  name: status
  type: string
- description: ''
  name: requiresAttributes
  type: array
- description: ''
  name: placementConstraints
  type: array
- description: ''
  name: compatibilities
  type: array
- description: ''
  name: requiresCompatibilities
  type: array
- description: ''
  name: cpu
  type: string
- description: ''
  name: memory
  type: string
- description: ''
  name: pidMode
  type: string
- description: ''
  name: ipcMode
  type: string
- description: ''
  name: inferenceAccelerators
  type: array
- description: Unix timestamp for when the task definition was registered.
  name: registeredAt
  type: number
- description: Unix timestamp for when the task definition was deregistered.
  name: deregisteredAt
  type: number
- description: ''
  name: registeredBy
  type: string
- description: ''
  name: enableFaultInjection
  type: boolean
- description: ''
  name: tags
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-task-definition-schema.json
slug: amazon-ecs-task-definition
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: TaskDefinition
---
