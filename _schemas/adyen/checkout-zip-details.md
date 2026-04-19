---
description: ZipDetails schema from Adyen API
layout: schema
name: ZipDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: Set this to **true** if the shopper would like to pick up and collect their order, instead of having the goods delivered to them.
  name: clickAndCollect
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**zip**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-zip-details-schema.json
slug: checkout-zip-details
tags:
- Payments
- Financial Services
- Fintech
title: ZipDetails
---
