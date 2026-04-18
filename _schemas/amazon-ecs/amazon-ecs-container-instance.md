---
description: An Amazon EC2 instance that is registered into an ECS cluster and running the ECS agent.
layout: schema
name: ContainerInstance
properties_list:
- description: ''
  name: containerInstanceArn
  type: string
- description: ''
  name: ec2InstanceId
  type: string
- description: ''
  name: version
  type: integer
- description: ''
  name: versionInfo
  type: object
- description: ''
  name: remainingResources
  type: array
- description: ''
  name: registeredResources
  type: array
- description: ''
  name: status
  type: string
- description: ''
  name: statusReason
  type: string
- description: ''
  name: agentConnected
  type: boolean
- description: ''
  name: runningTasksCount
  type: integer
- description: ''
  name: pendingTasksCount
  type: integer
- description: ''
  name: agentUpdateStatus
  type: string
- description: ''
  name: attributes
  type: array
- description: ''
  name: registeredAt
  type: number
- description: ''
  name: attachments
  type: array
- description: ''
  name: tags
  type: array
- description: ''
  name: capacityProviderName
  type: string
- description: ''
  name: healthStatus
  type: object
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-container-instance-schema.json
slug: amazon-ecs-container-instance
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: ContainerInstance
---
