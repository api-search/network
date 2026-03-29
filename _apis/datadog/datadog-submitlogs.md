---
aid: datadog:datadog-submitlogs
name: Send logs
tags:
- Logs
humanURL: 
properties: []
description: >-
  Sends log entries to the Datadog platform for indexing, storage, and analysis. Accepts log payloads in JSON format. Each log entry can include a message, hostname, service name, source, tags, and additional custom attributes. Supports batching multiple log entries in a single request. The maximum payload size is 5 MB for the HTTP intake endpoint. Logs must contain a message field.

---
