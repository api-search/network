---
description: MolPayDetails schema from Adyen API
layout: schema
name: MolPayDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The shopper's bank. Specify this with the issuer value that corresponds to this bank.
  name: issuer
  type: string
- description: '**molpay**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-mol-pay-details-schema.json
slug: checkout-mol-pay-details
tags:
- Payments
- Financial Services
- Fintech
title: MolPayDetails
---
