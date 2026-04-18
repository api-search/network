---
description: A Cortex XDR alert representing a single detection event.
layout: schema
name: Alert
properties_list:
- description: ''
  name: alert_id
  type: string
- description: Detection timestamp as Unix epoch milliseconds.
  name: detection_timestamp
  type: integer
- description: Alert name or rule name that triggered this alert.
  name: name
  type: string
- description: Alert category (e.g., Malware, Exploit, Lateral Movement).
  name: category
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: host_ip
  type: array
- description: ''
  name: host_name
  type: string
- description: ''
  name: user_name
  type: string
- description: ''
  name: mac
  type: array
- description: Data source that generated the alert.
  name: source
  type: string
- description: Action taken on the alert.
  name: action
  type: string
- description: ''
  name: action_pretty
  type: string
- description: ''
  name: severity
  type: string
- description: ''
  name: matching_status
  type: string
- description: ''
  name: alert_type
  type: string
- description: ''
  name: resolution_status
  type: string
- description: ''
  name: resolution_comment
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xdr-api-alert-schema.json
slug: cortex-xdr-api-alert
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Alert
---
