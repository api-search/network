---
description: Confirmed cargo shipment booking
layout: schema
name: Shipment
properties_list:
- description: Air Waybill number
  name: awbNumber
  type: string
- description: Shipment status
  name: status
  type: string
- description: Origin airport IATA code
  name: origin
  type: string
- description: Destination airport IATA code
  name: destination
  type: string
- description: Ship date
  name: shipDate
  type: string
- description: Estimated delivery date
  name: estimatedDelivery
  type: string
- description: Total cargo charge in USD
  name: totalCharge
  type: number
- description: Charge currency
  name: currency
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-cargo-shipment-schema.json
slug: alaska-air-cargo-shipment
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: Shipment
---
