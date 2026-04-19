---
description: An AGCO agricultural machine with telematics capabilities.
layout: schema
name: Machine
properties_list:
- description: Unique machine identifier.
  name: id
  type: string
- description: Machine serial number.
  name: serial_number
  type: string
- description: Machine model name.
  name: model
  type: string
- description: AGCO brand.
  name: brand
  type: string
- description: Machine type.
  name: type
  type: string
- description: Machine connectivity status.
  name: status
  type: string
- description: ''
  name: location
  type: object
- description: Total engine hours.
  name: engine_hours
  type: number
- description: Current fuel level percentage.
  name: fuel_level
  type: number
- description: Record creation timestamp.
  name: created_at
  type: string
- description: Record last updated timestamp.
  name: updated_at
  type: string
provider_name: agco
provider_slug: agco
schema_file: json-schema/agco-machine-schema.json
slug: agco-machine
tags: []
title: Machine
---
