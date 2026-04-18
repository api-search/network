---
description: ''
layout: schema
name: Error
properties_list:
- description: Information about where the error happened
  name: Source
  type: string
- description: An error code
  name: ReasonCode
  type: string
- description: A description of the error
  name: Description
  type: string
- description: Indicates if the request can be presented again for processing
  name: Recoverable
  type: boolean
- description: More details about the error
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-benefit-allocation-service-error-schema.json
slug: mastercard-benefit-allocation-service-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
