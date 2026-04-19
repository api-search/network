---
description: Balance breakdown for a banking account
layout: schema
name: AccountBalances
properties_list:
- description: Account identifier
  name: accountId
  type: string
- description: Currency of the balances
  name: currency
  type: string
- description: Current working balance including pending transactions
  name: workingBalance
  type: number
- description: Balance available for withdrawals and payments
  name: availableBalance
  type: number
- description: Balance of cleared funds only
  name: clearedBalance
  type: number
- description: Amount locked or blocked on the account
  name: lockedAmount
  type: number
- description: Approved overdraft facility amount
  name: overdraftLimit
  type: number
- description: Interest accrued but not yet capitalized
  name: accruedInterest
  type: number
- description: Deposits received but not yet cleared
  name: pendingDeposits
  type: number
- description: Timestamp when balances were calculated
  name: asOfDate
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-account-balances-schema.json
slug: temenos-transact-core-banking-account-balances
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: AccountBalances
---
