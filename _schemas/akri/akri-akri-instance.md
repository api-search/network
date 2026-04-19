---
description: Akri Instance custom resource (instances.akri.sh) representing a single discovered device. Automatically created and destroyed as devices appear and disappear.
layout: schema
name: AkriInstance
properties_list:
- description: API version of the Akri Instance resource
  name: apiVersion
  type: string
- description: Resource kind
  name: kind
  type: string
- description: Kubernetes object metadata
  name: metadata
  type: object
- description: Instance specification
  name: spec
  type: object
provider_name: Akri
provider_slug: akri
schema_file: json-schema/akri-akri-instance-schema.json
slug: akri-akri-instance
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
title: AkriInstance
---
