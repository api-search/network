---
description: An Amazon ECS task definition
layout: schema
name: TaskDefinition
properties_list:
- description: Full ARN of the task definition
  name: taskDefinitionArn
  type: string
- description: Family of the task definition
  name: family
  type: string
- description: Revision number
  name: revision
  type: integer
- description: Task definition status
  name: status
  type: string
- description: Launch types the task definition is compatible with
  name: requiresCompatibilities
  type: array
- description: Docker networking mode
  name: networkMode
  type: string
- description: Number of cpu units
  name: cpu
  type: string
- description: Amount of memory in MiB
  name: memory
  type: string
- description: ARN of task execution role
  name: executionRoleArn
  type: string
- description: ARN of task IAM role
  name: taskRoleArn
  type: string
- description: Container definitions
  name: containerDefinitions
  type: array
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-task-definition-schema.json
slug: amazon-fargate-task-definition
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: TaskDefinition
---
