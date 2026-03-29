---
aid: engineering-platform:engineering-platform-getapiversion
name: Get a version
tags:
- API
humanURL: 
properties: []
description: >-
  Gets information about an API version.  **Note:**  - For API editors, this endpoint returns an HTTP `302 Found` status code when the version status is pending. It also returns the `/apis/{apiId}/tasks/{taskId}` task status response header. - For API viewers, this endpoint returns an HTTP `404 Not Found` when the version status is pending.

---
