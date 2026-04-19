---
description: A complex type for the endpoint group. An Amazon Web Services Region can have only one endpoint group for a specific listener.
layout: schema
name: EndpointGroup
properties_list:
- description: ''
  name: EndpointGroupArn
  type: object
- description: ''
  name: EndpointGroupRegion
  type: object
- description: ''
  name: EndpointDescriptions
  type: object
- description: ''
  name: TrafficDialPercentage
  type: object
- description: ''
  name: HealthCheckPort
  type: object
- description: ''
  name: HealthCheckProtocol
  type: object
- description: ''
  name: HealthCheckPath
  type: object
- description: ''
  name: HealthCheckIntervalSeconds
  type: object
- description: ''
  name: ThresholdCount
  type: object
- description: ''
  name: PortOverrides
  type: object
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
schema_file: json-schema/global-accelerator-endpoint-group-schema.json
slug: global-accelerator-endpoint-group
tags:
- Availability
- AWS
- CDN
- Global
- Load Balancing
- Networking
- Performance
title: EndpointGroup
---
