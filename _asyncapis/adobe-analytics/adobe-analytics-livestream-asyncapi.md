---
channels:
- description: Persistent streaming channel for receiving real-time Analytics hit data. The client maintains a long-lived HTTPS connection and receives a continuous stream of newline-delimited JSON objects, one per Analytics hit, as they are processed.
  name: /{endpointName}
  operation: subscribe
  operation_id: receiveAnalyticsHit
  summary: Receive real-time Analytics hit data
description: The Adobe Analytics Livestream API delivers real-time analytics hit data to a connected client as each hit is processed by Adobe Analytics servers. Data is streamed in line-delimited JSON format compressed with gzip, reflecting traffic being collected by a report suite at the time it is processed. Clients connect to a named streaming endpoint provisioned by Adobe and maintain a persistent connection to receive the continuous data stream.
layout: asyncapi
messages:
- description: Represents one processed Analytics hit as received from a visitor's browser or server-side data collection. Contains all variables set during the hit including page information, visitor identifiers, eVars, props, and events.
  name: AnalyticsHit
  summary: A single Analytics data collection hit
  title: Analytics Hit
- description: An Analytics hit that includes additional geolocation information derived from the visitor's IP address, such as country, region, city, and DMA code.
  name: AnalyticsHitWithGeolocation
  summary: An Analytics hit enriched with geolocation data
  title: Analytics Hit With Geolocation
name: Adobe Analytics Livestream API
provider_name: Adobe Analytics
provider_slug: adobe-analytics
servers:
- description: Adobe Analytics Livestream endpoint. The endpoint name is provisioned by Adobe and corresponds to one or more report suites.
  name: adobeLivestream
  protocol: https
  url: https://livestream.adobe.net/api/1/stream/{endpointName}
slug: adobe-analytics-livestream-asyncapi
spec_file: asyncapi/adobe-analytics-livestream-asyncapi.yml
spec_url: https://raw.githubusercontent.com/api-evangelist/adobe-analytics/refs/heads/main/asyncapi/adobe-analytics-livestream-asyncapi.yml
tags:
- Adobe
- Analytics
- Business Intelligence
- Customer Intelligence
- Digital Marketing
- Marketing
- Web Analytics
- AsyncAPI
- Webhooks
- Events
version: '1.0'
---
