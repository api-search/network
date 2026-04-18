---
description: A container that is part of a task.
layout: schema
name: Container
properties_list:
- description: ''
  name: containerArn
  type: string
- description: ''
  name: taskArn
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: image
  type: string
- description: ''
  name: imageDigest
  type: string
- description: ''
  name: runtimeId
  type: string
- description: ''
  name: lastStatus
  type: string
- description: ''
  name: exitCode
  type: integer
- description: ''
  name: reason
  type: string
- description: ''
  name: healthStatus
  type: string
- description: ''
  name: cpu
  type: string
- description: ''
  name: memory
  type: string
- description: ''
  name: memoryReservation
  type: string
- description: ''
  name: gpuIds
  type: array
- description: ''
  name: networkBindings
  type: array
- description: ''
  name: networkInterfaces
  type: array
- description: ''
  name: managedAgents
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-container-schema.json
slug: amazon-ecs-container
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: Container
---
