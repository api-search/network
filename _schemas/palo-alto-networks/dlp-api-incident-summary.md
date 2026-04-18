---
description: IncidentSummary schema from Palo Alto Networks Enterprise DLP API
layout: schema
name: IncidentSummary
properties_list:
- description: Total number of incidents in the reporting period.
  name: total_incidents
  type: integer
- description: Number of incidents still in open status.
  name: open_incidents
  type: integer
- description: Number of resolved incidents.
  name: resolved_incidents
  type: integer
- description: Incident count breakdown by severity.
  name: by_severity
  type: object
- description: Incident count breakdown by detection channel.
  name: by_channel
  type: object
- description: Most frequently triggered data patterns.
  name: top_data_patterns
  type: array
- description: Users with the most incidents.
  name: top_users
  type: array
- description: Time range for the summary report.
  name: reporting_period
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/dlp-api-incident-summary-schema.json
slug: dlp-api-incident-summary
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: IncidentSummary
---
