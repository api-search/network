---
description: Tenant5GRequest schema from Palo Alto Networks SASE 5G Managed Services API
layout: schema
name: Tenant5GRequest
properties_list:
- description: Display name for the tenant configuration.
  name: name
  type: string
- description: Optional description.
  name: description
  type: string
- description: Network slice IDs to assign to this tenant.
  name: assigned_slices
  type: array
- description: Default security policy ID for this tenant.
  name: default_policy_id
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-5g-api-tenant5-g-request-schema.json
slug: sase-5g-api-tenant5-g-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: Tenant5GRequest
---
