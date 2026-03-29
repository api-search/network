---
aid: docker:docker-containerrestart
name: Container Restart
tags:
- Containers
- Restart
humanURL: 
properties: []
description: >-
  Restarts a specified Docker container by its ID or name. This operation performs a graceful stop of the container followed by a start, allowing running processes to shut down cleanly before restarting. An optional timeout parameter can be provided to specify how many seconds to wait before forcefully killing the container if it hasn't stopped gracefully. This is useful for applying configuration changes, recovering from errors, or implementing container lifecycle management without completely...

---
