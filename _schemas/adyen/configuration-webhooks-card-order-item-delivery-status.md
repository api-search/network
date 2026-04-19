---
description: CardOrderItemDeliveryStatus schema from Adyen API
layout: schema
name: CardOrderItemDeliveryStatus
properties_list:
- description: An error message.
  name: errorMessage
  type: string
- description: The status of the PIN delivery.
  name: status
  type: string
- description: The tracking number of the PIN delivery.
  name: trackingNumber
  type: string
provider_name: Adyen
provider_slug: adyen
schema_file: json-schema/configuration-webhooks-card-order-item-delivery-status-schema.json
slug: configuration-webhooks-card-order-item-delivery-status
tags:
- Payments
- Financial Services
- Fintech
title: CardOrderItemDeliveryStatus
---
