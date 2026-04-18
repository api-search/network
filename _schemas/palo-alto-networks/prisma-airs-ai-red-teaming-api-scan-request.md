---
description: ScanRequest schema from Palo Alto Networks Prisma AIRS AI Red Teaming API
layout: schema
name: ScanRequest
properties_list:
- description: ID of the scan target to assess.
  name: target_id
  type: string
- description: Attack category identifiers to include in the scan. Use GET /v1/attack-categories to retrieve available category IDs.
  name: attack_categories
  type: array
- description: Optional custom adversarial prompts to include alongside the built-in attack library. Useful for testing application-specific threat scenarios.
  name: custom_prompts
  type: array
- description: Maximum number of attack probes per category. Limits scan duration for large attack libraries. If omitted, all available attacks for each category are executed.
  name: max_attacks_per_category
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-ai-red-teaming-api-scan-request-schema.json
slug: prisma-airs-ai-red-teaming-api-scan-request
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
