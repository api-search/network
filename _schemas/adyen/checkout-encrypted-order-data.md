---
description: EncryptedOrderData schema from Adyen API
layout: schema
name: EncryptedOrderData
properties_list:
- description: The encrypted order data.
  name: orderData
  type: string
- description: The `pspReference` that belongs to the order.
  name: pspReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-encrypted-order-data-schema.json
slug: checkout-encrypted-order-data
tags:
- Payments
- Financial Services
- Fintech
title: EncryptedOrderData
---
