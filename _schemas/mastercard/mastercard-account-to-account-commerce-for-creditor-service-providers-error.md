---
description: A single error
layout: schema
name: Error
properties_list:
- description: Source of the error
  name: Source
  type: string
- description: Error Code
  name: ReasonCode
  type: string
- description: Error Description
  name: Description
  type: string
- description: Boolean value to specify if error is recoverable or not
  name: Recoverable
  type: boolean
- description: Optional details of the error
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-account-to-account-commerce-for-creditor-service-providers-error-schema.json
slug: mastercard-account-to-account-commerce-for-creditor-service-providers-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
