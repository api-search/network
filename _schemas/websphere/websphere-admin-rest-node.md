---
description: ''
layout: schema
name: Node
properties_list:
- description: Node name
  name: name
  type: string
- description: Hostname of the node
  name: hostName
  type: string
- description: Operating system platform
  name: platformOS
  type: string
- description: ''
  name: servers
  type: array
- description: Whether the node configuration is synchronized
  name: synchronized
  type: boolean
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-admin-rest-node-schema.json
slug: websphere-admin-rest-node
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: Node
---
