---
description: CreateIncidentRequest schema from Palo Alto Networks Cortex XSOAR REST API
layout: schema
name: CreateIncidentRequest
properties_list:
- description: Incident name.
  name: name
  type: string
- description: Incident type name.
  name: type
  type: string
- description: ''
  name: severity
  type: integer
- description: ''
  name: owner
  type: string
- description: ''
  name: occurred
  type: string
- description: ''
  name: details
  type: string
- description: ''
  name: labels
  type: array
- description: Whether to automatically create an investigation for this incident.
  name: createInvestigation
  type: boolean
- description: ''
  name: CustomFields
  type: object
- description: ''
  name: rawJson
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-create-incident-request-schema.json
slug: cortex-xsoar-api-create-incident-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: CreateIncidentRequest
---
