---
description: Scan schema from Palo Alto Networks Prisma AIRS AI Red Teaming API
layout: schema
name: Scan
properties_list:
- description: Unique identifier of the scan.
  name: scan_id
  type: string
- description: ID of the scan target being assessed.
  name: target_id
  type: string
- description: Display name of the scan target.
  name: target_name
  type: string
- description: Current status of the scan.
  name: status
  type: string
- description: Attack categories included in this scan.
  name: attack_categories
  type: array
- description: Scan completion progress from 0.0 to 1.0.
  name: progress
  type: number
- description: Total number of attack probes to be executed.
  name: total_attacks
  type: integer
- description: Number of attack probes completed so far.
  name: completed_attacks
  type: integer
- description: Number of vulnerabilities discovered so far.
  name: vulnerabilities_found
  type: integer
- description: Error description if the scan failed.
  name: error_message
  type: string
- description: Timestamp when the scan started.
  name: started_at
  type: string
- description: Timestamp when the scan completed.
  name: completed_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-ai-red-teaming-api-scan-schema.json
slug: prisma-airs-ai-red-teaming-api-scan
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Scan
---
