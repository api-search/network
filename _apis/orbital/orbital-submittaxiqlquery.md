---
aid: orbital:orbital-submittaxiqlquery
name: Orbital Submit a TaxiQL query
tags:
- Taxiql
humanURL: 
properties: []
description: >-
  Submits a TaxiQL query to Orbital for execution. Orbital uses the types referenced in the query to look up connected services that expose those values, then builds an integration plan to load the required data from across multiple sources. Queries start with a verb such as find (for finite result sets) or stream (for infinite streams). The response format depends on the Accept header - use application/json for batch results or text/event-stream for streaming results via Server-Sent Events.

---
