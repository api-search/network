---
description: Akri Configuration custom resource (configurations.akri.sh) that specifies device discovery settings and optional broker workload deployment specifications.
layout: schema
name: AkriConfiguration
properties_list:
- description: API version of the Akri Configuration resource
  name: apiVersion
  type: string
- description: Resource kind
  name: kind
  type: string
- description: Kubernetes object metadata
  name: metadata
  type: object
- description: Configuration specification
  name: spec
  type: object
provider_name: Akri
provider_slug: akri
schema_file: json-schema/akri-akri-configuration-schema.json
slug: akri-akri-configuration
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
title: AkriConfiguration
---
