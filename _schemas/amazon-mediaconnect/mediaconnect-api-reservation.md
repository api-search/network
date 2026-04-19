---
description: A pricing agreement for a discounted rate for a specific outbound bandwidth that your MediaConnect account will use each month over a specific time period. The discounted rate in the reservation applies to outbound bandwidth for all flows from your account until your account reaches the amount of bandwidth in your reservation. If you use more outbound bandwidth than the agreed upon amount in a single month, the overage is charged at the on-demand rate.
layout: schema
name: Reservation
properties_list:
- description: ''
  name: CurrencyCode
  type: object
- description: ''
  name: Duration
  type: object
- description: ''
  name: DurationUnits
  type: object
- description: ''
  name: End
  type: object
- description: ''
  name: OfferingArn
  type: object
- description: ''
  name: OfferingDescription
  type: object
- description: ''
  name: PricePerUnit
  type: object
- description: ''
  name: PriceUnits
  type: object
- description: ''
  name: ReservationArn
  type: object
- description: ''
  name: ReservationName
  type: object
- description: ''
  name: ReservationState
  type: object
- description: ''
  name: ResourceSpecification
  type: object
- description: ''
  name: Start
  type: object
provider_name: Amazon MediaConnect
provider_slug: amazon-mediaconnect
schema_file: json-schema/mediaconnect-api-reservation-schema.json
slug: mediaconnect-api-reservation
tags:
- AWS
- Broadcasting
- Live Video
- Media
- Media Transport
title: Reservation
---
