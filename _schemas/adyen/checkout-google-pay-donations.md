---
description: GooglePayDonations schema from Adyen API
layout: schema
name: GooglePayDonations
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.
  name: fundingSource
  type: string
- description: The selected payment card network.
  name: googlePayCardNetwork
  type: string
- description: The `token` that you obtained from the [Google Pay API](https://developers.google.com/pay/api/web/reference/response-objects#PaymentData) `PaymentData` response.
  name: googlePayToken
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**googlepay**, **paywithgoogle**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-google-pay-donations-schema.json
slug: checkout-google-pay-donations
tags:
- Payments
- Financial Services
- Fintech
title: GooglePayDonations
---
