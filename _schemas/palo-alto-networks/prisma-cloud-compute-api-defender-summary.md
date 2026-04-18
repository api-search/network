---
description: DefenderSummary schema from Palo Alto Networks Prisma Cloud Compute API
layout: schema
name: DefenderSummary
properties_list:
- description: Total number of deployed Defenders.
  name: total
  type: integer
- description: Number of currently connected Defenders.
  name: connected
  type: integer
- description: Number of disconnected Defenders.
  name: disconnected
  type: integer
- description: Defender count breakdown by deployment type.
  name: by_type
  type: object
- description: ''
  name: version_distribution
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-compute-api-defender-summary-schema.json
slug: prisma-cloud-compute-api-defender-summary
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: DefenderSummary
---
