---
description: A banking account arrangement in Temenos Transact. Created through the Arrangement Architecture supporting current, savings, corporate, Islamic, non-resident, and minor account types.
layout: schema
name: Account
properties_list:
- description: Unique system-generated account identifier
  name: accountId
  type: string
- description: Display name of the account
  name: accountName
  type: string
- description: Identifier of the owning customer
  name: customerId
  type: string
- description: Name of the owning customer
  name: customerName
  type: string
- description: Product identifier from the arrangement architecture
  name: productId
  type: string
- description: Human-readable product name
  name: productName
  type: string
- description: Type of account
  name: accountType
  type: string
- description: Account currency in ISO 4217 format
  name: currency
  type: string
- description: Current account status
  name: status
  type: string
- description: Date the account was opened
  name: openingDate
  type: string
- description: Current working balance of the account
  name: workingBalance
  type: number
- description: Available balance including overdraft facility
  name: availableBalance
  type: number
- description: Identifier of the assigned account officer
  name: accountOfficerId
  type: integer
- description: Branch where the account is held
  name: branchId
  type: string
- description: International Bank Account Number
  name: iban
  type: string
- description: Bank Identifier Code (SWIFT code)
  name: bic
  type: string
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-account-schema.json
slug: temenos-transact-core-banking-account
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Account
---
