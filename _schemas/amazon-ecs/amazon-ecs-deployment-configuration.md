---
description: Deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.
layout: schema
name: DeploymentConfiguration
properties_list:
- description: ''
  name: deploymentCircuitBreaker
  type: object
- description: The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running during a deployment.
  name: maximumPercent
  type: integer
- description: The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running during a deployment.
  name: minimumHealthyPercent
  type: integer
- description: ''
  name: alarms
  type: object
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-deployment-configuration-schema.json
slug: amazon-ecs-deployment-configuration
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: DeploymentConfiguration
---
