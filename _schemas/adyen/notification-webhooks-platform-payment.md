---
description: PlatformPayment schema from Adyen API
layout: schema
name: PlatformPayment
properties_list:
- description: The account given in the related split.
  name: account
  type: string
- description: The description of the related split.
  name: description
  type: string
- description: The merchant reference of the modification.
  name: modificationMerchantReference
  type: string
- description: The pspReference of the modification.
  name: modificationPspReference
  type: string
- description: The merchant reference of the payment.
  name: paymentMerchantReference
  type: string
- description: The pspReference of the payment.
  name: paymentPspReference
  type: string
- description: The reference of the related split.
  name: reference
  type: string
- description: The type of the related split.
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notification-webhooks-platform-payment-schema.json
slug: notification-webhooks-platform-payment
tags:
- Payments
- Financial Services
- Fintech
title: PlatformPayment
---
