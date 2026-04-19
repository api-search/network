---
description: VpcEndpoint schema from Amazon PrivateLink API
layout: schema
name: VpcEndpoint
properties_list:
- description: ID of the VPC endpoint
  name: VpcEndpointId
  type: string
- description: Type of VPC endpoint
  name: VpcEndpointType
  type: string
- description: ID of the VPC
  name: VpcId
  type: string
- description: Name of the service
  name: ServiceName
  type: string
- description: State of the endpoint
  name: State
  type: string
- description: Policy document
  name: PolicyDocument
  type: string
- description: Subnet IDs for interface endpoints
  name: SubnetIds
  type: array
- description: Network interface IDs
  name: NetworkInterfaceIds
  type: array
- description: DNS entries for the endpoint
  name: DnsEntries
  type: array
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
schema_file: json-schema/amazon-privatelink-vpc-endpoint-schema.json
slug: amazon-privatelink-vpc-endpoint
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
title: VpcEndpoint
---
