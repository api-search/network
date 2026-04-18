---
description: TenantSummary schema from Palo Alto Networks SASE Aggregate Monitoring API
layout: schema
name: TenantSummary
properties_list:
- description: Tenant Service Group ID.
  name: tsg_id
  type: string
- description: TSG display name.
  name: display_name
  type: string
- description: Parent TSG ID.
  name: parent_id
  type: string
- description: Depth in the hierarchy (0 for root).
  name: depth
  type: integer
- description: Number of direct child TSGs.
  name: child_count
  type: integer
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-aggregate-monitoring-api-tenant-summary-schema.json
slug: sase-aggregate-monitoring-api-tenant-summary
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: TenantSummary
---
