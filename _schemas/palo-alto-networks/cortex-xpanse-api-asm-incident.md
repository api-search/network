---
description: An attack surface incident representing a confirmed exposure requiring remediation.
layout: schema
name: AsmIncident
properties_list:
- description: Unique attack surface incident identifier.
  name: incident_id
  type: string
- description: ''
  name: incident_name
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: severity
  type: string
- description: Attack surface rule types that triggered this incident.
  name: incident_type
  type: array
- description: ''
  name: assigned_user_mail
  type: string
- description: ''
  name: assigned_user_pretty_name
  type: string
- description: ''
  name: alert_count
  type: integer
- description: ''
  name: description
  type: string
- description: Incident creation timestamp as Unix epoch milliseconds.
  name: creation_time
  type: integer
- description: ''
  name: modification_time
  type: integer
- description: ''
  name: resolved_by
  type: string
- description: ''
  name: resolve_comment
  type: string
- description: ''
  name: tags
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xpanse-api-asm-incident-schema.json
slug: cortex-xpanse-api-asm-incident
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AsmIncident
---
