---
description: Acronis protection agent registered on an endpoint
layout: schema
name: Agent
properties_list:
- description: Agent unique identifier
  name: id
  type: string
- description: Hostname of the protected machine
  name: hostname
  type: string
- description: Current agent connection status
  name: status
  type: string
- description: Agent software version
  name: version
  type: string
- description: Tenant this agent belongs to
  name: tenant_id
  type: string
- description: ''
  name: os
  type: object
- description: Last time agent communicated with the platform
  name: last_seen
  type: string
- description: ''
  name: registration_time
  type: string
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/agent-management-agent-schema.json
slug: agent-management-agent
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: Agent
---
