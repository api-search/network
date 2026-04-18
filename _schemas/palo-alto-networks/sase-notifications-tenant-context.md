---
description: Tenant context information for multitenant notification routing.
layout: schema
name: TenantContext
properties_list:
- description: Tenant Service Group identifier.
  name: tsg_id
  type: string
- description: Human-readable tenant name.
  name: tenantName
  type: string
- description: Parent Tenant Service Group identifier for hierarchical tenant structures.
  name: parentTsgId
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-notifications-tenant-context-schema.json
slug: sase-notifications-tenant-context
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: TenantContext
---
