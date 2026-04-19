---
description: AccountHolderTransactionListRequest schema from Adyen API
layout: schema
name: AccountHolderTransactionListRequest
properties_list:
- description: The code of the account holder that owns the account(s) of which retrieve the transaction list.
  name: accountHolderCode
  type: string
- description: A list of accounts to include in the transaction list. If left blank, the last fifty (50) transactions for all accounts of the account holder will be included.
  name: transactionListsPerAccount
  type: array
- description: 'A list of statuses to include in the transaction list. If left blank, all transactions will be included. >Permitted values: >* `PendingCredit` - a pending balance credit. >* `CreditFailed` - a pending'
  name: transactionStatuses
  type: array
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-account-holder-transaction-list-request-schema.json
slug: funds-account-holder-transaction-list-request
tags:
- Payments
- Financial Services
- Fintech
title: AccountHolderTransactionListRequest
---
