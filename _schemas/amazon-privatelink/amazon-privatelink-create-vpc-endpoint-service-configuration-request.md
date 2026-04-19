---
description: CreateVpcEndpointServiceConfigurationRequest schema from Amazon PrivateLink API
layout: schema
name: CreateVpcEndpointServiceConfigurationRequest
properties_list:
- description: ARNs of Network Load Balancers for the endpoint service
  name: NetworkLoadBalancerArn
  type: array
- description: ARNs of Gateway Load Balancers for the endpoint service
  name: GatewayLoadBalancerArn
  type: array
- description: Whether connection requests require manual acceptance
  name: AcceptanceRequired
  type: boolean
- description: Private DNS name for the endpoint service
  name: PrivateDnsName
  type: string
provider_name: Amazon PrivateLink
provider_slug: amazon-privatelink
schema_file: json-schema/amazon-privatelink-create-vpc-endpoint-service-configuration-request-schema.json
slug: amazon-privatelink-create-vpc-endpoint-service-configuration-request
tags:
- AWS
- Networking
- Private Connectivity
- Security
- VPC
- Zero Trust
- Endpoint Services
title: CreateVpcEndpointServiceConfigurationRequest
---
