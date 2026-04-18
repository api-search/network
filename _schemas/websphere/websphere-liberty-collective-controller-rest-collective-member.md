---
description: ''
layout: schema
name: CollectiveMember
properties_list:
- description: Member server name
  name: name
  type: string
- description: Host where the member is located
  name: hostName
  type: string
- description: User directory path
  name: userDir
  type: string
- description: Member status
  name: status
  type: string
- description: Cluster the member belongs to
  name: clusterName
  type: string
- description: HTTPS port
  name: httpsPort
  type: integer
- description: Liberty version
  name: wlpVersion
  type: string
- description: Java version
  name: javaVersion
  type: string
provider_name: IBM WebSphere
provider_slug: websphere
schema_file: json-schema/websphere-liberty-collective-controller-rest-collective-member-schema.json
slug: websphere-liberty-collective-controller-rest-collective-member
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
title: CollectiveMember
---
