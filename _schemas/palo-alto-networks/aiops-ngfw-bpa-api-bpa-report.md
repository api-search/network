---
description: BPAReport schema from Palo Alto Networks AIOps for NGFW BPA API
layout: schema
name: BPAReport
properties_list:
- description: Unique identifier of the report.
  name: report_id
  type: string
- description: ID of the BPA request that generated this report.
  name: request_id
  type: string
- description: Device serial number assessed.
  name: serial_number
  type: string
- description: PAN-OS version assessed.
  name: pan_os_version
  type: string
- description: Overall best practice compliance score from 0.0 to 100.0.
  name: overall_score
  type: number
- description: Compliance scores broken down by best practice category.
  name: category_scores
  type: array
- description: Total number of checks evaluated.
  name: total_checks
  type: integer
- description: Number of checks that passed.
  name: passed_checks
  type: integer
- description: Number of checks that failed.
  name: failed_checks
  type: integer
- description: Timestamp when the report was generated.
  name: generated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/aiops-ngfw-bpa-api-bpa-report-schema.json
slug: aiops-ngfw-bpa-api-bpa-report
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BPAReport
---
