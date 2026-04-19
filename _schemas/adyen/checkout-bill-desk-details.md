---
description: BillDeskDetails schema from Adyen API
layout: schema
name: BillDeskDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The issuer id of the shopper's selected bank.
  name: issuer
  type: string
- description: '**billdesk**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-bill-desk-details-schema.json
slug: checkout-bill-desk-details
tags:
- Payments
- Financial Services
- Fintech
title: BillDeskDetails
---
