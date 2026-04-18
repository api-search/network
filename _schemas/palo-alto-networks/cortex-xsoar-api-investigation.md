---
description: A Cortex XSOAR investigation containing war room entries and playbook state.
layout: schema
name: Investigation
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: name
  type: string
- description: ''
  name: status
  type: integer
- description: ''
  name: incidentId
  type: string
- description: ''
  name: created
  type: string
- description: ''
  name: modified
  type: string
- description: ''
  name: entries
  type: array
- description: ''
  name: playbookId
  type: string
- description: ''
  name: runningPlaybooks
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-investigation-schema.json
slug: cortex-xsoar-api-investigation
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Investigation
---
