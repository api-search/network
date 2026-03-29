---
aid: bugsnag:bugsnag-sendtraces
name: Send trace data
tags:
- Traces
humanURL: 
properties: []
description: >-
  Sends OpenTelemetry span data to Bugsnag using the OTLP HTTP protocol. Accepts payloads in JSON format (application/json) or protobuf format (application/x-protobuf). Spans represent individual operations such as HTTP requests, database queries, or function calls. Bugsnag assembles spans into traces to visualize request flow and identify performance bottlenecks. The maximum payload size is 1MB, and a batch size of approximately 200 spans is recommended.

---
