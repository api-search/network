---
description: Card schema from Adyen API
layout: schema
name: Card
properties_list:
- description: 'The [card verification code](https://docs.adyen.com/payments-fundamentals/payment-glossary#card-security-code-cvc-cvv-cid) (1-20 characters). Depending on the card brand, it is known also as: * CVV2/C'
  name: cvc
  type: string
- description: 'The card expiry month. Format: 2 digits, zero-padded for single digits. For example: * 03 = March * 11 = November'
  name: expiryMonth
  type: string
- description: 'The card expiry year. Format: 4 digits. For example: 2020'
  name: expiryYear
  type: string
- description: The name of the cardholder, as printed on the card.
  name: holderName
  type: string
- description: The issue number of the card (for some UK debit cards only).
  name: issueNumber
  type: string
- description: The card number (4-19 characters). Do not use any separators. When this value is returned in a response, only the last 4 digits of the card number are returned.
  name: number
  type: string
- description: The month component of the start date (for some UK debit cards only).
  name: startMonth
  type: string
- description: The year component of the start date (for some UK debit cards only).
  name: startYear
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-card-schema.json
slug: checkout-card
tags:
- Payments
- Financial Services
- Fintech
title: Card
---
