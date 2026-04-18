---
description: BrowserPolicyRequest schema from Palo Alto Networks Prisma Access Browser Management API
layout: schema
name: BrowserPolicyRequest
properties_list:
- description: Display name for the browser policy.
  name: name
  type: string
- description: Optional description.
  name: description
  type: string
- description: ''
  name: enabled
  type: boolean
- description: ''
  name: web_filtering
  type: object
- description: ''
  name: dlp_enabled
  type: boolean
- description: ''
  name: extension_policy
  type: string
- description: ''
  name: download_control
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-browser-api-browser-policy-request-schema.json
slug: prisma-access-browser-api-browser-policy-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BrowserPolicyRequest
---
