---
description: MonitoredApplication schema from Palo Alto Networks Autonomous DEM API
layout: schema
name: MonitoredApplication
properties_list:
- description: Unique application identifier.
  name: app_id
  type: string
- description: Application name.
  name: name
  type: string
- description: Application category (e.g., Collaboration, Productivity, Security).
  name: category
  type: string
- description: Whether the application is a SaaS or internal application.
  name: type
  type: string
- description: Primary URL for the application.
  name: url
  type: string
- description: Number of synthetic tests configured for this application.
  name: test_count
  type: integer
- description: Number of users with active monitoring for this application.
  name: monitored_users
  type: integer
- description: Timestamp when the application was added to monitoring.
  name: created_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/autonomous-dem-api-monitored-application-schema.json
slug: autonomous-dem-api-monitored-application
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: MonitoredApplication
---
