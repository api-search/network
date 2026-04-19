---
description: NotifyShopperResult schema from Adyen API
layout: schema
name: NotifyShopperResult
properties_list:
- description: Reference of Pre-debit notification that is displayed to the shopper
  name: displayedReference
  type: string
- description: A simple description of the `resultCode`.
  name: message
  type: string
- description: The unique reference that is associated with the request.
  name: pspReference
  type: string
- description: Reference of Pre-debit notification sent in my the merchant
  name: reference
  type: string
- description: The code indicating the status of notification.
  name: resultCode
  type: string
- description: The unique reference for the request sent downstream.
  name: shopperNotificationReference
  type: string
- description: This is the recurringDetailReference returned in the response when token was created
  name: storedPaymentMethodId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/recurring-notify-shopper-result-schema.json
slug: recurring-notify-shopper-result
tags:
- Payments
- Financial Services
- Fintech
title: NotifyShopperResult
---
