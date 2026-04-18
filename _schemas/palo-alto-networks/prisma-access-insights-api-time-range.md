---
description: Time range specification for the query
layout: schema
name: TimeRange
properties_list:
- description: Type of time range (absolute or relative)
  name: type
  type: string
- description: Time range value (required for ABSOLUTE type)
  name: value
  type: object
- description: Relative time range (required for RELATIVE type)
  name: last
  type: object
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-access-insights-api-time-range-schema.json
slug: prisma-access-insights-api-time-range
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: TimeRange
---
