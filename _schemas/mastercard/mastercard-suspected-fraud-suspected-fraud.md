---
description: ''
layout: schema
name: SuspectedFraud
properties_list:
- description: Cardholder account number used in the fraudulent transaction. Card number to be verified through Luhn's algorithm.
  name: cardNumber
  type: string
- description: Transaction amount at the merchant location (without any decimals).
  name: transactionAmount
  type: string
- description: Local date at the merchant location when the transaction occurred. Format is 'YYYYMMDD'.
  name: transactionDate
  type: string
- description: Date on which the fraud is posted in FLD by the originator. Format is 'YYYYMMDD'.
  name: fraudPostedDate
  type: string
- description: Code identifying the reason the originator submitted the transaction as fraud in FLD. Please refer to [TBD - Table 1](https://developer.mastercard.com/) for possible values.
  name: fraudTypeCode
  type: string
- description: Indicates if the account uses a magnetic stripe, chip, pin, contactless or any combination thereof. Please refer to [Table 3](https://developer.mastercard.com/fld-fraud-submission/documentation/parame
  name: accountDeviceType
  type: string
- description: Date on which the cardholder had reported the fraud. Format is 'YYYYMMDD'.
  name: cardholderReportedDate
  type: string
- description: Brief description by the originator providing some comment supporting the action.
  name: memo
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-suspected-fraud-suspected-fraud-schema.json
slug: mastercard-suspected-fraud-suspected-fraud
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: SuspectedFraud
---
