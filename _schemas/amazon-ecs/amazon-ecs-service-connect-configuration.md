---
description: ''
layout: schema
name: ServiceConnectConfiguration
properties_list:
- description: Whether Service Connect is enabled for this service.
  name: enabled
  type: boolean
- description: The namespace name or ARN of the Cloud Map namespace for the service.
  name: namespace
  type: string
- description: ''
  name: services
  type: array
- description: ''
  name: logConfiguration
  type: object
provider_name: Amazon ECS
provider_slug: amazon-ecs
schema_file: json-schema/amazon-ecs-service-connect-configuration-schema.json
slug: amazon-ecs-service-connect-configuration
tags:
- Amazon
- Aws
- Containers
- Docker
- Ecs
- Orchestration
title: ServiceConnectConfiguration
---
