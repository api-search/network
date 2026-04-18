---
description: ''
layout: schema
name: Error
properties_list:
- description: The application or component that generated this error.
  name: Source
  type: string
- description: Reason code is a unique constant identifying the error case encountered during request processing.
  name: ReasonCode
  type: string
- description: Human-readable short description of the reasonCode
  name: Description
  type: string
- description: Optional detailed description provides information about data received and calculated during request processing. This helps the user to diagnose errors.
  name: Details
  type: string
- description: Recoverable flag indicates whether this error is always returned for this request, or retrying could change the outcome. For example, 'true' or 'false'.
  name: Recoverable
  type: boolean
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-confirmed-fraud-error-schema.json
slug: mastercard-confirmed-fraud-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
