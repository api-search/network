---
description: A XSIAM alert representing a detection from any ingested data source.
layout: schema
name: Alert
properties_list:
- description: ''
  name: alert_id
  type: string
- description: ''
  name: detection_timestamp
  type: integer
- description: ''
  name: name
  type: string
- description: ''
  name: category
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: severity
  type: string
- description: Data source that generated this alert.
  name: source
  type: string
- description: ''
  name: host_name
  type: string
- description: ''
  name: user_name
  type: string
- description: ''
  name: action
  type: string
- description: ''
  name: alert_type
  type: string
- description: ''
  name: resolution_status
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-api-alert-schema.json
slug: cortex-xsiam-api-alert
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
