---
description: ''
layout: schema
name: Queue
properties_list:
- description: Queue name
  name: name
  type: string
- description: Queue type
  name: type
  type: string
- description: ''
  name: description
  type: string
- description: Maximum queue depth
  name: maxDepth
  type: integer
- description: Maximum message length in bytes
  name: maxMessageLength
  type: integer
- description: Current number of messages on the queue
  name: currentDepth
  type: integer
- description: Whether put operations are inhibited
  name: inhibitPut
  type: boolean
- description: Whether get operations are inhibited
  name: inhibitGet
  type: boolean
- description: ''
  name: persistence
  type: object
- description: ''
  name: cluster
  type: object
- description: ''
  name: status
  type: object
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-mq-rest-queue-schema.json
slug: websphere-mq-rest-queue
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: Queue
---
