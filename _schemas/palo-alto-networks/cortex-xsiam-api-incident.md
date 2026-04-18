---
description: A XSIAM incident correlating related alerts into a unified investigation.
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
- description: Creation timestamp as Unix epoch milliseconds.
  name: creation_time
  type: integer
- description: ''
  name: modification_time
  type: integer
- description: ''
  name: detection_time
  type: integer
- description: ''
  name: starred
  type: boolean
- description: ''
  name: xdr_url
  type: string
- description: ''
  name: mitre_tactics_ids_and_names
  type: array
- description: ''
  name: mitre_techniques_ids_and_names
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-api-incident-schema.json
slug: cortex-xsiam-api-incident
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
