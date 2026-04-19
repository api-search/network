---
description: PaymentMethod schema from Adyen API
layout: schema
name: PaymentMethod
properties_list:
- description: 'Brand for the selected gift card. For example: plastix, hmclub.'
  name: brand
  type: string
- description: 'List of possible brands. For example: visa, mc.'
  name: brands
  type: array
- description: The configuration of the payment method.
  name: configuration
  type: object
- description: The funding source of the payment method.
  name: fundingSource
  type: string
- description: The group where this payment method belongs to.
  name: group
  type: object
- description: All input details to be provided to complete the payment with this payment method.
  name: inputDetails
  type: array
- description: A list of issuers for this payment method.
  name: issuers
  type: array
- description: The displayable name of this payment method.
  name: name
  type: string
- description: The unique payment method code.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-payment-method-schema.json
slug: checkout-payment-method
tags:
- Payments
- Financial Services
- Fintech
title: PaymentMethod
---
