---
description: ReturnTransferRequest schema from Adyen API
layout: schema
name: ReturnTransferRequest
properties_list:
- description: Contains information about the amount to be returned.
  name: amount
  type: object
- description: Your internal reference for the return. If you don't provide this in the request, Adyen generates a unique reference. This reference is used in all communication with you about the instruction status.
  name: reference
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-return-transfer-request-schema.json
slug: transfers-return-transfer-request
tags:
- Payments
- Financial Services
- Fintech
title: ReturnTransferRequest
---
