---
description: RefundNotPaidOutTransfersResponse schema from Adyen API
layout: schema
name: RefundNotPaidOutTransfersResponse
properties_list:
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-refund-not-paid-out-transfers-response-schema.json
slug: funds-refund-not-paid-out-transfers-response
tags:
- Payments
- Financial Services
- Fintech
title: RefundNotPaidOutTransfersResponse
---
