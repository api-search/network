---
description: Tenant5G schema from Palo Alto Networks SASE 5G Managed Services API
layout: schema
name: Tenant5G
properties_list:
- description: Unique identifier of the 5G tenant configuration.
  name: tenant_id
  type: string
- description: Tenant display name.
  name: name
  type: string
- description: Description of the tenant.
  name: description
  type: string
- description: Network slice IDs assigned to this tenant.
  name: assigned_slices
  type: array
- description: Default security policy ID for this tenant's traffic.
  name: default_policy_id
  type: string
- description: ''
  name: created_at
  type: string
- description: ''
  name: updated_at
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-5g-api-tenant5-g-schema.json
slug: sase-5g-api-tenant5-g
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Tenant5G
---
