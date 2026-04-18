---
description: An audit management log entry recording an administrative action.
layout: schema
name: AuditLog
properties_list:
- description: Action timestamp as Unix epoch milliseconds.
  name: timestamp
  type: integer
- description: ''
  name: actor_primary_username
  type: string
- description: ''
  name: actor_email
  type: string
- description: ''
  name: actor_type
  type: string
- description: Action subtype (e.g., Login, PolicyUpdate, DatasourceCreate).
  name: sub_type
  type: string
- description: ''
  name: result
  type: string
- description: ''
  name: reason
  type: string
- description: ''
  name: ip
  type: string
- description: ''
  name: description
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-api-audit-log-schema.json
slug: cortex-xsiam-api-audit-log
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AuditLog
---
