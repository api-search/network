---
description: ''
layout: schema
name: Error
properties_list:
- description: The name of the application that generated this error.
  name: Source
  type: string
- description: A unique constant identifying the error case encountered while processing the API request.
  name: ReasonCode
  type: string
- description: A short description of the ReasonCode field.
  name: Description
  type: string
- description: 'Indicates whether this error will always be returned for this request, or retrying could change the outcome. For example, if the request contains an invalid signature, retrying will never result in a '
  name: Recoverable
  type: boolean
- description: Where appropriate, indicates detailed information about data received and calculated during request processing, to help the user with diagnosing errors.
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-consumer-credit-analytics-error-schema.json
slug: mastercard-consumer-credit-analytics-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
