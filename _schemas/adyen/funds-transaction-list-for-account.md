---
description: TransactionListForAccount schema from Adyen API
layout: schema
name: TransactionListForAccount
properties_list:
- description: The account for which to retrieve the transactions.
  name: accountCode
  type: string
- description: The page of transactions to retrieve. Each page lists fifty (50) transactions. The most recent transactions are included on page 1.
  name: page
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-transaction-list-for-account-schema.json
slug: funds-transaction-list-for-account
tags:
- Payments
- Financial Services
- Fintech
title: TransactionListForAccount
---
