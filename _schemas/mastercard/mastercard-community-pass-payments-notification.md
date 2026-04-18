---
description: notification request
layout: schema
name: Notification
properties_list:
- description: Application identifier for client.
  name: appId
  type: string
- description: 'Code to identify partner. Eg: school on Kupaa'
  name: partnerId
  type: string
- description: Unique transaction ID from Payment Provider
  name: providerReference
  type: string
- description: Payer mobile bank account number
  name: srcAccount
  type: string
- description: Depicts mode of payment as mentioned in enum.
  name: paymentChannel
  type: string
- description: Transaction amount
  name: transactionAmount
  type: number
- description: Payer's account id
  name: accountId
  type: string
- description: Transaction date in the format 'YYYY-MM-DD'
  name: transactionDate
  type: string
- description: Description of payment
  name: narration
  type: string
- description: Payer Name
  name: accountName
  type: string
- description: Destination account number
  name: accountNumber
  type: string
- description: Alphabetic code of currency as per ISO4217 standard.
  name: currency
  type: string
- description: ISO 3-alpha country code format.
  name: countryCode
  type: string
- description: Signature for request
  name: signature
  type: string
- description: CorrelationId for request
  name: correlationId
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-community-pass-payments-notification-schema.json
slug: mastercard-community-pass-payments-notification
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Notification
---
