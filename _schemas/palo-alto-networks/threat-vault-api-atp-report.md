---
description: Advanced Threat Prevention inline analysis report.
layout: schema
name: AtpReport
properties_list:
- description: Unique report identifier.
  name: id
  type: string
- description: SHA-256 hash of the analyzed sample.
  name: sha256
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: verdict
  type: string
- description: ''
  name: create_time
  type: string
- description: Detailed behavioral analysis data.
  name: report
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/threat-vault-api-atp-report-schema.json
slug: threat-vault-api-atp-report
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AtpReport
---
