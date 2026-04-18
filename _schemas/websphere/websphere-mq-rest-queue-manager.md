---
description: ''
layout: schema
name: QueueManager
properties_list:
- description: Queue manager name
  name: name
  type: string
- description: Queue manager state
  name: state
  type: string
- description: MQ version
  name: version
  type: string
- description: Platform type
  name: platform
  type: string
- description: Command level
  name: commandLevel
  type: integer
- description: Number of active connections
  name: connectionCount
  type: integer
- description: ''
  name: description
  type: string
- description: Maximum message length in bytes
  name: maximumMessageLength
  type: integer
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-mq-rest-queue-manager-schema.json
slug: websphere-mq-rest-queue-manager
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: QueueManager
---
