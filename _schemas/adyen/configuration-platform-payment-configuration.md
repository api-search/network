---
description: PlatformPaymentConfiguration schema from Adyen API
layout: schema
name: PlatformPaymentConfiguration
properties_list:
- description: 'Specifies at what time a [sales day](https://docs.adyen.com/marketplaces-and-platforms/settle-funds/sales-day-settlement#sales-day) ends. Possible values: Time in **"HH:MM"** format. **HH** ranges fro'
  name: salesDayClosingTime
  type: string
- description: Specifies after how many business days the funds in a [settlement batch](https://docs.adyen.com/marketplaces-and-platforms/settle-funds/sales-day-settlement#settlement-batch) are made available. Possi
  name: settlementDelayDays
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-platform-payment-configuration-schema.json
slug: configuration-platform-payment-configuration
tags:
- Payments
- Financial Services
- Fintech
title: PlatformPaymentConfiguration
---
