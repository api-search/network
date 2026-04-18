---
description: CreateEntryRequest schema from Palo Alto Networks Cortex XSOAR REST API
layout: schema
name: CreateEntryRequest
properties_list:
- description: ID of the investigation to add the entry to.
  name: investigationId
  type: string
- description: Entry content text or command to execute.
  name: data
  type: string
- description: Whether to render the content as Markdown.
  name: markdown
  type: boolean
- description: ''
  name: tags
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-create-entry-request-schema.json
slug: cortex-xsoar-api-create-entry-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: CreateEntryRequest
---
