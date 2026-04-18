---
description: ScanTarget schema from Palo Alto Networks Prisma AIRS AI Red Teaming API
layout: schema
name: ScanTarget
properties_list:
- description: Unique identifier of the scan target.
  name: target_id
  type: string
- description: Display name of the scan target.
  name: name
  type: string
- description: Description of the target AI application.
  name: description
  type: string
- description: AI interface type of the target endpoint.
  name: type
  type: string
- description: URL of the AI application endpoint.
  name: endpoint_url
  type: string
- description: AI model name or identifier used by the endpoint.
  name: model
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-ai-red-teaming-api-scan-target-schema.json
slug: prisma-airs-ai-red-teaming-api-scan-target
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanTarget
---
