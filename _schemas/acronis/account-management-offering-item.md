---
description: An Acronis service or feature that can be enabled for a tenant
layout: schema
name: OfferingItem
properties_list:
- description: Offering item identifier name
  name: name
  type: string
- description: Application that provides this offering item
  name: application_id
  type: string
- description: Item status (1=active, 0=inactive)
  name: status
  type: integer
- description: ''
  name: quota
  type: object
- description: Edition name this item belongs to
  name: edition
  type: string
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/account-management-offering-item-schema.json
slug: account-management-offering-item
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: OfferingItem
---
