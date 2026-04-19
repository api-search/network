---
description: NeighborConnectionDetail schema from Amazon Application Discovery Service API
layout: schema
name: NeighborConnectionDetail
properties_list:
- description: The ID of the server that opened the network connection.
  name: sourceServerId
  type: string
- description: The ID of the server that accepted the network connection.
  name: destinationServerId
  type: string
- description: The destination network port for the connection.
  name: destinationPort
  type: integer
- description: The network protocol used for the connection.
  name: transportProtocol
  type: string
- description: The number of open network connections with the neighboring server.
  name: connectionsCount
  type: integer
provider_name: Amazon Application Discovery Service
provider_slug: amazon-application-discovery-service
schema_file: json-schema/application-discovery-service-neighbor-connection-detail-schema.json
slug: application-discovery-service-neighbor-connection-detail
tags:
- Amazon Application Discovery Service
- Migration
- Discovery
- Infrastructure
- AWS
title: NeighborConnectionDetail
---
