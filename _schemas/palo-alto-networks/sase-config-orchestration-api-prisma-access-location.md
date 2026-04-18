---
description: PrismaAccessLocation schema from Palo Alto Networks SASE Configuration Orchestration API
layout: schema
name: PrismaAccessLocation
properties_list:
- description: Location identifier used in API requests.
  name: name
  type: string
- description: Human-readable location name.
  name: display_name
  type: string
- description: Geographic region (e.g., americas, europe, asia-pacific).
  name: region
  type: string
- description: Country code (ISO 3166-1 alpha-2).
  name: country
  type: string
- description: City name.
  name: city
  type: string
- description: Current availability status.
  name: status
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-config-orchestration-api-prisma-access-location-schema.json
slug: sase-config-orchestration-api-prisma-access-location
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: PrismaAccessLocation
---
