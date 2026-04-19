---
description: VpcEndpointConnection schema from Amazon PrivateLink API
layout: schema
name: VpcEndpointConnection
properties_list:
- description: ID of the endpoint service
  name: ServiceId
  type: string
- description: ID of the VPC endpoint
  name: VpcEndpointId
  type: string
- description: AWS account ID of the endpoint owner
  name: VpcEndpointOwner
  type: string
- description: State of the endpoint
  name: VpcEndpointState
  type: string
- description: Time the connection was created
  name: CreationTimestamp
  type: string
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
schema_file: json-schema/amazon-privatelink-vpc-endpoint-connection-schema.json
slug: amazon-privatelink-vpc-endpoint-connection
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
title: VpcEndpointConnection
---
