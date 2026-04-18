---
description: ''
layout: schema
name: ErrorItem
properties_list:
- description: Source of the error.
  name: Source
  type: string
- description: Short description of the ReasonCode field.
  name: Description
  type: string
- description: A unique constant identifying the error case encountered during API request processing.
  name: ReasonCode
  type: string
- description: Indicates whether this error will always be returned for this request, or retrying could change the outcome.
  name: Recoverable
  type: boolean
- description: Where appropriate, indicates detailed information about data received.
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-loyalty-insurance-error-item-schema.json
slug: mastercard-loyalty-insurance-error-item
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: ErrorItem
---
