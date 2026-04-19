---
description: RefundFundsTransferRequest schema from Adyen API
layout: schema
name: RefundFundsTransferRequest
properties_list:
- description: The amount to be transferred.
  name: amount
  type: object
- description: A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.
  name: merchantReference
  type: string
- description: A PSP reference of the original fund transfer.
  name: originalReference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/funds-refund-funds-transfer-request-schema.json
slug: funds-refund-funds-transfer-request
tags:
- Payments
- Financial Services
- Fintech
title: RefundFundsTransferRequest
---
