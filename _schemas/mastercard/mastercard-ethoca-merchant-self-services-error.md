---
description: Error object
layout: schema
name: Error
properties_list:
- description: Source of the error
  name: Source
  type: string
- description: A unique constant identifying the error
  name: ReasonCode
  type: string
- description: Short description of the error
  name: Description
  type: string
- description: Indicates whether this error will always be returned for this request, or retrying could change the outcome
  name: Recoverable
  type: boolean
- description: Optional detailed description of the issue
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-ethoca-merchant-self-services-error-schema.json
slug: mastercard-ethoca-merchant-self-services-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
