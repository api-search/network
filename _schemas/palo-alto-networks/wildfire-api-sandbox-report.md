---
description: Analysis results from a single sandbox execution environment.
layout: schema
name: SandboxReport
properties_list:
- description: Platform identifier (e.g., 100 for Windows XP SP3).
  name: platform
  type: string
- description: Sandbox software environment.
  name: software
  type: string
- description: ''
  name: version
  type: string
- description: ''
  name: summary
  type: object
- description: ''
  name: network
  type: object
- description: ''
  name: process_list
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/wildfire-api-sandbox-report-schema.json
slug: wildfire-api-sandbox-report
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SandboxReport
---
