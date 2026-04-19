---
class_count: 13
classes:
- HotelContact
- GeoCode
- HotelBasicInfo
- HotelContent
- HotelMediaItem
- HotelContentResponse
- HotelMediaData
- MediaAsset
- HotelDescription
- HotelAddress
- HotelMediaResponse
- email
- name
context_file: json-ld/amadeus-hotel-content-context.jsonld
context_url: https://raw.githubusercontent.com/api-evangelist/amadeus-media/refs/heads/main/json-ld/amadeus-hotel-content-context.jsonld
description: JSON-LD context defining the semantic vocabulary for Amadeus Hotel Content from Amadeus Media.
layout: jsonld
name: Amadeus Hotel Content Context
namespaces:
- prefix: amadeus
  uri: https://amadeus.com/schema/
- prefix: schema
  uri: https://schema.org/
- prefix: dcterms
  uri: http://purl.org/dc/terms/
- prefix: xsd
  uri: http://www.w3.org/2001/XMLSchema#
properties:
- container: ''
  name: phone
  type: string
- container: ''
  name: fax
  type: string
- container: ''
  name: website
  type: reference
- container: ''
  name: latitude
  type: double
- container: ''
  name: longitude
  type: double
- container: ''
  name: category
  type: integer
- container: ''
  name: rating
  type: string
- container: ''
  name: numberOfRooms
  type: integer
- container: ''
  name: checkInTime
  type: string
- container: ''
  name: checkOutTime
  type: string
- container: ''
  name: hotelId
  type: string
- container: ''
  name: chainCode
  type: string
- container: ''
  name: iataCode
  type: string
- container: ''
  name: basicInfo
  type: string
- container: set
  name: descriptions
  type: string
- container: ''
  name: contact
  type: string
- container: ''
  name: address
  type: string
- container: ''
  name: geoCode
  type: string
- container: set
  name: amenities
  type: string
- container: set
  name: media
  type: string
- container: ''
  name: id
  type: string
- container: ''
  name: uri
  type: reference
- container: ''
  name: thumbnailUri
  type: reference
- container: ''
  name: caption
  type: string
- container: ''
  name: width
  type: integer
- container: ''
  name: height
  type: integer
- container: ''
  name: format
  type: string
- container: ''
  name: isPrimary
  type: boolean
- container: set
  name: data
  type: string
- container: ''
  name: meta
  type: string
- container: ''
  name: lang
  type: string
- container: ''
  name: text
  type: string
- container: set
  name: lines
  type: string
- container: ''
  name: postalCode
  type: string
- container: ''
  name: cityName
  type: string
- container: ''
  name: countryCode
  type: string
- container: ''
  name: stateCode
  type: string
property_count: 37
provider_name: Amadeus Media
provider_slug: amadeus-media
slug: amadeus-hotel-content-context
tags:
- Content
- Hotels
- Images
- Media
- Travel
- JSON-LD
- Linked Data
- Semantic Web
---
