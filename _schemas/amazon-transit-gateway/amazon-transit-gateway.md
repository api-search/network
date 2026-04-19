---
description: Schema representing an Amazon Transit Gateway resource.
layout: schema
name: Amazon Transit Gateway
properties_list:
- description: The ID of the transit gateway.
  name: TransitGatewayId
  type: string
- description: The Amazon Resource Name (ARN) of the transit gateway.
  name: TransitGatewayArn
  type: string
- description: The state of the transit gateway.
  name: State
  type: string
- description: The ID of the AWS account that owns the transit gateway.
  name: OwnerId
  type: string
- description: The description of the transit gateway.
  name: Description
  type: string
- description: The transit gateway options.
  name: Options
  type: object
- description: The creation date and time of the transit gateway.
  name: CreationTime
  type: string
- description: The tags assigned to the transit gateway.
  name: Tags
  type: array
provider_name: Amazon Transit Gateway
provider_slug: amazon-transit-gateway
schema_file: json-schema/amazon-transit-gateway-schema.json
slug: amazon-transit-gateway
tags:
- AWS
- Cloud Networking
- Network Hub
- Networking
- Transit Gateway
- VPC
title: Amazon Transit Gateway
---
