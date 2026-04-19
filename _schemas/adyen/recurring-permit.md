---
description: Permit schema from Adyen API
layout: schema
name: Permit
properties_list:
- description: Partner ID (when using the permit-per-partner token sharing model).
  name: partnerId
  type: string
- description: The profile to apply to this permit (when using the shared permits model).
  name: profileReference
  type: string
- description: Permit level restriction overrides.
  name: restriction
  type: object
- description: The key to link permit requests to permit results.
  name: resultKey
  type: string
- description: The expiry date for this permit.
  name: validTillDate
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-permit-schema.json
slug: recurring-permit
tags:
- Payments
- Financial Services
- Fintech
title: Permit
---
