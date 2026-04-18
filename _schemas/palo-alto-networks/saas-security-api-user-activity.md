---
description: UserActivity schema from Palo Alto Networks SaaS Security API
layout: schema
name: UserActivity
properties_list:
- description: Unique activity record identifier.
  name: id
  type: string
- description: ID of the user who performed the action.
  name: user_id
  type: string
- description: SaaS application where the activity occurred.
  name: app_id
  type: string
- description: Type of action performed (e.g., file_download, share_external).
  name: action
  type: string
- description: ID of the asset involved in the activity.
  name: asset_id
  type: string
- description: Timestamp when the activity occurred.
  name: timestamp
  type: string
- description: Source IP address of the activity.
  name: ip_address
  type: string
- description: Risk level assigned to this activity.
  name: risk_level
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/saas-security-api-user-activity-schema.json
slug: saas-security-api-user-activity
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: UserActivity
---
