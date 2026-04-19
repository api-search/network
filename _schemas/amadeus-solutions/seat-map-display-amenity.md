---
description: 'Base data model related to Amenity, inherited amenities can be created using this baseline for extension ( using type for polymorphism ) amenityType : Enum related to generic Amenity model to identify which amenityType'
layout: schema
name: Amenity
properties_list:
- description: Specify if the traveler will need to pay extra in-flight to get the amenity
  name: isChargeable
  type: boolean
provider_name: Amadeus Solutions
provider_slug: amadeus-solutions
schema_file: json-schema/seat-map-display-amenity-schema.json
slug: seat-map-display-amenity
tags:
- Airlines
- Booking
- Flights
- GDS
- Hotels
- Travel
- Travel Technology
title: Amenity
---
