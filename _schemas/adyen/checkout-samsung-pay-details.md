---
description: SamsungPayDetails schema from Adyen API
layout: schema
name: SamsungPayDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.
  name: fundingSource
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: The payload you received from the Samsung Pay SDK response.
  name: samsungPayToken
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**samsungpay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-samsung-pay-details-schema.json
slug: checkout-samsung-pay-details
tags:
- Payments
- Financial Services
- Fintech
title: SamsungPayDetails
---
