---
description: An endpoint enrolled in Cortex XDR protection.
layout: schema
name: Endpoint
properties_list:
- description: Unique endpoint identifier.
  name: endpoint_id
  type: string
- description: Endpoint hostname.
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
- description: IP addresses assigned to the endpoint.
  name: ip
  type: array
- description: Users logged into the endpoint.
  name: users
  type: array
- description: ''
  name: domain
  type: string
- description: ''
  name: alias
  type: string
- description: First connection timestamp as Unix epoch milliseconds.
  name: first_seen
  type: integer
- description: Last connection timestamp as Unix epoch milliseconds.
  name: last_seen
  type: integer
- description: Cortex XDR agent content version.
  name: content_version
  type: string
- description: ''
  name: installation_package
  type: string
- description: ''
  name: active_directory
  type: string
- description: ''
  name: install_date
  type: integer
- description: Cortex XDR agent version.
  name: endpoint_version
  type: string
- description: ''
  name: is_isolated
  type: string
- description: ''
  name: isolation_reason
  type: string
- description: ''
  name: scan_status
  type: string
- description: ''
  name: group_name
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xdr-api-endpoint-schema.json
slug: cortex-xdr-api-endpoint
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
