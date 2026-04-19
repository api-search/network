---
description: Single runway data
layout: schema
name: RunwayContract
properties_list:
- description: 'Name of the runway. E.g.: 27L, 06, 36C, etc.'
  name: name
  type: string
- description: True heading of the runway in degrees
  name: trueHdg
  type: number
- description: ''
  name: length
  type: object
- description: ''
  name: width
  type: object
- description: Marker, if runway is closed
  name: isClosed
  type: boolean
- description: ''
  name: location
  type: object
- description: ''
  name: surface
  type: object
- description: ''
  name: displacedThreshold
  type: object
- description: Does runway has lights
  name: hasLighting
  type: boolean
provider_name: AeroDataBox
provider_slug: aerodatabox
schema_file: json-schema/aerodatabox-runway-contract-schema.json
slug: aerodatabox-runway-contract
tags:
- Aviation
- Flights
- Aerospace
- Flight Data
- Airport Data
title: RunwayContract
---
