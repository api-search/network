---
aid: docker:docker-plugincreate
name: Plugin Create
tags:
- Plugin
- Create
humanURL: 
properties: []
description: >-
  Creates a new plugin instance by pulling and installing a plugin from a registry or by creating it from a local tarball. The operation accepts a plugin name and optional configuration parameters, then downloads the specified plugin image, unpacks it, and registers it with the Docker daemon. The request can include a remote reference to pull from a registry or use a tarball from the request body for local installation. Authentication credentials can be provided via the X-Registry-Auth header w...

---
