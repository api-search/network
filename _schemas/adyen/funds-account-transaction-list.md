---
description: AccountTransactionList schema from Adyen API
layout: schema
name: AccountTransactionList
properties_list:
- description: The code of the account.
  name: accountCode
  type: string
- description: Indicates whether there is a next page of transactions available.
  name: hasNextPage
  type: boolean
- description: The list of transactions.
  name: transactions
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-account-transaction-list-schema.json
slug: funds-account-transaction-list
tags:
- Payments
- Financial Services
- Fintech
title: AccountTransactionList
---
