---
description: NetworkStats schema from Palo Alto Networks DNS Security API
layout: schema
name: NetworkStats
properties_list:
- description: Customer ID for which statistics are returned.
  name: customerid
  type: string
- description: ''
  name: period
  type: object
- description: Total DNS queries processed during the period.
  name: total_queries
  type: integer
- description: DNS queries blocked by DNS Security policy.
  name: blocked_queries
  type: integer
- description: DNS queries allowed by DNS Security policy.
  name: allowed_queries
  type: integer
- description: DNS queries redirected to sinkhole.
  name: sinkholed_queries
  type: integer
- description: Most frequently queried domains during the period.
  name: top_queried_domains
  type: array
- description: Query counts grouped by DNS Security category.
  name: category_breakdown
  type: array
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/dns-security-api-network-stats-schema.json
slug: dns-security-api-network-stats
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: NetworkStats
---
