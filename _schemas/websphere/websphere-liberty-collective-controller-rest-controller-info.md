---
description: ''
layout: schema
name: ControllerInfo
properties_list:
- description: Controller server name
  name: name
  type: string
- description: Controller hostname
  name: hostName
  type: string
- description: HTTPS port
  name: httpsPort
  type: integer
- description: Liberty version
  name: version
  type: string
- description: Total number of collective members
  name: memberCount
  type: integer
- description: Total number of clusters
  name: clusterCount
  type: integer
- description: Total number of hosts
  name: hostCount
  type: integer
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-liberty-collective-controller-rest-controller-info-schema.json
slug: websphere-liberty-collective-controller-rest-controller-info
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: ControllerInfo
---
