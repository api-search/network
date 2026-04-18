---
description: A Cortex XDR incident grouping related alerts.
layout: schema
name: Incident
properties_list:
- description: ''
  name: incident_id
  type: string
- description: ''
  name: incident_name
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: status
  type: string
- description: ''
  name: severity
  type: string
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
  name: low_severity_alert_count
  type: integer
- description: ''
  name: med_severity_alert_count
  type: integer
- description: ''
  name: high_severity_alert_count
  type: integer
- description: ''
  name: critical_severity_alert_count
  type: integer
- description: ''
  name: user_count
  type: integer
- description: ''
  name: host_count
  type: integer
- description: Incident creation timestamp as Unix epoch milliseconds.
  name: creation_time
  type: integer
- description: Last modification timestamp as Unix epoch milliseconds.
  name: modification_time
  type: integer
- description: ''
  name: detection_time
  type: integer
- description: ''
  name: starred
  type: boolean
- description: Direct URL to the incident in the XDR console.
  name: xdr_url
  type: string
- description: ''
  name: rule_based_score
  type: integer
- description: ''
  name: manual_score
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xdr-api-incident-schema.json
slug: cortex-xdr-api-incident
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Incident
---
