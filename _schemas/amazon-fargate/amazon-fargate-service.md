---
description: An Amazon ECS service
layout: schema
name: Service
properties_list:
- description: ARN of the service
  name: serviceArn
  type: string
- description: Name of the service
  name: serviceName
  type: string
- description: ARN of the cluster
  name: clusterArn
  type: string
- description: Task definition ARN or family:revision
  name: taskDefinition
  type: string
- description: Desired number of tasks
  name: desiredCount
  type: integer
- description: Number of running tasks
  name: runningCount
  type: integer
- description: Number of pending tasks
  name: pendingCount
  type: integer
- description: Service status
  name: status
  type: string
- description: Launch type
  name: launchType
  type: string
- description: ''
  name: networkConfiguration
  type: object
- description: Load balancer configurations
  name: loadBalancers
  type: array
- description: Service creation time
  name: createdAt
  type: string
- description: Tags
  name: tags
  type: array
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-service-schema.json
slug: amazon-fargate-service
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: Service
---
