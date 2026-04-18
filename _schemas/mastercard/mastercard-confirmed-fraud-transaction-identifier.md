---
description: Transaction Identifier containing CFC Indicator the key and value pair.
layout: schema
name: TransactionIdentifier
properties_list:
- description: Actual value depending on the 'CFC Indicator' subject to the following validations 1. For ARN, Min Length is 23, Max Length is 23 and Data Type is N. 2. For BRN, Min Length is 6, Max Length is 9 and D
  name: cfcValue
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-confirmed-fraud-transaction-identifier-schema.json
slug: mastercard-confirmed-fraud-transaction-identifier
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: TransactionIdentifier
---
