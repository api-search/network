---
description: TenantServiceGroup schema from Palo Alto Networks SASE Tenancy Service API
layout: schema
name: TenantServiceGroup
properties_list:
- description: Unique identifier of the Tenant Service Group.
  name: id
  type: string
- description: Human-readable display name of the TSG.
  name: display_name
  type: string
- description: Optional description of the TSG's purpose.
  name: description
  type: string
- description: ID of the parent TSG in the hierarchy. Null for root-level TSGs.
  name: parent_id
  type: string
- description: Associated Palo Alto Networks support account identifier.
  name: support_account_id
  type: string
- description: Industry vertical classification for the TSG.
  name: vertical
  type: string
- description: Primary geographic region for the TSG.
  name: region
  type: string
- description: Current status of the TSG.
  name: status
  type: string
- description: Number of direct child TSGs.
  name: child_count
  type: integer
- description: Timestamp when the TSG was created.
  name: created_at
  type: string
- description: Timestamp of the most recent TSG modification.
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-tenancy-api-tenant-service-group-schema.json
slug: sase-tenancy-api-tenant-service-group
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: TenantServiceGroup
---
