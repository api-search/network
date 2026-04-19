---
description: Acronis tenant representing a company, partner, or customer account
layout: schema
name: Tenant
properties_list:
- description: Tenant unique identifier
  name: id
  type: string
- description: Tenant display name
  name: name
  type: string
- description: Tenant type in the hierarchy
  name: kind
  type: string
- description: Whether the tenant is active
  name: enabled
  type: boolean
- description: Parent tenant UUID
  name: parent_id
  type: string
- description: Customer account type
  name: customer_type
  type: string
- description: Tenant creation timestamp
  name: created_at
  type: string
- description: Last update timestamp
  name: updated_at
  type: string
- description: Optimistic concurrency version
  name: version
  type: integer
- description: ''
  name: contact
  type: object
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/account-management-tenant-schema.json
slug: account-management-tenant
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: Tenant
---
