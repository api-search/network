---
description: Gauge tracking the number of discovered Akri instances per configuration
layout: schema
name: AkriInstanceCount
properties_list:
- description: Name of the Akri Configuration resource
  name: configuration
  type: string
- description: Whether the device is shared across multiple nodes
  name: shared
  type: string
- description: Current count of discovered instances
  name: value
  type: number
provider_name: Akri
provider_slug: akri
schema_file: json-schema/akri-akri-instance-count-schema.json
slug: akri-akri-instance-count
tags:
- Device Management
- Edge Computing
- IoT
- Kubernetes
- CNCF
- Open Source
- OPC UA
- ONVIF
- udev
title: AkriInstanceCount
---
