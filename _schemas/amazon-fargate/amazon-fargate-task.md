---
description: An Amazon ECS task running on Fargate
layout: schema
name: Task
properties_list:
- description: ARN of the task
  name: taskArn
  type: string
- description: ARN of the cluster
  name: clusterArn
  type: string
- description: ARN of the task definition
  name: taskDefinitionArn
  type: string
- description: Last known status
  name: lastStatus
  type: string
- description: Desired status
  name: desiredStatus
  type: string
- description: Launch type
  name: launchType
  type: string
- description: CPU units
  name: cpu
  type: string
- description: Memory in MiB
  name: memory
  type: string
- description: Time task was created
  name: createdAt
  type: string
- description: Time task started running
  name: startedAt
  type: string
- description: Time task stopped
  name: stoppedAt
  type: string
- description: Reason task stopped
  name: stoppedReason
  type: string
- description: Network interfaces
  name: networkInterfaces
  type: array
- description: Tags
  name: tags
  type: array
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-task-schema.json
slug: amazon-fargate-task
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: Task
---
