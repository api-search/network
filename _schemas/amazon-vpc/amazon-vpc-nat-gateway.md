---
description: Describes a NAT gateway
layout: schema
name: NatGateway
properties_list:
- description: The ID of the NAT gateway
  name: natGatewayId
  type: string
- description: The ID of the subnet in which the NAT gateway is located
  name: subnetId
  type: string
- description: The ID of the VPC in which the NAT gateway is located
  name: vpcId
  type: string
- description: The state of the NAT gateway
  name: state
  type: string
- description: Indicates whether the NAT gateway supports public or private connectivity
  name: connectivityType
  type: string
- description: Information about the IP addresses and network interface associated with the NAT gateway
  name: natGatewayAddresses
  type: array
- description: The date and time the NAT gateway was created
  name: createTime
  type: string
- description: Any tags assigned to the NAT gateway
  name: tags
  type: array
provider_name: Amazon VPC
provider_slug: amazon-vpc
schema_file: json-schema/amazon-vpc-nat-gateway-schema.json
slug: amazon-vpc-nat-gateway
tags:
- AWS
- Networking
- Private Cloud
- Security
- Subnets
- VPC
title: NatGateway
---
