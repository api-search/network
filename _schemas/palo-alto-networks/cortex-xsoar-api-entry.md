---
description: A war room entry in a Cortex XSOAR investigation.
layout: schema
name: Entry
properties_list:
- description: ''
  name: id
  type: string
- description: ''
  name: investigationId
  type: string
- description: 'Entry type: 1 (Note), 2 (Download), 3 (File), 4 (Error), 5 (Pinned), 6 (UserManagement), 7 (Image), 8 (PlaygroundCommand), 9 (PlaybookStatusNote), 10 (Canvas), 11 (Widget), 12 (Summary), 13 (Section),'
  name: type
  type: integer
- description: Username of the user who created the entry.
  name: user
  type: string
- description: ''
  name: created
  type: string
- description: ''
  name: modified
  type: string
- description: Entry content text.
  name: contents
  type: string
- description: Human-readable formatted content.
  name: humanReadable
  type: string
- description: ''
  name: tags
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/cortex-xsoar-api-entry-schema.json
slug: cortex-xsoar-api-entry
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Entry
---
