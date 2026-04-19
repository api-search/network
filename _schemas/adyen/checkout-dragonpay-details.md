---
description: DragonpayDetails schema from Adyen API
layout: schema
name: DragonpayDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The Dragonpay issuer value of the shopper's selected bank. Set this to an **id** of a Dragonpay issuer to preselect it.
  name: issuer
  type: string
- description: The shopper’s email address.
  name: shopperEmail
  type: string
- description: '**dragonpay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-dragonpay-details-schema.json
slug: checkout-dragonpay-details
tags:
- Payments
- Financial Services
- Fintech
title: DragonpayDetails
---
