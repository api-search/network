---
description: ''
layout: schema
name: Resource
properties_list:
- description: The resource's identifier.
  name: id
  type: string
- description: The parent resource's identifier.
  name: parentId
  type: string
- description: The last path segment for this resource.
  name: pathPart
  type: string
- description: The full path for this resource.
  name: path
  type: string
- description: Map of methods for this resource keyed by HTTP method type.
  name: resourceMethods
  type: object
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-resource-schema.json
slug: amazon-api-gateway-resource
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: Resource
---
