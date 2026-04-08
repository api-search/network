---
aid: new-relic:new-relic-sendtraces
name: New Relic Send trace spans
tags:
- Traces
humanURL: 
properties: []
description: >-
  Sends distributed trace spans to New Relic. Supports New Relic format (Content-Type application/json with Data-Format newrelic) and Zipkin JSON v2 format (Data-Format zipkin). Payloads can be gzip-compressed. A single request supports up to 10,000 spans and must not exceed 1 MB compressed.

---
