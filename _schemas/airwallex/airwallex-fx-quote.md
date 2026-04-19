---
description: An Airwallex foreign exchange rate quote for currency conversion.
layout: schema
name: FxQuote
properties_list:
- description: Unique quote identifier.
  name: quote_id
  type: string
- description: Source currency ISO 4217 code.
  name: from_currency
  type: string
- description: Target currency ISO 4217 code.
  name: to_currency
  type: string
- description: Quoted exchange rate (from_currency to to_currency).
  name: rate
  type: number
- description: Source amount to convert.
  name: from_amount
  type: number
- description: Target amount after conversion.
  name: to_amount
  type: number
- description: Timestamp when the quote expires.
  name: expires_at
  type: string
- description: Quote creation timestamp.
  name: created_at
  type: string
provider_name: Airwallex
provider_slug: airwallex
schema_file: json-schema/airwallex-fx-quote-schema.json
slug: airwallex-fx-quote
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
title: FxQuote
---
