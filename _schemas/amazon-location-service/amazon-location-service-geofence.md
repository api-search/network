---
description: Schema representing an Amazon Location Service geofence resource.
layout: schema
name: Amazon Location Service Geofence
properties_list:
- description: The identifier for the geofence.
  name: GeofenceId
  type: string
- description: The geofence geometry.
  name: Geometry
  type: object
- description: The status of the geofence.
  name: Status
  type: string
- description: The timestamp for when the geofence was created.
  name: CreateTime
  type: string
- description: The timestamp for when the geofence was last updated.
  name: UpdateTime
  type: string
- description: Key-value pairs of geofence properties.
  name: GeofenceProperties
  type: object
provider_name: Amazon Location Service
provider_slug: amazon-location-service
schema_file: json-schema/amazon-location-service-geofence-schema.json
slug: amazon-location-service-geofence
tags:
- AWS
- Geocoding
- Geofencing
- Location
- Maps
- Routing
title: Amazon Location Service Geofence
---
