---
description: Describes a VPC
layout: schema
name: Vpc
properties_list:
- description: The ID of the VPC
  name: vpcId
  type: string
- description: The current state of the VPC
  name: state
  type: string
- description: The primary IPv4 CIDR block for the VPC
  name: cidrBlock
  type: string
- description: Information about the IPv4 CIDR blocks associated with the VPC
  name: cidrBlockAssociationSet
  type: array
- description: Information about the IPv6 CIDR blocks associated with the VPC
  name: ipv6CidrBlockAssociationSet
  type: array
- description: The ID of the set of DHCP options associated with the VPC
  name: dhcpOptionsId
  type: string
- description: The allowed tenancy of instances launched into the VPC
  name: instanceTenancy
  type: string
- description: Indicates whether the VPC is the default VPC
  name: isDefault
  type: boolean
- description: The ID of the AWS account that owns the VPC
  name: ownerId
  type: string
- description: Any tags assigned to the VPC
  name: tags
  type: array
provider_name: Amazon VPC
provider_slug: amazon-vpc
schema_file: json-schema/amazon-vpc-vpc-schema.json
slug: amazon-vpc-vpc
tags:
- AWS
- Networking
- Private Cloud
- Security
- Subnets
- VPC
title: Vpc
---
