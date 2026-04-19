---
description: RatepayDetails schema from Adyen API
layout: schema
name: RatepayDetails
properties_list:
- description: The address where to send the invoice.
  name: billingAddress
  type: string
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The address where the goods should be delivered.
  name: deliveryAddress
  type: string
- description: Shopper name, date of birth, phone number, and email address.
  name: personalDetails
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**ratepay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-ratepay-details-schema.json
slug: checkout-ratepay-details
tags:
- Payments
- Financial Services
- Fintech
title: RatepayDetails
---
