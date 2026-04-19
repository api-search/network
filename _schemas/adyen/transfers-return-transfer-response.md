---
description: ReturnTransferResponse schema from Adyen API
layout: schema
name: ReturnTransferResponse
properties_list:
- description: The unique identifier of the return.
  name: id
  type: string
- description: Your internal reference for the return.
  name: reference
  type: string
- description: 'The resulting status of the return. Possible values: **Authorised**, **Declined**.'
  name: status
  type: string
- description: The unique identifier of the original transfer.
  name: transferId
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfers-return-transfer-response-schema.json
slug: transfers-return-transfer-response
tags:
- Payments
- Financial Services
- Fintech
title: ReturnTransferResponse
---
