---
description: Returns the ports and associated IP addresses and ports of Amazon EC2 instances in your virtual private cloud (VPC) subnets. Custom routing is a port mapping protocol in Global Accelerator that statically associates port ranges with VPC subnets, which allows Global Accelerator to route to specific instances and ports within one or more subnets.
layout: schema
name: PortMapping
properties_list:
- description: ''
  name: AcceleratorPort
  type: object
- description: ''
  name: EndpointGroupArn
  type: object
- description: ''
  name: EndpointId
  type: object
- description: ''
  name: DestinationSocketAddress
  type: object
- description: ''
  name: Protocols
  type: object
- description: ''
  name: DestinationTrafficState
  type: object
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
schema_file: json-schema/global-accelerator-port-mapping-schema.json
slug: global-accelerator-port-mapping
tags:
- Availability
- AWS
- CDN
- Global
- Load Balancing
- Networking
- Performance
title: PortMapping
---
