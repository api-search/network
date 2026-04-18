---
description: ''
layout: schema
name: Error
properties_list:
- description: The source of the problem. i.e where the error occurred
  name: Source
  type: string
- description: A code defining the error, as defined in documentation
  name: ReasonCode
  type: string
- description: A description for this specific occurrence of the above ReasonCode
  name: Description
  type: string
- description: Whether or not retrying this request could result in a successful response.
  name: Recoverable
  type: boolean
- description: More details of this specific error. This is an optional field and is sometimes used to give a more comprehensive description of the error that has occurred, when required.
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-identity-insights-for-transactions-error-schema.json
slug: mastercard-identity-insights-for-transactions-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
