---
description: GooglePayInfo schema from Adyen API
layout: schema
name: GooglePayInfo
properties_list:
- description: 'Google Pay [Merchant ID](https://support.google.com/paymentscenter/answer/7163092?hl=en). Character length and limitations: 16 alphanumeric characters or 20 numeric characters.'
  name: merchantId
  type: string
- description: 'Indicates whether the Google Pay Merchant ID is used for several merchant accounts. Default value: **false**.'
  name: reuseMerchantId
  type: boolean
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/management-google-pay-info-schema.json
slug: management-google-pay-info
tags:
- Payments
- Financial Services
- Fintech
title: GooglePayInfo
---
