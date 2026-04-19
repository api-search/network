---
description: Container definition for a task
layout: schema
name: ContainerDefinition
properties_list:
- description: Container name
  name: name
  type: string
- description: Docker image
  name: image
  type: string
- description: Whether container is essential
  name: essential
  type: boolean
- description: CPU units for the container
  name: cpu
  type: integer
- description: Memory limit in MiB
  name: memory
  type: integer
- description: Environment variables
  name: environment
  type: array
- description: Port mappings
  name: portMappings
  type: array
- description: ''
  name: logConfiguration
  type: object
provider_name: Amazon Fargate
provider_slug: amazon-fargate
schema_file: json-schema/amazon-fargate-container-definition-schema.json
slug: amazon-fargate-container-definition
tags:
- AWS
- Compute
- Containers
- ECS
- EKS
- Microservices
- Serverless
title: ContainerDefinition
---
