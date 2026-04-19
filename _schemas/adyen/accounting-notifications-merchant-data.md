---
description: MerchantData schema from Adyen API
layout: schema
name: MerchantData
properties_list:
- description: The merchant category code.
  name: mcc
  type: string
- description: The merchant identifier.
  name: merchantId
  type: string
- description: Contains the merchant's name and location.
  name: nameLocation
  type: object
- description: The merchant postal code.
  name: postalCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/accounting-notifications-merchant-data-schema.json
slug: accounting-notifications-merchant-data
tags:
- Payments
- Financial Services
- Fintech
title: MerchantData
---
