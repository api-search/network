---
description: Recipient Request
layout: schema
name: Recipient
properties_list:
- description: Client id generated for each beneficiary transaction by client application.
  name: clientId
  type: string
- description: Transcation id generated for each beneficiary transaction by payment provider.
  name: transactionId
  type: string
- description: Account Name
  name: accountName
  type: string
- description: Account Number
  name: accountNumber
  type: string
- description: Transaction Amount
  name: transactionAmount
  type: number
- description: Alphabetic code of currency as per ISO4217 standard.
  name: currency
  type: string
- description: ISO 3-alpha country code format.
  name: countryCode
  type: string
- description: Reason code
  name: responseCode
  type: string
- description: Response Message
  name: responseMessage
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-community-pass-payments-recipient-schema.json
slug: mastercard-community-pass-payments-recipient
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Recipient
---
