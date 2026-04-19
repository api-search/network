---
description: It conveys Information related to the reversal of a previous payment or a loyalty transaction. Content of the Reversal Request message.
layout: schema
name: ReversalRequest
properties_list:
- description: ''
  name: SaleData
  type: object
- description: ''
  name: OriginalPOITransaction
  type: object
- description: ReversedAmount is implicitely the AuthorizedAmount if absent.
  name: ReversedAmount
  type: number
- description: ''
  name: ReversalReason
  type: object
- description: ''
  name: CustomerOrder
  type: object
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/terminal-reversal-request-schema.json
slug: terminal-reversal-request
tags:
- Payments
- Financial Services
- Fintech
title: ReversalRequest
---
