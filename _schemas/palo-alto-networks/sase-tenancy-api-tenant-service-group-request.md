---
description: TenantServiceGroupRequest schema from Palo Alto Networks SASE Tenancy Service API
layout: schema
name: TenantServiceGroupRequest
properties_list:
- description: Display name for the new TSG.
  name: display_name
  type: string
- description: Optional description of the TSG's purpose.
  name: description
  type: string
- description: ID of the parent TSG under which to create this TSG.
  name: parent_id
  type: string
- description: Palo Alto Networks support account ID to associate with this TSG.
  name: support_account_id
  type: string
- description: Industry vertical classification.
  name: vertical
  type: string
- description: Primary geographic region.
  name: region
  type: string
provider_name: Palo Alto Networks
provider_slug: palo-alto-networks
schema_file: json-schema/sase-tenancy-api-tenant-service-group-request-schema.json
slug: sase-tenancy-api-tenant-service-group-request
tags:
- Cloud Security
- Cybersecurity
- Firewall
- Network Security
- SASE
- SOAR
- Threat Intelligence
- XDR
title: TenantServiceGroupRequest
---
