---
description: Represents an Amazon Virtual Private Cloud (VPC) with its associated configuration, networking, and metadata.
layout: schema
name: Amazon VPC
properties_list:
- description: The unique identifier for the VPC
  name: vpcId
  type: string
- description: The primary IPv4 CIDR block for the VPC
  name: cidrBlock
  type: string
- description: The current state of the VPC
  name: state
  type: string
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
- description: Information about the IPv4 CIDR blocks associated with the VPC
  name: cidrBlockAssociationSet
  type: array
- description: Information about the IPv6 CIDR blocks associated with the VPC
  name: ipv6CidrBlockAssociationSet
  type: array
- description: The subnets within the VPC
  name: subnets
  type: array
- description: Internet gateways attached to the VPC
  name: internetGateways
  type: array
- description: NAT gateways in the VPC
  name: natGateways
  type: array
- description: Route tables associated with the VPC
  name: routeTables
  type: array
- description: Network ACLs associated with the VPC
  name: networkAcls
  type: array
- description: Tags assigned to the VPC
  name: tags
  type: array
provider_name: Amazon VPC
provider_slug: amazon-vpc
schema_file: json-schema/amazon-vpc-schema.json
slug: amazon-vpc
tags:
- AWS
- Networking
- Private Cloud
- Security
- Subnets
- VPC
title: Amazon VPC
---
