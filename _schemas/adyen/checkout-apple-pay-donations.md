---
description: ApplePayDonations schema from Adyen API
layout: schema
name: ApplePayDonations
properties_list:
- description: The stringified and base64 encoded `paymentData` you retrieved from the Apple framework.
  name: applePayToken
  type: string
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.
  name: fundingSource
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**applepay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-apple-pay-donations-schema.json
slug: checkout-apple-pay-donations
tags:
- Payments
- Financial Services
- Fintech
title: ApplePayDonations
---
