---
description: Schema representing an AWS Storage Gateway resource. A Storage Gateway connects on-premises environments to AWS cloud storage, enabling hybrid cloud storage workflows with local caching for low-latency access.
layout: schema
name: Amazon Storage Gateway
properties_list:
- description: The Amazon Resource Name (ARN) of the gateway.
  name: GatewayARN
  type: string
- description: The unique identifier assigned to the gateway.
  name: GatewayId
  type: string
- description: The name of the gateway.
  name: GatewayName
  type: string
- description: A value that indicates the time zone configured for the gateway.
  name: GatewayTimezone
  type: string
- description: The type of the gateway.
  name: GatewayType
  type: string
- description: A value that indicates the operating state of the gateway.
  name: GatewayState
  type: string
- description: The state of the gateway.
  name: GatewayOperationalState
  type: string
- description: The ID of the Amazon EC2 instance that was used to launch the gateway.
  name: Ec2InstanceId
  type: string
- description: The AWS Region where the Amazon EC2 instance is located.
  name: Ec2InstanceRegion
  type: string
- description: A list of network interfaces on the gateway.
  name: GatewayNetworkInterfaces
  type: array
- description: The date on which the last software update was applied to the gateway.
  name: LastSoftwareUpdate
  type: string
- description: The date on which an update to the gateway is available.
  name: NextUpdateAvailabilityDate
  type: string
- description: A list of tags assigned to the gateway.
  name: Tags
  type: array
provider_name: Amazon Storage Gateway
provider_slug: amazon-storage-gateway
schema_file: json-schema/amazon-storage-gateway-schema.json
slug: amazon-storage-gateway
tags:
- AWS
- Backup
- File Storage
- Gateway
- Hybrid Cloud
- Storage
title: Amazon Storage Gateway
---
