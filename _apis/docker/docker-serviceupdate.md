---
aid: docker:docker-serviceupdate
name: Service Update
tags:
- Services
- Update
humanURL: 
properties: []
description: >-
  Updates the specified Docker service by its ID with new configuration parameters. This operation allows you to modify service properties such as the number of replicas, resource constraints, update configurations, network settings, and other service specifications. The update is performed using the service's ID in the path, and requires passing the new service configuration in the request body along with the current version number to prevent conflicts. Docker will perform a rolling update bas...

---
