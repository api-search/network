---
description: CapitalGrantAccount schema from Adyen API
layout: schema
name: CapitalGrantAccount
properties_list:
- description: The balances of the grant account.
  name: balances
  type: array
- description: The unique identifier of the balance account used to fund the grant.
  name: fundingBalanceAccountId
  type: string
- description: The identifier of the grant account.
  name: id
  type: string
- description: The limits of the grant account.
  name: limits
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-capital-grant-account-schema.json
slug: configuration-capital-grant-account
tags:
- Payments
- Financial Services
- Fintech
title: CapitalGrantAccount
---
