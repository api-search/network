---
description: RefundResult schema from Adyen API
layout: schema
name: RefundResult
properties_list:
- description: The transaction that has been refunded.
  name: originalTransaction
  type: object
- description: The reference of the refund.
  name: pspReference
  type: string
- description: The response indicating if the refund has been received for processing.
  name: response
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/notifications-refund-result-schema.json
slug: notifications-refund-result
tags:
- Payments
- Financial Services
- Fintech
title: RefundResult
---
