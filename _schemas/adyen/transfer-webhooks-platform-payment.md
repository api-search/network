---
description: PlatformPayment schema from Adyen API
layout: schema
name: PlatformPayment
properties_list:
- description: The capture's merchant reference included in the transfer.
  name: modificationMerchantReference
  type: string
- description: The capture reference included in the transfer.
  name: modificationPspReference
  type: string
- description: The payment's merchant reference included in the transfer.
  name: paymentMerchantReference
  type: string
- description: The type of the related split.
  name: platformPaymentType
  type: string
- description: The payment reference included in the transfer.
  name: pspPaymentReference
  type: string
- description: '**platformPayment**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-platform-payment-schema.json
slug: transfer-webhooks-platform-payment
tags:
- Payments
- Financial Services
- Fintech
title: PlatformPayment
---
