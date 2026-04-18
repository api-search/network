---
class_count: 11
classes:
- Place
- LocalBusiness
- PostalAddress
- GeoCoordinates
- OpeningHoursSpecification
- AggregateRating
- Review
- Person
- ImageObject
- id
- type
context_file: json-ld/google-maps-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/google-maps/refs/heads/main/json-ld/google-maps-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Google Maps from Google Maps Platform.
layout: jsonld
name: Google Maps Context
namespaces:
- prefix: schema
  uri: https://schema.org/
- prefix: geo
  uri: http://www.w3.org/2003/01/geo/wgs84_pos#
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
- prefix: goog
  uri: https://developers.google.com/maps/terms#
- prefix: gmaps
  uri: https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places#
properties:
- container: ''
  name: placeId
  type: string
- container: ''
  name: displayName
  type: string
- container: ''
  name: formattedAddress
  type: string
- container: ''
  name: shortFormattedAddress
  type: string
- container: list
  name: addressComponents
  type: ''
- container: ''
  name: longText
  type: string
- container: ''
  name: shortText
  type: string
- container: ''
  name: location
  type: reference
- container: ''
  name: latitude
  type: double
- container: ''
  name: longitude
  type: double
- container: ''
  name: lat
  type: double
- container: ''
  name: lng
  type: double
- container: ''
  name: viewport
  type: reference
- container: ''
  name: northeast
  type: reference
- container: ''
  name: southwest
  type: reference
- container: ''
  name: rating
  type: double
- container: ''
  name: userRatingCount
  type: integer
- container: ''
  name: aggregateRating
  type: AggregateRating
- container: ''
  name: nationalPhoneNumber
  type: string
- container: ''
  name: internationalPhoneNumber
  type: string
- container: ''
  name: websiteUri
  type: reference
- container: ''
  name: googleMapsUri
  type: reference
- container: set
  name: types
  type: ''
- container: ''
  name: primaryType
  type: string
- container: ''
  name: regularOpeningHours
  type: OpeningHoursSpecification
- container: ''
  name: currentOpeningHours
  type: OpeningHoursSpecification
- container: ''
  name: openNow
  type: boolean
- container: list
  name: weekdayDescriptions
  type: ''
- container: ''
  name: priceLevel
  type: string
- container: ''
  name: businessStatus
  type: string
- container: list
  name: reviews
  type: ''
- container: ''
  name: reviewRating
  type: schema:Rating
- container: ''
  name: reviewBody
  type: string
- container: ''
  name: authorAttribution
  type: Person
- container: ''
  name: publishTime
  type: dateTime
- container: list
  name: photos
  type: ''
- container: ''
  name: widthPx
  type: integer
- container: ''
  name: heightPx
  type: integer
- container: ''
  name: editorialSummary
  type: string
- container: ''
  name: plusCode
  type: reference
- container: ''
  name: globalCode
  type: string
- container: ''
  name: compoundCode
  type: string
- container: ''
  name: dineIn
  type: boolean
- container: ''
  name: takeout
  type: boolean
- container: ''
  name: delivery
  type: boolean
- container: ''
  name: curbsidePickup
  type: boolean
- container: ''
  name: reservable
  type: boolean
- container: ''
  name: servesBreakfast
  type: boolean
- container: ''
  name: servesLunch
  type: boolean
- container: ''
  name: servesDinner
  type: boolean
- container: ''
  name: servesBeer
  type: boolean
- container: ''
  name: servesWine
  type: boolean
- container: ''
  name: servesVegetarianFood
  type: boolean
- container: ''
  name: accessibilityOptions
  type: reference
- container: ''
  name: wheelchairAccessibleParking
  type: boolean
- container: ''
  name: wheelchairAccessibleEntrance
  type: boolean
- container: ''
  name: wheelchairAccessibleRestroom
  type: boolean
- container: ''
  name: wheelchairAccessibleSeating
  type: boolean
- container: ''
  name: parkingOptions
  type: reference
- container: ''
  name: paymentOptions
  type: reference
- container: ''
  name: formatted_address
  type: string
- container: list
  name: address_components
  type: ''
- container: ''
  name: long_name
  type: string
- container: ''
  name: short_name
  type: string
- container: ''
  name: geometry
  type: reference
- container: ''
  name: location_type
  type: string
- container: ''
  name: place_id
  type: string
- container: ''
  name: partial_match
  type: boolean
- container: ''
  name: plus_code
  type: reference
- container: ''
  name: global_code
  type: string
- container: ''
  name: compound_code
  type: string
- container: ''
  name: utcOffsetMinutes
  type: integer
- container: ''
  name: iconMaskBaseUri
  type: reference
- container: ''
  name: iconBackgroundColor
  type: string
- container: ''
  name: adrFormatAddress
  type: string
property_count: 75
provider_name: Google Maps Platform
provider_slug: google-maps
slug: google-maps-context
tags:
- Environment
- Geocoding
- Geolocation
- Maps
- Navigation
- Places
- Routing
- Solar
- JSON-LD
- Linked Data
- Semantic Web
---
