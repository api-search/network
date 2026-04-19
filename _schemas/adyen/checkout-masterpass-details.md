---
description: MasterpassDetails schema from Adyen API
layout: schema
name: MasterpassDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**.
  name: fundingSource
  type: string
- description: The Masterpass transaction ID.
  name: masterpassTransactionId
  type: string
- description: '**masterpass**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-masterpass-details-schema.json
slug: checkout-masterpass-details
tags:
- Payments
- Financial Services
- Fintech
title: MasterpassDetails
---
