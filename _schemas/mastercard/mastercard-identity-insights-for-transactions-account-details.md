---
description: ''
layout: schema
name: AccountDetails
properties_list:
- description: Unique identifier for the Primary Account Number of the card.
  name: accountNumber
  type: string
- description: The last four digits of the card number.
  name: cardLast4
  type: string
- description: The expiry year and month of the card in YYMM format.
  name: cardExpiryDate
  type: string
- description: The first digits of the card number.
  name: cardBin
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-account-details-schema.json
slug: mastercard-identity-insights-for-transactions-account-details
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: AccountDetails
---
