---
aid: engineering-platform:engineering-platform-synccollectionwithschema
name: Sync collection with schema
tags:
- API
- Collections
humanURL: 
properties: []
description: >-
  Syncs a collection attached to an API with the API schema.  This is an asynchronous endpoint that returns an HTTP `202 Accepted` response. The response contains a polling link to the `/apis/{apiId}/tasks/{taskId}` endpoint in the `Location` header.  **Note:**  This endpoint only supports the OpenAPI 3 schema type.

---
