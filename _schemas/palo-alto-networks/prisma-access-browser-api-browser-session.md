---
description: BrowserSession schema from Palo Alto Networks Prisma Access Browser Management API
layout: schema
name: BrowserSession
properties_list:
- description: Unique identifier of the browser session.
  name: session_id
  type: string
- description: User ID of the session owner.
  name: user_id
  type: string
- description: Device ID used in this session.
  name: device_id
  type: string
- description: Client IP address.
  name: ip_address
  type: string
- description: Policy applied during this session.
  name: policy_id
  type: string
- description: Prisma Access Browser version.
  name: browser_version
  type: string
- description: Session status.
  name: status
  type: string
- description: ''
  name: started_at
  type: string
- description: ''
  name: ended_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-browser-api-browser-session-schema.json
slug: prisma-access-browser-api-browser-session
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BrowserSession
---
