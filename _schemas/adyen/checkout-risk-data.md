---
description: RiskData schema from Adyen API
layout: schema
name: RiskData
properties_list:
- description: Contains client-side data, like the device fingerprint, cookies, and specific browser settings.
  name: clientData
  type: string
- description: Any custom fields used as part of the input to configured risk rules.
  name: customFields
  type: object
- description: An integer value that is added to the normal fraud score. The value can be either positive or negative.
  name: fraudOffset
  type: integer
- description: The risk profile to assign to this payment. When left empty, the merchant-level account's default risk profile will be applied.
  name: profileReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-risk-data-schema.json
slug: checkout-risk-data
tags:
- Payments
- Financial Services
- Fintech
title: RiskData
---
