---
description: ''
layout: schema
name: ManagedServer
properties_list:
- description: Unique server identifier
  name: id
  type: string
- description: Server name
  name: name
  type: string
- description: ''
  name: type
  type: string
- description: WebSphere version
  name: version
  type: string
- description: Server hostname
  name: host
  type: string
- description: Server port
  name: port
  type: integer
- description: ''
  name: status
  type: string
- description: Number of open vulnerabilities
  name: vulnerabilityCount
  type: integer
- description: ''
  name: lastScanDate
  type: string
- description: ''
  name: registeredDate
  type: string
- description: List of installed fix IDs
  name: installedFixes
  type: array
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-automation-rest-managed-server-schema.json
slug: websphere-automation-rest-managed-server
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: ManagedServer
---
