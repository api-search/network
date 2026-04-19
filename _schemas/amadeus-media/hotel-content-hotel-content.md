---
description: Detailed content for a single hotel property.
layout: schema
name: HotelContent
properties_list:
- description: Amadeus property code (8 characters).
  name: hotelId
  type: string
- description: Hotel chain code.
  name: chainCode
  type: string
- description: IATA city code where the hotel is located.
  name: iataCode
  type: string
- description: Hotel name.
  name: name
  type: string
- description: ''
  name: basicInfo
  type: object
- description: Hotel descriptions in various languages.
  name: descriptions
  type: array
- description: ''
  name: contact
  type: object
- description: ''
  name: address
  type: object
- description: ''
  name: geoCode
  type: object
- description: List of hotel amenity codes.
  name: amenities
  type: array
- description: List of hotel media assets.
  name: media
  type: array
provider_name: Amadeus Media
provider_slug: amadeus-media
schema_file: json-schema/hotel-content-hotel-content-schema.json
slug: hotel-content-hotel-content
tags:
- Content
- Hotels
- Images
- Media
- Travel
title: HotelContent
---
