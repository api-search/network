---
description: <p>An object that represents the type of virtual gateway connection pool.</p> <p>Only one protocol is used at a time and should be the same protocol as the one chosen under port mapping.</p> <p>If not present the default value for <code>maxPendingRequests</code> is <code>2147483647</code>.</p>
layout: schema
name: VirtualGatewayConnectionPool
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
provider_name: Amazon App Mesh
provider_slug: amazon-app-mesh
schema_file: json-schema/amazon-app-mesh-virtualgatewayconnectionpool-schema.json
slug: amazon-app-mesh-virtualgatewayconnectionpool
tags:
- AWS
- Microservices
- Networking
- Service Mesh
title: VirtualGatewayConnectionPool
---
