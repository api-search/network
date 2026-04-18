---
description: User schema from Palo Alto Networks SaaS Security API
layout: schema
name: User
properties_list:
- description: Unique user identifier.
  name: id
  type: string
- description: User email address.
  name: email
  type: string
- description: User display name.
  name: display_name
  type: string
- description: SaaS application ID the user belongs to.
  name: app_id
  type: string
- description: Type of user account.
  name: account_type
  type: string
- description: Timestamp of the user's most recent activity.
  name: last_activity
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/saas-security-api-user-schema.json
slug: saas-security-api-user
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: User
---
