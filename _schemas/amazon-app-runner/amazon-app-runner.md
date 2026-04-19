---
description: Schema defining the structure of an AWS App Runner service resource, including source configuration, instance configuration, networking, auto scaling, health checks, and observability settings.
layout: schema
name: AWS App Runner Service
properties_list:
- description: The customer-provided service name.
  name: ServiceName
  type: string
- description: An ID that App Runner generated for this service.
  name: ServiceId
  type: string
- description: The Amazon Resource Name (ARN) of the service.
  name: ServiceArn
  type: string
- description: A subdomain URL for the App Runner service.
  name: ServiceUrl
  type: string
- description: The current state of the App Runner service.
  name: Status
  type: string
- description: ''
  name: SourceConfiguration
  type: object
- description: ''
  name: InstanceConfiguration
  type: object
- description: ''
  name: AutoScalingConfigurationSummary
  type: object
- description: ''
  name: HealthCheckConfiguration
  type: object
- description: ''
  name: NetworkConfiguration
  type: object
- description: ''
  name: ObservabilityConfiguration
  type: object
- description: The time when the service was created.
  name: CreatedAt
  type: string
- description: The time when the service was last updated.
  name: UpdatedAt
  type: string
provider_name: Amazon App Runner
provider_slug: amazon-app-runner
schema_file: json-schema/amazon-app-runner-schema.json
slug: amazon-app-runner
tags:
- AWS
- CI/CD
- Containers
- Deployment
- Managed Service
- Serverless
- Web Applications
title: AWS App Runner Service
---
