---
description: ScanRequest schema from Palo Alto Networks Prisma AIRS API
layout: schema
name: ScanRequest
properties_list:
- description: Reference to the AI security profile to apply during scanning.
  name: ai_profile
  type: object
- description: Array of prompt/response pairs to scan. Each item represents one LLM interaction. For batch scanning, include multiple items.
  name: contents
  type: array
- description: Optional caller-supplied transaction ID for correlating scan requests with application-side records.
  name: tr_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-api-scan-request-schema.json
slug: prisma-airs-api-scan-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanRequest
---
