---
description: Standard error response.
layout: schema
name: ErrorResponse
properties_list:
- description: The HTTP status code.
  name: code
  type: integer
- description: A human-readable error message.
  name: message
  type: string
- description: Detailed error information.
  name: errors
  type: array
provider_name: Atlassian
provider_slug: atlassian
schema_file: json-schema/atlassian-admin-error-response-schema.json
slug: atlassian-admin-error-response
tags:
- Code
- Collaboration
- Platform
- Productivity
- Software Development
title: ErrorResponse
---
