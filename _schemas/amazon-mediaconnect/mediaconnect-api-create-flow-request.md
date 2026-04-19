---
description: Creates a new flow. The request must include one source. The request optionally can include outputs (up to 50) and entitlements (up to 50).
layout: schema
name: CreateFlowRequest
properties_list:
- description: ''
  name: AvailabilityZone
  type: object
- description: ''
  name: Entitlements
  type: object
- description: ''
  name: MediaStreams
  type: object
- description: ''
  name: Name
  type: object
- description: ''
  name: Outputs
  type: object
- description: ''
  name: Source
  type: object
- description: ''
  name: SourceFailoverConfig
  type: object
- description: ''
  name: Sources
  type: object
- description: ''
  name: VpcInterfaces
  type: object
- description: ''
  name: Maintenance
  type: object
provider_name: Amazon MediaConnect
provider_slug: amazon-mediaconnect
schema_file: json-schema/mediaconnect-api-create-flow-request-schema.json
slug: mediaconnect-api-create-flow-request
tags:
- AWS
- Broadcasting
- Live Video
- Media
- Media Transport
title: CreateFlowRequest
---
