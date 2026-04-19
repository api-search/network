---
description: AdditionalDataWallets schema from Adyen API
layout: schema
name: AdditionalDataWallets
properties_list:
- description: The Android Pay token retrieved from the SDK.
  name: androidpay.token
  type: string
- description: The Mastercard Masterpass Transaction ID retrieved from the SDK.
  name: masterpass.transactionId
  type: string
- description: The Apple Pay token retrieved from the SDK.
  name: payment.token
  type: string
- description: The Google Pay token retrieved from the SDK.
  name: paywithgoogle.token
  type: string
- description: The Samsung Pay token retrieved from the SDK.
  name: samsungpay.token
  type: string
- description: The Visa Checkout Call ID retrieved from the SDK.
  name: visacheckout.callId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-additional-data-wallets-schema.json
slug: checkout-additional-data-wallets
tags:
- Payments
- Financial Services
- Fintech
title: AdditionalDataWallets
---
