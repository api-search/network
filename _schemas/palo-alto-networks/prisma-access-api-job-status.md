---
description: JobStatus schema from Palo Alto Networks Prisma Access Configuration API
layout: schema
name: JobStatus
properties_list:
- description: Unique job identifier.
  name: id
  type: string
- description: Type of asynchronous job.
  name: type
  type: string
- description: Current status of the job.
  name: status
  type: string
- description: Final result of the job once completed.
  name: result
  type: string
- description: Timestamp when the job started.
  name: start_ts
  type: string
- description: Timestamp when the job completed.
  name: end_ts
  type: string
- description: Job description.
  name: description
  type: string
- description: Job status detail messages.
  name: details
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-api-job-status-schema.json
slug: prisma-access-api-job-status
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: JobStatus
---
