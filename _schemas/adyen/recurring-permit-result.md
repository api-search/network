---
description: PermitResult schema from Adyen API
layout: schema
name: PermitResult
properties_list:
- description: The key to link permit requests to permit results.
  name: resultKey
  type: string
- description: The permit token which is used to make payments by the partner company.
  name: token
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-permit-result-schema.json
slug: recurring-permit-result
tags:
- Payments
- Financial Services
- Fintech
title: PermitResult
---
