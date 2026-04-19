---
description: ''
layout: schema
name: ListingCreate
properties_list:
- description: The display name of the listing.
  name: name
  type: string
- description: The full description of the property.
  name: description
  type: string
- description: The type of property being listed.
  name: property_type
  type: string
- description: The type of room or space being offered.
  name: room_type
  type: string
- description: ''
  name: address
  type: object
- description: The number of bedrooms in the property.
  name: bedrooms
  type: integer
- description: The number of bathrooms in the property.
  name: bathrooms
  type: number
- description: The total number of beds in the property.
  name: beds
  type: integer
- description: The maximum number of guests allowed.
  name: max_guests
  type: integer
- description: The list of amenity identifiers available at the property.
  name: amenities
  type: array
- description: The house rules and guidelines for guests.
  name: house_rules
  type: string
- description: The earliest check-in time in HH:MM format.
  name: check_in_time
  type: string
- description: The latest check-out time in HH:MM format.
  name: check_out_time
  type: string
- description: The cancellation policy applied to the listing.
  name: cancellation_policy
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-listing-create-schema.json
slug: airbnb-listing-create
tags: []
title: ListingCreate
---
