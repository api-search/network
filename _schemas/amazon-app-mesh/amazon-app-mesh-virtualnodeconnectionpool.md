---
description: <p>An object that represents the type of virtual node connection pool.</p> <p>Only one protocol is used at a time and should be the same protocol as the one chosen under port mapping.</p> <p>If not present the default value for <code>maxPendingRequests</code> is <code>2147483647</code>.</p> <p/>
layout: schema
name: VirtualNodeConnectionPool
properties_list:
- description: ''
  name: grpc
  type: object
- description: ''
  name: http
  type: object
- description: ''
  name: http2
  type: object
- description: ''
  name: tcp
  type: object
provider_name: Amazon App Mesh
provider_slug: amazon-app-mesh
schema_file: json-schema/amazon-app-mesh-virtualnodeconnectionpool-schema.json
slug: amazon-app-mesh-virtualnodeconnectionpool
tags:
- AWS
- Microservices
- Networking
- Service Mesh
title: VirtualNodeConnectionPool
---
