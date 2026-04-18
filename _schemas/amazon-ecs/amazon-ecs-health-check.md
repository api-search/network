---
description: ''
layout: schema
name: HealthCheck
properties_list:
- description: A string array representing the command that the container runs to determine if it is healthy. The first element is CMD or CMD-SHELL.
  name: command
  type: array
- description: The time period in seconds between each health check execution (default 30).
  name: interval
  type: integer
- description: The time period in seconds to wait for a health check to succeed before it is considered a failure (default 5).
  name: timeout
  type: integer
- description: The number of times to retry a failed health check before the container is considered unhealthy (default 3).
  name: retries
  type: integer
- description: The optional grace period to provide containers time to bootstrap before failed health checks count towards the maximum retries (default 0).
  name: startPeriod
  type: integer
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-health-check-schema.json
slug: amazon-ecs-health-check
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: HealthCheck
---
