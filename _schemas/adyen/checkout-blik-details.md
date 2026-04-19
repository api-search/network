---
description: BlikDetails schema from Adyen API
layout: schema
name: BlikDetails
properties_list:
- description: BLIK code consisting of 6 digits.
  name: blikCode
  type: string
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**blik**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-blik-details-schema.json
slug: checkout-blik-details
tags:
- Payments
- Financial Services
- Fintech
title: BlikDetails
---
