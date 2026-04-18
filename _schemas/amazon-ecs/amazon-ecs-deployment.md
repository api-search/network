---
description: ''
layout: schema
name: Deployment
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: taskDefinition
  type: string
- description: ''
  name: desiredCount
  type: integer
- description: ''
  name: pendingCount
  type: integer
- description: ''
  name: runningCount
  type: integer
- description: ''
  name: failedTasks
  type: integer
- description: ''
  name: createdAt
  type: number
- description: ''
  name: updatedAt
  type: number
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
  name: rolloutState
  type: string
- description: ''
  name: rolloutStateReason
  type: string
- description: ''
  name: capacityProviderStrategy
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-deployment-schema.json
slug: amazon-ecs-deployment
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: Deployment
---
