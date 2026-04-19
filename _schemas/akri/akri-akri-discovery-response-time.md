---
description: Histogram of Discovery Handler response latency in seconds
layout: schema
name: AkriDiscoveryResponseTime
properties_list:
- description: Name of the Akri Configuration resource
  name: configuration
  type: string
- description: Histogram bucket upper bound in seconds
  name: le
  type: string
- description: Count of observations within this bucket
  name: value
  type: number
provider_name: Akri
provider_slug: akri
schema_file: json-schema/akri-akri-discovery-response-time-schema.json
slug: akri-akri-discovery-response-time
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
title: AkriDiscoveryResponseTime
---
