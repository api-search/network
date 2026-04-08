---
aid: statsig:statsig-downloadconfigspecs
name: Download configuration specs
tags:
- Configuration
humanURL: 
properties: []
description: >-
  Downloads the full project configuration for server-side local evaluation. This endpoint is the primary mechanism used by server SDKs to retrieve all gate, config, experiment, and layer definitions. The downloaded specs enable sub-millisecond feature gate checks without per-request network calls. Server SDKs periodically poll this endpoint to stay up to date with configuration changes.

---
