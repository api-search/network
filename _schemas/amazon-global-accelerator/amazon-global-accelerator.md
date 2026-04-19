---
description: Represents an Amazon Global Accelerator with its associated configuration, state, and metadata.
layout: schema
name: Amazon Global Accelerator
properties_list:
- description: The Amazon Resource Name (ARN) of the accelerator
  name: acceleratorArn
  type: string
- description: The name of the accelerator
  name: name
  type: string
- description: The IP address type
  name: ipAddressType
  type: string
- description: Whether the accelerator is enabled
  name: enabled
  type: boolean
- description: The static IP addresses associated with the accelerator
  name: ipSets
  type: array
- description: The DNS name of the accelerator
  name: dnsName
  type: string
- description: The deployment status of the accelerator
  name: status
  type: string
- description: The time the accelerator was created
  name: createdTime
  type: string
- description: The time the accelerator was last modified
  name: lastModifiedTime
  type: string
provider_name: Amazon Global Accelerator
provider_slug: amazon-global-accelerator
schema_file: json-schema/amazon-global-accelerator-schema.json
slug: amazon-global-accelerator
tags:
- Availability
- AWS
- CDN
- Global
- Load Balancing
- Networking
- Performance
title: Amazon Global Accelerator
---
