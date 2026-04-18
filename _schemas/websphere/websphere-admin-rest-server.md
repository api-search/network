---
description: ''
layout: schema
name: Server
properties_list:
- description: Server name
  name: name
  type: string
- description: Node where the server resides
  name: nodeName
  type: string
- description: Cluster membership
  name: clusterName
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: serverType
  type: string
- description: Process ID
  name: pid
  type: integer
- description: ''
  name: ports
  type: array
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-admin-rest-server-schema.json
slug: websphere-admin-rest-server
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: Server
---
