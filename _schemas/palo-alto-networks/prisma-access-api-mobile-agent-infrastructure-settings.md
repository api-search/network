---
description: MobileAgentInfrastructureSettings schema from Palo Alto Networks Prisma Access Configuration API
layout: schema
name: MobileAgentInfrastructureSettings
properties_list:
- description: ''
  name: id
  type: string
- description: Name for the infrastructure settings configuration.
  name: name
  type: string
- description: IP address pools for mobile user address allocation.
  name: ip_pool
  type: array
- description: DNS server IP addresses for mobile users.
  name: dns_servers
  type: array
- description: DNS suffixes to append for mobile users.
  name: dns_suffix
  type: array
- description: Compute regions for mobile user connectivity.
  name: regions
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-api-mobile-agent-infrastructure-settings-schema.json
slug: prisma-access-api-mobile-agent-infrastructure-settings
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: MobileAgentInfrastructureSettings
---
