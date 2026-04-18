---
description: A regional grouping of one or more container instances on which you can run tasks and services.
layout: schema
name: Cluster
properties_list:
- description: The ARN that identifies the cluster.
  name: clusterArn
  type: string
- description: A user-generated string that you use to identify your cluster.
  name: clusterName
  type: string
- description: The status of the cluster.
  name: status
  type: string
- description: The number of container instances registered into the cluster.
  name: registeredContainerInstancesCount
  type: integer
- description: The number of tasks in the cluster that are in the RUNNING state.
  name: runningTasksCount
  type: integer
- description: The number of tasks in the cluster that are in the PENDING state.
  name: pendingTasksCount
  type: integer
- description: The number of services in the cluster that are in an ACTIVE state.
  name: activeServicesCount
  type: integer
- description: ''
  name: statistics
  type: array
- description: ''
  name: tags
  type: array
- description: ''
  name: settings
  type: array
- description: ''
  name: capacityProviders
  type: array
- description: ''
  name: defaultCapacityProviderStrategy
  type: array
- description: ''
  name: attachments
  type: array
- description: ''
  name: attachmentsStatus
  type: string
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-cluster-schema.json
slug: amazon-ecs-cluster
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: Cluster
---
