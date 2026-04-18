---
description: An endpoint enrolled in XSIAM protection.
layout: schema
name: Endpoint
properties_list:
- description: ''
  name: endpoint_id
  type: string
- description: ''
  name: endpoint_name
  type: string
- description: ''
  name: endpoint_type
  type: string
- description: ''
  name: endpoint_status
  type: string
- description: ''
  name: os_type
  type: string
- description: ''
  name: ip
  type: array
- description: ''
  name: users
  type: array
- description: ''
  name: domain
  type: string
- description: ''
  name: first_seen
  type: integer
- description: ''
  name: last_seen
  type: integer
- description: ''
  name: endpoint_version
  type: string
- description: ''
  name: content_version
  type: string
- description: ''
  name: is_isolated
  type: string
- description: ''
  name: scan_status
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsiam-api-endpoint-schema.json
slug: cortex-xsiam-api-endpoint
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Endpoint
---
