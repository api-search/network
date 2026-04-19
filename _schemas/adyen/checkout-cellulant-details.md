---
description: CellulantDetails schema from Adyen API
layout: schema
name: CellulantDetails
properties_list:
- description: The checkout attempt identifier.
  name: checkoutAttemptId
  type: string
- description: The Cellulant issuer.
  name: issuer
  type: string
- description: '**Cellulant**'
  name: type
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-cellulant-details-schema.json
slug: checkout-cellulant-details
tags:
- Payments
- Financial Services
- Fintech
title: CellulantDetails
---
