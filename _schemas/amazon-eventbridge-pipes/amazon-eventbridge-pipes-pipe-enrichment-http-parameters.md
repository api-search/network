---
description: These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations. In the latter case, these are merged with any InvocationParameters specified on the Connection, with any values from the Connection taking precedence.
layout: schema
name: PipeEnrichmentHttpParameters
properties_list:
- description: ''
  name: HeaderParameters
  type: object
- description: ''
  name: PathParameterValues
  type: object
- description: ''
  name: QueryStringParameters
  type: object
provider_name: Amazon EventBridge Pipes
provider_slug: amazon-eventbridge-pipes
schema_file: json-schema/amazon-eventbridge-pipes-pipe-enrichment-http-parameters-schema.json
slug: amazon-eventbridge-pipes-pipe-enrichment-http-parameters
tags:
- Amazon Web Services
- AWS
- Event-Driven
- Integration
- Messaging
- Serverless
title: PipeEnrichmentHttpParameters
---
