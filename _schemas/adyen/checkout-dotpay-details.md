---
description: DotpayDetails schema from Adyen API
layout: schema
name: DotpayDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The Dotpay issuer value of the shopper's selected bank. Set this to an **id** of a Dotpay issuer to preselect it.
  name: issuer
  type: string
- description: '**dotpay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-dotpay-details-schema.json
slug: checkout-dotpay-details
tags:
- Payments
- Financial Services
- Fintech
title: DotpayDetails
---
