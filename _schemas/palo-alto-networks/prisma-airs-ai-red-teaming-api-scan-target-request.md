---
description: ScanTargetRequest schema from Palo Alto Networks Prisma AIRS AI Red Teaming API
layout: schema
name: ScanTargetRequest
properties_list:
- description: Display name for the scan target.
  name: name
  type: string
- description: Optional description of the target application.
  name: description
  type: string
- description: AI interface type of the target endpoint.
  name: type
  type: string
- description: URL of the AI application endpoint to scan.
  name: endpoint_url
  type: string
- description: AI model name to include in requests (e.g., gpt-4o, claude-3-5-sonnet-20241022).
  name: model
  type: string
- description: Authentication configuration for the target endpoint.
  name: auth_config
  type: object
- description: System prompt to include in requests to the target. Used to scope red teaming attacks to the intended application context.
  name: system_prompt
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-ai-red-teaming-api-scan-target-request-schema.json
slug: prisma-airs-ai-red-teaming-api-scan-target-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanTargetRequest
---
