---
description: GiropayDetails schema from Adyen API
layout: schema
name: GiropayDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**giropay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-giropay-details-schema.json
slug: checkout-giropay-details
tags:
- Payments
- Financial Services
- Fintech
title: GiropayDetails
---
