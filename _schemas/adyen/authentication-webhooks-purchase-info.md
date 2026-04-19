---
description: PurchaseInfo schema from Adyen API
layout: schema
name: PurchaseInfo
properties_list:
- description: Date of the purchase.
  name: date
  type: string
- description: Name of the merchant.
  name: merchantName
  type: string
- description: Amount of the purchase.
  name: originalAmount
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/authentication-webhooks-purchase-info-schema.json
slug: authentication-webhooks-purchase-info
tags:
- Payments
- Financial Services
- Fintech
title: PurchaseInfo
---
