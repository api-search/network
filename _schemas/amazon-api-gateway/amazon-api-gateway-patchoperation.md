---
description: ''
layout: schema
name: PatchOperation
properties_list:
- description: The operation type.
  name: op
  type: string
- description: The op operation's target, as identified by a JSON Pointer value.
  name: path
  type: string
- description: The new target value of the update operation. It is applicable for the add or replace operation.
  name: value
  type: string
- description: The copy update operation's source as identified by a JSON Pointer value.
  name: from
  type: string
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-patchoperation-schema.json
slug: amazon-api-gateway-patchoperation
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: PatchOperation
---
