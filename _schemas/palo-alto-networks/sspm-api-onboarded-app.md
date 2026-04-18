---
description: OnboardedApp schema from Palo Alto Networks SaaS Security Posture Management API
layout: schema
name: OnboardedApp
properties_list:
- description: Unique identifier for the onboarded application.
  name: app_id
  type: string
- description: Application type identifier (e.g., google_workspace, microsoft_365).
  name: app_type
  type: string
- description: Human-readable name for the onboarded application instance.
  name: display_name
  type: string
- description: Current connection status.
  name: status
  type: string
- description: Tenant or domain identifier within the SaaS application.
  name: tenant_id
  type: string
- description: Summary counts of posture check results by severity.
  name: check_summary
  type: object
- description: Timestamp of the most recent posture scan.
  name: last_scanned_at
  type: string
- description: Timestamp when the application was onboarded.
  name: onboarded_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sspm-api-onboarded-app-schema.json
slug: sspm-api-onboarded-app
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: OnboardedApp
---
