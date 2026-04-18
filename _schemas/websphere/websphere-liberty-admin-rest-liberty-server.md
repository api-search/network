---
description: ''
layout: schema
name: LibertyServer
properties_list:
- description: Server name
  name: name
  type: string
- description: Liberty version
  name: wlpVersion
  type: string
- description: Product edition
  name: productEdition
  type: string
- description: Java version
  name: javaVersion
  type: string
- description: Java vendor
  name: javaVendor
  type: string
- description: ''
  name: serverStatus
  type: string
- description: Server uptime in milliseconds
  name: uptime
  type: integer
- description: Liberty installation directory
  name: installDirectory
  type: string
- description: Server configuration directory
  name: serverDirectory
  type: string
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-liberty-admin-rest-liberty-server-schema.json
slug: websphere-liberty-admin-rest-liberty-server
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: LibertyServer
---
