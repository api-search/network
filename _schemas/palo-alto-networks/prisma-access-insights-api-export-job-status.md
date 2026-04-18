---
description: Status and result of an export job
layout: schema
name: ExportJobStatus
properties_list:
- description: Export job identifier
  name: job_id
  type: string
- description: Current job status
  name: status
  type: string
- description: Signed URL to download the export file (available when COMPLETED)
  name: download_url
  type: string
- description: Expiration time of the download URL
  name: expires_at
  type: string
- description: Error description if the job failed
  name: error_message
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-insights-api-export-job-status-schema.json
slug: prisma-access-insights-api-export-job-status
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ExportJobStatus
---
