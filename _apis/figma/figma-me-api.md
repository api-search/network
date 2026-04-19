---
aid: figma:figma-me-api
baseURL: https://api.figma.com
description: Figma Me API provides the endpoint for retrieving information about the currently authenticated user.
humanURL: https://developers.figma.com/docs/rest-api/users-endpoints/
image: https://www.figma.com/favicon.ico
layout: api
name: Figma Me API
properties:
- type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/openapi/figma-me-api-openapi.yml
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/json-schema/figma-me-user-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/json-schema/figma-me-user-with-email-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/json-schema/figma-me-error-response-payload-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/json-schema/figma-me-forbidden-error-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/json-schema/figma-me-internal-server-error-schema.json
- type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/json-schema/figma-me-too-many-requests-error-schema.json
- type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/json-ld/figma-me-context.jsonld
- type: Documentation
  url: https://developers.figma.com/docs/rest-api/users-endpoints/
provider_name: Figma
provider_slug: figma
slug: figma-me-api
tags:
- Authentication
- Users
---
