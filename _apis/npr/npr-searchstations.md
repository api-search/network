---
aid: npr:npr-searchstations
name: NPR List stations close to you or filter by search criteria
tags:
- Stationfinder
humanURL: 
properties: []
description: >-
  This endpoint has two main use cases:  - If no query parameters passed in, it returns a list of stations that are geographically closest to the calling client (based on GeoIP information) - If one or more query parameters are passed in, it performs a search of NPR stations that match those search criteria (not taking into account the client's physical location)  Clients wanting to implement a 'Change Station' UI should use this endpoint to power their search. In most cases, you'll want to bui...

---
