---
description: ''
layout: schema
name: RegisterTaskDefinitionRequest
properties_list:
- description: You must specify a family for a task definition. Up to 255 characters (uppercase and lowercase letters, numbers, underscores, and hyphens are allowed).
  name: family
  type: string
- description: A list of container definitions that describe the containers that make up the task.
  name: containerDefinitions
  type: array
- description: The short name or full ARN of the IAM role that containers in this task can assume.
  name: taskRoleArn
  type: string
- description: The ARN of the task execution role that grants the ECS container agent permission to make API calls on your behalf.
  name: executionRoleArn
  type: string
- description: The Docker networking mode to use for the containers in the task.
  name: networkMode
  type: string
- description: A list of volume definitions for the task.
  name: volumes
  type: array
- description: ''
  name: placementConstraints
  type: array
- description: The task launch type compatibility requirement.
  name: requiresCompatibilities
  type: array
- description: 'The number of CPU units used by the task. Required for Fargate launch type. Valid values: 256 (.25 vCPU) through 16384 (16 vCPU).'
  name: cpu
  type: string
- description: The amount of memory (in MiB) used by the task. Required for Fargate launch type.
  name: memory
  type: string
- description: ''
  name: tags
  type: array
- description: The process namespace to use for the containers in the task.
  name: pidMode
  type: string
- description: The IPC resource namespace to use for the containers in the task.
  name: ipcMode
  type: string
- description: ''
  name: inferenceAccelerators
  type: array
- description: Whether to enable fault injection for the task definition.
  name: enableFaultInjection
  type: boolean
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-register-task-definition-request-schema.json
slug: amazon-ecs-register-task-definition-request
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: RegisterTaskDefinitionRequest
---
