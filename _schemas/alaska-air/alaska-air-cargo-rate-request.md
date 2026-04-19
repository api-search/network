---
description: Request for cargo rate estimate
layout: schema
name: RateRequest
properties_list:
- description: Origin airport IATA code
  name: origin
  type: string
- description: Destination airport IATA code
  name: destination
  type: string
- description: Desired ship date
  name: shipDate
  type: string
- description: Shipment weight
  name: weight
  type: number
- description: Weight unit
  name: weightUnit
  type: string
- description: Number of pieces
  name: pieces
  type: integer
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-cargo-rate-request-schema.json
slug: alaska-air-cargo-rate-request
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: RateRequest
---
