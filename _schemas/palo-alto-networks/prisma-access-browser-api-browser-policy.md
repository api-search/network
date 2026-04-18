---
description: BrowserPolicy schema from Palo Alto Networks Prisma Access Browser Management API
layout: schema
name: BrowserPolicy
properties_list:
- description: Unique identifier of the browser policy.
  name: policy_id
  type: string
- description: Display name of the policy.
  name: name
  type: string
- description: Description of the policy's purpose.
  name: description
  type: string
- description: Whether the policy is active.
  name: enabled
  type: boolean
- description: Web filtering configuration.
  name: web_filtering
  type: object
- description: Whether DLP controls are enabled.
  name: dlp_enabled
  type: boolean
- description: Extension installation policy.
  name: extension_policy
  type: string
- description: File download control setting.
  name: download_control
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-browser-api-browser-policy-schema.json
slug: prisma-access-browser-api-browser-policy
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: BrowserPolicy
---
