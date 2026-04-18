---
description: ''
layout: schema
name: ServerHealth
properties_list:
- description: ''
  name: serverId
  type: string
- description: ''
  name: serverName
  type: string
- description: ''
  name: status
  type: string
- description: Uptime in seconds
  name: uptime
  type: integer
- description: CPU usage percentage
  name: cpuUsage
  type: number
- description: Memory usage percentage
  name: memoryUsage
  type: number
- description: ''
  name: openVulnerabilities
  type: integer
- description: ''
  name: lastHealthCheck
  type: string
- description: ''
  name: checks
  type: array
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-automation-rest-server-health-schema.json
slug: websphere-automation-rest-server-health
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: ServerHealth
---
