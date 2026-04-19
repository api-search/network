---
description: An Amazon Location Service tracker resource for tracking device positions.
layout: schema
name: Tracker
properties_list:
- description: The name of the tracker resource.
  name: TrackerName
  type: string
- description: The Amazon Resource Name (ARN) for the tracker.
  name: TrackerArn
  type: string
- description: The optional description for the tracker resource.
  name: Description
  type: string
- description: The position filtering method of the tracker resource.
  name: PositionFiltering
  type: string
- description: The timestamp for when the tracker resource was created.
  name: CreateTime
  type: string
provider_name: Amazon Location Service
provider_slug: amazon-location-service
schema_file: json-schema/amazon-location-service-tracker-schema.json
slug: amazon-location-service-tracker
tags:
- AWS
- Geocoding
- Geofencing
- Location
- Maps
- Routing
title: Tracker
---
