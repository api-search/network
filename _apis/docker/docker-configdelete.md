---
aid: docker:docker-configdelete
name: Config Delete
tags:
- Delete
humanURL: 
properties: []
description: >-
  Removes a Docker config from the swarm cluster by its unique identifier. This operation permanently deletes the specified config object, making it unavailable to any services that might reference it. The config must not be in use by any active services at the time of deletion, otherwise the operation will fail. Once deleted, the config cannot be recovered and any services attempting to use it will encounter errors. This is a privileged operation that requires appropriate administrative permis...

---
