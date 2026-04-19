---
description: RefundFundsTransferResponse schema from Adyen API
layout: schema
name: RefundFundsTransferResponse
properties_list:
- description: Contains field validation errors that would prevent requests from being processed.
  name: invalidFields
  type: array
- description: The value supplied by the executing user when initiating the transfer refund; may be used to link multiple transactions.
  name: merchantReference
  type: string
- description: The message of the response.
  name: message
  type: string
- description: A PSP reference of the original fund transfer.
  name: originalReference
  type: string
- description: The reference of a request. Can be used to uniquely identify the request.
  name: pspReference
  type: string
- description: The result code.
  name: resultCode
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-refund-funds-transfer-response-schema.json
slug: funds-refund-funds-transfer-response
tags:
- Payments
- Financial Services
- Fintech
title: RefundFundsTransferResponse
---
