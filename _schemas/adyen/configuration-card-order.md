---
description: CardOrder schema from Adyen API
layout: schema
name: CardOrder
properties_list:
- description: The date when the card order is created.
  name: beginDate
  type: string
- description: The unique identifier of the card manufacturer profile.
  name: cardManufacturingProfileId
  type: string
- description: The date when the card order processing ends.
  name: closedDate
  type: string
- description: The date when you manually closed the card order. Card orders are automatically closed by the end of the day it was created. If you manually closed it beforehand, the closing date is shown as the `end
  name: endDate
  type: string
- description: The unique identifier of the card order.
  name: id
  type: string
- description: The date when the card order processing begins.
  name: lockDate
  type: string
- description: The service center.
  name: serviceCenter
  type: string
- description: 'The status of the card order. Possible values: **Open**, **Closed**.'
  name: status
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-card-order-schema.json
slug: configuration-card-order
tags:
- Payments
- Financial Services
- Fintech
title: CardOrder
---
