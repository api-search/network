---
description: An Airwallex cross-border transfer to a beneficiary account.
layout: schema
name: Transfer
properties_list:
- description: Unique transfer identifier.
  name: id
  type: string
- description: Amount debited from the source account.
  name: source_amount
  type: number
- description: ISO 4217 currency code of the source amount.
  name: source_currency
  type: string
- description: Amount received by the beneficiary.
  name: target_amount
  type: number
- description: ISO 4217 currency code of the target amount.
  name: target_currency
  type: string
- description: Current transfer status.
  name: status
  type: string
- description: ID of the beneficiary account.
  name: beneficiary_id
  type: string
- description: Payment reference for the transfer.
  name: reference
  type: string
- description: Transfer fee charged.
  name: fee
  type: number
- description: Currency of the fee.
  name: fee_currency
  type: string
- description: Applied foreign exchange rate.
  name: fx_rate
  type: number
- description: Timestamp when the transfer was created.
  name: created_at
  type: string
provider_name: Airwallex
provider_slug: airwallex
schema_file: json-schema/airwallex-transfer-schema.json
slug: airwallex-transfer
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
title: Transfer
---
