---
description: UsageReport schema from Palo Alto Networks Prisma Access Browser Management API
layout: schema
name: UsageReport
properties_list:
- description: ''
  name: period
  type: object
- description: Number of unique active users during the period.
  name: active_users
  type: integer
- description: Total browser sessions started during the period.
  name: total_sessions
  type: integer
- description: Total data transferred through the browser in GB.
  name: data_transferred_gb
  type: number
- description: Number of threats blocked by the browser.
  name: threats_blocked
  type: integer
- description: Number of DLP policy events triggered.
  name: dlp_events
  type: integer
- description: Time-series data points for the report.
  name: data_points
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-browser-api-usage-report-schema.json
slug: prisma-access-browser-api-usage-report
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: UsageReport
---
