---
description: AgentScore schema from Palo Alto Networks Autonomous DEM API
layout: schema
name: AgentScore
properties_list:
- description: Time bucket for the aggregated score.
  name: timestamp
  type: string
- description: Unique ADEM agent identifier.
  name: agent_id
  type: string
- description: User identifier associated with the agent.
  name: user_id
  type: string
- description: Hostname of the endpoint device.
  name: device_name
  type: string
- description: Site name where the agent is located.
  name: site_name
  type: string
- description: Overall experience score for this agent.
  name: overall_score
  type: integer
- description: Endpoint hardware and software health score.
  name: endpoint_score
  type: integer
- description: Network connectivity quality score.
  name: network_score
  type: integer
- description: CPU usage percentage on the endpoint.
  name: cpu_usage_pct
  type: number
- description: Memory usage percentage on the endpoint.
  name: memory_usage_pct
  type: number
- description: Number of measurement samples in this time bucket.
  name: sample_count
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/autonomous-dem-api-agent-score-schema.json
slug: autonomous-dem-api-agent-score
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: AgentScore
---
