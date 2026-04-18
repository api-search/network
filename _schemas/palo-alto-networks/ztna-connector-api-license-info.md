---
description: LicenseInfo schema from Palo Alto Networks ZTNA Connector API
layout: schema
name: LicenseInfo
properties_list:
- description: Total number of ZTNA user licenses purchased.
  name: licensed_users
  type: integer
- description: Number of users actively using ZTNA.
  name: active_users
  type: integer
- description: Subscription identifier.
  name: subscription_id
  type: string
- description: Subscription expiration date and time.
  name: expires_at
  type: string
- description: List of enabled ZTNA feature entitlements.
  name: features
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/ztna-connector-api-license-info-schema.json
slug: ztna-connector-api-license-info
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: LicenseInfo
---
