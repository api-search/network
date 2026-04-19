---
description: GenericIssuerPaymentMethodDetails schema from Adyen API
layout: schema
name: GenericIssuerPaymentMethodDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The issuer id of the shopper's selected bank.
  name: issuer
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: recurringDetailReference
  type: string
- description: This is the `recurringDetailReference` returned in the response when you created the token.
  name: storedPaymentMethodId
  type: string
- description: '**genericissuer**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-generic-issuer-payment-method-details-schema.json
slug: checkout-generic-issuer-payment-method-details
tags:
- Payments
- Financial Services
- Fintech
title: GenericIssuerPaymentMethodDetails
---
