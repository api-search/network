---
description: The overrides associated with a task.
layout: schema
name: TaskOverride
properties_list:
- description: ''
  name: containerOverrides
  type: array
- description: ''
  name: cpu
  type: string
- description: ''
  name: memory
  type: string
- description: ''
  name: taskRoleArn
  type: string
- description: ''
  name: executionRoleArn
  type: string
- description: ''
  name: inferenceAcceleratorOverrides
  type: array
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-task-override-schema.json
slug: amazon-ecs-task-override
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: TaskOverride
---
