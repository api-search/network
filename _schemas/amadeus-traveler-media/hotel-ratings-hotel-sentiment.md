---
description: HotelSentiment schema
layout: schema
name: HotelSentiment
properties_list:
- description: Amadeus Hotel Ids are found in the Hotel Search response (parameter name is 'hotelId')
  name: hotelId
  type: string
- description: ''
  name: type
  type: string
- description: ''
  name: overallRating
  type: object
- description: ''
  name: numberOfRatings
  type: integer
- description: ''
  name: numberOfReviews
  type: integer
- description: Dictionary containing scores for all the available categories. If a property does not have any category this object will not be present in the response.
  name: sentiments
  type: object
provider_name: Amadeus Traveler Media
provider_slug: amadeus-traveler-media
schema_file: json-schema/hotel-ratings-hotel-sentiment-schema.json
slug: hotel-ratings-hotel-sentiment
tags:
- Content
- Destination
- Media
- Photos
- Points of Interest
- Tourism
- Travel
title: HotelSentiment
---
