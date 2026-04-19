---
description: ''
layout: schema
name: EndpointConfiguration
properties_list:
- description: A list of endpoint types of an API or its custom domain name.
  name: types
  type: array
- description: A list of VPC endpoint IDs of an API against which to create Route53 ALIASes.
  name: vpcEndpointIds
  type: array
provider_name: Amazon API Gateway
provider_slug: amazon-api-gateway
schema_file: json-schema/amazon-api-gateway-endpointconfiguration-schema.json
slug: amazon-api-gateway-endpointconfiguration
tags:
- AWS
- Gateway
- HTTP API
- REST API
- Serverless
- WebSocket
title: EndpointConfiguration
---
