---
aid: docker:docker-execstart
name: Exec Start
tags:
- Start
humanURL: 
properties: []
description: >-
  Starts a previously created exec instance by its ID. This endpoint executes the command that was configured when the exec instance was created using /exec/create. The request can specify whether to detach from the exec command, allocate a TTY, or upgrade the connection to a multiplexed stream for interactive use. When successful, it returns the output stream from the executed command, which may include stdout and stderr depending on the configuration. The exec instance must exist and not have...

---
