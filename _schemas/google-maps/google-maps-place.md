---
description: A place as represented by the Google Maps Places API (New). Contains comprehensive information about a physical location including identity, contact details, location data, ratings, reviews, opening hours, and service options. Based on the Google Maps Platform Places API documentation.
layout: schema
name: Google Maps Place
properties_list:
- description: The resource name of this place in the format places/{placeId}
  name: name
  type: string
- description: The unique place ID. A textual identifier that uniquely identifies a place in the Google Places database and on Google Maps.
  name: id
  type: string
- description: The localized display name of the place, suitable for short textual identification
  name: displayName
  type: object
- description: A set of type tags for this place. A place can have multiple types. Full list defined by Google Maps Place Types.
  name: types
  type: array
- description: The primary type of this place, representing the most specific type tag
  name: primaryType
  type: string
- description: The display name of the primary type, localized to the request language
  name: primaryTypeDisplayName
  type: object
- description: The place's phone number in national format
  name: nationalPhoneNumber
  type: string
- description: The place's phone number in international format, including country code
  name: internationalPhoneNumber
  type: string
- description: The full human-readable address for this place, including street, city, state/province, postal code, and country
  name: formattedAddress
  type: string
- description: A short human-readable address, typically including only the street address and city
  name: shortFormattedAddress
  type: string
- description: The individual address components of the place's address, broken down by type (street number, route, locality, etc.)
  name: addressComponents
  type: array
- description: The geographic location of the place as latitude/longitude coordinates
  name: location
  type: object
- description: A viewport suitable for displaying the place on a map of average size
  name: viewport
  type: object
- description: The place's overall rating based on aggregated user reviews, on a scale of 1.0 to 5.0
  name: rating
  type: number
- description: The total number of user ratings that contributed to the place's overall rating
  name: userRatingCount
  type: integer
- description: A URL pointing to this place's page on Google Maps
  name: googleMapsUri
  type: string
- description: The authoritative website URL for this place, if known
  name: websiteUri
  type: string
- description: The regular (non-holiday) opening hours for this place
  name: regularOpeningHours
  type: object
- description: The current opening hours, which may differ from regular hours due to holidays or special events
  name: currentOpeningHours
  type: object
- description: The price level of the place, indicating relative cost
  name: priceLevel
  type: string
- description: The operational status of the business
  name: businessStatus
  type: string
- description: Number of minutes this place's current timezone is offset from UTC
  name: utcOffsetMinutes
  type: integer
- description: A list of up to 5 reviews for this place, sorted by relevance
  name: reviews
  type: array
- description: Photos associated with this place, including references for fetching photo media
  name: photos
  type: array
- description: A brief editorial summary of the place, written by Google
  name: editorialSummary
  type: object
- description: The place's address in adr microformat (http://microformats.org/wiki/adr)
  name: adrFormatAddress
  type: string
- description: A URL to an SVG icon mask that can be used to represent the place's type
  name: iconMaskBaseUri
  type: string
- description: The background color for the place's type icon, in hex format
  name: iconBackgroundColor
  type: string
- description: The Open Location Code (plus code) for this place
  name: plusCode
  type: object
- description: Accessibility features available at this place
  name: accessibilityOptions
  type: object
- description: Parking options available at this place
  name: parkingOptions
  type: object
- description: Payment methods accepted at this place
  name: paymentOptions
  type: object
- description: Whether the place supports dine-in service
  name: dineIn
  type: boolean
- description: Whether the place offers takeout service
  name: takeout
  type: boolean
- description: Whether the place offers delivery service
  name: delivery
  type: boolean
- description: Whether the place offers curbside pickup
  name: curbsidePickup
  type: boolean
- description: Whether the place accepts reservations
  name: reservable
  type: boolean
- description: Whether the place serves breakfast
  name: servesBreakfast
  type: boolean
- description: Whether the place serves lunch
  name: servesLunch
  type: boolean
- description: Whether the place serves dinner
  name: servesDinner
  type: boolean
- description: Whether the place serves beer
  name: servesBeer
  type: boolean
- description: Whether the place serves wine
  name: servesWine
  type: boolean
- description: Whether the place serves vegetarian food
  name: servesVegetarianFood
  type: boolean
provider_name: Google Maps Platform
provider_slug: google-maps
schema_file: json-schema/google-maps-place-schema.json
slug: google-maps-place
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
title: Google Maps Place
---
