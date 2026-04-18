---
description: Validation Request
layout: schema
name: Validation
properties_list:
- description: Application identifier for client.
  name: appId
  type: string
- description: 'Code to identify partner. E,g: school on Kupaa.'
  name: partnerId
  type: string
- description: 'Account Number being validated. E.g: student id.'
  name: accountId
  type: string
- description: Partner type can be one of values in enum.
  name: partnerType
  type: string
- description: Correlation Id for tracking request
  name: correlationId
  type: string
- description: Transaction time in the format 'YYYY-MM-DDThh:mm:ssTZD'
  name: transactionTime
  type: string
- description: Depicts mode of payment as mentioned in enum.
  name: paymentChannel
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-community-pass-payments-validation-schema.json
slug: mastercard-community-pass-payments-validation
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Validation
---
