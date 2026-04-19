---
description: Describes an internet gateway
layout: schema
name: InternetGateway
properties_list:
- description: The ID of the internet gateway
  name: internetGatewayId
  type: string
- description: Any VPCs attached to the internet gateway
  name: attachments
  type: array
- description: The ID of the AWS account that owns the internet gateway
  name: ownerId
  type: string
- description: Any tags assigned to the internet gateway
  name: tags
  type: array
provider_name: Amazon VPC
provider_slug: amazon-vpc
schema_file: json-schema/amazon-vpc-internet-gateway-schema.json
slug: amazon-vpc-internet-gateway
tags:
- AWS
- Networking
- Private Cloud
- Security
- Subnets
- VPC
title: InternetGateway
---
