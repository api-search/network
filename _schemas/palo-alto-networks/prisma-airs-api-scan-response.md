---
description: ScanResponse schema from Palo Alto Networks Prisma AIRS API
layout: schema
name: ScanResponse
properties_list:
- description: Unique identifier of the scan.
  name: scan_id
  type: string
- description: Current or final status of the scan.
  name: status
  type: string
- description: Identifier for the detailed scan report.
  name: report_id
  type: string
- description: Highest severity threat category detected.
  name: scan_category
  type: string
- description: Per-content scan results corresponding to each submitted content item.
  name: results
  type: array
- description: Transaction ID echoed from the request if provided.
  name: tr_id
  type: string
- description: Timestamp when the scan was submitted.
  name: created_at
  type: string
- description: Timestamp when the scan completed.
  name: completed_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-airs-api-scan-response-schema.json
slug: prisma-airs-api-scan-response
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanResponse
---
