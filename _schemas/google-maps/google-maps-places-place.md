---
description: A complete place representation from the Places API (New)
layout: schema
name: Place
properties_list:
- description: The resource name of this place in the format places/{placeId}.
  name: name
  type: string
- description: The unique place ID
  name: id
  type: string
- description: A set of type tags for this place. Full list at https://developers.google.com/maps/documentation/places/web-service/place-types
  name: types
  type: array
- description: The primary type of this place
  name: primaryType
  type: string
- description: The place's phone number in national format
  name: nationalPhoneNumber
  type: string
- description: The place's phone number in international format
  name: internationalPhoneNumber
  type: string
- description: The full human-readable address for this place
  name: formattedAddress
  type: string
- description: A short human-readable address for this place
  name: shortFormattedAddress
  type: string
- description: The individual address components of the place
  name: addressComponents
  type: array
- description: The place's rating on a scale of 1.0 to 5.0
  name: rating
  type: number
- description: The total number of user ratings
  name: userRatingCount
  type: integer
- description: A URL to the place's page on Google Maps
  name: googleMapsUri
  type: string
- description: The place's website URL
  name: websiteUri
  type: string
- description: The price level of the place
  name: priceLevel
  type: string
- description: The business status of the place
  name: businessStatus
  type: string
- description: Number of minutes this place's current timezone is offset from UTC
  name: utcOffsetMinutes
  type: integer
- description: Up to 5 reviews for this place
  name: reviews
  type: array
- description: Photos associated with this place
  name: photos
  type: array
- description: The place's address in adr microformat
  name: adrFormatAddress
  type: string
- description: A URL for an SVG icon mask
  name: iconMaskBaseUri
  type: string
- description: Background color for the icon in hex format
  name: iconBackgroundColor
  type: string
- description: Whether the place supports dine-in
  name: dineIn
  type: boolean
- description: Whether the place supports takeout
  name: takeout
  type: boolean
- description: Whether the place supports delivery
  name: delivery
  type: boolean
- description: Whether the place supports curbside pickup
  name: curbsidePickup
  type: boolean
- description: Whether the place supports reservations
  name: reservable
  type: boolean
- description: ''
  name: servesBreakfast
  type: boolean
- description: ''
  name: servesLunch
  type: boolean
- description: ''
  name: servesDinner
  type: boolean
- description: ''
  name: servesBeer
  type: boolean
- description: ''
  name: servesWine
  type: boolean
- description: ''
  name: servesVegetarianFood
  type: boolean
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-places-place-schema.json
slug: google-maps-places-place
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Place
---
