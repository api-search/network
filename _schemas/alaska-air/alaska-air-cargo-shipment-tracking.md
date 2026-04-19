---
description: Shipment tracking details with event history
layout: schema
name: ShipmentTracking
properties_list:
- description: Air Waybill number
  name: awbNumber
  type: string
- description: Current status
  name: status
  type: string
- description: Origin airport IATA code
  name: origin
  type: string
- description: Destination airport IATA code
  name: destination
  type: string
- description: Current location IATA code
  name: currentLocation
  type: string
- description: Estimated delivery date
  name: estimatedDelivery
  type: string
- description: Tracking event history
  name: events
  type: array
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-cargo-shipment-tracking-schema.json
slug: alaska-air-cargo-shipment-tracking
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: ShipmentTracking
---
