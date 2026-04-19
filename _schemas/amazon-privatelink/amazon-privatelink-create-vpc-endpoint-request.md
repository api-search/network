---
description: CreateVpcEndpointRequest schema from Amazon PrivateLink API
layout: schema
name: CreateVpcEndpointRequest
properties_list:
- description: ID of the VPC for the endpoint
  name: VpcId
  type: string
- description: Service name for the endpoint
  name: ServiceName
  type: string
- description: Type of VPC endpoint
  name: VpcEndpointType
  type: string
- description: IDs of subnets for interface endpoints
  name: SubnetId
  type: array
- description: IDs of security groups for interface endpoints
  name: SecurityGroupId
  type: array
- description: Policy document for gateway endpoints
  name: PolicyDocument
  type: string
- description: Enable private DNS for interface endpoints
  name: PrivateDnsEnabled
  type: boolean
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
schema_file: json-schema/amazon-privatelink-create-vpc-endpoint-request-schema.json
slug: amazon-privatelink-create-vpc-endpoint-request
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
title: CreateVpcEndpointRequest
---
