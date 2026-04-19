---
description: Historical location data point for an AGCO machine.
layout: schema
name: MachineLocation
properties_list:
- description: Machine identifier.
  name: machine_id
  type: string
- description: Latitude in decimal degrees.
  name: latitude
  type: number
- description: Longitude in decimal degrees.
  name: longitude
  type: number
- description: Altitude in meters.
  name: altitude
  type: number
- description: Direction of travel in degrees (0-360).
  name: heading
  type: number
- description: Ground speed in km/h at this location.
  name: ground_speed
  type: number
- description: Location timestamp.
  name: timestamp
  type: string
provider_name: agco
provider_slug: agco
schema_file: json-schema/agco-location-schema.json
slug: agco-location
tags: []
title: MachineLocation
---
