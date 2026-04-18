---
description: MonitoredAgent schema from Palo Alto Networks Autonomous DEM API
layout: schema
name: MonitoredAgent
properties_list:
- description: Unique ADEM agent identifier.
  name: agent_id
  type: string
- description: User email or identifier associated with this agent.
  name: user_id
  type: string
- description: Hostname of the endpoint device.
  name: device_name
  type: string
- description: Operating system of the endpoint.
  name: os
  type: string
- description: Operating system version string.
  name: os_version
  type: string
- description: ADEM agent software version.
  name: agent_version
  type: string
- description: Site name where the agent is located.
  name: site_name
  type: string
- description: Current agent connectivity status.
  name: status
  type: string
- description: Timestamp of the last agent heartbeat.
  name: last_seen
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/autonomous-dem-api-monitored-agent-schema.json
slug: autonomous-dem-api-monitored-agent
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: MonitoredAgent
---
