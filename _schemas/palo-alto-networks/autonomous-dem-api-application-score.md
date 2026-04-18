---
description: ApplicationScore schema from Palo Alto Networks Autonomous DEM API
layout: schema
name: ApplicationScore
properties_list:
- description: Time bucket for the aggregated score.
  name: timestamp
  type: string
- description: Monitored application identifier.
  name: app_id
  type: string
- description: Name of the monitored application.
  name: application
  type: string
- description: User identifier if filtering by user.
  name: user_id
  type: string
- description: Site name if filtering by site.
  name: site_name
  type: string
- description: Overall experience score from 0 to 100.
  name: overall_score
  type: integer
- description: Endpoint health score.
  name: endpoint_score
  type: integer
- description: Network path score.
  name: network_score
  type: integer
- description: Application responsiveness score.
  name: application_score
  type: integer
- description: Average round-trip latency in milliseconds.
  name: latency_ms
  type: number
- description: Packet loss percentage.
  name: packet_loss_pct
  type: number
- description: Latency variation in milliseconds.
  name: jitter_ms
  type: number
- description: Number of measurement samples in this time bucket.
  name: sample_count
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/autonomous-dem-api-application-score-schema.json
slug: autonomous-dem-api-application-score
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: ApplicationScore
---
