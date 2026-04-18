---
description: Contains the a single or dual message transaction identifier values used for searching the respective transaction. Acquirer Reference Number, Banknet Reference Number, Trace Id and Serial Id values are captured.
layout: schema
name: TransactionIdentifier
properties_list:
- description: Contains Acquirer Reference Number for a transaction.
  name: acqRefNum
  type: string
- description: Contains Banknet Reference Number for a transaction.
  name: banknetRefNum
  type: string
- description: Contains Trace Id for a transaction.
  name: traceId
  type: string
- description: Contains Serial Id for a transaction.
  name: serialId
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-suspected-fraud-transaction-identifier-schema.json
slug: mastercard-suspected-fraud-transaction-identifier
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TransactionIdentifier
---
