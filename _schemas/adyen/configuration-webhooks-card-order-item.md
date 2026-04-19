---
description: CardOrderItem schema from Adyen API
layout: schema
name: CardOrderItem
properties_list:
- description: The unique identifier of the balance platform.
  name: balancePlatform
  type: string
- description: 'The status of the card delivery. Possible values: **created**, **rejected**, **processing**, **produced**, **shipped**, **delivered**, **notApplicable**, **unknown**.'
  name: card
  type: object
- description: The unique identifier of the card order item.
  name: cardOrderItemId
  type: string
- description: The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**.
  name: creationDate
  type: string
- description: The ID of the resource.
  name: id
  type: string
- description: The unique identifier of the payment instrument related to the card order item.
  name: paymentInstrumentId
  type: string
- description: Contains information about the status of the PIN delivery.
  name: pin
  type: object
- description: The shipping method used to deliver the card or the PIN.
  name: shippingMethod
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-card-order-item-schema.json
slug: configuration-webhooks-card-order-item
tags:
- Payments
- Financial Services
- Fintech
title: CardOrderItem
---
