---
description: Error object which contains details about a single error.
layout: schema
name: Error
properties_list:
- description: The application name that generated this error. If an error is generated and returned by the gateway, then this field will have value as `Gateway`. Other possible values are `CARBON CALCULATOR`, `DONA
  name: Source
  type: string
- description: A unique constant identifying the error case encountered during request processing.
  name: ReasonCode
  type: string
- description: Short description of the `ReasonCode` field.
  name: Description
  type: string
- description: Indicates whether this error will always be returned for this request, or retrying could change the outcome.
  name: Recoverable
  type: boolean
- description: (Optional) Where appropriate, indicates detailed information about data received and calculated during the request processing, to help the user with diagnosing errors.
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-carbon-calculator-experience-error-schema.json
slug: mastercard-carbon-calculator-experience-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: Error
---
