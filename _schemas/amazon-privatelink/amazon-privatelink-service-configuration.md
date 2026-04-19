---
description: ServiceConfiguration schema from Amazon PrivateLink API
layout: schema
name: ServiceConfiguration
properties_list:
- description: Type of service (Interface or Gateway)
  name: ServiceType
  type: array
- description: Unique ID of the endpoint service
  name: ServiceId
  type: string
- description: Name of the endpoint service
  name: ServiceName
  type: string
- description: State of the endpoint service
  name: ServiceState
  type: string
- description: Whether connections require acceptance
  name: AcceptanceRequired
  type: boolean
- description: Availability zones where the service is available
  name: AvailabilityZones
  type: array
- description: ARNs of Network Load Balancers
  name: NetworkLoadBalancerArns
  type: array
- description: Private DNS name
  name: PrivateDnsName
  type: string
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
schema_file: json-schema/amazon-privatelink-service-configuration-schema.json
slug: amazon-privatelink-service-configuration
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
title: ServiceConfiguration
---
