---
aid: docker:docker-plugindelete
name: Plugin Delete
tags:
- Plugin
- Delete
humanURL: 
properties: []
description: >-
  The Docker Plugin Delete API operation removes a specified plugin from the Docker host by sending a DELETE request to the /plugins/{name} endpoint, where {name} represents the name or ID of the plugin to be deleted. This operation permanently removes the plugin and its associated data from the system. The plugin must be disabled before it can be deleted, otherwise the operation will fail. Optional query parameters can be included to force removal even if the plugin is in use. Upon successful ...

---
