---
description: Basic hotel classification information.
layout: schema
name: HotelBasicInfo
properties_list:
- description: Hotel star category (1-5).
  name: category
  type: integer
- description: Hotel rating classification.
  name: rating
  type: string
- description: Total number of rooms in the property.
  name: numberOfRooms
  type: integer
- description: Standard check-in time (HH:MM format).
  name: checkInTime
  type: string
- description: Standard check-out time (HH:MM format).
  name: checkOutTime
  type: string
provider_name: Amadeus Media
provider_slug: amadeus-media
schema_file: json-schema/hotel-content-hotel-basic-info-schema.json
slug: hotel-content-hotel-basic-info
tags:
- Content
- Hotels
- Images
- Media
- Travel
title: HotelBasicInfo
---
