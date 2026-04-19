---
description: An Amazon Lightsail virtual server instance.
layout: schema
name: Instance
properties_list:
- description: The name the user gave the instance.
  name: name
  type: string
- description: The Amazon Resource Name (ARN) of the instance.
  name: arn
  type: string
- description: The blueprint ID of the instance.
  name: blueprintId
  type: string
- description: The bundle for the instance.
  name: bundleId
  type: string
- description: The public IP address of the instance.
  name: publicIpAddress
  type: string
- description: The private IP address of the instance.
  name: privateIpAddress
  type: string
- description: The timestamp when the instance was created.
  name: createdAt
  type: string
provider_name: Amazon Lightsail
provider_slug: amazon-lightsail
schema_file: json-schema/amazon-lightsail-instance-schema.json
slug: amazon-lightsail-instance
tags: []
title: Instance
---
