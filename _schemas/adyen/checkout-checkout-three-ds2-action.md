---
description: CheckoutThreeDS2Action schema from Adyen API
layout: schema
name: CheckoutThreeDS2Action
properties_list:
- description: A token needed to authorise a payment.
  name: authorisationToken
  type: string
- description: Encoded payment data.
  name: paymentData
  type: string
- description: Specifies the payment method.
  name: paymentMethodType
  type: string
- description: A subtype of the token.
  name: subtype
  type: string
- description: A token to pass to the 3DS2 Component to get the fingerprint.
  name: token
  type: string
- description: '**threeDS2**'
  name: type
  type: string
- description: Specifies the URL to redirect to.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-three-ds2-action-schema.json
slug: checkout-checkout-three-ds2-action
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutThreeDS2Action
---
