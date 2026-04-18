---
description: Asset schema from Palo Alto Networks SaaS Security API
layout: schema
name: Asset
properties_list:
- description: Unique asset identifier.
  name: id
  type: string
- description: Asset name or filename.
  name: name
  type: string
- description: Asset type.
  name: type
  type: string
- description: ID of the SaaS application containing the asset.
  name: app_id
  type: string
- description: Name of the SaaS application.
  name: app_name
  type: string
- description: User ID of the asset owner.
  name: owner
  type: string
- description: Current exposure level of the asset.
  name: exposure
  type: string
- description: Asset size in bytes.
  name: size_bytes
  type: integer
- description: DLP policy violation names triggered for this asset.
  name: dlp_violations
  type: array
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
- description: ''
  name: last_scanned_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/saas-security-api-asset-schema.json
slug: saas-security-api-asset
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Asset
---
