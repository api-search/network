---
description: CatalogApp schema from Palo Alto Networks SaaS Security Posture Management API
layout: schema
name: CatalogApp
properties_list:
- description: Application type identifier used for onboarding.
  name: app_type
  type: string
- description: Human-readable application name.
  name: display_name
  type: string
- description: Application category (e.g., collaboration, crm, storage).
  name: category
  type: string
- description: Number of posture checks available for this application.
  name: check_count
  type: integer
- description: Compliance frameworks covered by checks for this application.
  name: compliance_frameworks
  type: array
- description: URL to the application logo.
  name: logo_url
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sspm-api-catalog-app-schema.json
slug: sspm-api-catalog-app
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: CatalogApp
---
