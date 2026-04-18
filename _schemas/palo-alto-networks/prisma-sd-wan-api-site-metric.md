---
description: SiteMetric schema from Palo Alto Networks Prisma SD-WAN API
layout: schema
name: SiteMetric
properties_list:
- description: Time bucket for the aggregated metric.
  name: timestamp
  type: string
- description: Site identifier.
  name: site_id
  type: string
- description: WAN interface name.
  name: interface_name
  type: string
- description: Type of metric.
  name: metric_type
  type: string
- description: Metric value.
  name: value
  type: number
- description: Unit of measurement (e.g., Mbps, ms, pct).
  name: unit
  type: string
- description: Traffic direction for bandwidth metrics.
  name: direction
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/prisma-sd-wan-api-site-metric-schema.json
slug: prisma-sd-wan-api-site-metric
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: SiteMetric
---
