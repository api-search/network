---
description: Describes a route table
layout: schema
name: RouteTable
properties_list:
- description: The ID of the route table
  name: routeTableId
  type: string
- description: The ID of the VPC
  name: vpcId
  type: string
- description: The routes in the route table
  name: routes
  type: array
- description: The associations between the route table and subnets or gateways
  name: associations
  type: array
- description: The ID of the AWS account that owns the route table
  name: ownerId
  type: string
- description: Any tags assigned to the route table
  name: tags
  type: array
provider_name: Amazon VPC
provider_slug: amazon-vpc
schema_file: json-schema/amazon-vpc-route-table-schema.json
slug: amazon-vpc-route-table
tags:
- AWS
- Networking
- Private Cloud
- Security
- Subnets
- VPC
title: RouteTable
---
