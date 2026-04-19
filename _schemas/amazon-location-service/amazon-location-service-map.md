---
description: An Amazon Location Service map resource.
layout: schema
name: MapResource
properties_list:
- description: The name of the map resource.
  name: MapName
  type: string
- description: The Amazon Resource Name (ARN) for the map resource.
  name: MapArn
  type: string
- description: Specifies the map data provider.
  name: DataSource
  type: string
- description: An optional description for the map resource.
  name: Description
  type: string
- description: The timestamp for when the map resource was created.
  name: CreateTime
  type: string
- description: The timestamp for when the map resource was last updated.
  name: UpdateTime
  type: string
provider_name: Amazon Location Service
provider_slug: amazon-location-service
schema_file: json-schema/amazon-location-service-map-schema.json
slug: amazon-location-service-map
tags:
- AWS
- Geocoding
- Geofencing
- Location
- Maps
- Routing
title: MapResource
---
