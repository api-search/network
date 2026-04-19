---
description: 'The overrides that are sent to a container. An empty container override can be passed in. An example of an empty container override is <code>{"containerOverrides": [ ] }</code>. If a non-empty container override is specified, the <code>name</code> parameter must be included.'
layout: schema
name: EcsContainerOverride
properties_list:
- description: ''
  name: Command
  type: object
- description: ''
  name: Cpu
  type: object
- description: ''
  name: Environment
  type: object
- description: ''
  name: EnvironmentFiles
  type: object
- description: ''
  name: Memory
  type: object
- description: ''
  name: MemoryReservation
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: ResourceRequirements
  type: object
provider_name: Amazon EventBridge Pipes
provider_slug: amazon-eventbridge-pipes
schema_file: json-schema/amazon-eventbridge-pipes-ecs-container-override-schema.json
slug: amazon-eventbridge-pipes-ecs-container-override
tags:
- Amazon Web Services
- AWS
- Event-Driven
- Integration
- Messaging
- Serverless
title: EcsContainerOverride
---
