---
description: ''
layout: schema
name: CreateServiceRequest
properties_list:
- description: The name of your service (up to 255 characters).
  name: serviceName
  type: string
- description: The short name or full ARN of the cluster to run the service on.
  name: cluster
  type: string
- description: The family and revision or full ARN of the task definition.
  name: taskDefinition
  type: string
- description: The number of instantiations of the specified task definition to place and keep running.
  name: desiredCount
  type: integer
- description: The launch type on which to run your service.
  name: launchType
  type: string
- description: ''
  name: capacityProviderStrategy
  type: array
- description: The platform version that your tasks in the service are running on (Fargate only).
  name: platformVersion
  type: string
- description: A load balancer object representing the load balancers to use with your service.
  name: loadBalancers
  type: array
- description: The scheduling strategy to use for the service.
  name: schedulingStrategy
  type: string
- description: ''
  name: placementConstraints
  type: array
- description: ''
  name: placementStrategy
  type: array
- description: The period of time, in seconds, that the ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started.
  name: healthCheckGracePeriodSeconds
  type: integer
- description: ''
  name: enableECSManagedTags
  type: boolean
- description: Whether to enable Amazon ECS Exec for the tasks within the service.
  name: enableExecuteCommand
  type: boolean
- description: ''
  name: propagateTags
  type: string
- description: The IAM role that allows Amazon ECS to make calls to your load balancer.
  name: role
  type: string
- description: ''
  name: serviceRegistries
  type: array
- description: ''
  name: tags
  type: array
- description: An identifier you provide to ensure the idempotency of the request.
  name: clientToken
  type: string
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-create-service-request-schema.json
slug: amazon-ecs-create-service-request
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: CreateServiceRequest
---
