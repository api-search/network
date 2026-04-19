---
description: An Amazon ECS cluster
layout: schema
name: Cluster
properties_list:
- description: The ARN of the cluster
  name: clusterArn
  type: string
- description: The name of the cluster
  name: clusterName
  type: string
- description: Cluster status
  name: status
  type: string
- description: Number of registered container instances
  name: registeredContainerInstancesCount
  type: integer
- description: Number of running tasks
  name: runningTasksCount
  type: integer
- description: Number of pending tasks
  name: pendingTasksCount
  type: integer
- description: Number of active services
  name: activeServicesCount
  type: integer
- description: Tags associated with the cluster
  name: tags
  type: array
- description: Cluster settings
  name: settings
  type: array
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-cluster-schema.json
slug: amazon-fargate-cluster
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: Cluster
---
