---
description: ContentScanResult schema from Palo Alto Networks Prisma AIRS API
layout: schema
name: ContentScanResult
properties_list:
- description: Threats detected in the prompt field.
  name: prompt_detected
  type: object
- description: Threats detected in the response field.
  name: response_detected
  type: object
- description: Overall verdict for this content pair.
  name: verdict
  type: string
- description: Action taken based on the security profile configuration.
  name: action
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-api-content-scan-result-schema.json
slug: prisma-airs-api-content-scan-result
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ContentScanResult
---
