---
description: CheckoutSDKAction schema from Adyen API
layout: schema
name: CheckoutSDKAction
properties_list:
- description: Encoded payment data.
  name: paymentData
  type: string
- description: Specifies the payment method.
  name: paymentMethodType
  type: string
- description: The data to pass to the SDK.
  name: sdkData
  type: object
- description: The type of the action.
  name: type
  type: string
- description: Specifies the URL to redirect to.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-sdk-action-schema.json
slug: checkout-checkout-sdk-action
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutSDKAction
---
