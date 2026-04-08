---
aid: thanos:thanos-remotewrite
name: Thanos Ingest metrics via Prometheus Remote Write
tags:
- Remote Write
humanURL: 
properties: []
description: >-
  Accepts Prometheus Remote Write requests containing time series data. The request body must be a Snappy-compressed protobuf-encoded WriteRequest. Multi-tenancy is supported via the THANOS-TENANT HTTP header. Requests may be forwarded to other Receive instances based on hashring routing configuration.

---
