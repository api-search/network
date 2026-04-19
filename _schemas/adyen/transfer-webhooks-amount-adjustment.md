---
description: AmountAdjustment schema from Adyen API
layout: schema
name: AmountAdjustment
properties_list:
- description: The adjustment amount.
  name: amount
  type: object
- description: 'The type of markup that is applied to an authorised payment. Possible values: **exchange**, **forexMarkup**, **authHoldReserve**, **atmMarkup**.'
  name: amountAdjustmentType
  type: string
- description: The basepoints associated with the applied markup.
  name: basepoints
  type: integer
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/transfer-webhooks-amount-adjustment-schema.json
slug: transfer-webhooks-amount-adjustment
tags:
- Payments
- Financial Services
- Fintech
title: AmountAdjustment
---
