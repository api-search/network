---
aid: docker:docker-servicelogs
name: Service Logs
tags:
- Services
- Logs
humanURL: 
properties: []
description: >-
  Get stdout and stderr logs from a service. This endpoint returns a stream of logs from the specified service. The logs can be filtered by timestamp and can include both stdout and stderr output. It supports following the log output in real-time similar to the `docker service logs` command. The response is returned as a streaming text format, with each log entry prefixed with stream identifier information. Optional query parameters allow controlling the number of lines returned, filtering by t...

---
