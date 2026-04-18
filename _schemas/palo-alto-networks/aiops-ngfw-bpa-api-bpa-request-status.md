---
description: BPARequestStatus schema from Palo Alto Networks AIOps for NGFW BPA API
layout: schema
name: BPARequestStatus
properties_list:
- description: Unique identifier of the BPA request.
  name: request_id
  type: string
- description: Device serial number for which the assessment was submitted.
  name: serial_number
  type: string
- description: Current processing status of the request.
  name: status
  type: string
- description: Report identifier available when status is completed. Use with GET /reports/{report_id} to retrieve the full report.
  name: report_id
  type: string
- description: Error description when status is failed.
  name: error_message
  type: string
- description: Timestamp when the request was submitted.
  name: submitted_at
  type: string
- description: Timestamp when processing completed.
  name: completed_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/aiops-ngfw-bpa-api-bpa-request-status-schema.json
slug: aiops-ngfw-bpa-api-bpa-request-status
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BPARequestStatus
---
