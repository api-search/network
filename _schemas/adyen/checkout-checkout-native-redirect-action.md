---
description: CheckoutNativeRedirectAction schema from Adyen API
layout: schema
name: CheckoutNativeRedirectAction
properties_list:
- description: When the redirect URL must be accessed via POST, use this data to post to the redirect URL.
  name: data
  type: object
- description: Specifies the HTTP method, for example GET or POST.
  name: method
  type: string
- description: Native SDK's redirect data containing the direct issuer link and state data that must be submitted to the /v1/nativeRedirect/redirectResult.
  name: nativeRedirectData
  type: string
- description: Specifies the payment method.
  name: paymentMethodType
  type: string
- description: '**nativeRedirect**'
  name: type
  type: string
- description: Specifies the URL to redirect to.
  name: url
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-checkout-native-redirect-action-schema.json
slug: checkout-checkout-native-redirect-action
tags:
- Payments
- Financial Services
- Fintech
title: CheckoutNativeRedirectAction
---
