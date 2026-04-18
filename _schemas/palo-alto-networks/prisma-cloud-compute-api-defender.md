---
description: Defender schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: Defender
properties_list:
- description: Hostname where the Defender is deployed.
  name: hostname
  type: string
- description: Defender agent version.
  name: version
  type: string
- description: Type of Defender deployment.
  name: type
  type: string
- description: Whether the Defender is currently connected to the Console.
  name: connected
  type: boolean
- description: Timestamp of the last status update from the Defender.
  name: lastModified
  type: string
- description: Kubernetes cluster name if applicable.
  name: cluster
  type: string
- description: ''
  name: cloudMetadata
  type: object
- description: ''
  name: category
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-defender-schema.json
slug: prisma-cloud-compute-api-defender
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Defender
---
