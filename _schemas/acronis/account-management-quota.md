---
description: Quota configuration for an offering item
layout: schema
name: Quota
properties_list:
- description: Quota value (null for unlimited)
  name: value
  type: number
- description: Allowed overage beyond quota
  name: overage
  type: number
- description: Quota version for concurrency
  name: version
  type: integer
provider_name: Acronis
provider_slug: acronis
schema_file: json-schema/account-management-quota-schema.json
slug: account-management-quota
tags:
- Cybersecurity
- Data Protection
- Endpoint Management
title: Quota
---
