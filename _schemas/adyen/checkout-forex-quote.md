---
description: ForexQuote schema from Adyen API
layout: schema
name: ForexQuote
properties_list:
- description: The account name.
  name: account
  type: string
- description: The account type.
  name: accountType
  type: string
- description: The base amount.
  name: baseAmount
  type: object
- description: The base points.
  name: basePoints
  type: integer
- description: The buy rate.
  name: buy
  type: object
- description: The interbank amount.
  name: interbank
  type: object
- description: The reference assigned to the forex quote request.
  name: reference
  type: string
- description: The sell rate.
  name: sell
  type: object
- description: The signature to validate the integrity.
  name: signature
  type: string
- description: The source of the forex quote.
  name: source
  type: string
- description: The type of forex.
  name: type
  type: string
- description: The date until which the forex quote is valid.
  name: validTill
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/checkout-forex-quote-schema.json
slug: checkout-forex-quote
tags:
- Payments
- Financial Services
- Fintech
title: ForexQuote
---
