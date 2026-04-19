---
description: ServiceDetail schema from Amazon PrivateLink API
layout: schema
name: ServiceDetail
properties_list:
- description: Name of the endpoint service
  name: ServiceName
  type: string
- description: Unique ID of the endpoint service
  name: ServiceId
  type: string
- description: Type of service
  name: ServiceType
  type: array
- description: Availability zones
  name: AvailabilityZones
  type: array
- description: Owner AWS account ID
  name: Owner
  type: string
- description: Base DNS names for the endpoint service
  name: BaseEndpointDnsNames
  type: array
- description: Private DNS name
  name: PrivateDnsName
  type: string
- description: Whether acceptance is required
  name: AcceptanceRequired
  type: boolean
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
schema_file: json-schema/amazon-privatelink-service-detail-schema.json
slug: amazon-privatelink-service-detail
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
title: ServiceDetail
---
