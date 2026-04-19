---
description: Cargo rate estimate response
layout: schema
name: RateResponse
properties_list:
- description: Origin airport IATA code
  name: origin
  type: string
- description: Destination airport IATA code
  name: destination
  type: string
- description: Ship date
  name: shipDate
  type: string
- description: Estimated total charge
  name: totalCharge
  type: number
- description: Currency code
  name: currency
  type: string
- description: Rate per kilogram
  name: ratePerKg
  type: number
- description: Estimated transit days
  name: transitDays
  type: integer
- description: Service type
  name: serviceType
  type: string
provider_name: Alaska Airlines
provider_slug: alaska-air
schema_file: json-schema/alaska-air-cargo-rate-response-schema.json
slug: alaska-air-cargo-rate-response
tags:
- Airlines
- Aviation
- Travel
- Cargo
- Loyalty
- Flight Status
title: RateResponse
---
