---
description: BrowserUser schema from Palo Alto Networks Prisma Access Browser Management API
layout: schema
name: BrowserUser
properties_list:
- description: Unique identifier of the browser user.
  name: user_id
  type: string
- description: User email address.
  name: email
  type: string
- description: User display name.
  name: display_name
  type: string
- description: ID of the browser policy assigned to this user.
  name: policy_id
  type: string
- description: Current number of active browser sessions.
  name: active_sessions
  type: integer
- description: ''
  name: last_active_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-browser-api-browser-user-schema.json
slug: prisma-access-browser-api-browser-user
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BrowserUser
---
