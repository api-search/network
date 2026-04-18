---
description: ScanReport schema from Palo Alto Networks Prisma AIRS AI Red Teaming API
layout: schema
name: ScanReport
properties_list:
- description: Unique identifier of the scan.
  name: scan_id
  type: string
- description: ID of the assessed target.
  name: target_id
  type: string
- description: Display name of the assessed target.
  name: target_name
  type: string
- description: Overall vulnerability risk score from 0.0 (no risk) to 10.0 (critical).
  name: overall_risk_score
  type: number
- description: Total number of attack probes executed.
  name: total_attacks_executed
  type: integer
- description: Total number of vulnerabilities discovered.
  name: vulnerabilities_found
  type: integer
- description: Vulnerability summary per attack category.
  name: category_summaries
  type: array
- description: Individual vulnerability findings.
  name: findings
  type: array
- description: Timestamp when the report was generated.
  name: generated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-ai-red-teaming-api-scan-report-schema.json
slug: prisma-airs-ai-red-teaming-api-scan-report
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanReport
---
