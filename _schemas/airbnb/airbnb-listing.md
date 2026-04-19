---
description: ''
layout: schema
name: Listing
properties_list:
- description: The unique identifier of the listing.
  name: id
  type: string
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
- description: The current status of the listing on the platform.
  name: status
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
- description: ''
  name: pricing
  type: object
- description: The photos associated with the listing.
  name: photos
  type: array
- description: The cancellation policy applied to the listing.
  name: cancellation_policy
  type: string
- description: The timestamp when the listing was created.
  name: created_at
  type: string
- description: The timestamp when the listing was last updated.
  name: updated_at
  type: string
provider_name: airbnb
provider_slug: airbnb
schema_file: json-schema/airbnb-listing-schema.json
slug: airbnb-listing
tags: []
title: Listing
---
