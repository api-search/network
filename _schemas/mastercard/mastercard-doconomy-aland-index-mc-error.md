---
description: Error object which contains details about error
layout: schema
name: MCError
properties_list:
- description: The application name that generated this error. Every error message that is generated and returned by the gateway will have this field equal to Gateway. Other possible values are Doconomy-Proxy and Do
  name: Source
  type: string
- description: A unique constant identifying the error case encountered during request processing.
  name: ReasonCode
  type: string
- description: Short description of the ReasonCode field.
  name: Description
  type: string
- description: Indicates whether this error will always be returned for this request, or retrying could change the outcome.
  name: Recoverable
  type: boolean
- description: (Optional) Where appropriate, indicates detailed information about data received and calculated during request processing, to help the user with diagnosing errors.
  name: Details
  type: string
provider_name: Mastercard
provider_slug: mastercard
schema_file: json-schema/mastercard-doconomy-aland-index-mc-error-schema.json
slug: mastercard-doconomy-aland-index-mc-error
tags:
- Credit Cards
- Digital Identity
- Financial Services
- Fraud Detection
- Open Banking
- Payments
title: MCError
---
