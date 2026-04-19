---
description: ApplePaySessionRequest schema from Adyen API
layout: schema
name: ApplePaySessionRequest
properties_list:
- description: This is the name that your shoppers will see in the Apple Pay interface. The value returned as `configuration.merchantName` field from the [`/paymentMethods`](https://docs.adyen.com/api-explorer/#/Che
  name: displayName
  type: string
- description: The domain name you provided when you added Apple Pay in your Customer Area. This must match the `window.location.hostname` of the web shop.
  name: domainName
  type: string
- description: Your merchant identifier registered with Apple Pay. Use the value of the `configuration.merchantId` field from the [`/paymentMethods`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post
  name: merchantIdentifier
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-apple-pay-session-request-schema.json
slug: checkout-apple-pay-session-request
tags:
- Payments
- Financial Services
- Fintech
title: ApplePaySessionRequest
---
