---
description: Application schema from Palo Alto Networks SaaS Security API
layout: schema
name: Application
properties_list:
- description: Unique application identifier.
  name: id
  type: string
- description: SaaS application name (e.g., Google Drive, Microsoft SharePoint).
  name: name
  type: string
- description: Application type or category.
  name: type
  type: string
- description: Current connection status.
  name: status
  type: string
- description: Number of assets scanned for this application.
  name: asset_count
  type: integer
- description: Number of active incidents for this application.
  name: incident_count
  type: integer
- description: Timestamp when the application was connected.
  name: connected_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/saas-security-api-application-schema.json
slug: saas-security-api-application
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Application
---
