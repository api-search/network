---
description: Standard error response from the Figma API.
layout: schema
name: ErrorResponse
properties_list:
- description: Always true for error responses.
  name: error
  type: boolean
- description: The HTTP status code.
  name: status
  type: integer
- description: A human-readable description of the error.
  name: message
  type: string
provider_name: Figma
provider_slug: figma
schema_file: json-schema/figma-rest-error-response-schema.json
slug: figma-rest-error-response
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
title: ErrorResponse
---
