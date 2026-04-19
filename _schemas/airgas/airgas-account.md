---
description: An Airgas B2B customer account.
layout: schema
name: Account
properties_list:
- description: Unique Airgas account number.
  name: account_number
  type: string
- description: Business name for the account.
  name: company_name
  type: string
- description: Type of customer account.
  name: account_type
  type: string
- description: ''
  name: primary_contact
  type: object
- description: ''
  name: billing_address
  type: object
- description: Account credit limit in USD.
  name: credit_limit
  type: number
- description: Payment terms for the account.
  name: payment_terms
  type: string
- description: Whether the account is active.
  name: is_active
  type: boolean
provider_name: Airgas
provider_slug: airgas
schema_file: json-schema/airgas-account-schema.json
slug: airgas-account
tags:
- Industrial Gases
- Welding
- Safety
- B2B
- Supply Chain
- Manufacturing
- Healthcare
title: Account
---
