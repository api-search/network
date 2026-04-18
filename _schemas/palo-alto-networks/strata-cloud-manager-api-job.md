---
description: An asynchronous job tracking configuration push or commit operations.
layout: schema
name: Job
properties_list:
- description: Unique job identifier.
  name: id
  type: string
- description: Job type (e.g., push, commit).
  name: type
  type: string
- description: Current job status.
  name: status
  type: string
- description: ''
  name: result
  type: string
- description: Job start timestamp.
  name: start_ts
  type: string
- description: Job completion timestamp.
  name: end_ts
  type: string
- description: Job completion percentage (0-100).
  name: percent
  type: integer
- description: Additional job details and error messages.
  name: details
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/strata-cloud-manager-api-job-schema.json
slug: strata-cloud-manager-api-job
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Job
---
