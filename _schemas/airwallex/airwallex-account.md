---
description: An Airwallex global multi-currency account.
layout: schema
name: Account
properties_list:
- description: Unique account identifier.
  name: id
  type: string
- description: Business name of the account holder.
  name: account_name
  type: string
- description: Account status.
  name: status
  type: string
- description: Primary currency for the account.
  name: primary_currency
  type: string
- description: Currency balances held in the account.
  name: balances
  type: array
- description: ISO 3166-1 alpha-2 country code of the account.
  name: country_code
  type: string
- description: Account creation timestamp.
  name: created_at
  type: string
provider_name: Airwallex
provider_slug: airwallex
schema_file: json-schema/airwallex-account-schema.json
slug: airwallex-account
tags:
- Cross-Border Payments
- FinTech
- Foreign Exchange
- Payments
- Global
- Embedded Finance
- Multi-Currency
title: Account
---
