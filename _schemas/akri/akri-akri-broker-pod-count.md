---
description: Gauge tracking the number of broker pods per configuration and node
layout: schema
name: AkriBrokerPodCount
properties_list:
- description: Name of the Akri Configuration resource
  name: configuration
  type: string
- description: Kubernetes node name
  name: node
  type: string
- description: Current count of broker pods
  name: value
  type: number
provider_name: Akri
provider_slug: akri
schema_file: json-schema/akri-akri-broker-pod-count-schema.json
slug: akri-akri-broker-pod-count
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
title: AkriBrokerPodCount
---
