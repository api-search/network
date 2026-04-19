---
description: AccountHolderBalanceResponse schema from Adyen API
layout: schema
name: AccountHolderBalanceResponse
properties_list:
- description: A list of each account and their balances.
  name: balancePerAccount
  type: array
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
- description: The total balance of the account holder.
  name: totalBalance
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-account-holder-balance-response-schema.json
slug: funds-account-holder-balance-response
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderBalanceResponse
---
