---
description: A debit or credit card linked to a customer account
layout: schema
name: Card
properties_list:
- description: Unique card identifier
  name: cardId
  type: string
- description: Masked card number
  name: cardNumber
  type: string
- description: Type of card
  name: cardType
  type: string
- description: Linked account identifier
  name: accountId
  type: string
- description: Card holder customer identifier
  name: customerId
  type: string
- description: Name on the card
  name: cardholderName
  type: string
- description: Card expiry date (MM/YY)
  name: expiryDate
  type: string
- description: Card status
  name: status
  type: string
- description: Daily transaction limit
  name: dailyLimit
  type: number
- description: Available spending limit
  name: availableLimit
  type: number
provider_name: Temenos Transact
provider_slug: temenos-transact
schema_file: json-schema/temenos-transact-core-banking-card-schema.json
slug: temenos-transact-core-banking-card
tags:
- Banking
- Core Banking
- Digital Banking
- Enterprise
- Financial Services
- Fintech
title: Card
---
