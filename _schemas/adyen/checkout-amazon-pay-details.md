---
description: AmazonPayDetails schema from Adyen API
layout: schema
name: AmazonPayDetails
properties_list:
- description: This is the `amazonPayToken` that you obtained from the [Get Checkout Session](https://amazon-pay-acquirer-guide.s3-eu-west-1.amazonaws.com/v1/amazon-pay-api-v2/checkout-session.html#get-checkout-sess
  name: amazonPayToken
  type: string
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The `checkoutSessionId` is used to identify the checkout session at the Amazon Pay side. This field is required only for drop-in and components integration, where it replaces the amazonPayToken.
  name: checkoutSessionId
  type: string
- description: '**amazonpay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-amazon-pay-details-schema.json
slug: checkout-amazon-pay-details
tags:
- Payments
- Financial Services
- Fintech
title: AmazonPayDetails
---
