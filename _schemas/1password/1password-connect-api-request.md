---
description: Represents a record of an API request made to the Connect server.
layout: schema
name: APIRequest
properties_list:
- description: The unique identifier for the API request.
  name: requestId
  type: string
- description: When the request was made.
  name: timestamp
  type: string
- description: The HTTP method of the request.
  name: action
  type: string
- description: The result status of the request.
  name: result
  type: string
- description: The actor who made the request.
  name: actor
  type: object
- description: The resource that was accessed.
  name: resource
  type: object
provider_name: 1Password
provider_slug: 1password
schema_file: json-schema/1password-connect-api-request-schema.json
slug: 1password-connect-api-request
tags:
- Password Manager
- Passwords
- Security
- Secrets
title: APIRequest
---
