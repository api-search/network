---
description: A Cortex XSOAR integration pack providing connectivity to a third-party tool.
layout: schema
name: Integration
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: name
  type: string
- description: Human-readable display name.
  name: display
  type: string
- description: Integration category (e.g., Endpoint, Firewall, SIEM).
  name: category
  type: string
- description: ''
  name: description
  type: string
- description: ''
  name: version
  type: integer
- description: ''
  name: fromVersion
  type: string
- description: ''
  name: deprecated
  type: boolean
- description: ''
  name: beta
  type: boolean
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-integration-schema.json
slug: cortex-xsoar-api-integration
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Integration
---
