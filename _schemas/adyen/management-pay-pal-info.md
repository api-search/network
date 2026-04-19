---
description: PayPalInfo schema from Adyen API
layout: schema
name: PayPalInfo
properties_list:
- description: Indicates if direct (immediate) capture for PayPal is enabled. If set to **true**, this setting overrides the [capture](https://docs.adyen.com/online-payments/capture) settings of your merchant accoun
  name: directCapture
  type: boolean
- description: 'PayPal Merchant ID. Character length and limitations: 13 single-byte alphanumeric characters.'
  name: payerId
  type: string
- description: Your business email address.
  name: subject
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-pay-pal-info-schema.json
slug: management-pay-pal-info
tags:
- Payments
- Financial Services
- Fintech
title: PayPalInfo
---
