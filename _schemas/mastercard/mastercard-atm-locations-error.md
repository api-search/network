---
description: Details of the error condition such as the source of the error, reason code for the error, if the error is recoverable, and details about the error
layout: schema
name: Error
properties_list:
- description: The application that generated this error
  name: Source
  type: string
- description: A unique constant identifying the error case encountered during transaction processing
  name: ReasonCode
  type: string
- description: Short description of the ReasonCode field
  name: Description
  type: string
- description: Indicates whether this error will always be returned for this request, or retrying could change the outcome
  name: Recoverable
  type: boolean
- description: Description of the issue
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-atm-locations-error-schema.json
slug: mastercard-atm-locations-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
