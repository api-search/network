---
description: Request body for creating a cargo shipment booking
layout: schema
name: ShipmentRequest
properties_list:
- description: Origin airport IATA code
  name: origin
  type: string
- description: Destination airport IATA code
  name: destination
  type: string
- description: Desired ship date (YYYY-MM-DD)
  name: shipDate
  type: string
- description: Commodity description
  name: commodity
  type: string
- description: Total shipment weight
  name: weight
  type: number
- description: Weight unit
  name: weightUnit
  type: string
- description: Number of pieces in shipment
  name: pieces
  type: integer
- description: ''
  name: dimensions
  type: object
- description: Special handling requirements
  name: specialHandling
  type: array
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-cargo-shipment-request-schema.json
slug: alaska-air-cargo-shipment-request
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: ShipmentRequest
---
