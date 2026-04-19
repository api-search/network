---
description: TransferNotificationMerchantData schema from Adyen API
layout: schema
name: TransferNotificationMerchantData
properties_list:
- description: The unique identifier of the merchant's acquirer.
  name: acquirerId
  type: string
- description: The city where the merchant is located.
  name: city
  type: string
- description: The country where the merchant is located.
  name: country
  type: string
- description: The merchant category code.
  name: mcc
  type: string
- description: The merchant identifier.
  name: merchantId
  type: string
- description: The name of the merchant's shop or service.
  name: name
  type: string
- description: The merchant postal code.
  name: postalCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-transfer-notification-merchant-data-schema.json
slug: transfer-webhooks-transfer-notification-merchant-data
tags:
- Payments
- Financial Services
- Fintech
title: TransferNotificationMerchantData
---
