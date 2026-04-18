---
description: ScanContent schema from Palo Alto Networks Prisma AIRS API
layout: schema
name: ScanContent
properties_list:
- description: The user prompt or input text sent to the AI model. Evaluated for prompt injection, jailbreak attempts, and other input-side threats.
  name: prompt
  type: string
- description: The AI model response or output text. When provided, also evaluated for data leakage, toxic content, and other output-side threats. May be omitted to scan only the prompt.
  name: response
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-api-scan-content-schema.json
slug: prisma-airs-api-scan-content
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanContent
---
