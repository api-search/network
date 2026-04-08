---
aid: statsig:statsig-initializeclient
name: Initialize client SDK
tags:
- Initialization
humanURL: 
properties: []
description: >-
  Returns all evaluated gates, configs, experiments, and layers for a given user. This is the primary endpoint called during client SDK initialization. The response contains hashed entity names for security, and the client SDK decodes them locally. The response is optimized for client-side caching and includes a hash for detecting changes on subsequent requests.

---
