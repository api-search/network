---
description: ScanStatus schema from Palo Alto Networks Prisma Cloud Code Security API
layout: schema
name: ScanStatus
properties_list:
- description: Unique scan identifier.
  name: scan_id
  type: string
- description: Repository that was scanned.
  name: repositoryId
  type: string
- description: Branch that was scanned.
  name: branch
  type: string
- description: Current scan status.
  name: status
  type: string
- description: Scan start timestamp.
  name: startTime
  type: string
- description: Scan completion timestamp.
  name: endTime
  type: string
- description: Types of scans included in this run.
  name: scanTypes
  type: array
- description: High-level scan result summary. Available after completion.
  name: summary
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-cloud-code-security-api-scan-status-schema.json
slug: prisma-cloud-code-security-api-scan-status
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ScanStatus
---
