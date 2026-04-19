---
description: A deposit arrangement in Temenos Transact
layout: schema
name: Deposit
properties_list:
- description: Unique deposit identifier
  name: depositId
  type: string
- description: Customer identifier
  name: customerId
  type: string
- description: Deposit product identifier
  name: productId
  type: string
- description: Name of the deposit product
  name: productName
  type: string
- description: Original deposit principal amount
  name: principalAmount
  type: number
- description: Current balance including accrued interest
  name: currentBalance
  type: number
- description: Deposit currency
  name: currency
  type: string
- description: Applied interest rate percentage
  name: interestRate
  type: number
- description: Interest accrued but not yet capitalized
  name: accruedInterest
  type: number
- description: Deposit start date
  name: startDate
  type: string
- description: Deposit maturity date
  name: maturityDate
  type: string
- description: Deposit term description
  name: term
  type: string
- description: Automatic renewal behaviour
  name: renewalType
  type: string
- description: Deposit status
  name: status
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-deposit-schema.json
slug: temenos-transact-core-banking-deposit
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Deposit
---
